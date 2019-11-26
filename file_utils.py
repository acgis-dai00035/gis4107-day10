# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------
import os

def main():
    pass

def get_file_content(file_name):
    """Function documentation:
       - return the entire content of the specific file as a string
       - expected parameter value(s): exist on the system
       - return a string of the content
       - demo.txt which content is '123 456'"""
    try:
        content = ''
        script_folder = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(script_folder, "data", file_name))as in_file:
            for line in in_file:
                content += line.rstrip()
        return content
    except IOError:
        return os.path.join(script_folder, "data", file_name)+' does not exist'

def write_to_file(file_name , content):
    script_folder = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_folder, "data", file_name),'w') as out_file:
        out_file.write(content)
    return get_file_content(file_name)

if __name__ == '__main__':
    main()