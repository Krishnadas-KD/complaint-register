import smtplib


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER ='collegecomplaint512@gmail.com'
EMAIL_HOST_PASSWORD = '**************'

def mailsender(Email,text):
    smtpserver=smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
    SUBJECT="new Job added"
    TEXT=text
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    smtpserver.sendmail(EMAIL_HOST_USER,Email,message)
    smtpserver.close()

