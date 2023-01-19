queries = {
            "getAllClients":"SELECT * FROM client",
            "getAllCaretaker":"SELECT * FROM caretaker",
            "addNewCaretaker":"INSERT INTO caretaker (email, password, fullname, gender, start_date, is_active, phone)VALUES('{}','{}','{}','{}','{}','{}','{}')",
            "addNewClient":"INSERT INTO client (id,email, password, fullname, gender, birthday, phone,address)VALUES({},'{}','{}','{}','{}','{}','{}','{}')"

        }