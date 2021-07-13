from flask import Flask, render_template, request, session, flash
import datetime
from datetime import date
import pymysql.cursors
import json
from Config import usercfg,passwordcfg,hostcfg,dbcfg,portcfg

connection = pymysql.connect(host=hostcfg,
                             user=usercfg,
                             password=passwordcfg,
                             db=dbcfg,
                             port = portcfg)

cursor = connection.cursor()
app = Flask(__name__)
app.config["DEBUG"] = True
today = date.today()
app.secret_key = '123'

@app.route('/', methods=['GET'])
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')

@app.route('/updatepassword', methods=['GET'])
def updatepassword():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('passwordupdate.html')

@app.route('/resetuserpassword', methods=['GET'])
def resetuserpassword():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if session['Username'] == 'admin':
            return render_template('resetuserpassword.html')
        else:
            return render_template('notadmin.html')

@app.route('/submitpasswordreset', methods=['GET','POST'])
def submitpasswordreset():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method== 'POST':
            querytext = """SELECT * FROM Users"""
            cursor.execute(str(querytext))
            results = cursor.fetchall()
            cursor.close
            for row in results:
                userid = row[0]
                username = row[1]
                password = row[2]
                if username==request.form['User']:
                        query2text= "UPDATE `Users` SET `Password` = '1717222817' WHERE `UserName` = '"+request.form['User']+"';"
                        cursor.execute(str(query2text))
                        connection.commit()
        return render_template('submitpasswordreset.html')

@app.route('/submitupdatepassword', methods=['GET','POST'])
def submitupdatepassword():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        error = ''
        if request.method == 'POST':
            PUDetails = request.form
            OldPassword = PUDetails['OldPassword']
            NewPassword = PUDetails['NewPassword']
            ConfirmNewPassword = PUDetails['ConfirmNewPassword']
            HashPass = hash(OldPassword+'2YYkejP-:s')
            NewHashPass = hash(NewPassword+'2YYkejP-:s')
            if ConfirmNewPassword==NewPassword:
                querytext = """SELECT * FROM Users"""
                cursor.execute(str(querytext))
                results = cursor.fetchall()
                cursor.close
                for row in results:
                    userid = row[0]
                    username = row[1]
                    password = row[2]
                    if username==session['Username']:
                        if password==str(HashPass):
                            query2text= "UPDATE `Users` SET `Password` = '"+str(NewHashPass)+"' WHERE `UserName` = '"+str(username)+"';"
                            cursor.execute(str(query2text))
                            connection.commit()
                            error+='False'
        if error=='False':    
            Action = 'UpdatedPassword'
            Details = ''
            User = session['Username']
            DateTime = str(datetime.datetime.now())
            loginsert = """INSERT INTO Log(DateTime,User,Action,Details) VALUES(%s, %s, %s, %s)"""
            logvalues = (DateTime,User,Action,Details)
            cursor.execute(loginsert,logvalues)
            connection.commit()
            return render_template('submitupdatepassword.html')
        else:
            return render_template('error.html')

@app.route('/login', methods=['POST'])
def login():
    Username = request.form['Username']
    Password = request.form['Password']
    HashPass = hash(Password+'2YYkejP-:s')
    querytext = """SELECT * FROM Users"""
    cursor.execute(str(querytext))
    results = cursor.fetchall()
    cursor.close
    for row in results:
        userid = row[0]
        username = row[1]
        password = row[2]
        if username==Username:
            if password==str(HashPass):
                session['logged_in'] = True 
                session['Username'] = request.form['Username']
                Action = 'Logged In'
                Details = ''
                User = session['Username']
                DateTime = str(datetime.datetime.now())
                loginsert = """INSERT INTO Log(DateTime,User,Action,Details) VALUES(%s, %s, %s, %s)"""
                logvalues = (DateTime,User,Action,Details)
                cursor.execute(loginsert,logvalues)
                connection.commit()
                    
    return home()
 
@app.route('/home', methods=['GET'])
def home2():
    return home()
    
