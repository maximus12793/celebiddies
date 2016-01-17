#!/usr/bin/python
import json
from pprint import pprint
import MySQLdb


print 'here'
# db = MySQLdb.connect(user="root",         # your username
#                      passwd="swaglords",  # your password
#                      # db="mysql", #this is noT celeb!!!
#                      # host="localhost")
#                      db="celeb", #this is noT celeb!!!
#                      host="mydb.cjtvopykxeid.us-west-2.rds.amazonaws.com")



db = MySQLdb.connect(user="root",         # your username
                     passwd="",  # your password
                     db="mysql", #this is noT celeb!!!
                     host="localhost")

# you must create a Cursor object. It will let
#  you execute all the queries you need
print 'completed\n\n'
cur = db.cursor()

# Use all the SQL you like
cur.execute("use celebs;") #make sure we are using the celebs db
cur.execute("show databases;")


# def addUser(name, worth):
#     cur.execute("insert ")
#     "INSERT INTO MyTable (PriKey, Description)
#        VALUES (123, 'A description of part 123.');"


def createRow():
    default="CREATE TABLE MyGuests (" + \
        "id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY," + \
        "firstname VARCHAR(30) NOT NULL,"+ \
        "lastname VARCHAR(30) NOT NULL,"+ \
        "email VARCHAR(50),"+ \
        "reg_date TIMESTAMP"+ \
        ")"
    go = raw_input('add a user?')
    if go.lower() == 'y':
        name  = raw_input('enter a name: ')
        worth = raw_input('enter a worth: ')
        sex   = raw_input('enter a sex: ')
        volt  = raw_input('enter a volt: ')
        go = "CREATE TABLE %s (" % name
        go += "id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY," + \
        "name VARCHAR(30) NOT NULL,"+ \
        "worth VARCHAR(30) NOT NULL,"+ \
        "sex CHAR(1),"+ \
        "volt INT(3) UNSIGNED ,"+ \
        "reg_date TIMESTAMP"+ \
        ")"
        print go, "\n\n\n"
        cur.execute(go)
        print 'Celeb added!'
        return
    else:
        return

rows = None
def show():
    global rows
    cur.execute("show tables;")
    idx = 1
    rows = []
    for row in cur.fetchall():
        rows.append((idx, row[0]))
        print(idx, row[0])
        idx+=1

prompt = "y"

while prompt == 'y':

    prompt = raw_input('add a person?')
    if prompt.lower() == 'y':
        createRow()
    # s  ssh -i "swaglords.pem" ec2-user@52.32.91.227
    # print all the first cell of all the rows

    show()

    #deleteCeleb() basically this shit
    prompt = raw_input('delete a row?')
    if prompt.lower() == 'y':
        g = cur.execute("show tables;")
        print "YOLO \n\n\n"
        print g
        cur.execute("SET FOREIGN_KEY_CHECKS=0;")
        prompt = input('enter the number... ')
        global rows
        print rows[prompt-1][1], "\n\n\n\n"
        # print rows[prompt-1], "\n\n\n\n"
        cur.execute("Drop Table "+ rows[prompt-1][1]+ ";")
    prompt = raw_input('again?')

#give a list to delete
db.close()


