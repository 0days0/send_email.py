import smtplib,ssl

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

sender_email = "CHANGE" #Gönderen 
receiver_email = "CHANGE" #Alıcı

text = "CHANGE" #Gönderilecek mesaj

message = MIMEMultipart()
message["From"] = sender_email
message["To"]   = receiver_email
message["Subject"] = "CHANGE"

message.attach(MIMEText(text, "plain"))
filepath = "CHANGE" #Gönderilecek dosya yolu
part = MIMEBase("application", "octet-stream")
part.set_payload(open (filepath, "rb").read())
encoders.encode_base64(part)

part.add_header("Content-Disposition", "attachment; filename ='CHANGE' ") #Filename gönderilen dosyanın ismini istediğimiz şekilde değiştiriyoruz
message.attach(part)

context = ssl.create_default_context()
server = smtplib.SMTP("CHANGE", PORT) #SMTP ve port bilgisi girilir
server.starttls()
server.ehlo_or_helo_if_needed() #ESMTP sunucusuna kendimizi tanıtıyoruz.
server.sendmail(
        sender_email, receiver_email, message.as_string())
print("Message Sent..")