@app.route('/viewquestiongroups', methods=['GET'])
def viewquestiongroups():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        querytext = """SELECT * FROM QuestionGroups"""
        cursor.execute(str(querytext))
        results = cursor.fetchall()
        fieldnames = [i[0] for i in cursor.description]
        return render_template('viewquery.html', fieldnames=fieldnames, results=results)

@app.route('/adduser', methods=['GET'])
def adduser():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if session['Username'] == 'admin':
            return render_template('adduser.html')
        else:
            return render_template('notadmin.html')

@app.route('/submitnewuser', methods=['GET','POST'])
def submitnewuser():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == 'POST':
            NUDetails = request.form
            NewUserName = NUDetails['User']
            temppass = str(hash('TempPass2YYkejP-:s'))
            newusersql = """INSERT INTO Users(UserName,Password) VALUES(%s,%s)"""
            newuservalues = (NewUserName,temppass)
            cursor.execute(newusersql,newuservalues)
            connection.commit()
            Action = 'CreatedNewUser'
            Details = str(NewUserName)
            User = session['Username']
            DateTime = str(datetime.datetime.now())
            loginsert = """INSERT INTO Log(DateTime,User,Action,Details) VALUES(%s, %s, %s, %s)"""
            logvalues = (DateTime,User,Action,Details)
            cursor.execute(loginsert,logvalues)
            connection.commit()
        return render_template('submitnewuser.html')
    
@app.route('/createquestiongroup', methods=['GET'])
def createquestiongroup():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('createquestiongroup.html')

@app.route('/submitnewgroupname.php', methods=['GET','POST'])
def submitnewgroupname():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == 'POST':
            GNDetails = request.form
            NewGroupName = GNDetails['NewGroupName']
            DateCreated = str(today)
            
            newgroupsql = """INSERT INTO QuestionGroups(QuestionGroupName,DateCreated) VALUES(%s, %s)"""
            newgroupvalues = (NewGroupName,DateCreated)
            cursor.execute(newgroupsql,newgroupvalues)
            connection.commit()
            Action = 'CreatedGroup'
            Details = str(NewGroupName)
            User = session['Username']
            DateTime = str(datetime.datetime.now())
            loginsert = """INSERT INTO Log(DateTime,User,Action,Details) VALUES(%s, %s, %s, %s)"""
            logvalues = (DateTime,User,Action,Details)
            cursor.execute(loginsert,logvalues)
            connection.commit()
        return render_template('submitnewgroupname.html')
    
@app.route('/addquestions', methods=['GET'])
def addquestions():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('addquestions.html')

@app.route('/addquestions2', methods=['GET'])
def addquestions2():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('addquestions2.html')
    
@app.route('/addquestions3', methods=['GET'])
def addquestions3():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('addquestions3.html')
    
@app.route('/addquestions4', methods=['GET'])
def addquestions4():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('addquestions4.html')
    
@app.route('/submitquestions2.php', methods=['GET','POST'])
def submitquestions2():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == 'POST':
            qdetails = request.form
            QuestionText = qdetails['QuestionText']
            QuestionClass = qdetails['QuestionClass']
            QuestionType = qdetails['QuestionType']
            QuestionGroupID = qdetails['QuestionGroup']
            Choice1Text = qdetails['Choice1Text']
            Choice1ImageURL = qdetails['Choice1ImageURL']
            Choice2Text = qdetails['Choice2Text']
            Choice2ImageURL = qdetails['Choice2ImageURL']
            
            newquestionsql = """INSERT INTO Questions(QuestionText,QuestionClass,QuestionType,QuestionGroupID) VALUES(%s, %s, %s, %s)"""
            newquestionvalues = (QuestionText,QuestionClass,QuestionType,QuestionGroupID)
            cursor.execute(newquestionsql,newquestionvalues)
            connection.commit()
            getquestionid = """SELECT * FROM Questions ORDER BY QuestionID DESC LIMIT 1"""
            cursor.execute(getquestionid)
            results = cursor.fetchall()
            QuestionID = ''
            for row in results:
                newquestionid = row[0]
                QuestionID = newquestionid
                newchoicessql = """INSERT INTO Choices(ChoiceText,ChoiceImageURL, QuestionID) VALUES(%s, %s, %s)"""
                newchoicevalues = (Choice1Text,Choice1ImageURL,str(newquestionid))
                cursor.execute(newchoicessql,newchoicevalues)
                connection.commit()
                newchoices2sql = """INSERT INTO Choices(ChoiceText,ChoiceImageURL, QuestionID) VALUES(%s, %s, %s)"""
                newchoice2values = (Choice2Text,Choice2ImageURL,str(newquestionid))
                cursor.execute(newchoices2sql,newchoice2values)
                connection.commit()
            Action = 'CreatedQuestion'
            Details = str(QuestionText)
            User = session['Username']
            DateTime = str(datetime.datetime.now())
            loginsert = """INSERT INTO Log(DateTime,User,Action,Details) VALUES(%s, %s, %s, %s)"""
            logvalues = (DateTime,User,Action,Details)
            cursor.execute(loginsert,logvalues)
            connection.commit()
        return render_template('postquestionadd.html')

