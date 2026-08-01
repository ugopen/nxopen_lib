-------------------------------------------------------------------------------

       Copyright (c) 2016 Siemens Product Lifecycle Management Software Inc. 
                           All Rights Reserved.

   
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
        Block Styler Change Face Color NX Open Python Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example has a simple dialog with a Face Collector block and an Object Color Picker block. 
The user can select faces that should have the color changed using the Face Collector and see 
pick the new face color using the Object Color Picker. Clicking on OK or Apply will set the color
of the selected faces to the selected color. The user can pick different selection intent rules 
to use for selecting faces using the Face Rule list on the Top Border Bar in NX. 

The example uses both NX Open Common API and NX Open UF API methods and properties to access 
the face properties. The Block Styler dialog elements are controlled using methods and properties 
on the Block Styler classes instead of the generic property list methods.

--------------
Files required
--------------

    1.  ChangeFaceColor.py 
    2.  ChangeFaceColor.dlx 

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

        2.  Create a new part and create solid geometry in it or open an existing
            part that contains solid geometry.

        3.  Invoke ChangeFaceColor.py file using Tools->Journal->Play (Alt+F8).

        4.  It will launch the Change Face Color dialog.

        5.  Select one or more faces in the Face Collector block. 
            You can specify face selection intent rules from the Face Rule list 
            on the Top Border Bar. 
            
        6.  Select the new color for your selected faces using the Object Color
            Picker block. 

        7.  Click OK or Apply to set the color of the selected faces to the new 
            color.

