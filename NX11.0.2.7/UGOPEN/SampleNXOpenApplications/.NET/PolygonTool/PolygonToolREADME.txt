-------------------------------------------------------------------------------


          Copyright 2010 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                            PolygonTool Example
-------------------------------------------------------------------------------

-----------
Description
-----------

This example demonstrates the use of the NX Automation API in conjunction with
Winforms. The example uses sketcher functionality to create constrained
polygons based on parameter data supplied by the user via a Winform.

--------------
Files required
--------------
 1.PolygonTool.vbproj
 2.PolygonTool.vb
 3.PolygonTool.resx
 4.PolygonToolAssemblyInfo.vb
 5.PolygonDraw.vb
 6.across_flats.bmp
 7.across_corners.bmp
 8.App.ico

 All the above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/PolygonTool
 
-----------
Build Steps
----------- 

 Windows
 ---------
   1. Open Microsoft Visual Studio .Net.
   2. Open up the VB project PolygonTool.vbroj
   3. Add the following references,
        3.1. NXOpen.dll 
        3.2. NXOpenUI.dll 
        
		3.3. NXOpen.Utilities.dll
        3.4. NXOpen.UF.dll.

      To do this, right click on the project in Solution Explorer. Pick Add Reference->Browse->
      Go to %UGII_BASE_DIR%\nxbin\managed.  Select and add the DLL's one after the other.
	  Set the copy local attribute for these DLLs to be false so you always use the versions from the NX install.

   		
   4. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, 
      right click on project name and select Build.
   5. This will create an executable called PolygonTool.dll in the \obj\Release directory.
   
   
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

 1. Change the Role to Advanced.
 
--------------------------
Example execution steps
--------------------------
  
  1. Start NX.
  
  2. Open a new part, go to Start -> Modeling or (Ctrl+M), and then into Sketcher (Insert->Sketch in Task Environment). 
  
  3. Go to Task -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog. Navigate to PolygonTool.dll file.
  
  4. "Create Polygon" form appears.
  
  5. Enter in the number of sides, diameter, and set the inscribed/circumscribed
     option.Press OK to create the constrained polygon.
-----
Note:
-----
  "NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."
  
 	 
	
	
       



