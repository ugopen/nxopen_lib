-------------------------------------------------------------------------------

       Copyright 2016 Siemens Product Lifecycle Management Software Inc. 
                           All Rights Reserved.

   
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
        Block Styler List Curve Properties NX Open Python Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example has a simple lightweight dialog with a Curve Collector block, an Action Button,
and a List Box. The user can select curves or edges using the Curve Collector and see the 
properties of the selected curves or edges in the List Box. Pressing the Action Button will 
deselect the selected curves or edges and clear the List Box. The user can pick different 
selection intent rules to use for selecting curves or edges using the Curve Rule list on 
the Top Border Bar in NX. Other buttons such as Allow Selection of Hidden Wireframe and 
Highlight Hidden Edges are available on the Top Border Bar to control the selection operation
of the Curve Collector just like internal NX dialogs using Curve Collector blocks.

The example uses both NX Open Common API and NX Open UF API methods and properties to access 
the curve or edge properties. The Block Styler dialog elements are controlled using methods 
and properties on the Block Styler classes instead of the generic property list methods.

--------------
Files required
--------------

    1.  ListCurveProperties.py 
    2.  ListCurveProperties.dlx 

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

        2.  Create a new part and create solid geometry or wireframe curves in it or open 
		    an existing part that contains solid geometry or wireframe curves.

        3.  Invoke ListCurveProperties.py file using Tools->Journal->Play (Alt+F8).

        4.  It will launch the List Curve Properties dialog.

        5.  Select one or more curves or edges in the Select Edges block. 
            Specify selection intent rules from the Curve Rule list on the Top
            Border Bar. As you select curves or edges in the Select Edge block,
			the properties of the selected curves or edges are shown in the 
			list box on the dialog.

        6.  Press the Clear Selection button to clear the list box and 
            deselect all the selected curves or edges.

