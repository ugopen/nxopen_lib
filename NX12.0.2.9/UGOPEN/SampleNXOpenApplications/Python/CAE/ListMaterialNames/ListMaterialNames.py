# Program to list names of materials stored in the 
# sample materials library provided with NX

import NXOpen

import functools
import locale
import os
import os.path
import xml.etree.ElementTree as ET

def main():
    theSession  = NXOpen.Session.GetSession()

    # NX provides a sample NX Materials Library with
    # the material properties specified using the MatML
    # XML schema. We will use the xml.etree.ElementTree
    # python module to find all the names of the materials
    # contained in this XML file. 
    libname = 'physicalmateriallibrary.xml'
    libpath = os.path.join(os.environ['UGII_BASE_DIR'], 'UGII', 'materials', libname)
    tree = ET.parse(libpath)
    root = tree.getroot()
    materialList = root.findall('./Material/BulkDetails/Name')

    # Form string list containing material names
    material_name_list = []
    for material in materialList:
        material_name_list.append(material.text)

    # Output list of strings to NX Listing Window.
    # Sort material names using locale specific 
    # sorting so that names with lowercase characters
    # are properly sorted.
    lw = theSession.ListingWindow
    lw.Open()
    locale.setlocale(locale.LC_ALL, '')
    lw.WriteLine("Materials in NX Library: {}".format(libname))
    for material in sorted(material_name_list, key=functools.cmp_to_key(locale.strcoll)):
        lw.WriteLine(material)

if __name__ == '__main__':
    main()


