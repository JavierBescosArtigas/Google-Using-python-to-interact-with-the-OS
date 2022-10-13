#! /usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase): # esto indica que heredamos esta clase. assertEqual es de esta clase
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_names(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_uniname(self):
        testcase = "Javier"
        expected = "Javier"
        self.assertEqual(rearrange_name(testcase), expected)
unittest.main()
