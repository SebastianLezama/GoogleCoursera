from email.message import EmailMessage
import os.path
import mimetypes
import smtplib
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

# Categories of sales.
# Generate a PDF
# Mail pdf.
#

message = EmailMessage()
sender = 'slezama.dev@gmail.com'
recipient = 'sebastian.lezama@gmail.com'
message['From'] = sender
message['To'] = recipient
subject = 'Test'
message['Subject'] = subject
mail_body = """Hello fellow Dev!

Rock on!"""
message.set_content(mail_body)


"""
attachment_path = './report.pdf' # example.png
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path) # image/png -> type/subtype
mime_type, mime_subtype = mime_type.split('/', 1) # image png

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(), 
                        maintype=mime_type,
                        subtype=mime_subtype,
                        filename=attachment_filename)
"""

mail_server = smtplib.SMTP_SSL('smtp.gmail.com', port=465)

mail_pass = 'bphzsthldfxxfxjs'
mail_server.login(sender, mail_pass) # returns tuple of status, u need to handle smtp auth error exception
mail_server.send_message(message) # returns dict of unreached receipients
mail_server.quit()
