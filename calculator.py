import unittest

class Calculator():
    def sum(self, *args):
        return -sum(args)
    def dif(self, a = 0, b = 0):
            return a-b
