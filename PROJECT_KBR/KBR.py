from flask import Flask, render_template, request
import psycopg2
import pdf as pdf_creator
from datetime import date
import subprocess


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
                    WHERE a.cod_acc ilike any (%s)
                        or a.description  ilike any (%s)
                        or a.cod_supp  ilike any (%s)            
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
                        a.cod_supp,
                        a.id
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

    def create_order(notes):
        c = conn.cursor()
        query = """ insert into order_id
                        (id,
                        created_at,
                        supp_id,
                        notes)
                    values(default, default, %s, %s)
                    returning id;
                """
        c.execute(query, (request.form.get('supp_id'), notes,))
        conn.commit()
        ord_id = c.fetchall()
        c.close()
        return ord_id

    def fill_order(list_acc, list_qty, ord_id):
        c = conn.cursor()
        i = 0
        while i < len(list_acc):
            query = """ insert into orders
                            (id,
                            acc_id,
                            qty,
                            ord_id)
                        values(default, %s, %s, %s);
                    """
            c.execute(query, (list_acc[i], list_qty[i], ord_id,))
            conn.commit()
            i += 1
        c.close()

    def print_order(ord_id):
        c = conn.cursor()
        query = ''' select
                        a.cod_acc,
                        a.cod_supp,
                        o.qty,
                        concat(to_char (oi.created_at, 'YY'), '-', to_char(oi.id, 'fm0000')) as ord_name,
                        oi.supp_id,
                        to_char (oi.created_at, 'DD-MM-YYYY'),
                        oi.notes
                    from 
                        orders o
                    join 
                        order_id oi on o.ord_id = oi.id
                    join
                        accessories a on o.acc_id = a.id
                    join
                        supplier s on oi.supp_id = s.id
                    where oi.id = %s
                    order by o.id;
                '''
        c.execute(query, (ord_id,))
        ord_data = c.fetchall()
        c.close()
        return ord_data

    def show_orders():
        c = conn.cursor()
        query = '''select
                        concat(to_char (o.created_at, 'YY'), '-', to_char(o.id, 'fm0000')) as ord_name,
                        s.supplier,
                        to_char (o.created_at, 'DD-MM-YYYY'),
                        o.id
                    from 
                        order_id o
                    join 
                        supplier s on o.supp_id = s.id
                    order by o.id;
                '''
        c.execute(query)
        all_ord = c.fetchall()
        c.close()
        return all_ord

    def show_five_orders():
        c = conn.cursor()
        query = '''select
                        concat(to_char (o.created_at, 'YY'), '-', to_char(o.id, 'fm0000')) as ord_name,
                        s.supplier,
                        to_char (o.created_at, 'DD-MM-YYYY'),
                        o.id
                    from 
                        order_id o
                    join 
                        supplier s on o.supp_id = s.id
                    order by o.created_at desc
                    limit 10;
                '''
        c.execute(query)
        five_ord = c.fetchall()
        c.close()
        return five_ord


    def show_order(oi_id):
        c = conn.cursor()
        query = '''select
                        concat(to_char (oi.created_at, 'YY'), '-', to_char(oi.id, 'fm0000')) as ord_name,
                        a.cod_acc,
                        a.description,
                        o.qty,
                        s.supplier,
                        to_char (oi.created_at, 'DD-MM-YYYY'),
                        a.cod_supp,
                        oi.notes
                    from 
                        orders o
                    join 
                        order_id oi on o.ord_id = oi.id
                    join
                        supplier s on oi.supp_id = s.id    
                    join
                        accessories a on o.acc_id = a.id
                    where oi.id=(%s);
                '''
        c.execute(query, (oi_id,))
        one_ord = c.fetchall()
        c.close()
        return one_ord


    def search_ord(s1, s2, s3, s4):
        c = conn.cursor()
        query = '''select
                        concat(to_char (oi.created_at, 'YY'), '-', to_char(oi.id, 'fm0000')) as ord_name,
                        s.supplier,
                        to_char (oi.created_at, 'DD-MM-YYYY'),
                        a.cod_acc,
                        a.description,
                        o.qty,
                        oi.id
                    from 
                        orders o
                    join 
                        order_id oi on o.ord_id = oi.id
                    join
                        supplier s on oi.supp_id = s.id    
                    join
                        accessories a on o.acc_id = a.id
                    where a.cod_acc ilike any (%s)
                        or a.description ilike any (%s)
                        or s.supplier ilike any (%s)
                        or concat(to_char (oi.created_at, 'YY'), '-', to_char(oi.id, 'fm0000')) ilike any (%s)
                    order by o.id;
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
    five_orders = show_five_orders()
    return render_template('home.html', orders=five_orders)


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
    ls = s.split()
    sch = '{"%' + '%", "%'.join(ls) + '%"}'
    table_supp = search_supplier(sch, sch, sch, sch)
    return render_template('furnizori.html', supplier=table_supp, search=s)


@app.route('/comenzi/')
def orders():
    all_ord = show_orders()
    return render_template('orders.html', orders=all_ord)


@app.route('/comenzi/<oi_id>/')
def order(oi_id):
    one_ord = show_order(oi_id)
    return render_template('order.html', orders=one_ord, order_id=oi_id)


@app.route('/comenzi/search/', methods=['POST'])
def search_orders():
    s = request.form.get('search')
    ls = s.split()
    sch = '{"%' + '%", "%'.join(ls) + '%"}'
    all_ord = search_ord(sch, sch, sch, sch)
    return render_template('orders.html', search_orders=all_ord, search=s)


@app.route('/comanda_noua/')
def new_order():
    tb_supp = supplier2()
    return render_template('comanda_noua.html', supp=tb_supp)


@app.route('/comanda_noua/furnizor/', methods=['POST'])
def new_order2():
    supp = one_supplier(request.form.get('supplier'))
    acc = acc_by_supp(request.form.get('supplier'))
    return render_template('comanda_noua.html', def_supplier=supp[0], accessories=acc)


@app.route('/comanda_noua/new_order_done/', methods=['POST'])
def new_order_done():
    notes = request.form.get('note')
    o = create_order(notes)
    ord_id = o[0][0]
    list_acc = request.form.getlist('accessories[]')
    list_qty = request.form.getlist('qty[]')
    fill_order(list_acc, list_qty, ord_id)
    ord_data = print_order(ord_id)
    supp_data = one_supplier(request.form.get('supp_id'))
    body = {
        "data": {
            "order_id": ord_id,
            "order": ord_data,
            "supplier": supp_data,
            "note": notes,
            "today": date.today(),
        }
    }
    outfile = f"order {ord_data[0][3]}.pdf"
    pdf_creator.convert_html_to_pdf(body, outfile)

    return order(ord_id)


@app.route('/comenzi/open_PDF/<oi_id>/')
def order_open_pdf(oi_id):
    ord_data = print_order(oi_id)
    supp_data = one_supplier(ord_data[0][4])
    notes = ord_data[0][6]
    body = {
        "data": {
            "order_id": oi_id,
            "order": ord_data,
            "supplier": supp_data,
            "note": notes,
            "today": date.today(),
        }
    }
    outfile = f"order {ord_data[0][3]}.pdf"
    pdf_creator.convert_html_to_pdf(body, outfile)
    subprocess.Popen([outfile], shell=True)
    return order(oi_id)


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
    ls = s.split()
    sch = '{"%' + '%", "%'.join(ls) + '%"}'
    table_acc = search_accessory(sch, sch, sch)
    print(table_acc)
    return render_template('database.html', accessories=table_acc, search=s)


if __name__ == '__main__':
    app.run(debug=True)
