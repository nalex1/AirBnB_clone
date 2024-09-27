#!/usr/bin/python3
"""Defines unittests for test_base_model.py"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unitest.TestCase):
    Unittests for testing intantiation of the BaseModel class.

    def test_no_args_instances(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def
