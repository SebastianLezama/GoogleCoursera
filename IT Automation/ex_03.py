# Categories of sales.
# Generate a PDF
# Mail pdf.

import emails
import os
import reports
import json
from operator import itemgetter
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import VerticalBarChart

car_sales = 'C:\\Users\\Sebastian Lezama\\GoogleCoursera\\IT Automation\\Text_files\\car_sales.json'
sender = 'automation@example.com'
recipient = '<user>@example.com'

def process_data():
    per_car_sale = {}
    sales = []
    year = {}
    pdf_table = []
    pdf_col = ['ID', 'Car', 'Price', 'Total Sales']

    with open(car_sales, 'rb') as f:
        json_data = json.loads(f.read())
        for car_sale in json_data:
            # Calulate highest selling car by revenue.
            price = car_sale['price']
            stripped_price = price.strip('$')
            total = car_sale['total_sales']
            car_name = (
                car_sale['car']['car_make'] +' '+ 
                car_sale['car']['car_model'] + ' (' + 
                str(car_sale['car']['car_year']) + ')'
                )
            total_sale = float(stripped_price) * total
            per_car_sale[total_sale] = car_name
            sales.append(total_sale)

            # Calculate most popular year.
            car_y = str(car_sale['car']['car_year'])
            year[car_y] = year.get(car_y, 0) + 1
            most_popular_year = max(year, key=year.get)
            amount_of_sales = year[most_popular_year]
            pdf_table.append([
                car_sale['id'], 
                car_name, 
                car_sale['price'], 
                car_sale['total_sales']
                ])

        # Sorting and formatting strings
        pdf_table = sorted(pdf_table, key=itemgetter(3), reverse=True)
        # Pie chart
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
        for car in pdf_table:
            report_pie.data.append(car[3])
            report_pie.labels.append(car[1])
        report_chart = Drawing()
        report_chart.add(report_pie)

        # Bar chart
        print(sales)
        bar_chart = VerticalBarChart()
        for i in range(1,11):
            bar_chart.data.append(sales[i])
            bar_chart.categoryAxis.categoryNames = str(pdf_table[i][1])

        pdf_table.insert(0, pdf_col)
        sales.sort()
        highest_selling_car = per_car_sale[sales[-1]]
        summary_string = (
            "The {} generated the most revenue: {}".format(highest_selling_car, 
            str("$"+"{:,.2f}".format(sales[-1], 2)))
            )
        summary_car = "The {} had the most sales: {}".format(pdf_table[1][1], pdf_table[1][3])
        mp_year = "The most popular year was {} with {} sales.".format(most_popular_year, amount_of_sales)

    subject = 'Sales summary for last month'
    nl = '\n'
    email_text = summary_string + nl + summary_car + nl + mp_year
    br = "<br/>"
    pdf_text= summary_string + br + summary_car + br + mp_year
    att_path = "C:\\Users\\Sebastian Lezama\\GoogleCoursera\\IT Automation\\Text_files\\cars.pdf"
    reports.generate(att_path, subject, pdf_text, pdf_table, report_chart)
#    message = emails.generate(sender, recipient, subject, email_text, att_path)
#    emails.send(message)



if __name__ == '__main__':
    process_data()
