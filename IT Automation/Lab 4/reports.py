# generate pdf report
from run import batch_db_to_web_service
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(filename, date, path):
    dict = batch_db_to_web_service(path)
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph("Processed Update on" + date, styles["h1"])
    empty_line = '<br/>'
    template = [report_title, empty_line]
    for item in dict:
        first_line = Paragraph("name: " + item['name'], styles["BodyText"])
        second_line = Paragraph("weight: " + item['weight'] + " lbs", styles["BodyText"])
        template.append(first_line, second_line, empty_line)
    report.build(template)
