from flask import Flask,request,render_template
from collections import Counter
#from mail import send
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def rootpage():
    a = ''
    b = ''
    p = ''
    lst=''
    z=''
    em=''
    if request.method == 'POST' and 'uname' in request.form:
        a = request.form.get('uname')
        b = request.form.get('oname')
        z=b
        lst=a+b
        #em=send(lst)
        a=a.lower()
        b=b.lower()
        a=list(a)
        b=list(b)
        res1=list((Counter(a)-Counter(b)).elements())
        res2=list((Counter(b)-Counter(a)).elements())
        c=len(res1)+len(res2)
        if c==3 or c==5:
            p='is your crime partner'
        elif c==10:
            p="secretly loves you"
        elif c==8 or c==12 or c==13:
            p="always attracted by you"
        elif c==6 or c==11:
            p="gonna marry you soon"
        elif c==2 or c==4 or c==7 or c==9:
            p="is your sworn enemies"
        elif c==1:
            p="shares womb with you"
        else:
            p="ERROR 404 : match not found"
    return render_template("index.html",
                            k=p,z=z,em=em)