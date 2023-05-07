import sqlite3
from flask import Flask, request, render_template

self = sqlite3.connect('split.db',check_same_thread=False)
cursor = self.cursor()
query = 'CREATE TABLE IF NOT EXISTS GROUPS (GROUP_NAME CHAR(60),NUMBER INT);'
cursor.execute(query)
query = 'CREATE TABLE IF NOT EXISTS FRIENDS (NAME CHAR(60),AMT_OWED INT);'
cursor.execute(query)
query = 'CREATE TABLE IF NOT EXISTS USERS (USERID CHAR(4), NAME CHAR(60),EMAIL CHAR(40),PASSWORD CHAR(20));'
cursor.execute(query)
query = 'INSERT INTO FRIENDS (NAME,AMT_OWED) VALUES("Akshada",0);'
cursor.execute(query)
query = 'INSERT INTO FRIENDS (NAME,AMT_OWED) VALUES("Bhavani",0);'
cursor.execute(query)
query = 'INSERT INTO GROUPS VALUES("Trip",3);'
cursor.execute(query)
query = 'INSERT INTO GROUPS VALUES("Rent",3);'
cursor.execute(query)
query = 'INSERT INTO USERS VALUES("U1","Akshada","a@gmail.com","akshada");'
cursor.execute(query)
query = 'INSERT INTO USERS VALUES("U2","Bhavani","b@gmail.com","bhavani");'
cursor.execute(query)

app = Flask(__name__)
app.static_folder = '.'
app.template_folder='.'
@app.route('/')

def reg():
    return render_template('reg.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    # do something with the data here
    return render_template('home.html')


@app.route('/signup')
def signup():
    return render_template('reg.html')


@app.route('/friends')
def friends():
    query = 'SELECT * FROM FRIENDS;'
    cursor.execute(query)
    result=cursor.fetchall()
    return render_template('friends.html',result=result)

@app.route('/addgroup',methods=['POST'])
def addgroup():
    column1 = request.form['column1']
    cursor.execute('SELECT EXISTS(SELECT * FROM GROUPS WHERE GROUP_NAME=?)',[column1])
    result=cursor.fetchall()
    exists=0
    for i in result:
        if i!='[':
            for j in i:
                exists=int(j)
            #print(exists)
    if exists==0:    
        cursor.execute("INSERT INTO GROUPS VALUES (?,?)",(column1,"$4"))
        query = 'SELECT * FROM GROUPS;'
        cursor.execute(query)
        result=cursor.fetchall()
        cursor.execute('SELECT * FROM FRIENDS;')
        friends=cursor.fetchall()
        return render_template('groups.html',result=result,friends=friends)
    else:
        query = 'SELECT * FROM GROUPS;'
        cursor.execute(query)
        result=cursor.fetchall()
        cursor.execute('SELECT * FROM FRIENDS;')
        friends=cursor.fetchall()
        return render_template('groups.html',result=result,friends=friends)

@app.route('/addfriend',methods=['POST'])
def addfriend():
    column1 = request.form['column1']
    cursor.execute('SELECT EXISTS(SELECT * FROM FRIENDS WHERE NAME=?)',[column1])
    result=cursor.fetchall()
    exists=0
    for i in result:
        if i!='[':
            for j in i:
                exists=int(j)
            #print(exists)
    if exists==0:    
        cursor.execute("INSERT INTO FRIENDS VALUES (?,?)",(column1,"$4"))
        query = 'SELECT * FROM FRIENDS;'
        cursor.execute(query)
        result=cursor.fetchall()
        return render_template('friends.html',result=result)
    else:
        query = 'SELECT * FROM FRIENDS;'
        cursor.execute(query)
        result=cursor.fetchall()
        return render_template('friends.html',result=result)



@app.route('/groups')
def groups():
    query = 'SELECT * FROM GROUPS;'
    cursor.execute(query)
    result=cursor.fetchall()
    return render_template('groups.html',result=result)

@app.route('/expense')
def expense():
    query = 'SELECT * FROM FRIENDS;'
    cursor.execute(query)
    friends=cursor.fetchall()
    query = 'SELECT * FROM GROUPS;'
    cursor.execute(query)
    groups=cursor.fetchall()
    return render_template('expense.html',groups=groups,friends=friends)
    
@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__': 
    app.run(host='0.0.0.0')

