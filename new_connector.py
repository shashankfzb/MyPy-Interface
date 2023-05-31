def drop():
    j=int(input('What do you want to do ?\n1.Drop Database\n2.Drop PRIMARY KEY\n'))
    if j==1:
        print("_"*66,"\n","All Available DataBases :-\n")
        cur.execute("show databases")
        for x in cur:
            s=np.array(x)
            print(s)
        print("_"*66)
        k=int(input("how many databases you want to drop:--"))
        for i in range(k):
            o=input("Name of DataBase you want to drop:- ")
            cur.execute("drop database {0}".format(o))
            con.commit()
        p=input("You want to view the rest available databases:--(y/n)")
        if p=='y' or 'Y':
            print("_"*66,"\n","All Available DataBases :-\n")
            cur.execute("show databases")
            for x in cur:
                s=np.array(x)
                print(s)
            print("_"*66)
        else:
            pass
    elif j==2:
        print("_"*66,"\n","All Available DataBases :-\n")
        cur.execute("show databases")
        for x in cur:
            s=np.array(x)
            print(s)
        print("_"*66)
        k=input("Name of Database to use:--")
        cur.execute("use {0}".format(k))
        print('_'*66,"\n\tAvailable Tables\n")
        cur.execute('show tables')
        for x in cur:
            i=np.array(x)
            print(i)
        print('_'*66)
        n=input('name of table from which you want to drop a PRIMARY KEY')
        cur.execute('alter table {0} DROP primary key'.format(n))
        con.commit()
        print("\nPRIMARY KEY dropped successfully :-)\n")


def update():
    print("_"*66,"\n","All Available DataBases :-\n")
    cur.execute("show databases")
    for x in cur:
        s=np.array(x)
        print(s)
    print("_"*66)
    a=input("name of database")
    cur.execute("use {0}".format(a))
    con.commit()
    print("_"*66,"\n","All Available Tables :-\n")
    cur.execute("show tables")
    for x in cur:
        s=np.array(x)
        print(s)
    print("_"*66)
    c=input("name of table :-")
    print("_"*66,"\n","Records :-\n")
    cur.execute("select *from {0}".format(c))
    for x in cur:
        s=np.array(x)
        print(s)
    print("_"*66)
    cur.execute("desc {0}".format(c))
    for x in cur:
        s=np.array(x)
        print(s)
    print("_"*66) 
    d=input("column name:-")
    e=input("new data:-")
    f=input("condition:-")
    cur.execute("update {0} set {1}={2} where {3}".format(c,d,e,f))
    con.commit()
    print("_"*70," \nyour new updated table is here:---/n  ")
    cur.execute("select * from {0}".format(c))
    for x in cur:
        s=np.array(x)
        print(s)
    print("_"*70)

def Alter():
    print("_"*70,"\n \tAvailable Databases:-")
    cur.execute("show databases")
    for x in cur:
        s=np.array(x)
        print(s)
    print("_"*70)
    a=input("name of database")
    cur.execute("use {0}".format(a))
    b=int(input("what you want to do ?\n1.Changing field name\n2.Modfying datatypes\n3.Adding Primary key:-"))
    if b==1:
        print('_'*66,"\n \tAvailable tables\n")
        cur.execute("show tables")
        for x in cur:
            s=np.array(x)
            print(s)
        print("_"*66)
        c=input("name of table, whose field name you want to change:-")
        cur.execute('desc {0}'.format(c))
        for x in cur:
            s=np.array(x)
            print(s)
        d=input(" old field name:-")
        e=input("new field name:-")
        f=input("its datatype")
        cur.execute("ALTER TABLE {0} Change {1} {2} {3}".format(c,d,e,f))
        con.commit()
        print(" \nyour new updated table is here:---/n  ")
        cur.execute('desc {0}'.format(c))
        for x in cur:
            s=np.array(x)
            print(s)
    elif b==2:
        cur.execute("show tables")
        for x in cur:
            print(x)
        c=input("name of table, whose field datatype you want to MODIFY :-")
        cur.execute('desc {0}'.format(c))
        for x in cur:
            s=np.array(x)
            print(s)
        d=input(" field name:-")
        e=input("its datatype")
        cur.execute("ALTER TABLE {0} Change {1} {1} {3}".format(c,d,e))
        con.commit()
        print(" \nyour new updated table is here:---/n  ")
        cur.execute('desc {0}'.format(c))
        for x in cur:
            s=np.array(x)
            print(s)
    elif b==3:
        print('_'*66,"\n \tAvailable tables\n")
        cur.execute("show tables")
        for x in cur:
            s=np.array(x)
            print(s)
        print('_'*66,"\n")
        c=input("name of table:-")
        print('_'*66,"\n \t\n")
        cur.execute("desc {0}".format(c))
        for x in cur:
            s=np.array(x)
            print(s)
        print('_'*66,"\n \tAvailable tables\n")
        q=input("name of field to make primary key:-")
        cur.execute("Alter table {0} add primary key ({1})".format(c,q))
        con.commit()
        print('_'*66,"\nPRIMARY KEY added successfully...\nYour new updated table is here:---\n","_"*66)
        cur.execute("desc {0}".format(c))
        for x in cur:
            s=np.array(x)
            print(s)      

