# Categories of sales.
# Generate a PDF
# Mail pdf.

import emails
import os
import reports
import json
from operator import itemgetter


car_sales = 'C:\\Users\\Sebastian Lezama\\GoogleCoursera\\IT Automation\\Text_files\\car_sales.json'

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
        pdf_table.insert(0, pdf_col)
        sales.sort()
        highest_selling_car = per_car_sale[sales[-1]]
        summary_string = (
            "The {} generated the most revenue: {}".format(highest_selling_car, 
            str("$"+"{:,.2f}".format(sales[-1], 2)))
            )
        summary_car = "The {} had the most sales: {}".format(pdf_table[1][1], pdf_table[1][3])
        mp_year = "The most popular year was {} with {} sales.".format(most_popular_year, amount_of_sales)

        print(summary_string)
        print(summary_car)
        print(mp_year)
        
    br = "<br/>"
    pdf_text= summary_string + br + summary_car + br + mp_year
    reports.generate(
        "C:\\Users\\Sebastian Lezama\\GoogleCoursera\\IT Automation\\Text_files\\cars.pdf", 
        "A Complete Inventory of My Fruit", pdf_text, pdf_table)


# calculate most popular car_year (viejitud) across all make/models
# make an item sum per car_year, then return highest

    total_sales = 0
    summary = []
"""
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "List of Fruits"
    body = "Hi\n\nI'm sending an attachment with all my fruit."
    message = emails.generate(sender, receiver, subject, body, "/tmp/report.pdf")
    emails.send(message)
"""


if __name__ == '__main__':
    process_data()
