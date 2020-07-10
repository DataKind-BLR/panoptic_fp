import mysql.connector

def connection():
    conn = mysql.connector.connect (
        host = "127.0.0.1",
        user = "root",
        password = "mysqlroot"
    )

    return conn

def execute_select_query(query:str):

    conn = connection()

    cursor = conn.cursor()
    cursor.execute(query)

    # Get all the columns of data
    headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()
    conn.close()

    return headers, data