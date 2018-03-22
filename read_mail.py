import smtplib
import time
import imaplib
import email
import MySQLdb
import re


ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "ar10695" + ORG_EMAIL
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993    


mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL,FROM_PWD)
mail.select('INBOX')
type, data = mail.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.split() 
latest_email_id = int(id_list[-1])


type, data = mail.fetch(latest_email_id, '(RFC822)' )
fw=open("mail_write","w")
for response_part in data:
    if isinstance(response_part, tuple):
        msg = email.message_from_string(response_part[1])
        email_subject = msg['subject']
        email_from = msg['from']
        print 'From : ' + email_from + '\n'
        print 'Subject : ' + email_subject + '\n'
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                fw.write(part.get_payload())
fw.close()
