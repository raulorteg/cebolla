import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import typer

from cebolla.process import generate_summary
from cebolla.settings import *
from cebolla.utils import get_username

SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 587
SMTP_USERNAME = MAIL
SMTP_PASSWORD = PASSWORD
EMAIL_FROM = MAIL
EMAIL_SUBJECT = "Cebolla project Update"
app = typer.Typer()


@app.command()
def send_email(to: str):

    attachments = ["moistures.png", "humidity.png", "temperature.png"]
    attachments = [join(LOGGER_DIRECTORY, at) for at in attachments]

    msgRoot = MIMEMultipart("related")
    msgRoot["Subject"] = EMAIL_SUBJECT
    msgRoot["From"] = EMAIL_FROM
    msgRoot["To"] = to
    # msgRoot['Cc'] =cc
    msgRoot.preamble = "Multi-part message in MIME format."

    msgAlternative = MIMEMultipart("alternative")
    msgRoot.attach(msgAlternative)

    msgText = MIMEText("Alternative plain text message.")
    msgAlternative.attach(msgText)

    msgText = MIMEText(
        f'''
        Dear {get_username()}, <br>
        Here is your update on the Plants status.
        <br>
        Please note you cant unsuscribe from this service, this is not
        optional. >:)
        <br>
        <br><img src="cid:image1"><br>
        <img src="cid:image2"><br>
        <img src="cid:image3"><br>
        ''',
        "html",
    )
    msgAlternative.attach(msgText)

    # Attach Image
    for i, attachment in enumerate(attachments):
        with open(attachment, "rb") as fp:
            msgImage = MIMEImage(fp.read())

        # Define the image's ID as referenced above
        msgImage.add_header("Content-ID", f"<image{i+1}>")
        msgRoot.attach(msgImage)

    debuglevel = False
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.set_debuglevel(debuglevel)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, to, msgRoot.as_string())
    mail.quit()


if __name__ == "__main__":
    generate_summary("week")
    app()
