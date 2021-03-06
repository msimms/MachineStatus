# MIT License
# 
# Copyright (c) 2018 Mike Simms
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Utility module, providing routines for sending emails, text messages, etc."""

import smtplib

def send_sms(to, msg):
    """Sends an SMS message. Not implemented yet."""
    pass

def send_email(from_addr, to_addr, msg, username, password, server):
    """Connects to an SMTP server using TLS to send an email."""
    msg = "To:" + to_addr + "\r\nFrom: " + from_addr + "\r\nSubject:New IP Address\r\n\r\n" + msg + "\r\n\r\n"

    server = smtplib.SMTP(server + ':587')
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr, to_addr, msg)
    server.quit()
