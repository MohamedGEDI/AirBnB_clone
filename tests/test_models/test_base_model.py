#!/usr/bin/python3
"""test Base Model"""
import unittest
from models.base_model import BaseModel
import datetime


"""test Class """


class TestBaseModel(unittest.TestCase):
    """test Basemodel"""
    def test_id(self):
        """test if id exists"""
        base = BaseModel()
        self.assertIsNotNone(base.id, "Id must exist")  # add assertion here



if __name__ == '__main__':
    unittest.main()
