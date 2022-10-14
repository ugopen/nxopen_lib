'==================================================================================
'
'       Copyright (c) 2018 Siemens Product Lifecycle Management Software Inc.
'                            All Rights Reserved.
'
'===================================================================================
'    

------------------------------------------------------------------------------------
                        ValidateNXOpenSetup Example
------------------------------------------------------------------------------------

-----------
Description
-----------

    This example first obtains a Session object and with the help of Session object, 
    it creates a system log file and reads the environment variable to get the full 
    version number of the installed Siemens NX software. If the Siemens NX software 
    is successfully installed then the application receives the version number and 
    it displays the version number on the listing window as well in the system log 
    file. This is a simple NX Open batch application program and the fact that it 
    runs validates the NX Open software automation setup.

--------------
Files required
--------------

    1. ValidateNXOpenSetup.cs
    2. ValidateNXOpenSetup.vb

------------
Build steps
------------

   Windows
  ---------
    -NA-
  
   Linux
   -------
    -NA-
   
----------------------------
Settings before Launching NX
----------------------------
    -NA-

----------------------------
Settings after Launching NX
----------------------------
    -NA-

-----------------------
Example execution steps
-----------------------
    
   Windows
  ---------
    1. Start up a NX command prompt window.
    
    2. Type command %UGII_BASE_DIR%\nxbin\run_journal ValidateNXOpenSetup.cs or
       Type command %UGII_BASE_DIR%\nxbin\run_journal ValidateNXOpenSetup.vb
    
	
   Linux
   -------	
    -NA-  
	
------
Notes
------
    "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

