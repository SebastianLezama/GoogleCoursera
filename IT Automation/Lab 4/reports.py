# generate pdf report
from run import batch_db_to_list
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(filename, title, path_data):
    dict = batch_db_to_list(path_data)
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    empty_line = "<br/><br/>"
    ttle = title + empty_line
    report_title = Paragraph(ttle, styles["h1"])
    template = [report_title]
    for item in dict:
        text = "name: " + item['name'] + "<br/>" + "weight: " + str(item['weight']) + " lbs" + empty_line
        info = Paragraph(text, styles["BodyText"])
        template.append(info)
    report.build(template)
