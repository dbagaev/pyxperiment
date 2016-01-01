from random import random

from ..MeasuredTest import MeasuredTest
from ..TestMetric import TestMetric

@MeasuredTest
class SimpleTest:
    def __init__(self, name=None):
        self.data = ""
        self.name = name

        self._Size = 0
        self._Value = 0.1
        self._Is = True
        self._Message = ""

    def test(self):
        self._Size = 42
        self._Value = random()
        if random() < 0.1:
            self._Is = False
        else:
            self._Is = True
        self._Message = "Hey from test " + self.name
        print("DoOtherTest.test()")

    @classmethod
    def findTests(cls):
        return [cls("Case_000"), cls("Case_001"), cls("Case_002")]

    @TestMetric
    def Size(self):
        return self._Size

    @TestMetric
    def Value(self):
        return self._Value

    @TestMetric
    def Is(self):
        return self._Is

    @TestMetric
    def Message(self):
        return self._Message