import unittest
from Interactions import show_time_of_pid


class testShowTimeOfPid(unittest.TestCase):
    def test_empty(self):
        testCase = ''
        expected = ''
        self.assertEqual(show_time_of_pid(testCase), expected)

    def test_sample(self):
        testCase = "Jul 12 14:01:23 computer.name CRON[29440]: USER (good_user)"
        expected = 'Jul 12 14:01:23 pid:29440'
        self.assertEqual(show_time_of_pid(testCase), expected)

    def test_edges_start(self):
        testCase = "Jan 1 00:00:01 computer.name CRON[00001]: USER (good_user)"
        expected = 'Jan 1 00:00:01 pid:00001'
        self.assertEqual(show_time_of_pid(testCase), expected)

    def test_edges_end(self):
        testCase = "Dec 31 11:59:59 computer.name CRON[99999]: USER (good_user)"
        expected = 'Dec 31 11:59:59 pid:99999'
        self.assertEqual(show_time_of_pid(testCase), expected)

    def test_no_pid(self):
        testCase = "Dec 6 14:01:23 computer.name: USER (good_user)"
        expected = ''
        self.assertEqual(show_time_of_pid(testCase), expected)


unittest.main()
