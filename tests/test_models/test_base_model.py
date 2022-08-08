#!/usr/bin/python3
"""Module for testing base_model"""

import unittest
from models.base_model import Basemodel

class TestBaseModel(unittest.Testcase):
    def test_name(self):
        b = Basemodel()
        self.assertEqual(b.name, "My First Model")

    def test_id(self):
        b = Basemodel()
        self.assertEqual()