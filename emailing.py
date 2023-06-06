import smtplib
import imghdr
from email.message import EmailMessage

password = "ydwkxrilrjmluedd"
sender = "tanishkmalhotra190804@gmail.com"
receiver = "tanishkvmalhotra@gmail.com"

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Person found!"
    email_message.set_content("Hey, a person was spot on the camera.")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content), filename="image")

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, receiver, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email()
