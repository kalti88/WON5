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
                        a.cod_supp,
                        a.id
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


    def one_acc(a_id):
        c = conn.cursor()
        query = ''' select
                        a.cod_acc,
                        a.cod_supp,
                        a.description,
                        s.supplier,
                        a.id,
                        s.id
                    from 
                        accessories a
                    join 
                        supplier s on a.supp_id = s.id
                    where a.id = %s
                    order by a.cod_acc;
                '''
        c.execute(query, (a_id,))
        dtbs = c.fetchall()
        c.close()
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
        return dtbs, supp

    def update_accessory():
        c = conn.cursor()
        query = """ update accessories set
                           cod_acc=%s,
                           cod_supp=%s,
                           description=%s,
                           supp_id=%s
                       where id = %s;
                   """
        c.execute(query,
                  (
                      request.form.get('cod_acc'),
                      request.form.get('cod_supp'),
                      request.form.get('description'),
                      request.form.get('supp_id'),
                      request.form.get('id'),
                  )
                  )
        conn.commit()
        c.close()

    def new_acc():
        c = conn.cursor()
        query = """ insert into accessories
                        (id,
                        cod_acc,
                        cod_supp,
                        description,
                        supp_id)
                    values(default, %s, %s, %s, %s)
                    returning id;
                """
        c.execute(query,
                  (
                      request.form.get('cod_acc'),
                      request.form.get('cod_supp'),
                      request.form.get('description'),
                      request.form.get('supp_id'),
                  )
                  )
        conn.commit()
        new_supp_id = c.fetchone()
        c.close()
        return new_supp_id

    def search_accessory(s1, s2, s3):
        c = conn.cursor()
        query = ''' SELECT 
                        a.cod_acc,
                        a.description,
                        s.supplier,
                        a.cod_supp,
                        a.id
                    FROM 
                        accessories a
                    JOIN
                        supplier s on a.supp_id = s.id
                    WHERE cod_acc ilike any (%s)
                        or description  ilike any (%s)
                        or cod_supp  ilike any (%s)            
                    order by a.cod_acc;
                '''

        c.execute(query, (s1, s2, s3,))
        supp = c.fetchall()
        c.close()
        return supp

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
                    WHERE supplier ilike any (%s)
                        or address  ilike any (%s)
                        or email_address  ilike any (%s)
                        or phone ilike any (%s)
                    order by s.supplier;
                '''
        c.execute(query, (s1, s2, s3, s4,))
        supp = c.fetchall()
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
    sch = '{"%' + '%", "%'.join(ls) + '%"}'
    table_supp = search_supplier(sch, sch, sch, sch)
    return render_template('furnizori.html', supplier=table_supp)


@app.route('/comenzi/')
def orders():
    return render_template('comenzi.html')


@app.route('/comanda_noua/')
def new_order():
    tb_supp = supplier2()
    return render_template('comanda_noua.html', supp=tb_supp)


@app.route('/comanda_noua/furnizor/', methods=['POST'])
def new_order2():
    supp = one_supplier(request.form.get('supp_id'))
    acc = acc_by_supp(request.form.get('supp_id'))
    return render_template('comanda_noua.html', def_supplier=supp[0][0], accessories=acc)


@app.route('/comanda_noua/new_order_done/', methods=['POST'])
def new_order_done():
    # supp = one_supplier(request.form.get('supp_id'))
    # print(supp[0])
    # acc = acc_by_supp(request.form.get('supp_id'))
    print(request.form.get('accessories[]'))
    print(request.form.get('qty[]'))
    return render_template('PDF_template.html')


@app.route('/accessories/')
def database():
    table_db = data_base()
    return render_template('database.html', accessories=table_db)


@app.route('/accessories/edit/<acc>/')
def edit_accessory(acc):
    a, s = one_acc(acc)
    return render_template('accessory.html', suppliers=s, accessory=a[0])


@app.route('/accessories/save/', methods=['POST'])
def save_accessory():
    update_accessory()
    a, s = one_acc(request.form.get('id'))
    return render_template('accessory.html', suppliers=s, updated_accessory=a[0])


@app.route('/accessories/new/')
def new_accessory():
    s = supplier2()
    return render_template('new_accessory.html', suppliers=s, accessory='')


@app.route('/accessories/new/save/', methods=['POST'])
def save_new_accessory():
    a, s = one_acc(new_acc())
    return render_template('new_accessory.html', suppliers=s, accessory=a[0])


@app.route('/accessories/search/', methods=['POST'])
def search_acc():
    s = request.form.get('search')
    ls = s.split(' ')
    sch = '{"%' + '%", "%'.join(ls) + '%"}'
    print(sch)
    table_acc = search_accessory(sch, sch, sch)
    print(table_acc)
    return render_template('database.html', accessories=table_acc)


if __name__ == '__main__':
    app.run(debug=True)
