from flask import Flask, render_template, request
import psycopg2


conn = None
try:
    conn = psycopg2.connect(host="localhost", database="KBR_database",
                            user="postgres", password="Kaltidata22")


    def data_base():
        c = conn.cursor()
        query = ''' select
                        a.cod_acc,
                        a.description,
                        s.supplier,
                        a.cod_supp
                    from 
                        accessories a
                    join 
                        supplier s on a.supp_id = s.id
                    order by a.cod_acc;
                '''
        c.execute(query)
        dtbs = c.fetchall()
        c.close()
        return dtbs

    def supplier():
        c = conn.cursor()
        query = ''' select
                        s.supplier,
                        s.address,
                        s.email_address,
                        s.phone,
                        s.id
                    from 
                        supplier s
                    order by s.supplier;
                '''
        c.execute(query)
        supp = c.fetchall()
        c.close()
        return supp

    def supplier2():
        c = conn.cursor()
        query = ''' select
                        s.supplier,
                        s.id
                    from 
                        supplier s
                    order by s.supplier;
                '''
        c.execute(query)
        supp = c.fetchall()
        c.close()
        return supp


    def acc_by_supp(s_id):
        c = conn.cursor()
        query = ''' select
                        a.cod_acc,
                        a.description,
                        a.cod_supp
                    from 
                        accessories a
                    join 
                        supplier s on a.supp_id = s.id
                    where s.id=%s
                    order by a.cod_acc;
                '''
        c.execute(query, (s_id,))
        supp = c.fetchall()
        c.close()
        return supp

    def one_supplier(s_id):
        c = conn.cursor()
        query = ''' select
                        s.supplier,
                        s.address,
                        s.email_address,
                        s.phone,
                        s.id
                    from 
                        supplier s
                    where s.id = %s;
                '''
        c.execute(query, (s_id,))
        supp = c.fetchall()
        c.close()
        return supp

    def update_supplier():
        c = conn.cursor()
        query = """ update supplier set
                        supplier=%s,
                        address=%s,
                        email_address=%s,
                        phone=%s
                    where id = %s;
                """
        c.execute(query,
                  (
                    request.form.get('supplier'),
                    request.form.get('address'),
                    request.form.get('email_address'),
                    request.form.get('phone'),
                    request.form.get('id'),
                    )
                  )
        conn.commit()
        c.close()

    def new_supp():
        c = conn.cursor()
        query = """ insert into supplier
                        (id,
                        supplier,
                        address,
                        email_address,
                        phone)
                    values(default, %s, %s, %s, %s)
                    returning id;
                """
        c.execute(query,
                  (
                      request.form.get('supplier'),
                      request.form.get('address'),
                      request.form.get('email_address'),
                      request.form.get('phone'),
                    )
                  )
        conn.commit()
        new_supp_id = c.fetchone()
        c.close()
        return new_supp_id


    def search_supplier(s1, s2, s3, s4):
        c = conn.cursor()
        query = ''' SELECT 
                        s.supplier,
                        s.address,
                        s.email_address,
                        s.phone,
                        s.id
                    FROM supplier s  
                        WHERE supplier ilike any (values(%s))
                            or address  ilike any (values(%s))
                            or email_address  ilike any (values(%s))
                            or phone ilike any (values(%s))
                    order by s.supplier;
                '''
        c.execute(query, (s1, s2, s3, s4,))
        supp = c.fetchall()
        print(query)
        c.close()
        return supp

except psycopg2.OperationalError as ex:
    print('Database error:', ex)

app = Flask('KBH')


@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')


@app.route('/furnizori/')
def suppliers():
    table_supp = supplier()
    return render_template('furnizori.html', supplier=table_supp)


@app.route('/furnizori/edit/<supp>/')
def edit_supplier(supp):
    s = one_supplier(supp)
    return render_template('furnizor.html', supplier=s[0])


@app.route('/furnizori/save/', methods=['POST'])
def save_supplier():
    update_supplier()
    s = one_supplier(request.form.get('id'))
    return render_template('furnizor.html', updated_supplier=s[0])


@app.route('/furnizori/new/')
def new_supplier():
    return render_template('new_furnizor.html', supplier='')


@app.route('/furnizori/new/save/', methods=['POST'])
def save_new_supplier():
    s = one_supplier(new_supp())
    return render_template('new_furnizor.html', supplier=s[0])


@app.route('/furnizori/search/', methods=['POST'])
def search_supp():
    s = request.form.get('search')
    ls = s.split(' ')
    sch = "%" + "%'), ('%".join(ls) + "%"
    print(sch)
    table_supp = search_supplier(sch, sch, sch, sch)
    return render_template('furnizori.html', supplier=table_supp)


@app.route('/comenzi/')
def orders():
    return render_template('comenzi.html')


@app.route('/comanda_noua/')
def new_order():
    tb_supp = supplier2()
    return render_template('comanda_noua.html', supp=tb_supp)


@app.route('/comanda_noua/furnizor/')
def new_order2():
    tb_supp = supplier2()
    supp_id = 0
    for i in tb_supp:
        if i[0] == request.args.get('supplier'):
            supp_id = int(i[1])
    acc = acc_by_supp(supp_id)
    return render_template('comanda_noua.html', supp=tb_supp, def_supplier=request.args.get('supplier'), accessories=acc)


@app.route('/database/')
def database():
    table_db = data_base()
    return render_template('database.html', accessories=table_db)


if __name__ == '__main__':
    app.run(debug=True)
