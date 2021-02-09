import smtplib
import socket
socket.setdefaulttimeout(30)
def send(msg):
    try:
        sender="flames123@gmail.com"
        recevier="your mail-ID"
        pswrd="lbemgukarpljllys"
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender,pswrd)
        server.sendmail(sender,recevier,msg)
        server.quit()
        return 'success'
    except:
        return "fail"