def database():
    cur.execute('create database {0}'.format(a))
    con.commit()
    o=input("you want to create table:-(y/n)")
    if o=="y" or "Y":
        cur.execute('use {0}'.format(a))
        con.commit()
        createnew()


def createnew():
    os.system("cls")
    print("_"*70,"\n Choose Databases:-")
    cur.execute("Show databases")
    for x in cur:
        s=np.array(x)
        print(s)
    print("_"*70)
    a=input("database name to use ")
    cur.execute('use {0}'.format(a))
    print("_"*66,"\nAvailable tables")
    cur.execute("show tables")
    for x in cur:
        s=np.array(x)
        print(s)
    print("_"*66)
    a=input("new table name:-")
    b=int(input("how many fields you are going to have first:-"))
    l=[]
    for i in range(0,b):
        c=input("enter field name and datatype with constraint sep=(,):--")
        l.append(c)
    j=str(l).replace('[',"(").replace("]",")").replace("'","")
    cur.execute('create table if not exists {0} {1}'.format(a,j))
    con.commit()
    print("_"*70)
    cur.execute("desc {0}".format(a))
    for x in cur:
        s=np.array(x)
        print(s)
    print("_"*70)
    enter()


def enter():
    a=int(input("1.enter records in existing table \n2.create new table and add records \nchoice:--"))
    if a==1:
        print("_"*70,"\n\t Tables")
        cur.execute("show tables")
        for x in cur:
            s=np.array(x)
            print(s)
        print("_"*70)
        b=input("table name to use:--")
        c=int(input("how many records you are going to enter:--"))
        l=[]
        print("_"*70)
        cur.execute("desc {0}".format(b))
        for x in cur:
            s=np.array(x)
            print(s)
        print("_"*70)
        print("_"*70)
        print("Please read the instructions Carefully for entering records:-\n1. Characters must be enclosed in single quotes( 'abc' )\n2.Numeric Values are written without single quotes\n")
        print("_"*70)
        print("_"*70)
        for i in range(0,c):
            d=input("enter records in sequence of your table: ")
            l.append(d)
            j=str(l).replace('[',"(").replace("]",")").replace('"',' ')
            print(j)
            cur.execute('insert into {0} values {1}'.format(b,j))
            con.commit()
            l.pop()
        print("_"*75)    
        e=input("want to view the records(y/n)")
        print("_"*75)
        print("_"*75)
        if e =="y" or "Y":
            cur.execute("select * from {0}".format(b))
            for q in cur:
                i=np.array(q)
                print(i)
            print("_"*75)
            print("_"*75)
        else:
            os.exit(0)
            
    elif a==2:
        createnew()



#Connecting database and calling all the functions




import time
import os
import numpy as np
import mysql.connector

ch=int(input("Connect to:\n\t1.AWS Cloud.\n\t2.LocalHost\nChoice :- "))

if ch==1:
    a3=input("END-Point URL")
    a1=input("enter user name:-")
    a2=input("enter password:-")
    con=mysql.connector.connect(host=a3,user=a1,password=a2)
    if con.is_connected():
        print("\nAWS Database Connected Successfully")
        for i in range(3):
            print(".")
            time.sleep(0.5)
        time.sleep(0.5)
        os.system("cls")
        cur=con.cursor()
        f=int(input("What you want to do ?\n1.create new database\n2.create new table\n3.Entering Records\n4.Updation\n5.Alternation\n6.Drop DataBase\n Choice:- "))
        if f==1:
            a=input("enter new database name")
            database()
        elif f==2:
            createnew()
        elif f==3:
            print("_"*66,"\nAvailable Databases:-\n")
            cur.execute('show databases')
            for x in cur:
                s=np.array(x)
                print(s)
            print('_'*66)
            i=input("database name to use: ")
            cur.execute("use {0}".format(i))
            enter()
        elif f==4:
            update()
        elif f==5:
            Alter()
        elif f==6:
            drop()
    else:
        print("No user found....\ncheck user_name and password")
    

    

elif ch==2:
    a1=input("enter user name:-")
    a2=input("enter password:-")
    con=mysql.connector.connect(host="localhost",user=a1,password=a2)
    if con.is_connected():
        for i in range(3):
            print(".")
            time.sleep(0.5)
        time.sleep(0.5)
        os.system("cls")
        cur=con.cursor()
        f=int(input("What you want to do ?\n1.create new database\n2.create new table\n3.Entering Records\n4.Updation\n5.Alternation\n6.Drop DataBase\n Choice:- "))
        if f==1:
            a=input("enter new database name")
            database()
        elif f==2:
            createnew()
        elif f==3:
            print("_"*66,"\nAvailable Databases:-\n")
            cur.execute('show databases')
            for x in cur:
                s=np.array(x)
                print(s)
            print('_'*66)
            i=input("database name to use: ")
            cur.execute("use {0}".format(i))
            enter()
        elif f==4:
            update()
        elif f==5:
            Alter()
        elif f==6:
            drop()
    else:
        print("No user found....\ncheck user_name and password")
    
    






