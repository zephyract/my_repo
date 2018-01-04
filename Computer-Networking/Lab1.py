#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from email.mime.text import MIMEText
from smtplib import SMTP
import pdb

sender = ""
mail_user = ""
mail_auth = ""
smtp_host = ""
receivers = []

def get_sender_and_host():
    global sender, mail_auth, mail_user, smtp_host
    sender = raw_input("Sender: (Support qq and 163)")
    mail_auth = raw_input("Authorization Code: ")
    
    if sender.endswith("@163.com"):
        smtp_host = "smtp.163.com"
        mail_user = sender[: -8]
    elif sender.endswith("@qq.com"):
        smtp_host = "smtp.qq.com"
        mail_user = sender[: -7]
    else:
        print "\n[*]Not a supported email format!\n"
        exit


def get_receivers():
    global receivers
    cnt = 1
    while True:
        tmp = raw_input("Reveiver #%d (type over to end input)" % cnt)
        if tmp == "over":

            if len(receivers) < 1:
                print "1 receiver at least!"
                continue

            print "\n[*] %d receivers in all.\n" % (cnt - 1)
            break

        receivers.append(tmp)
        cnt += 1

def get_subject_and_content():
    subject = raw_input("Subject: ")
    content = raw_input("Content: ")

    message = MIMEText(content, "plain", "utf-8")
    message["From"] = sender
    message["Subject"] = subject
    
    return message

def send_email(message):
    server = SMTP()
    #  pdb.set_trace()
    server.connect(smtp_host, 25)
    server.login(mail_user, mail_auth)

    try:
        for receive in receivers:
            message["To"] = receive
            server.sendmail(sender, [receive], message.as_string())

    except Exception as e:
        print "\n[*]Error!\n"
        print e
        exit

    server.quit()
    print "\n[*]email sent succeed!\n"
    

if __name__ == "__main__":
    #  pdb.set_trace()
    get_sender_and_host()
    get_receivers()
    message = get_subject_and_content()
    send_email(message)