@app.route('/submitquestions3.php', methods=['GET','POST'])
def submitquestions3():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == 'POST':
            qdetails = request.form
            QuestionText = qdetails['QuestionText']
            QuestionClass = qdetails['QuestionClass']
            QuestionType = qdetails['QuestionType']
            QuestionGroupID = qdetails['QuestionGroup']
            Choice1Text = qdetails['Choice1Text']
            Choice1ImageURL = qdetails['Choice1ImageURL']
            Choice2Text = qdetails['Choice2Text']
            Choice2ImageURL = qdetails['Choice2ImageURL']
            Choice3Text = qdetails['Choice3Text']
            Choice3ImageURL = qdetails['Choice3ImageURL']
            
            newquestionsql = """INSERT INTO Questions(QuestionText,QuestionClass,QuestionType,QuestionGroupID) VALUES(%s, %s, %s, %s)"""
            newquestionvalues = (QuestionText,QuestionClass,QuestionType,QuestionGroupID)
            cursor.execute(newquestionsql,newquestionvalues)
            connection.commit()
            getquestionid = """SELECT * FROM Questions ORDER BY QuestionID DESC LIMIT 1"""
            cursor.execute(getquestionid)
            results = cursor.fetchall()
            QuestionID = ''
            for row in results:
                newquestionid = row[0]
                QuestionID = newquestionid
                newchoicessql = """INSERT INTO Choices(ChoiceText,ChoiceImageURL, QuestionID) VALUES(%s, %s, %s)"""
                newchoicevalues = (Choice1Text,Choice1ImageURL,str(newquestionid))
                cursor.execute(newchoicessql,newchoicevalues)
                connection.commit()
                newchoices2sql = """INSERT INTO Choices(ChoiceText,ChoiceImageURL, QuestionID) VALUES(%s, %s, %s)"""
                newchoice2values = (Choice2Text,Choice2ImageURL,str(newquestionid))
                cursor.execute(newchoices2sql,newchoice2values)
                connection.commit()
                newchoices3sql = """INSERT INTO Choices(ChoiceText,ChoiceImageURL, QuestionID) VALUES(%s, %s, %s)"""
                newchoice3values = (Choice3Text,Choice3ImageURL,str(newquestionid))
                cursor.execute(newchoices3sql,newchoice3values)
                connection.commit()
            Action = 'CreatedQuestion'
            Details = str(QuestionText)
            User = session['Username']
            DateTime = str(datetime.datetime.now())
            loginsert = """INSERT INTO Log(DateTime,User,Action,Details) VALUES(%s, %s, %s, %s)"""
            logvalues = (DateTime,User,Action,Details)
            cursor.execute(loginsert,logvalues)
            connection.commit()
        return render_template('postquestionadd.html')

