import os
from dotenv import load_dotenv
import smtplib, ssl
import urllib.request

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmailMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonEmail(metaclass=SendEmailMeta):
    def __init__(self):
        self.msg = MIMEMultipart()
        load_dotenv()        
        self.email_from = os.getenv('email_from')
        self.password = os.getenv('password')
        
        
    def connect(self, host='http://google.com'):
        try:
            urllib.request.urlopen(host) 
            return True
        except:
            return False
          
          
    def send_email(self, email_to, text):
        if self.connect():
          context = ssl.create_default_context()
          with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.email_from, self.password)

            self.msg['Subject'] = 'Task added'
            self.msg['From'] = self.email_from
            self.msg['To'] = ", ".join([email_to])

            body = text

            self.msg.attach(MIMEText(body, 'html'))  # set to whatever text format is preferred
            server.sendmail(self.email_from, email_to, self.msg.as_string())
        else :
          print("Check your internet connection")        
