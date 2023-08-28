import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",passwd="123456",database="school")
mycursor=mycon.cursor()

def qualified():
    qu="create table qualified (name char(50),mark int)"
    mycursor.execute(qu)
    mycon.commit()
    
def admin():
    qu="create table admin(name char(70),workid int)"
    mycursor.execute(qu)
    mycon.commit()

def admininsert():
    q1="insert into admin values('ashok',101010)"
    q2="insert into admin values('rithik',103003)"
    q3="insert into admin values('preeti',123233)"
    q4="insert into admin values('preeti',123233)"
    q5="insert into admin values('uma',763823)"
    q6="insert into admin values('kumar',948593)"
    mycursor.execute(q1,q2,q3,q4,q5,q6)
    mycon.commit()

    
def createevent():
    q="create table events (volunteertype char(90),eventname char(90),companyorganised char(90),number int)"
    mycursor.execute(q)
    mycon.commit()
    

def create():
    qu="create table draft2 (name char(50),username char(50),password int,age int,country char(90),city char(90),nationality char(90),emailid char(70),phoneno int)"
    mycursor.execute(qu)
    mycon.commit()

def create3():
    q="create table schedeule (username char(90),enrolledevents char(90),attended char(4))"
    mycursor.execute(q)
    mycon.commit()

def createaccount():
    n=input("enter your name")
    q="select name from qualified"
    mycursor.execute(q)
    d=mycursor.fetchall()
    for i in d:
        if i==(n,):
            print("Congrats! you have successfully passed the quiz. Enter your details and make your account!")
            name=input("enter the name:")
            username=input("enter the username-can be alphanumeric:")
            password=int(input("enter the password-numeric passwords only!:"))
            age=int(input("enter the age:"))
            country=input("enter the country of residence:")
            city=input("enter the city of residence:")
            nationality=input("enter your nationality:")
            emailid=input("enter your email id for updates!:")
            phoneno=int(input("enter your phone number:"))
            qu="insert into draft2 values('{}','{}',{},{},'{}','{}','{}','{}',{})".format(name,username,password,age,country,city,nationality,emailid,phoneno)
            mycursor.execute(qu)
            mycon.commit()
            print("account succesfully created!")
            break
        
        
        
def signin():
    print("please SIGN IN")
    ask=input("enter your username:")
    take=int(input("enter your password:"))
    qu="select username from draft2 where username='{}' and password= {}".format(ask,take)
    mycursor.execute(qu)
    data=mycursor.fetchall()
    for i in data:
        if i==(ask,):
            print("successfully authorised!")
            ans='y'
            while ans=='y':
                print("enter 1 to view profile")
                print("enter 2 to update profile")
                print("enter 3 to see your schedeule")
                ch=int(input("enter your choice"))
                if ch==1:
                    qu="select * from draft2 where username='{}'".format(ask)
                    mycursor.execute(qu)
                    data=mycursor.fetchall()
                    for i in data:
                        print(i)
                    ans=input("do you want to continue using your profile?(y/n)")
                if ch==2:
                    print("enter 1 to change your age")
                    print("enter 2 to change ur username")
                    print("enter 3 to change your country of residence" )
                    print("enter 4 to change your city of residence" )
                    print("enter 5 to change your phone number")
                    ch2=int(input("enter ur choice:"))
                    if ch2==1:
                        age1=int(input("enter new age:"))
                        qu="update draft2 set age={} where username='{}'".format(age1,ask)
                        mycursor.execute(qu)
                        mycon.commit()
                        ans=input("do you want to continue using your profile?(y/n)")
                
                    if ch2==2:
                        user=input("enter the new username:")
                        qu="update draft2 set username='{}' where username='{}')".format(user,ask)
                        mycursor.execute(qu)
                        mycon.commit()
                        ans=input("do you want to continue using your profile?(y/n)")
                    if ch2==3:
                        country=input("enter your updated country of residence:")
                        q="update draft2 set country='{}' where username='{}'".format(country,ask)
                        mycursor.execute(q)
                        mycon.commit()
                        ans=input("do you want to continue using your profile?(y/n)")
                    if ch2==4:  
                        city=input("enter your updated country of residence:")
                        q="update draft2 set city='{}' where username='{}'".format(city,ask)
                        mycursor.execute(q)
                        mycon.commit()
                        ans=input("do you want to continue using your profile?(y/n)")
                    if ch2==5:
                        phoneno=input("enter your updated country of residence:")
                        q="update draft2 set phoneno='{}' where username='{}'".format(phoneno,ask)
                        mycursor.execute(q)
                        mycon.commit()
                        ans=input("do you want to continue using your profile?(y/n)")
                if ch==3:
                    w="select enrolledevents,attended from schedeule where username='{}'".format(ask)
                    mycursor.execute(w)
                    data=mycursor.fetchall()
                    for i in data:
                        print(i)
                    ans=input("do you want to continue using your profile?(y/n)")
        else:
             print("wrong data!")
             break
       

