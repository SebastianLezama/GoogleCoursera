import os
import sys
import unittest

from reportlab.platypus import paragraph
from run import batch_db_to_list, post_request
from emails import generate_email
from reports import generate_report
from changeImage import image_convert_resize_to_jpg

source = 'c:\\Users\\Sebastian Lezama\\GoogleCoursera\\IT Automation\\Lab 4\\text_files\\'

class TestRun(unittest.TestCase):
    def test_post(self):
        url_test = 'https://httpbin.org/post'
        test_case = batch_db_to_list(source)
        exp_result = 200
        post = post_request(url_test, test_case)
        self.assertEqual(post, exp_result)

    def test_batch_db(self):
        exp_result = 2
        len_of_fc = len(batch_db_to_list(source))
        self.assertEqual(len_of_fc, exp_result)

    def test_batch_db_output(self):
        expected = [
            {"name": "Watermelon", "weight": 500, 
            "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", 
            "image_name": "001.jpeg"},
            {"name": "Grapes", "weight": 300, 
            "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", 
            "image_name": "002.jpeg"}]
        self.assertEqual(batch_db_to_list(source), expected)

    def test_generate_email_no_att(self):
        sender = 'automation@example.com'
        to = 'username@example.com'
        subject = 'Upload Completed - Online Fruit Store'
        body = "Absolution calling."
        email_message = generate_email(sender, to, subject, body)
        self.assertTrue(email_message != None)

    def test_generate_email_with_att(self):
        sender = 'automation@example.com'
        to = 'username@example.com'
        subject = 'Upload Completed - Online Fruit Store'
        body = "Absolution calling."
        att = 'C:\\Users\\Sebastian Lezama\\GoogleCoursera\\IT Automation\\Lab 4\\text_files\\cars.pdf'
        email_message = generate_email(sender, to, subject, body, att)
        self.assertTrue(email_message != None)

    def test_generate_report(self):
        title = "Processed Update on "
        filename = 'C:\\Users\\Sebastian Lezama\\GoogleCoursera\\IT Automation\\Lab 4\\text_files\\processed.pdf'
        paragraph = batch_db_to_list(source)
        generate_report(filename, title, paragraph)
        self.assertTrue(os.path.isfile(filename))

    def test_convert_image(self):
        source_path = '\\Pictures\\'
        dest_path = 'C:\\Users\\Sebastian Lezama\\Pictures\\Saved Pictures\\'
        size = (600,400)
        im_format = '.jpeg'
        image_convert_resize_to_jpg(source_path, dest_path, size, im_format)


if __name__ == '__main__':
    suite = unittest.TestSuite((unittest.makeSuite(TestRun)))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