@app.route('/submitquestions4.php', methods=['GET','POST'])
def submitquestions4():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == 'POST':
            qdetails = request.form
            QuestionText = qdetails['QuestionText']
            QuestionClass = qdetails['QuestionClass']
            QuestionType = qdetails['QuestionType']
            QuestionGroupID = qdetails['QuestionGroup']
            Choice1Text = qdetails['Choice1Text']
            Choice1ImageURL = qdetails['Choice1ImageURL']
            Choice2Text = qdetails['Choice2Text']
            Choice2ImageURL = qdetails['Choice2ImageURL']
            Choice3Text = qdetails['Choice3Text']
            Choice3ImageURL = qdetails['Choice3ImageURL']
            Choice4Text = qdetails['Choice4Text']
            Choice4ImageURL = qdetails['Choice4ImageURL']
            
            newquestionsql = """INSERT INTO Questions(QuestionText,QuestionClass,QuestionType,QuestionGroupID) VALUES(%s, %s, %s, %s)"""
            newquestionvalues = (QuestionText,QuestionClass,QuestionType,QuestionGroupID)
            cursor.execute(newquestionsql,newquestionvalues)
            connection.commit()
            getquestionid = """SELECT * FROM Questions ORDER BY QuestionID DESC LIMIT 1"""
            cursor.execute(getquestionid)
            results = cursor.fetchall()
            QuestionID = ''
            for row in results:
                newquestionid = row[0]
                QuestionID = newquestionid
                newchoicessql = """INSERT INTO Choices(ChoiceText,ChoiceImageURL, QuestionID) VALUES(%s, %s, %s)"""
                newchoicevalues = (Choice1Text,Choice1ImageURL,str(newquestionid))
                cursor.execute(newchoicessql,newchoicevalues)
                connection.commit()
                newchoices2sql = """INSERT INTO Choices(ChoiceText,ChoiceImageURL, QuestionID) VALUES(%s, %s, %s)"""
                newchoice2values = (Choice2Text,Choice2ImageURL,str(newquestionid))
                cursor.execute(newchoices2sql,newchoice2values)
                connection.commit()
                newchoices3sql = """INSERT INTO Choices(ChoiceText,ChoiceImageURL, QuestionID) VALUES(%s, %s, %s)"""
                newchoice3values = (Choice3Text,Choice3ImageURL,str(newquestionid))
                cursor.execute(newchoices3sql,newchoice3values)
                connection.commit()
                newchoices4sql = """INSERT INTO Choices(ChoiceText,ChoiceImageURL, QuestionID) VALUES(%s, %s, %s)"""
                newchoice4values = (Choice4Text,Choice4ImageURL,str(newquestionid))
                cursor.execute(newchoices4sql,newchoice4values)
                connection.commit()
            Action = 'CreatedQuestion'
            Details = str(QuestionText)
            User = session['Username']
            DateTime = str(datetime.datetime.now())
            loginsert = """INSERT INTO Log(DateTime,User,Action,Details) VALUES(%s, %s, %s, %s)"""
            logvalues = (DateTime,User,Action,Details)
            cursor.execute(loginsert,logvalues)
            connection.commit()
        return render_template('postquestionadd.html')
    
@app.route('/query', methods=['GET'])
def query():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('query.html')

@app.route('/viewquery.php', methods=['GET','POST'])
def viewquery():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == 'POST':
            queryform = request.form
            querytext = queryform['SQL Query']
            if session['Username']=='admin':
                cursor.execute(str(querytext))
                results = cursor.fetchall()
                fieldnames = [i[0] for i in cursor.description]
                Action = 'ViewedQuery'
                Details = str(querytext)
                User = session['Username']
                DateTime = str(datetime.datetime.now())
                loginsert = """INSERT INTO Log(DateTime,User,Action,Details) VALUES(%s, %s, %s, %s)"""
                logvalues = (DateTime,User,Action,Details)
                cursor.execute(loginsert,logvalues)
                connection.commit()
                return render_template('viewquery.html', fieldnames=fieldnames, results=results)
            else:
                if not 'Users' in querytext:
                    if not 'Log' in querytext:
                        cursor.execute(str(querytext))
                        results = cursor.fetchall()
                        fieldnames = [i[0] for i in cursor.description]
                        Action = 'ViewedQuery'
                        Details = str(querytext)
                        User = session['Username']
                        DateTime = str(datetime.datetime.now())
                        loginsert = """INSERT INTO Log(DateTime,User,Action,Details) VALUES(%s, %s, %s, %s)"""
                        logvalues = (DateTime,User,Action,Details)
                        cursor.execute(loginsert,logvalues)
                        connection.commit()
                        return render_template('viewquery.html', fieldnames=fieldnames, results=results)
                    else:
                        return render_template('logquery.html')
                else:
                    return render_template('userquery.html')

