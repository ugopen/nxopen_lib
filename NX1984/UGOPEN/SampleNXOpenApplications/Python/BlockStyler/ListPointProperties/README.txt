-------------------------------------------------------------------------------

       Copyright 2016 Siemens Product Lifecycle Management Software Inc. 
                           All Rights Reserved.

   
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
        Block Styler List Point Properties NX Open Python Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example has a simple lightweight dialog with a Super Point block, an Action Button,
and a List Box. The user can select points using the Super Point block and see the coordinates
of the selected point in the List Box. Pressing the Action Button will deselect the points and
clear the List Box. The user can pick different point selection intent rules to use for selecting 
points using the Curve Rule list on the Top Border Bar in NX. Snap Point rules are also available
if you click Enable Snap Point. 

The Block Styler dialog elements are controlled using methods and properties on the Block Styler 
classes instead of the generic property list methods.

--------------
Files required
--------------

    1.  ListPointProperties.py 
    2.  ListPointProperties.dlx 

----------------------------
Settings before Launching NX
----------------------------
The dlx file must be placed in one of the following locations:
    1.  From where NX session is launched
    2.  $UGII_USER_DIR/application
    3.  For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
        recommended. This variable is set to a full directory path to a file 
        containing a list of root directories for all custom applications.
        e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat

----------------------------
Settings after Launching NX
----------------------------

    1.  Change the Role to Advanced.

--------------------------
Example execution steps
--------------------------

    Use Tools->Journal->Play

        1.  Start NX.

        2.  Create a new part and create points in it or open an existing part
            that contains points. You can also pick points from solid geometry
            if you enable snap points.

        3.  Invoke ListPointProperties.py file using Tools->Journal->Play (Alt+F8).

        4.  It will launch the List Point Properties dialog.

        5.  Select one or more points in the Select Points block. 
            This selection block is a Super Point block so you can specify selection 
            intent rules for selecting points from the Curve Rule list on the Top 
            Border Bar. As you select points in the Select Point block, the 
            coordinates of the selected points are shown in the list box on
            the dialog.

        5.  You can press the Clear Selection button to clear the list box and 
            deselect all the selected points.

