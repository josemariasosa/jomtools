#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Email MIME type: plain text
#
from email.mime.text import MIMEText
from utils.config import MAIL
import smtplib


class Mail():
    def __init__(self, subject, to_addrs, message):
        self.server = MAIL["SERVER"]
        self.port = MAIL["PORT"]
        self.username = MAIL["USERNAME"]
        self.password = MAIL["PASSWORD"]
        self.auth = MAIL["AUTH"]

        self.from_addr = MAIL["FROM"]
        self.to_addrs = to_addrs

        self.message = MIMEText(message)
        self.message["Subject"] = subject
        self.message["From"] = self.from_addr
        self.message["To"] = ", ".join(self.to_addrs)

    def send(self):
        smtp = smtplib.SMTP(self.server, self.port)
        if self.auth:
            smtp.login(self.username, self.password)
        smtp.sendmail(self.from_addr, self.to_addrs, self.message.as_string())
        return smtp.quit()
