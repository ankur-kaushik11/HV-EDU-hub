# from mysql import connector
import mysql.connector as sql

conn= sql.connect(host='localhost',user='root',password='Ankur123') #connect mysql
conn.autocommit=True
cur=conn.cursor() #make cursor 

# cur.execute("create database if not exists newData;") # queary here
# cur.execute("use newdata;")
# cur.execute("create table if not exists student(roll int, name varchar(50), per float);")
# # cur.execute("insert into student values(101,'Ankur',99);")
# while True:
#     roll=int(input("Enter Roll no: "))
#     name=input("Enter Name: ")
#     per=float(input("Enter Percentage: "))

#     query=f"insert into student values({roll},'{name}',{per});"

#     cur.execute(query)
#     n=input("You want to add more data (Y/N): ")
#     if n=="N" or n=="n":
#         break

cur.execute("use newdata;")
cur.execute("select * from student;")
# data=cur.fetchall()
# print(data)
while True:
    data=cur.fetchone()
    if data== None:
        break
    print(data)
    
# conn.commit()
cur.close() #close cursor
conn.close() #close connection
