#=============database create=========
import sqlite3
ef create_db:
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,charge text,description text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gendre text,dob text,contact text,admission text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,course text,marks_ob text,full_marks text,per text)")
    con.commit()

    con.close()



create_db()