def insertintoevents():
    ans="y"
    while ans=="y":
        volunteertype=input("enter the volunteer type of the event:")
        eventname=input("enter the eventname:")
        companyorganised=input("enter the company organising:")
        number=int(input("enter the number of volunteers avaliable:"))
        q="insert into events values('{}','{}','{}',{})".format(volunteertype,eventname,companyorganised,number)
        mycursor.execute(q)
        mycon.commit()
        ans=input("do you want to continue?")
    

    

def events():
    print("please SIGN IN")
    ask=input("enter your username:")
    take=int(input("enter your password:"))
    qu="select username from draft2 where username='{}' and password= {}".format(ask,take)
    mycursor.execute(qu)
    data=mycursor.fetchall()
    for i in data:
        if i==(ask,):
            print("successfully authorised!")
            print()
            print("WELCOME TO EVENTS SECTION!")
            print()
            print("you have medical volunteering opportunities,public service volunteering,charity volunteering,old age home volunteering and business vounterring avaliable!")
            print()
            
            ch=input("enter the area of volunteering you interested in:")
            q="select * from events where volunteertype='{}'".format(ch)
            mycursor.execute(q)
            data=mycursor.fetchall()
            for i in data:
                print(i)
            print("are you interested in enrolling yourself in any of the events?")
            ch=input("enter your choice if your interested in enrolling? (y/n)")
            if ch=="y":
                eventname=input("enter the event name you interested in enrolling:")
                q1="update events SET number=number-1 where eventname='{}'".format(eventname)
                mycursor.execute(q1)
                mycon.commit()
                q2="insert into schedeule values('{}','{}',NULL)".format(ask,eventname)
                mycursor.execute(q2)
                mycon.commit()
                print("congrats!, ur enrolled!")
                
        else:
            print("sorry,wrong data entered")
            break
    
            
def detailsofeventtable():
    q="create table detailsofevent (eventname char(90),detail char(90),companyorganised char(90),time char(90),location char(90))"
    mycursor.execute(q)
    mycon.commit()


def insertintodetailsofevents():
    event=input("enter the eventname")
    detail=input("enter the details of the event")
    company=input("enter the company organised")
    time=input("enter the time of event")
    location=input("enter the location of event")
    q="insert into detailsofevent values('{}','{}','{}','{}','{}')".format(event,detail,company,time,location)
    mycursor.execute(q)
    mycon.commit()
    
def quiz():
    print("Welcome! you are needed to pass this quiz for being able to make an account")
    print("INSTRUCTIONS")
    print("1. There are a total of 5 questions which are multiple choice type")
    print("you gain 1 point for every right answer and -1 for every wrong answer")
    print("3.you have to enter the right options number")
    print("4.you have to get 4 points to pass")
    print("all the best !")
    name=input("enter your name")
    count=0
    print("question1: what is the full form of NGO?")
    print("options:")
    print("1) national geographical organisation")
    print("2) national union organisation")
    print("3) non governement organisation")
    q=int(input("enter the correct option:"))
    if q==3:
        print("Correct!")
        count=count+1
    else:
        print("incorrect!")
        count=count-1
    print("question2: what doesnt biosphere consist of?")
    print("options:")
    print("1)water")
    print("2)plastics")
    print("3)land")
    q=int(input("enter the correct option:"))
    if q==2:
        print("Correct!")
        count=count+1
    else:
        print("incorrect!")
        count=count-1
    print("question3:This organisation works in how many countries?")
    print("options:")
    print("1)15")
    print("2)20")
    print("3)35")
    q=int(input("enter the correct option:"))
    if q==2:
        print("Correct!")
        count=count+1
    else:
        print("incorrect!")
        count=count-1
    print("question5: Why do you wish to become a volunteer?")
    print("options:")
    print("1)to earn certificate")
    print("2)to get into good college")
    print("3)to help needy people and build a healthy society")
    q=int(input("enter the correct option:"))
    if q==3:
        print("Correct!")
        count=count+1
    else:
        print("incorrect!")
        count=count-1
    print("question5:which of the following is not an ngo in india?")
    print("options:")
    print("1)katha")
    print("2)make a wish")
    print("3)karuna trust")
    q=int(input("enter the correct option:"))
    if q==2:
        print("Correct!")
        count=count+1
    else:
        print("incorrect!")
        count=count-1
    print("The quiz has been compeleted!")
    print("you score is:",count)
    if count>=4:
        print("congrats, your qualified!")
        print("now you can create an account")
        qu="insert into qualified values('{}',{})".format(name,count)
        mycursor.execute(qu)
        mycon.commit()
    else:
        print("sorry!you didnt make it.try again :)")
        
