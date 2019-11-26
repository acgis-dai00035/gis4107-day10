# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        water_stn_converter.py
#
# Purpose:
#    Converts a JSON file created using the water_stn_downloader module to
#    CSV or KML.
#    For the CSV, the output columns will be:
#      {Station_Number}, {Station_Name}, {Longitude}, {Latitude}, LINK
#
#    where LINK is
#    https://wateroffice.ec.gc.ca/report/real_time_e.html?stn={Station_Number}
#
#    Header for CSV will be:
#      StationNumber, StationName, Longitude, Latitude, WaterOfficeLink
#
#    For the KML, the <Placemark> element will have the following sub-elements:
#              <name>{Station_Name}</name>
#              <description>
#                 link
#              </description>
#              <Point>
#                <coordinates>{Longitude},{Latitude},0</coordinates>
#              </Point>
#
#   Items enclosed by { } are the keys in the dictionary associated with
#   each feature (a key:value dictionary of values).
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------
import os
import json
import csv

in_json_filename = ''
out_csv_filename = ''
out_kml_filename = ''

def json_to_csv():
    """Converts a JSON file created using the water_stn_downloader module
    to CSV"""

    script_folder =  os.path.dirname(os.path.abspath(__file__))
    # Call load_json_file_to_dict()
    #
    dict_j = load_json_file_to_dict()

    # Create a unicode format string for 5 comma-separated values terminated
    # with a new line character (e.g. u'abc' is a unicode string)
    #
    i = 0
    fmt = u'Station_Number,\n Station_Name,\n Longitude,\n Latitude,\n wateroffice link,\n'
    with open(os.path.join(script_folder, "data", 'json_to.csv'),"wb") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(fmt.replace(',','').split())
        for feature in dict_j["features"]:
            list1 = []
            for item in get_values_from_feature(i):
                list1.append(item.encode(encoding='UTF-8'))
            list1.append(get_wateroffice_link(get_values_from_feature(i)[1]))
            writer.writerow(list1)
            i+=1




    # Use with to open out_csv_filename
    #

        # Write the header to the CSV file
        #


        # Loop through all the features and write the results to the CSV file
        # NOTE:  use .encode('utf-8') on the string before writing to the file
        #




def json_to_kml():
    """Converts a JSON file created using the water_stn_downloader module
    to KML"""
    dict_js = load_json_file_to_dict()
    script_folder = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_folder,"data",'out_kml.kml'),'w') as out_file:
        out_file.write(get_kml_header())
        i=0
        for feature in dict_js["features"]:
            out_file.write(get_placemark(dict_js["features"][i]["attributes"]['Station_Name'], dict_js["features"][i]["attributes"]['Longitude'], dict_js["features"][i]["attributes"]['Latitude'], get_wateroffice_link(dict_js["features"][i]["attributes"]['Station_Number'])).encode(encoding='UTF-8'))
            i+=1
        out_file.write(get_kml_footer())

def load_json_file_to_dict():
    """Use json.load(file_object) to convert the contents of in_json_filename
    to a Python dictionary.  Return the resulting dictionary.
    """
    # Use with to open in_json_filename and use that file object as an
    # argument to json.load.  This will return a Python dict with nested
    # lists and dictionaries
    with open(in_json_filename,'r') as in_file:
        dict_in = json.load(in_file)
        return dict_in



def get_values_from_feature(feature):
    """Given a dictionary of feature attributes, return the following:
        Station_Number, Station_name, Longitude, Latitude  """
    dict_f = load_json_file_to_dict()
    list1 = [
              dict_f["features"][feature]["attributes"]['Station_Number'],
              dict_f["features"][feature]["attributes"]['Station_Name'],
              dict_f["features"][feature]["attributes"]['Longitude'],
              dict_f["features"][feature]["attributes"]['Latitude']
            ]
    return list1
def get_wateroffice_link(station_number):
    link = 'https://wateroffice.ec.gc.ca/report/real_time_e.html?stn='
    return  link + str(station_number.encode(encoding='UTF-8'))
    """Given a station_number, return the English wateroffice link"""

def get_kml_header():
    """Return the xml header including the Document start tag
    """
    return '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'


def get_kml_footer():
    """Return the document and kml end tags
    """
    return '\n</Document>\n</kml>'


# Create a placemark format string that can be used for creating KML Placemark
# elements in get_placemark.  Remember to make this a unicode string since
# some of the placemark content will contain unicode characters
#
pm_fmt = ''


def get_placemark(name, longitude, latitude, wateroffice_link):
    """Return the KML Placemark element including start and end tags
    NOTE:  .encode('utf-8') is used on the resulting string to ensure
           proper encoding of characters
    """
    return '\n <Placemark>\n  <name>' + name + '</name>\n  <description>\n' +'   '+ wateroffice_link + '\n  </description>\n  <Point>\n' +'   <coordinates>'+ longitude +','+latitude + '</coordinates>\n  </Point>\n </Placemark>'