@app.route('/samplequestionnaire', methods=['GET'])
def samplequestionnaire():
    query = 'SELECT * FROM QuestionGroups'
    cursor.execute(str(query))
    results = cursor.fetchall()
    GroupNames = []
    for row in results:
        QuestionGroupName = row[1]
        GroupNames.append(str(QuestionGroupName))
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('samplequestionnaire.html', GroupNames=GroupNames)
            
@app.route('/getsamplequestionnaire', methods=['GET','POST'])
def getsamplequestionnaire():
    QGN = request.args.get('QuestionGroup')
    QNUM = request.args.get('Question')
    ResLQ = 'False'
    if request.method=='POST':
        Response = request.form
        ResLQ = Response['LastQuestion']
    if ResLQ!='True':
        if QNUM!='All':
            NQNUM = int(QNUM)+1
        querytext3 = 'SELECT * FROM QuestionGroups WHERE QuestionGroupName="'+str(QGN)+'"'
        cursor.execute(str(querytext3))
        results3 = cursor.fetchall()
        Questions = []
        for row3 in results3:
            QGID = row3[0]
            querytext = 'SELECT * FROM Questions WHERE QuestionGroupID="'+str(QGID)+'"'
            cursor.execute(str(querytext))
            results = cursor.fetchall()
            n = 1
            for row in results:
                QuestionID = row[0]
                QDict = {}
                Choices = []
                QDict.update({'QuestionID': str(QuestionID)})
                QDict.update({'QuestionNumber': n})
                QDict.update({'QuestionText': str(row[1])})
                query2text = 'SELECT * FROM Choices WHERE QuestionID="'+str(QuestionID)+'"'
                cursor.execute(str(query2text))
                results2= cursor.fetchall()
                for line in results2:
                    CDict={}
                    CDict.update({'ChoiceID': str(line[0])})
                    CDict.update({'ChoiceText': str(line[1])})
                    CDict.update({'ChoiceImageURL': str(line[2])})
                    Choices.append(CDict)
                QDict.update({'Choices': Choices})
                Questions.append(QDict)
                n+=1
                
        NumOfQs = len(Questions)
        
        if QNUM=='1':
            Action = 'ViewedQuestionnaire'
            Details = str(QGN)
            User = session['Username']
            DateTime = str(datetime.datetime.now())
            loginsert = """INSERT INTO Log(DateTime,User,Action,Details) VALUES(%s, %s, %s, %s)"""
            logvalues = (DateTime,User,Action,Details)
            cursor.execute(loginsert,logvalues)
            connection.commit()
        
        return render_template('testquestionnaire.html', Questions=Questions, QGN=QGN, NQNUM=NQNUM, QNUM=QNUM, NumOfQs=NumOfQs)
    else:
        return render_template('questionnairecomplete.html')