def adminlogin():
    name=input("Enter your name:")
    workid=int(input("Enter your work id:"))
    qu="select * from admin"
    mycursor.execute(qu)
    d=mycursor.fetchall()
    for i in d:
        if i==(name,workid):
            print("successfully logged in")
            ans='y'
            while ans=='y':
                print("Enter 1 to insert into events")
                print("Enter 2 to delete a student record")
                print("Enter 3 to view a student records based on conditions")
                ch=int(input("enter the choice:"))
                if ch==1:
                    insertintoevents()
                    ans=input("do you want to continue using your profile(y/n):")
                if ch==2:
                    name=input("enter the name of student whose records are to be deleted")
                    qu="delete from draft2 where name='{}'".format(name)
                    mycursor.execute(qu)
                    mycon.commit()
                    ans=input("do you want to continue using your profile(y/n):")
                if ch==3:
                    print("enter 1 to view all profiles") 
                    print("enter 2 to view based on country of residence")
                    print("enter 3 to view based on city")
                    ch2=int(input("enter your choice:"))
                    if ch2==1:
                        qu="select * from draft2"
                        mycursor.execute(qu)
                        a=mycursor.fetchall()
                        for i in a:
                            print(i)
                        ans=input("do you want to continue using your profile(y/n):")
                    if ch2==2:
                        country=input("enter the country you want to search on:")
                        qu="select * from draft2 where country='{}'".format(country)
                        mycursor.execute(qu)
                        b=mycursor.fetchall()
                        for i in b:
                            print(i)
                        ans=input("do you want to continue using your profile(y/n):")
                    if ch2==3:
                        city=input("enter the city you want to search on:")
                        qu="select * from draft2 where city='{}'".format(city)
                        mycursor.execute(qu)
                        b=mycursor.fetchall()
                        for i in b:
                            print(i)
                        ans=input("do you want to continue using your profile(y/n):")
                
def intro():
    print("Welcome to our website!")
    print("Our aim is to help the needy and build up skilled volunteers which in future will serve as responsible citizens.")
    print("We operate in about 20 countries,where we do book fests and various other activities to gather money which is then delievered to people in need.")
    print("you can help contribute to our mission! All you have to do is sign up and help us :))")
                
        

     
print("you can create your account(only if you passed the quiz),sign up and view all the upcoming events and make this world a better place!")
ans="y"
while ans=="y":
    print("Enter 1 to know more about us and our mission ")
    print("Enter 2 to write the quiz")
    print("Enter 3 to create a account")
    print("Enter 4 to sign in")
    print("Enter 5 to view events and enroll")
    print("Enter 6 to admin sign in")
    ch=int(input("enter your choice"))
    if ch==1:
        intro()
        ans=input("do you want to continue using website?(y/n)")
    if ch==2:
        quiz()
        ans=input("do you want to continue using website?(y/n)")
    if ch==3:
        createaccount()
        ans=input("do you want to continue using website?(y/n)")
    if ch==4:
        signin()
        ans=input("do you want to continue using website?(y/n)")
    if ch==5:
        events()
        ans=input("do you want to continue using website?(y/n)")
    if ch==6:
        adminlogin()
        ans=input("do you want to continue using website?(y/n)")
    else:
        print("thanks for using our website!")
        
