#-------------------------------------------------------------------------------
# Name:        fix_haiti_file.py
# Purpose:     Fix admin_codes in Haiti data files.
#
# Author:      David Viljoen
#
# Created:     02/10/2018
#-------------------------------------------------------------------------------

import csv
import os

in_csv = 'Haiti_Admin_Names.csv'
out_csv = 'haiti_admin_names_fixed.csv'
admin_code_column_index = 4

def process_file():
    """in_csv = file where a column contains a admin_code that needs fixing.
                That is, the 5th character in admin_code needs to be removed.
       out_csv = file with same contents as in_csv with fixed admin_code
       admin_code_column_index = 0-based index of column containing the
                                 admin_code
    """
    script_folder = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_folder,"data",out_csv),'wb') as out_file :
        writer = csv.writer(out_file)
        with open(os.path.join(script_folder,"data",in_csv),'rb') as in_file :
            reader = csv.reader(in_file)
            writer.writerow(reader.next())
            for row in reader:
                row[0] = _fix_code(row[0])
                writer.writerow(row)







def _fix_code(admin_code):
    """Returns code with 5th character removed.  For example,
       given HT12345-01, return "HT1245-01"""
    return admin_code[:admin_code_column_index] + admin_code[admin_code_column_index+1:]

