@app.route('/getquestionnaire', methods=['GET','POST'])
def getquestionnaire():
    ResLQ = 'False'
    Res =''
    GetRes = request.args.get('Respondent')
    if GetRes!= None:
        Res = GetRes
    if request.method=='POST':
        Response = request.form
        ResCID = Response['ChoiceID']
        ResQID = Response['QuestionID']
        Res = Response['Respondent']
        ResLQ = Response['LastQuestion']
        ResDT = str(datetime.datetime.now())
        QueryRespondentSQL = 'Select * FROM Respondents WHERE RespondentName="'+Res+'"'
        cursor.execute(str(QueryRespondentSQL))
        results = cursor.fetchall()
        ResID =''
        for row in results:
            ResID+= str(row[0])
        
        if ResID=='':
            InsertResponseSQL = """INSERT INTO Respondents(RespondentName) VALUES(%s)"""
            InsertValues = (Res)
            cursor.execute(InsertResponseSQL,InsertValues)
            connection.commit()
            QueryRespondentSQL = 'Select * FROM Respondents WHERE RespondentName="'+Res+'"'
            cursor.execute(str(QueryRespondentSQL))
            results = cursor.fetchall()
            ResID =''
            for row in results:
                ResID+= str(row[0])
            
        InsertResponseSQL = """INSERT INTO Responses(RespondentID,QuestionID,ChoiceID,DateTime) VALUES(%s, %s, %s, %s)"""
        InsertValues = (ResID,ResQID,ResCID,ResDT)
        cursor.execute(InsertResponseSQL,InsertValues)
        connection.commit()
    if ResLQ!='True':
        QGN = request.args.get('QuestionGroup')
        QNUM = request.args.get('Question')
        DEV = request.args.get('Developer')
        if QNUM!='All':
            NQNUM = int(QNUM)+1
        querytext3 = 'SELECT * FROM QuestionGroups WHERE QuestionGroupName="'+str(QGN)+'"'
        cursor.execute(str(querytext3))
        results3 = cursor.fetchall()
        Questions = []
        for row3 in results3:
            QGID = row3[0]
            querytext = 'SELECT * FROM Questions WHERE QuestionGroupID="'+str(QGID)+'"'
            cursor.execute(str(querytext))
            results = cursor.fetchall()
            n = 1
            for row in results:
                QuestionID = row[0]
                QDict = {}
                Choices = []
                QDict.update({'QuestionID': str(QuestionID)})
                QDict.update({'QuestionNumber': n})
                QDict.update({'QuestionText': str(row[1])})
                query2text = 'SELECT * FROM Choices WHERE QuestionID="'+str(QuestionID)+'"'
                cursor.execute(str(query2text))
                results2= cursor.fetchall()
                for line in results2:
                    CDict={}
                    CDict.update({'ChoiceID': str(line[0])})
                    CDict.update({'ChoiceText': str(line[1])})
                    CDict.update({'ChoiceImageURL': str(line[2])})
                    Choices.append(CDict)
                QDict.update({'Choices': Choices})
                Questions.append(QDict)
                n+=1
                
        NumOfQs = len(Questions)
        
        return render_template('questionnaire.html', Questions=Questions, QGN=QGN, NQNUM=NQNUM, QNUM=QNUM, NumOfQs=NumOfQs,Res=Res)
    else:
        return render_template('questionnairecomplete.html')

@app.route('/api/getquestions', methods=['GET'])
def apigetquestions():
    QGN = request.args.get('QuestionGroup')
    querytext3 = 'SELECT * FROM QuestionGroups WHERE QuestionGroupName="'+str(QGN)+'"'
    cursor.execute(str(querytext3))
    results3 = cursor.fetchall()
    Questions = []
    for row3 in results3:
        QGID = row3[0]
        querytext = 'SELECT * FROM Questions WHERE QuestionGroupID="'+str(QGID)+'"'
        cursor.execute(str(querytext))
        results = cursor.fetchall()
        n = 1
        for row in results:
            QuestionID = row[0]
            QDict = {}
            Choices = []
            QDict.update({'QuestionNumber': n})
            QDict.update({'QuestionText': str(row[1])})
            query2text = 'SELECT * FROM Choices WHERE QuestionID="'+str(QuestionID)+'"'
            cursor.execute(str(query2text))
            results2= cursor.fetchall()
            for line in results2:
                CDict={}
                CDict.update({'ChoiceText': str(line[1])})
                CDict.update({'ChoiceImg': str(line[2])})
                Choices.append(CDict)
            QDict.update({'Choices': Choices})
            Questions.append(QDict)
            n+=1
    
    j = json.dumps(Questions)
    
    return j
    
