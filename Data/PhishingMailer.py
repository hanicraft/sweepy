import MySQLdb
import smtplib
import commands
import time
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import urllib2

def send_mail(server,from_address,to_address,subject):
	msg = MIMEMultipart()
	msg['From'] = from_address
	msg['To'] = to_address
	msg['Date'] = formatdate(localtime=True)
	msg['Subject'] = subject
	body="""
EMAIL CONTENT GOES IN HERE
"""
	msg.attach(MIMEText(body))
	smtp = smtplib.SMTP(server)
	smtp.sendmail(from_address, to_address, msg.as_string())
	smtp.close()

server = input("Enter Server (For Example 192.168.0.100) : ")
from_address = input("Enter Address For Sending (For Example John Smith <john.smith@example.com>) : ")
subject = input("Enter Subject/Email Title (For Example PayPal Verifacation) : ")
 
addresses = ["John Doe <John.Doe@targetdomain.co.uk>"," Jane Doe <Jane.Doe@targetdomain.co.uk >"]
 
for to_address in addresses:
	print("[*] Sending Mail To "+to_address)
	send_mail(server,from_address,to_address,subject)
	time.sleep(10)