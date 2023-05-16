#!/usr/bin/env python

def test(value):
    assert value

def run_test(testcase):
    try:
        test(testcase)
    except Exception as e:
        e.add_note(f"Test failed with '{testcase}'")
        raise

def run_tests():
    testcases = [False, "foo", None, {"x": "y"}, [], 42]

    for testcase in testcases:
        run_test(testcase)

run_tests()
