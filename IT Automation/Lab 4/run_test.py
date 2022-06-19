import unittest
from run import batch_db_to_web_service, post_request

source = 'c:\\Users\\Sebastian Lezama\\GoogleCoursera\\IT Automation\\Lab 4\\text_files\\'

class TestRun(unittest.TestCase):
    def test_post(self):
        url_test = 'https://httpbin.org/post'
        test_case = batch_db_to_web_service(source)
        exp_result = 200
        post = post_request(url_test, test_case)
        self.assertEqual(post, exp_result)

    def test_batch_db(self):
        exp_result = 2
        len_of_fc = len(batch_db_to_web_service(source))
        self.assertEqual(len_of_fc, exp_result)

    def test_batch_db_output(self):
        expected = [
            {"name": "Watermelon", "weight": 500, 
            "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", 
            "image_name": "001.jpeg"},
            {"name": "Grapes", "weight": 300, 
            "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", 
            "image_name": "002.jpeg"}]
        self.assertEqual(batch_db_to_web_service(source), expected)

unittest.main()
