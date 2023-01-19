from flask import Flask, render_template, session,json
from flask import request
from flask import jsonify
from heperfunctions import *
from flask import Response
from psycopg2 import IntegrityError


app = Flask(__name__)

conn = create_db_connection()


@app.route('/getAllClients')
def getAllClients():
    cur = conn.cursor()
    cur.execute(queries["getAllClients"])
    rows = cur.fetchall()
    col_names = [desc[0] for desc in cur.description]
    formatted_result = format_userinfo(rows,col_names)
    return formatted_result
    
@app.route('/getAllCaretakers')
def getAllCaretakers():
    cur = conn.cursor()
    cur.execute(queries["getAllCaretaker"])
    rows = cur.fetchall()
    col_names = [desc[0] for desc in cur.description]
    formatted_result = format_userinfo(rows,col_names)
    return formatted_result

#API for get clients using GET METHOD
# @app.route('/clients', methods=["GET"])
# def get_clients():
#     clients = Client.query.all()
#     client_list = []
#     for client in clients:
#         client_list.append(client.name)
#     return jsonify(client_list)
  
# API for creating new_user in database using POST METHOD
@app.route('/addNewCaretaker', methods=['POST'])
def add_new_caretaker():
    response_dict = {}
    if request.method == 'POST':
        data = json.loads(request.data)
        email= data['email']
        password= data['password']
        fullname= data['fullname']
        gender= data['gender']
        start_date= data['start_date']
        is_active= data['is_active']
        phone= data['phone']

        try:

            cursor = conn.cursor()
            cursor.execute(queries["addNewCaretaker"].format(email,password,fullname,gender,start_date,is_active,phone))
            conn.commit()

        except Exception as e:
            message=str(e)
            response_dict['message'] = message
            return Response(response=json.dumps(response_dict),
            status=405,
            mimetype="application/json")

        if cursor.rowcount > 0:
            message = "Data was inserted successfully"
        else:
            message = "Could not insert data"

        response_dict['message'] = message
        return Response(response=json.dumps(response_dict),
        status=200,
        mimetype="application/json")
    else:
        message = "Excpected API type POST"
        response_dict['message'] = message
        return Response(response=json.dumps(response_dict),
        status=405,
        mimetype="application/json")


#API for add new client data in database using POST METHOD

@app.route('/addNewClient', methods=['POST'])
def add_new_client():
    response_dict = {}
    if request.method == 'POST':
        data = json.loads(request.data)
        id=data['id']
        email= data['email']
        password= data['password']
        fullname= data['fullname']
        gender= data['gender']
        birthday= data['birthday']
        phone= data['phone']
        address= data['address']

        try:

            cursor = conn.cursor()
            cursor.execute(queries["addNewClient"].format(id,email,password,fullname,gender,birthday,phone,address))
            conn.commit()
        
        except Exception as e:
            message=str(e)
            response_dict['message'] = message
            return Response(response=json.dumps(response_dict),
            status=405,
            mimetype="application/json")

        if cursor.rowcount > 0:
            message = "Data was inserted successfully"
        else:
            message = "Could not insert data"

        response_dict['message'] = message
        return Response(response=json.dumps(response_dict),
        status=200,
        mimetype="application/json")
    else:
        message = "Excpected API type POST"
        response_dict['message'] = message
        return Response(response=json.dumps(response_dict),
        status=405,
        mimetype="application/json")

# API for creating a new_user in database using POST METHOD
# @app.route('/users', methods=["POST"])
# def create_user():
#     name = request.json.get('name')
#     email = request.json.get('email')
#     new_user = User(name=name, email=email)
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({"message": "User created"})

@app.route('/bootstrap')
def login():
    return render_template('index.html')

@app.route('/sum',methods=['GET'])
def sum():
    num1=int(request.args.get('num1'))
    num2=int(request.args.get('num2'))
    return str(num1+num2)
@app.route('/testcase')
def test_multiple_primary_key_edge_case():
    # Create a new record with duplicate primary key values
    record1 = {'id': 1, 'product_id': 1, 'name': 'Apple', 'price': 0.99}
    record2 = {'id': 1, 'product_id': 1, 'name': 'Banana', 'price': 0.89}
    try:
        insert_into_table('products', record1)
        insert_into_table('products', record2)
        # If the second insert is successful, the test fails
        assert False, "Insert of record with duplicate primary key should have failed"
    except IntegrityError:
        # If an IntegrityError is raised, the test passes
        assert True

@app.errorhandler(Exception)
def error_handler(e):
    app.logger.error(e)
    return jsonify(error=str(e)),500
# def test_multiple_primary_key_edge_case():
#  record1 = {'id': 1, 'product_id': 1, 'name': 'Apple', 'price': 0.99}
#     record2 = {'id': 1, 'product_id': 1, 'name': 'Banana', 'price': 0.89}
#     try:
#         insert_into_table('products', record1)
#         insert_into_table('products', record2)
#         # If the second insert is successful, the test fails
#         assert False, "Insert of record with duplicate primary key should have failed"
#     except IntegrityError:
#         # If an IntegrityError is raised, the test passes
#         assert True
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'GET':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

# @app.route("/firstpage")
# # def hello_world():
# #     user_id=session["user_id"]
# #     # print("return se upar")
# #     return name
# #     # return "<p>Hello, World,to my first page!</p>"

# def get_username():
#     username=request.args.get("username")
#     if username:
#         return f"Welcome!,{username}"
#     else:
#         return "Please provide a username in the URL, e.g. http://localhost:5000/?username=johndoe"


if __name__ == '__main__':
   app.run(host='localhost',port=7000,debug = True)

