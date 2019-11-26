#-------------------------------------------------------------------------------
# Name:        Fix_Haiti_File_Tests.py
# Purpose:
#
# Author:      David Viljoen
#
# Created:     02/10/2018
#-------------------------------------------------------------------------------

import os
import sys
import csv
import inspect
import fix_haiti_file as fh
reload(fh)

_script_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(_script_folder)

def main():
    # Find and call all functions that begin with "test"
    test_funcs = get_test_functions()
    for test_func in test_funcs:
        test_func()

# Copy/paste/change the test template below to create new test functions, where:
#    - the test function name must begin with the word "test"
#    - the Docstring should briefly describe the test
#    - expected = Expected result from calling the function
#    - actual = Actual result from calling the function
#    - func = Function being tested (the actual function, not the name)"""
def template_for_test_functions():
    """Docstring to describe test function"""

    expected = ""
    actual = ""
    print_test_results(func, expected, actual)


def test_fix_code_typical_code():
    """Given HT12345-01, expecting HT1245-01"""
    admin_code = 'HT12345-01'
    expected = 'HT1245-01'
    actual = fh._fix_code(admin_code)
    print_test_results(fh._fix_code, expected, actual)


def test_process_file():
    """Haiti_Admin_Names.csv contains ADMIN_CODES in the first column
        Haiti_Admin_Names_fixed.csv contains a fixed version. """

    ## Once you have process_file "working", uncomment the 5 lines starting with
    ## file1 = ""
    ## Set kdiffexe to the path to kdiff3.exe on your computer
    ## Set file1 and file2 to the original and fixed eversion of the files
    ## This should provide a nice visual comparison of the file with and
    ## without the fix.  In general, this is not a good practice for testing.
    ## That is, launching an external applicaiton to show the results.
    ##
    process_file()
    file1 = ""
    file2 = ""
    kdiffexe = '"C:\Program Files\KDiff3\kdiff3.exe"'
    cmd = r'{} {} {}'.format(kdiffexe, file1, file2)
    os.system(cmd)





# ------------------------------------------------------------------------------
# Testing helper functions
# ------------------------------------------------------------------------------
def get_test_functions():
    """Returns a list of functions that begin with the word test in the order
       they appear in this file."""

    test_funcs = [obj for name,obj in inspect.getmembers(sys.modules[__name__])
                     if (inspect.isfunction(obj) and name.startswith('test'))]
    src = inspect.getsource(sys.modules[__name__])
    lines = src.split('\n')

    # Create a dictionary with key=function name and value is 0-based order
    # in the module
    ordered_func_names = dict()
    ordered_funcs = list()
    func_index = 0
    for line in lines:
        if line.find("def test") > -1 and not line.find('line.find') > -1:
            func_name = line.split("(")[0].split()[1]
            ordered_func_names[func_name] = func_index
            # Create an empty list with sampe number of elements as test
            # functions
            ordered_funcs.append('')
            func_index += 1
    for test_func in test_funcs:
        index = ordered_func_names[test_func.__name__]
        ordered_funcs[index] = test_func
    return ordered_funcs

def print_test_results(func_tested, expected, actual):
    """func_tested is the function being tested
       expected = Expected result of test
       actual = Actual result of test """

    if not callable(func_tested):
        raise Exception("{} is not a function".format(func_tested))

    func_name = func_tested.__name__
    desc = func_tested.__doc__

    if expected == actual:
        print "PASSED: {}".format(func_name)
    else:
        print "FAILED: {}".format(func_name)
        print "Expect: {}".format(expected)
        print "Actual: {}".format(actual)
        print "__doc__:{}".format(desc)

    print ""

if __name__ == '__main__':
    main()