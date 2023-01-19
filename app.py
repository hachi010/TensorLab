from flask import Flask, render_template, session,json
from flask import request
from flask import jsonify
from heperfunctions import *
from constants import *
from flask import Response
from psycopg2 import IntegrityError
import logging


# logging.basicConfig(filename='LogFolder/app_los.log' ,level = logging.DEBUG)

app = Flask(__name__)
logger = get_logger(__name__)
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
            logger.error(message)
            response_dict['message'] = message
            return Response(response=json.dumps(response_dict),
            status=405,
            mimetype="application/json")

        if cursor.rowcount > 0:
            message = "Data was inserted successfully"
            logger.info(message)
        else:
            message = "Could not insert data"
            logger.error(message)

        response_dict['message'] = message
        return Response(response=json.dumps(response_dict),
        status=200,
        mimetype="application/json")
    else:
        message = "Excpected API type POST"
        logger.warning(message)
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
        address= ngrok http 80data['address']

        try:

            cursor = conn.cursor()
            cursor.execute(queries["addNewClient"].format(id,email,password,fullname,gender,birthday,phone,address))
            conn.commit()
        
        except Exception as e:
            message=str(e)
            logger.error(message)
            response_dict['message'] = message
            returngrok http 80n Response(response=json.dumps(response_dict),
            status=405,
            mimetype="application/json")

        if cursor.rowcount > 0:
            message = "Data was inserted successfully"
            logger.info(message)
        else:
            message = "Could not insert data"
            logger.error(message)

        response_dict['message'] = message
        return Response(response=json.dumps(response_dict),
        status=200,
        mimetype="application/json")
    else:
        message = "Excpected API type POST"
        logger.warning(message)
        response_dict['message'] = message
        return Response(response=json.dumps(response_dict),
        status=405,
        mimetype="application/json")



if __name__ == '__main__':

   app.run(host='localhost',port=7000,debug = True)

