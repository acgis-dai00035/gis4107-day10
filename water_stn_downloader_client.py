# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        water_stn_downloader_client.py
#
# Purpose:     Client to water_stn_downloader module.  This script sets the
#              attributes and calls the method to download and save a
#              response to a RESTful request to a file
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------

import os
import water_stn_downloader as wsd
reload(wsd)

# Path to folder containing this script
#
_script_folder = os.path.dirname(os.path.abspath(__file__))

# Use os.chdir to make _script_folder the current active folder
#
os.chdir(_script_folder)

def main():
    # Set the wsd.url to the RESTful API endpoint.  That is http:// to the
    # last character before the parameters (i.e. the "?")
    # For long urls, use string concatenation or line continuation to limit
    # statement length to 80 char or less
    #
    wsd.url = 'https://maps-cartes.ec.gc.ca/arcgis/rest/services/CESI_FGP_All_Layers/MapServer/6/query'

    # Set the wsd.params argument where
    # key = name of the string query parameter and
    # value = content assigned to the query parameter
    #
    wsd.params = {'outFields' : '*', 'where' : 'OBJECTID>0' , 'f' : 'json'}

    # Use os.path.join to set wsd.out_json_filename to a file in the data
    # subfolder of the _script_folder
    #
    wsd.out_json_filename = os.path.join(_script_folder, "data", '123.json')

    # Call wsd.download_to_file() and set the return value to a variable
    # named status
    #
    status = wsd.download_to_file()
    print status

    # Based on the value of status, print "Download successful" or
    # print the status value


if __name__ == '__main__':
    main()