@app.route('/api/getnextquestion', methods=['GET','POST'])
def apigetnextquestion():
    QGN = request.args.get('QuestionGroup')
    QNUM = 0
    querytext3 = 'SELECT * FROM QuestionGroups WHERE QuestionGroupName="'+str(QGN)+'"'
    cursor.execute(str(querytext3))
    results3 = cursor.fetchall()
    Questions = []
    for row3 in results3:
        QGID = row3[0]
        querytext = 'SELECT * FROM Questions WHERE QuestionGroupID="'+str(QGID)+'"'
        cursor.execute(str(querytext))
        results = cursor.fetchall()
        n = 1
        for row in results:
            QuestionID = row[0]
            QDict = {}
            Choices = []
            QDict.update({'QuestionNumber': n})
            QDict.update({'QuestionText': str(row[1])})
            query2text = 'SELECT * FROM Choices WHERE QuestionID="'+str(QuestionID)+'"'
            cursor.execute(str(query2text))
            results2= cursor.fetchall()
            for line in results2:
                CDict={}
                CDict.update({'ChoiceText': str(line[1])})
                CDict.update({'ChoiceImg': str(line[2])})
                Choices.append(CDict)
            QDict.update({'Choices': Choices})
            Questions.append(QDict)
            n+=1
    TQNUM = len(Questions)
    TQNUM1 = int(TQNUM)+1
    if request.method=='POST':
        qdetails = request.form
        pqnum = qdetails['QuestionNumber']
        QNUM += int(pqnum)+1
    if QNUM==0:
        j = json.dumps(Questions[int(QNUM)])
    elif QNUM==TQNUM1:
        j = json.dumps(['There are no more questions for this question group'])
    else:
        j = json.dumps(Questions[int(QNUM)-1])
    
    
    return j

@app.route('/api/submitallresponses', methods=['POST'])
def apisubmitallresponses():
    Response = request.form
    json.loads(Response)
    for dict in Response:
        Res = dict['Respondent']
        ResCID = dict['ChoiceID']
        ResQID = dict['QuestionID']
        ResDT = str(datetime.datetime.now())
        QueryRespondentSQL = 'Select * FROM Respondents WHERE RespondentName="'+Res+'"'
        cursor.execute(str(QueryRespondentSQL))
        results = cursor.fetchall()
        ResID =''
        for row in results:
            ResID+= str(row[0])
        
        if ResID=='':
            InsertResponseSQL = """INSERT INTO Respondents(RespondentName) VALUES(%s)"""
            InsertValues = (Res)
            cursor.execute(InsertResponseSQL,InsertValues)
            connection.commit()
            QueryRespondentSQL = 'Select * FROM Respondents WHERE RespondentName="'+Res+'"'
            cursor.execute(str(QueryRespondentSQL))
            results = cursor.fetchall()
            ResID =''
            for row in results:
                ResID+= str(row[0])
        
    InsertResponseSQL = """INSERT INTO Responses(RespondentID,QuestionID,ChoiceID,DateTime) VALUES(%s, %s, %s, %s)"""
    InsertValues = (ResID,ResQID,ResCID,ResDT)
    cursor.execute(InsertResponseSQL,InsertValues)
    connection.commit()

    
@app.route('/api/submitresponse', methods=['POST'])
def apisubmitresponse():
    Response = request.form
    Res = Response['Respondent']
    ResCID = Response['ChoiceID']
    ResQID = Response['QuestionID']
    ResDT = str(datetime.datetime.now())
    QueryRespondentSQL = 'Select * FROM Respondents WHERE RespondentName="'+Res+'"'
    cursor.execute(str(QueryRespondentSQL))
    results = cursor.fetchall()
    ResID =''
    for row in results:
        ResID+= str(row[0])
    
    if ResID=='':
        InsertResponseSQL = """INSERT INTO Respondents(RespondentName) VALUES(%s)"""
        InsertValues = (Res)
        cursor.execute(InsertResponseSQL,InsertValues)
        connection.commit()
        QueryRespondentSQL = 'Select * FROM Respondents WHERE RespondentName="'+Res+'"'
        cursor.execute(str(QueryRespondentSQL))
        results = cursor.fetchall()
        ResID =''
        for row in results:
            ResID+= str(row[0])
        
    InsertResponseSQL = """INSERT INTO Responses(RespondentID,QuestionID,ChoiceID,DateTime) VALUES(%s, %s, %s, %s)"""
    InsertValues = (ResID,ResQID,ResCID,ResDT)
    cursor.execute(InsertResponseSQL,InsertValues)
    connection.commit()

app.run()