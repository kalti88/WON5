from flask import Flask, render_template, request
import psycopg2


conn = None
try:
    conn = psycopg2.connect(host="localhost", database="KBR_database",
                            user="postgres", password="Kaltidata22")


    def data_base():
        c1 = conn.cursor()
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
        c1.execute(query)
        dtbs = c1.fetchall()
        c1.close()
        return dtbs

    def supplier():
        c2 = conn.cursor()
        query = ''' select
                        s.supplier,
                        s.address,
                        s.email_address,
                        s.phone
                    from 
                        supplier s
                    order by s.supplier;
                '''
        c2.execute(query)
        supp = c2.fetchall()
        c2.close()
        return supp

    def supplier2():
        c2 = conn.cursor()
        query = ''' select
                        s.supplier,
                        s.id
                    from 
                        supplier s
                    order by s.supplier;
                '''
        c2.execute(query)
        supp = c2.fetchall()
        c2.close()
        return supp

    def acc_by_supp(s_id):
        c3 = conn.cursor()
        query = f''' select
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
        c3.execute(query, (s_id,))
        supp = c3.fetchall()
        c3.close()
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


@app.route('/furnizori/search')
def search_supp():
    table_supp = supplier()
    return render_template('furnizori.html', supplier=table_supp)


if __name__ == '__main__':
    app.run(debug=True)
