#!/usr/bin/env python

def test(value):
    assert value

def run_test(testcase):
    try:
        test(testcase)
    except Exception as e:
        e.add_note(f"Test failed with '{testcase}'")
        raise e

def run_tests():
    testcases = [False, "foo", None, {"x": "y"}, [], 42]

    exceptions = []
    for testcase in testcases:
        try:
            run_test(testcase)
        except Exception as e:
            exceptions.append(e)

    if exceptions:
        raise ExceptionGroup("Tests Failed", exceptions)

run_tests()
