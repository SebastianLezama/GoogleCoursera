import json
import locale
import sys
import os

import emails
import reports
from operator import itemgetter
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie


def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(
        car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    """Analyzes the data, looking for maximums.

    Returns a list of lines that summarize the information.
    """
    max_revenue = {"revenue": 0}
    max_sales = {"total_sales": 0}
    year = {}

    for item in data:
        # Calculate the revenue generated by this model (price * total_sales)
        # We need to convert the price from "$1234.56" to 1234.56
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item
        # TODO: also handle max sales
        if item["total_sales"] > max_sales["total_sales"]:
            max_sales = item

        # TODO: also handle most popular car_year
        car_y = item["car"]["car_year"]
        year[car_y] = year.get(car_y, 0) + 1
        most_popular_year = max(year, key=year.get)
        mpy_sales = year[most_popular_year]
        summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), str("$"+"{:,.2f}".format(max_revenue["revenue"]))),
        "The {} had the most sales: {}".format(format_car(max_sales["car"]), max_sales["total_sales"]),
        "The most popular year was {} with {} sales.".format(most_popular_year, mpy_sales)
        ]

    return summary


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = []
    for item in car_data:
        table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
    # Sorted table_data by total_sales.
    table_data = sorted(table_data, key=itemgetter(3), reverse=True)
    return table_data

def cars_table_to_piechart(car_data):
    """Turns table_data to a pie chart."""
    report_pie = Pie(width=3, height=3)
    report_pie.data = []
    report_pie.labels = []
    report_pie.width = 120
    report_pie.height = 120
    report_pie.checkLabelOverlap = True
    report_pie.sideLabels = True
    report_pie.simpleLabels = False
    report_pie.x = 120
    report_pie.y = 70
    for car in car_data:
        report_pie.data.append(car[3])
        report_pie.labels.append(car[1])
    report_chart = Drawing()
    report_chart.add(report_pie)
    return report_chart

def make_pdf_report(data, summary, subject, path):
    col = ["ID", "Car", "Price", "Total Sales"]
    pdf_table = cars_dict_to_table(data)
    pie_chart = cars_table_to_piechart(pdf_table)
    pdf_table.insert(0, col)
    subject = "Sales summary for last month"
    br = "<br/>"
    pdf_text= summary[0] + br + summary[1] + br + summary[2]
    reports.generate(path, subject, pdf_text, pdf_table, pie_chart)

def send_mail(summary, subject, email_text, att_path):
    nl = "\n"
    email_text = summary[0] + nl + summary[1] + nl + summary[2]
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    message = emails.generate(sender, receiver, subject, email_text, att_path)
    emails.send(message)


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data("C:\\Users\\Sebastian Lezama\\GoogleCoursera\\IT Automation\\Text_files\\car_sales.json")
    summary = process_data(data)
    att_path = "C:\\Users\\Sebastian Lezama\\GoogleCoursera\\IT Automation\\Text_files\\cars.pdf"
    subject = "Sales summary for last month"

    # TODO: turn this into a PDF report
    make_pdf_report(data, summary, subject, att_path)

    # TODO: send the PDF report as an email attachment


if __name__ == "__main__":
    main(sys.argv)
