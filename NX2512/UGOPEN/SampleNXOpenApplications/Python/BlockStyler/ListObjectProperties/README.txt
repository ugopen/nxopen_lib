-------------------------------------------------------------------------------

       Copyright 2016 Siemens Product Lifecycle Management Software Inc. 
                           All Rights Reserved.

   
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
        Block Styler List Object Properties NX Open Python Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example has a simple lightweight dialog with a Select Object block, an Action Button,
and a List Box. The user can select NX objects using the Select Object block and see the 
properties of the selected objects in the List Box. Pressing the Action Button will 
deselect the selected objects and clear the List Box. The user can implement selection 
filters to use for selecting objects. The filters can select objects based on attributes
the user defines on the objects

The example uses both NX Open Common API and NX Open UF API methods and properties to access 
the object properties. The Block Styler dialog elements are controlled using methods 
and properties on the Block Styler classes instead of the generic property list methods.

--------------
Files required
--------------

    List Object Properties Example - Generic Select Object example that works on NX tagged objects.
	Some sample selection filtering code is included and commented out for users to modify as needed.

    1.  ListObjectProperties.py 
    2.  ListObjectProperties.dlx 
    
    List Component Properties Example - Select Object example with selection filtering for components.
    
    1.  ListComponentProperties.py
    2.  ListObjectProperties.dlx

----------------------------
Settings before Launching NX
----------------------------
The dlx file must be placed in one of the following locations:
    1.  From where NX session is launched
    2.  $UGII_USER_DIR/application
    3.  For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
        recommended. Set this variable to a full directory path to a file 
        containing a list of root directories for all custom applications,
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

        2.  Create a new part and create NX objects in it such as solid geometry or wireframe curves
            or open an existing part that contains solid geometry or wireframe curves.

        3.  Invoke ListObjectProperties.py file using Tools->Journal->Play (Alt+F8).

        4.  It will launch the List Object Properties dialog.

        5.  Select one or more objects in the Select Object block. 
            As you select objects in the Select Object block, the properties 
            of the selected objects are shown in the list box on the dialog.

        6.  Press the Clear Selection button to clear the list box and 
            deselect all the selected curves or edges.

