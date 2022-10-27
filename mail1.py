import csv, smtplib, ssl

# message = """Subject: Spardha Volunteer Certificate

# Hi {name}, Thank you for your participation"""
# from_address = "acm.vvit@gmail.com"
# password = 'izmmlqqgyitnnqjw'

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#     server.login(from_address, password)
#     with open("C:\\Users\\manoj\\Downloads\\mk.csv") as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header row
#         for name, mail in reader:
#             server.sendmail(
#                 from_address,
#                 mail,
#                 message.format(name=name),
#             )
# Python code to illustrate Sending mail with attachments
# from your Gmail account 
  
# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
   
fromaddr = "acm.vvit@gmail.com"
print(1)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
print(2)

# start TLS for security
s.starttls()
print(3)

# Authentication
s.login("acm.vvit@gmail.com", "nmadkmgnapqouago")
with open("C:\\Users\\alekh\\Downloads\\AAVEGA REVERSE CODING PARTICIPATION LIST.csv") as file:
    reader = csv.reader(file)
    print(4)
    next(reader)  # Skip header row
    for mail,name in reader:
        # server.sendmail(
            #from_address,
        #     mail,
        #     message.format(name=name),
        # )
        
# instance of MIMEMultipart
            msg = MIMEMultipart()
            print(5)
        # storing the senders email address  
            msg['From'] = "VVIT ACM"
            print(6)
            fromaddr="acm.vvit@gmail.com"
        
        # storing the receivers email address 
            msg['To'] = mail
            print(7)
        
        # storing the subject 
            msg['Subject'] = "Aavega Participation Certificate"
        
        # string to store the body of the mail
            body = '''Gratitude for your participation in Riches Rummage from ACM VVIT.'''
        
        # attach the body with the msg instance
            msg.attach(MIMEText(body, 'plain'))
            
        
        # open the file to be sent 
            filename = name+'.pdf'
            attachment = open("C:\\Users\\alekh\\Downloads\\vollkorn\\"+filename, "rb")
        
        # instance of MIMEBase and named as p
            p = MIMEBase('application', 'octet-stream')
        
        # To change the payload into encoded form
            p.set_payload((attachment).read())
        
        # encode into base64
            encoders.encode_base64(p)
        
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        
        # attach the instance 'p' to instance 'msg'
            msg.attach(p)
    
        # Converts the Multipart msg into a string
            text = msg.as_string()
            
        # sending the mail
            s.sendmail(fromaddr, mail, text)
            print("Mail has been sent to {}".format(mail))
            
            
        # terminating the session
s.quit()
