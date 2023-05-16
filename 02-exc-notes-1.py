#!/usr/bin/env python

class TestError(Exception):
    pass

def test(value):
    assert value

def run_test(testcase):
    try:
        test(testcase)
    except Exception as e:
        raise TestError(f"Test failed with '{testcase}'") from e

def run_tests():
    testcases = [False, "foo", None, {"x": "y"}, [], 42]

    for testcase in testcases:
        run_test(testcase)

run_tests()
