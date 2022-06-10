
import smtplib
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

from process import generate_summary
from settings import *


SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 587
SMTP_USERNAME = MAIL
SMTP_PASSWORD = PASSWORD
EMAIL_FROM = MAIL
EMAIL_TO = "example@gmail.com"
EMAIL_SUBJECT = "Cebolla project Update"


def send_email(to:str):


    attachments = ["logs/moistures.png","logs/humidity.png","logs/temperature.png"]

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = EMAIL_SUBJECT
    msgRoot['From'] = EMAIL_FROM 
    msgRoot['To'] = to
    #msgRoot['Cc'] =cc
    msgRoot.preamble = 'Multi-part message in MIME format.'

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('Alternative plain text message.')
    msgAlternative.attach(msgText)

    msgText = MIMEText('<b>Your update on the Plants status. <br><img src="cid:image1"><br><img src="cid:image2"><br><img src="cid:image3"><br>', 'html')
    msgAlternative.attach(msgText)

    #Attach Image 
    fp = open("logs/moistures.png", 'rb') #Read image 
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    fp = open("logs/humidity.png", 'rb') #Read image 
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image2>')
    msgRoot.attach(msgImage)

    fp = open("logs/temperature.png", 'rb') #Read image 
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image3>')
    msgRoot.attach(msgImage)

    #debuglevel = True
    debuglevel = False
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.set_debuglevel(debuglevel)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msgRoot.as_string())
    mail.quit()

if __name__=='__main__':
    generate_summary("all")
    for to in EMAIL_TO:
        send_email(to)
        break
