import sqlite3
from sqlite3 import Error

def init_conn(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print ("Connection established!")
    except Error as e:
        print (e)
        print ("Connection failed!")
    return conn    

def init_tables(connection):
    sql = "CREATE TABLE IF NOT EXISTS hardware( id integer PRIMARY KEY, unit text NOT NULL, value text NOT NULL);"
    connection.execute(sql)

def prepareDb(name):
    conn = init_conn(name)
    init_tables(conn)
    conn.close()

def getData(name):
    connection = init_conn(name)
    sql = "SELECT * FROM hardware;"
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()

    return rows

def generateDataHTMLTable(rows):
    dataTable = "<table border='1'>"
    for row in rows:
        dataTable += "<tr>"
        for cell in row:
            dataTable += "<td>" + str(cell) + "</td>"
        dataTable += "</tr>"
    dataTable += "</table>"
    return dataTable

def sendData(db, unit, value):
    connection = init_conn(db)
    sql = "INSERT INTO hardware(`unit`, `value`) VALUES(?, ?);"
    args = (unit, value)
    cursor = connection.cursor()
    cursor.execute(sql, args)
    connection.commit()
    connection.close()
