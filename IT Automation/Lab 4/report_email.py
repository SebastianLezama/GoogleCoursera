# email report
import os
import datetime
import reports
import emails

date = datetime.datetime.now
path = ''
sender = 'automation@example.com'
to = 'username@example.com'
subject = 'Upload Completed - Online Fruit Store'
body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
attachment = path + 'processed.pdf'

if __name__ == '__main__':
    reports.generate_report('processed', date, path)
    message = emails.generate_email(sender, to, subject, body, attachment)
    emails.send_email(message)
