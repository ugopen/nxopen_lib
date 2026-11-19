-------------------------------------------------------------------------------


          Copyright 2016 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                            MDP Management Example
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates how to use the enable\disable Multiple Display Parts(MDP) API.  This API is 
present to deal with issues that may arise with legacy NXOpen applications that may not work
as desired with MDP.  These legacy applications may have issues if they assume that NX has only 
one DisplayedPart. 

This API can be used by those applications to disable Multiple Displayed Parts as one 
option to deal the assumption of only one DisplayedPart. This API can be used to  
disable MDP before doing the automation workflow, and then re-enabling MDP when the program exits.

This example can also be used to re-enable MDP in an NX session if an NX Open application using this
API fails to re-enable MDP when it exits. This could occur if the application fails to re-enable MDP
when exiting normally, or has some abnormal exit that skips the code that re-enables MDP.

The easiest way to use this example is to tie the two journal files to a button.  This procedure 
is documented in the NXOpen Programmer's Guide, in the section Execution Methods - Applications from 
a Toolbar Button (interactive).

The Python file named MDP_On.py will enable MDP, and then display an NXMessageBox with the MDP status 
showing that MDP is enabled. The MDP_Off.py file will disable MDP, and then display an NXMessageBox with 
the MDP status showing that MDP is disabled.

This example is meant to be executed internally inside an NX session. It reports the MDP status using an NXMessageBox 
which only works in a full NX session. If this example is run externally in batch mode, no feedback will be given 
via the NXMessageBox. Also, MDP support only applies to NX sessions with graphics since batch NX sessions
do not display parts graphically.

--------------
Files required
--------------
 1.MDP_On.py
 2.MDP_Off.py

 All the above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/Python/MDP
 
-----------
Build Steps
----------- 

This example can be run using the Journal Manager or setting up the Python files to be 
run off a button.
   
   
----------------------------
Settings before Launching NX
----------------------------
   -NA-
   
 
--------------------------
Example execution steps
--------------------------
  
  1. Start NX.
  
  2. Create a new part, and then create another one.
  
  3. Tile the Windows horizontally so you can confirm that there are two DisplayedParts.
  
  4. Run the MDP_Off.py journal and observe that MDP will be disabled with only one DisplayedPart.
  
  5. Attempt to Display the other part (ex. Using Window pull-down) and see that NX shows only one DisplayedPart.
  
  5. Run the MDP_On.py journal and observe that MDP will be enabled with NX showing only one DisplayedPart.
  
  6. However, now that MDP is enabled, NX will show two DisplayedParts if you try to Display the other part.
  
  

  
 	 
	
	
       



