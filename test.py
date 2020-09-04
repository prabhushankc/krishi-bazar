import unittest
from log import LogIn
import tkinter
from buy import Two


class Test(unittest.TestCase):
    def test_login(self):
        add = LogIn(tkinter.Tk())
        actual_result = add.logbtn('test', 'test')
        self.assertTrue(actual_result)

    def test_add_item(self):
        item_test = Two(tkinter.Tk())
        result = item_test.add_item('q', 1, 1)
        self.assertTrue(result)
