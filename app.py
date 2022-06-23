import email
from pydoc import describe
from flask import *
import flask
from dbconnect import *
import os
from emailsend import mailsender

app=Flask(__name__)
app.secret_key="bnm"


@app.route('/',methods=['GET','POST'])
def home():
    if session.get('mode') is None:
        return render_template("login.html")
    else:
        if session['mode']=="user":
            val=selectcond("select * from complaint where email=%s",(session['email']))
            return render_template("user.html",vals=val)
        if session['mode']=="principal":

            val=selectcond("select * from complaint where solved=%s and (principal=%s or pta=%s)",("","true","true"))
            val1=selectcond("select * from complaint where solved=%s",("solved"))
            val2=selectcond("select * from complaint where solved=%s",("rejected"))
            return render_template("admin.html",vals=val,vals1=val1,vals2=val2)
        if session['mode']=="hod":
            print(session["department"])
            val=selectcond("select * from complaint where deaprtment=%s and solved=%s",(session['department'],""))
            val1=selectcond("select * from complaint where solved=%s",("solved"))
            val2=selectcond("select * from complaint where solved=%s",("rejected"))
            return render_template("admin.html",vals=val,vals1=val1,vals2=val2)
        if session['mode']=="pta":
            val=selectcond("select * from complaint where solved=%s and pta=%s",("","true"))
            val1=selectcond("select * from complaint where solved=%s",("solved"))
            val2=selectcond("select * from complaint where solved=%s",("rejected"))
            return render_template("admin.html",vals=val,vals1=val1,vals2=val2)
        if session['mode']=="":
             return render_template("login.html")        

@app.route('/login',methods=['POST','GET'])
def login():
    email=request.form['email']
    password=request.form['pwd']
    val=selectonecond("select * from login where email=%s and pass=%s",(email,password))
    if val!=None:
        session['email']=email
        session['mode']=val[4]
        return redirect('/')

    val=selectonecond("select * from hod where email=%s and pass=%s",(email,password))
    if val!=None:
        session['email']=email
        session['mode']=val[4]
        session['department']=val[5]
        return redirect('/')
    val=selectonecond("select * from admins where email=%s and pass=%s",(email,password))
    if val!=None:
        session['email']=email
        session['mode']=val[4]
        return redirect('/')
    msg="Invalid email or password"
    return render_template("login.html",msg=msg)


@app.route('/reg',methods=['POST','GET'])
def reg():
    email=request.form['email']
    password=request.form['pwd']
    gander=request.form['gander']
    name=request.form['name']
    val=iud("insert into login values(%s,%s,%s,%s,%s)",(email,name,gander,password,"user"))
    session['email']=email
    session['mode']="user"
    return redirect('/')

@app.route('/complaintsubmit',methods=['POST','GET'])
def complaintsubmit():
    if 'subject' not in request.form:
            return redirect('/')
    email=session['email']
    describe=request.form['subject']
    department=request.form['department']
    sub=request.form['sub']
    val=iud("insert into complaint(email,deaprtment,subject,description,hod,principal,pta,status) values(%s,%s,%s,%s,%s,%s,%s,%s)",(email,department,sub,describe,"true","false","false","Not viewed"))
    val=selectcond("select * from complaint where email=%s",(session["email"]))
    val2=selectonecond("select * from hod where department=%s",(department))
    s="from:"+email+"\n"+"department:"+department+"\n"+"complaint:"+describe
    mailsender(val2[1],s)
    return render_template("user.html",msg="Successfully submitted",vals=val)

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/logout',methods=['POST','GET'])
def logout():
    del session['email']
    del session['mode']
    return redirect('/')

@app.route('/complaint')
def complaint():
    return render_template("complaint.html")


@app.route('/viewc/<id>')
def view(id):
    val=selectonecond("select * from complaint where id=%s",(id))
    if(val[7]=="Not viewed"):
        iud("update complaint set status=%s where id=%s",(session['mode']+" viewed..",id))
    if session['mode']=="hod":
        if val[5]=="true":
            
            return render_template("view.html",val=val,p="true",)
        else:
            return render_template("view.html",val=val,p="false")
    if session['mode']=="principal":
        if val[6]=="true":
            return render_template("view.html",val=val,p="true")
        else:
            return render_template("view.html",val=val,p="false")
    if session['mode']=="pta":
        if val[7]=="true":
            return render_template("view.html",val=val,p="true")
        else:
            return render_template("view.html",val=val,p="false")


@app.route('/solved/<id>')
def solved(id):
    val=iud("update complaint set status=%s,solved=%s where id=%s",(session['mode']+" solved","solved",id))
    val2=selectonecond("select * from complaint where id=%s",(id))
    mailsender(val2[1],"complaint solved complaint id:"+id)
    return redirect('/')


@app.route('/Canceled/<id>')
def Canceled(id):
    val=iud("update complaint set status=%s,solved=%s where id=%s",(session['mode']+" rejected","rejected",id))
    val2=selectonecond("select * from complaint where id=%s",(id))
    mailsender(val[1],"complaint is rejected complaint id:"+id)
    return redirect('/')


@app.route('/sabove/<id>')
def sabove(id):
   
    if session['mode']=="hod":
        val=iud("update complaint set status=%s,hod=%s,principal=%s where id=%s",(session['mode']+" Send to Above","false","true",id))
        val2=selectcond("select * from complaint where id=%s",(id))
        val3=selectonecond("select * from admin where mode=pta")
        mailsender(val3[1],s)
        return redirect('/')
    if session['mode']=="principal":
        val=iud("update complaint set status=%s,principal=%s,pta=%s where id=%s",(session['mode']+" Send to Above","false","true",id))
        val2=selectcond("select * from complaint where id=%s",(id))
        s="from:"+val2[1]+"\n"+"department:"+val2[2]+"\n"+"complaint:"+val2[4]
        val3=selectonecond("select * from admin where mode=principal")
        mailsender(val3[1],s)
        return redirect('/')



if __name__ == "__main__":
  app.run(debug=True)