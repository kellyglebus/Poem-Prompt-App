import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

#load env variables
load_dotenv()

def send_texts():
    print('hey hey hey')
    #Access the variables
    # sender_email = os.getenv("SENDER_EMAIL")
    # sender_password = os.getenv("SENDER_PASSWORD")
    # receiver_email = ""