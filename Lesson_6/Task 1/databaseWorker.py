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
    sql = "CREATE TABLE IF NOT EXISTS messages( id integer PRIMARY KEY, nickname text NOT NULL, message text NOT NULL);"
    connection.execute(sql)

def prepareDb(name):
    conn = init_conn(name)
    init_tables(conn)
    conn.close()

def getMessages(name):
    connection = init_conn(name)
    sql = "SELECT * FROM messages;"
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()

    return rows

def generateMessagesHTMLTable(rows):
    messagesTable = "<table border='1'>"
    for row in rows:
        messagesTable += "<tr>"
        for cell in row:
            messagesTable += "<td>" + str(cell) + "</td>"
        messagesTable += "</tr>"
    messagesTable += "</table>"
    return messagesTable

def sendMessage(db, nickname, message):
    connection = init_conn(db)
    sql = "INSERT INTO messages(`nickname`, `message`) VALUES('{}', '{}')".format(nickname, message)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()
