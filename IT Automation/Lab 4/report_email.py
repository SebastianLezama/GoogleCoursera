# email report
import os
from datetime import datetime
import reports
import emails

time = str(datetime.now())
date = "{}".format(time[:10])
title = "Processed Update on " + date
path = '~/supplier-data/descriptions/'
sender = 'automation@example.com'
to = 'username@example.com'
subject = 'Upload Completed - Online Fruit Store'
body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
attachment = '/tmp/processed.pdf'

if __name__ == '__main__':
    reports.generate_report(attachment, title, path)
    message = emails.generate_email(sender, to, subject, body, attachment)
    emails.send_email(message)
