# generate pdf report
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(filename, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    empty_line = "<br/><br/>"
    report_title = Paragraph(title + empty_line, styles["h1"])
    template = [report_title]
    for item in paragraph:
        weight = "weight: " + str(item['weight']) + " lbs"
        text = "name: " + item['name'] + "<br/>" + weight + empty_line
        info = Paragraph(text, styles["BodyText"])
        template.append(info)
    report.build(template)
