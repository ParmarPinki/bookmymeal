# import MySQLdb
import mysql.connector

# db=MySQLdb.connect('localhost','root','root','myproject3-430')
db=mysql.connector.connect(host='localhost',database='register',user='pinkiparmar',password='08Oct2000')

cursor=db.cursor()
print("connection done....")