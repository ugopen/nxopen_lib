=========================================================================
			NXOpen.UF Examples 
=========================================================================

Purpose of this Example: 
------------------------

These examples are designed to demonstrate the use of the NX Open UF API.
The directory contains C#(C-Sharp) as well as some VB.NET examples.

This ReadMe file gives steps for building and running each and every 
example in this folder.

VB examples are there at the end of this file.

#################################### CS Examples #####################################

How to Build C-Sharp examples
-----------------------------
1. Open Microsoft Visual Studio.

2. Create new project as:
	1. File->New->Project.
	2. Select Visual C# Projects, Console Application, Enter name as 
	   CS_NXOpen_UF_Examples (you can specify name of your choice). 
	3. Click on Ok.
3. Remove the Class1.cs file from the project.  Highlight it in the Solution Explorer
   and use the 3rd mouse button and pull to delete it.  You will receive a pop-up 
   that says it will be permanently removed.  Hit OK.
4. Follow the same steps as in step 3 to remove AssemblyInfo.cs, App.ico.

5. Add references of following files:
	   1. NXOpen.dll 
	   2. NXOpenUI.dll 
	   3. NXOpen.Utilities.dll
	   4. NXOpen.UF.dll.
	   To do this, right click on "References" under the project in Solution
	   Explorer. Pick Add Reference->Browse->Go to %UGII_BASE_DIR%\nxbin\managed,
	   select DLL (since here there are multiple dll, press CTRL Key and then
	   start selecting DLLs).

6. In the Solution Explorer highlight the project name and use the 3rd mouse 
  button and drag to Add.  Choose Add Existing Item.  Navigate to and add any 
  of the *.cs file. (Please Note each CS file is an example, so add one at a time)
   		.
7. Go to Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right
   click on project name and select Build.

How to Run C-Sharp Examples
---------------------------
NOTE: Some examples you need to execute in interactive mode and some in the batch mode.
       You will find this information along with individual CS file description at the
       end of this file but before VB examples.

Once you have successfully finished with "How to Build C-Sharp examples" steps, it will 
create executable called CS_NXOpen_UF_Examples.exe in bin\Debug folder of the project dir.

How to Run C-Sharp example in the interactive mode
--------------------------------------------------
1. Start NX.
2. Go to File Menu -> Execute ->NX Open.
3. You will lead to window called "Execute User Function". 
4. Navigate to the location of the exe file.  It will be in the bin\Debug directory under 
   the directory named for the C# project.
5. Select .exe filename and Click ok.
   
How to Run C-Sharp example in the batch mode 
--------------------------------------------
Here you have two choices: (follow any one of these)

1. Executing this project thru Visual Studio:
	1. Click on Debug->Start or Start icon.
OR

2. Executing this project using executable:
	1. Execute exe file in an “Explorer” window or a command prompt 
	   (Go to <Project Folder>\bin\Debug to find exe file).
	
To Build another C-Sharp example
--------------------------------
1. You need to get into Visual Studio and remove the CS file that was just built from 
  the project.  Highlight the CS file in the Solution Explorer and use the 3rd mouse 
  button and pull to Delete it.  You will receive a pop-up that says it will be 
  permanently removed.  Hit OK.
2. In the Solution Explorer highlight the project name and use the 3rd mouse 
  button and drag to Add.  Choose Add Existing Item.  Navigate to and add any 
  of the *.cs file.
3. Go to Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right
   click on project name and select Build.

C-Sharp Examples
----------------

EX_Curve_CreateArc.cs:

	This example will create EX_Curve_CreateArc.prt, EX_Curve_CreateArc.log files 
	under <Project Folder>\bin\Debug folder and creates an Arc using theUfSession.Curve.CreateArc()
	method. The program prints the report to the log file called "EX_Curve_CreateArc.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build C-Sharp examples" section of this
	file if you are creating this example as first example or follow "To execute 
	another CS example" section of this file.

	The output should be as follows:
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin\Debug.
	
	If you are running the example in interactive mode mode, you will find generated log file 
	as well as part file at current working directory.
	
	Compare the contents of the log "EX_Curve_CreateArc.log"  file with the contents of 
	EX_Curve_CreateArc.mstlog.

	You may get difference for following strings:
	Loaded: <Location of part file>
	
EX_Curve_CreateFillet.cs: 

	This example will create EX_Curve_CreateFillet.prt, EX_Curve_CreateFillet.log files 
	under <Project Folder>\bin\Debug folder and creates fillet between Line and Arc 
	using theUfSession.Curve.CreateFillet()	method. 
	The program prints the report to the log file called "EX_Curve_CreateFillet.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build C-Sharp examples" section of this
	file if you are creating this example as first example or follow "To execute 
	another CS example" section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin\Debug.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Curve_CreateFillet.log"  file with the contents of 
	EX_Curve_CreateFillet.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>
    
EX_Curve_CreateSpline.cs: 

	This example will create EX_Curve_CreateSpline.prt, EX_Curve_CreateSpline.log files 
	under <Project Folder>\bin\Debug folder and creates two planar B-curves and calculates 
	their inflection points	using theUfSession.Curve.AskCurveInflections().
	The program prints the report to the log file called "EX_Curve_CreateSpline.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build C-Sharp examples" section of this
	file if you are creating this example as first example or follow "To execute 
	another CS example" section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin\Debug.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Curve_CreateSpline.log"  file with the contents of 
	EX_Curve_CreateSpline.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>


EX_Curve_CreateSplineThruPts.cs : 

	This example will create EX_Curve_CreateSplineThruPts.prt, EX_Curve_CreateSplineThruPts.log files 
	under <Project Folder>\bin\Debug folder and creates spline through points using 
	theUfSession.Curve.CreateSplineThruPts(().
	The program prints the report to the log file called "EX_Curve_CreateSplineThruPts.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build C-Sharp examples" section of this
	file if you are creating this example as first example or follow "To execute 
	another CS example" section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin\Debug.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Curve_CreateSplineThruPts.log"  file with the contents of 
	EX_Curve_CreateSplineThruPts.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>

	
EX_Curve_ProjCurves.cs: 

	This example will create EX_Curve_ProjCurves.prt, EX_Curve_ProjCurves.log files 
	under <Project Folder>\bin\Debug folder and demonstrates curve projection functionality 
	usung theUfSession.Curve.CreateProjCurves().
	The program prints the report to the log file called "EX_Curve_ProjCurves.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build C-Sharp examples" section of this
	file if you are creating this example as first example or follow "To execute 
	another CS example" section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin\Debug.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Curve_ProjCurves.mstlog"  file with the contents of 
	EX_Curve_ProjCurves.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>
	Any Tag representation



EX_DirPath.cs: 

	This example will create EX_DirPath.prt, EX_DirPath.log files under 
	<Project Folder>\bin\Debug folder and queries directories at UGII_BASE_DIR and 
	directories created using theUfSession.Dirpath.CreateFromDirs(), 
	using theUfSession.Dirpath.AskDirs() method. The program prints the report to the 
	log file called "EX_DirPath.log".
	
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build C-Sharp examples" section of this
	file if you are creating this example as first example or follow "To execute 
	another CS example" section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin\Debug.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_DirPath.log"  file with the contents of 
	EX_DirPath.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>
	First, Dir Path: <Value of Environment var, UGII_BASE_DIR>


EX_Drf_AskPreferences.cs: 

	This example will create EX_Drf_AskPreferences.prt, EX_Drf_AskPreferences.log files under 
	<Project Folder>\bin\Debug folder and queries the current settings of the drafting 
	parameters using theUfSession.Drf.AskPreferences().
	The program prints the report to the log file called "EX_Drf_AskPreferences.log".

	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build C-Sharp examples" section of this
	file if you are creating this example as first example or follow "To execute 
	another CS example" section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin\Debug.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Drf_AskPreferences.log"  file with the contents of 
	EX_Drf_AskPreferences.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>

	
EX_Facet.cs: 
	
	This example will create EX_Facet.prt, EX_Facet.log files under 
	<Project Folder>\bin\Debug folder. 
	For each facet it prints the position, vertex 
   	normal, and vertex convexity for each vertex.The program prints the report to the 
	log file called "EX_Facet.log".
	
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build C-Sharp examples" section of this
	file if you are creating this example as first example or follow "To execute 
	another CS example" section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin\Debug.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Facet.log"  file with the contents of 
	EX_Facet.mstlog.

EX_Modl_AskBsurf.cs: 
	
	This example will create EX_Modl_AskBsurf.prt, EX_Modl_AskBsurf.log files 
	under <Project Folder>\bin\Debug folder and creates B-Surface and Spline, 
	and then queries its data. 
	The program prints the report to the log file called "EX_Modl_AskBsurf.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build C-Sharp examples" section of this
	file if you are creating this example as first example or follow "To execute 
	another CS example" section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin\Debug.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Modl_AskBsurf.log"  file with the contents of 
	EX_Modl_AskBsurf.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>


EX_Modl_Create.cs:

	This example will create EX_Modl_Create.prt, EX_Modl_Create.log files 
	under <Project Folder>\bin\Debug folder and creates rectangular groove
	using theUfSession.Modl.CreateRectGroove() method.
	The program prints the report to the log file called "EX_Modl_Create.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build C-Sharp examples" section of this
	file if you are creating this example as first example or follow "To execute 
	another CS example" section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin\Debug.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Modl_Create.log"  file with the contents of 
	EX_Modl_Create.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>
	Any Tag representation


EX_Modl_CreateBlend.cs: 
	
	This example will create EX_Modl_CreateBlend.prt, EX_Modl_CreateBlend.log files 
	under <Project Folder>\bin\Debug folder and creates a block 1x2x3 units. 
	The four 3-unit edges are blended using method theUfSession.Modl.CreateBlend()
	with a variable radius.
	The program prints the report to the log file called "EX_Modl_CreateBlend.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build C-Sharp examples" section of this
	file if you are creating this example as first example or follow "To execute 
	another CS example" section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin\Debug.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Modl_CreateBlend.log"  file with the contents of 
	EX_Modl_CreateBlend.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>


EX_Modl_CreateExtruded.cs: 

	This example will create EX_Modl_CreateExtruded.prt, EX_Modl_CreateExtruded.log files 
	under <Project Folder>\bin\Debug folder. This example extrudes lines and arcs along 
	the z-axis. Three lines and two arcs are drawn. The center line is a reference line
	only, and is not included in the objects to be extruded.
	The program prints the report to the log file called "EX_Modl_CreateExtruded.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build C-Sharp examples" section of this
	file if you are creating this example as first example or follow "To execute 
	another CS example" section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin\Debug.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Modl_CreateExtruded.log"  file with the contents of 
	EX_Modl_CreateExtruded.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>


EX_Modl_FeatureType.cs: 

	This example program requires a work part with at least one feature. The
	example extracts the feature information of a given solid body via 
	theUfSession.Modl.AskFeatType(), theUfSession.Modl.AskMaster(), 
	theUfSession.Modl.AskFeatRelatives() etc. The program  prints a report 
	to the listing window.
 
	This example should run in the interactive mode.

	1. Start NX.
	2. Open Part file, analyasisArclengthDistance.prt (This file is provided along
	   with CS files. You can use any other part file containing at least one feature,
	   but then, you will get different information into the log file).
	3. Follow, step nos. 2,3,4,5 in "How to Run example in the interactive mode" 
	   section of this file.
	4. See the information displayed into the Listing Window. Compare the contents 
	   of the Listing Window with the contents of EX_Modl_FeatureType.mstlog.

	You may get difference for following strings :
	Any Tag representation

EX_Ui_ListingWindow.cs: 
	
	This example demonstrates how to open Listing Window device in using,
	theUfSession.Ui.OpenListingWindow() and prints data using, 
	theUfSession.Ui.WriteListingWindow() method.
	The program will create EX_Ui_ListingWindow.prt file and prints
	the name of the feature created into the Listing Window device.
	 
	This example should run in the interactive mode.

	1. Start NX.
	2. Follow, step nos. 2,3,4,5 in "How to Run example in the interactive mode" 
	   section of this file.
	3. See the information displayed into the Listing Window. Compare the contents 
	   of the Listing Window with the contents of EX_Ui_ListingWindow.mstlog.

	
#################################### VB Examples #####################################

Users can run the VB examples by using two approaches :

1. Read section, "How to Run VB example in the interactive mode".
2. Users can build dll/exe file to execute the example. For this read section 
   "How to Build VB examples" followed by "How to Run VB examples".
      
   FIRST APPROACH IS THE PREFERED APPROACH.

How to Run VB example in the interactive mode
---------------------------------------------
Here you have to choices : ( follow any one of these)

1. Thru Tools Menu :

	1. Start NX.
	2. Go to Tools Menu -> Journal -> Play.
	3. You will lead to window called "Journal Manager". 
	4. Navigate to the location of the VB file using Browse Button.
	5. Click on Run Button.

How to Build VB examples
------------------------
1. Open Microsoft Visual Studio.

2. Create new project as :
	1. File->New->Project.
	2. Select Visual Basic Projects, Console Application, Enter
	   name as VB_NXOpen_UF_Examples(you can specify name of your choice). 
	3. Click on Ok. 
3. Remove the AssemblyInfo.vb file from the project.  Highlight it in the Solution Explorer
   and use the 3rd mouse button and pull to Delete it.  You will receive a pop-up 
   that says it will be permanently removed. Hit OK.
4. Remove Module1.vb. Follow the same steps followed for removing AssemblyInfo.vb(step 3).
 
5. Add references of following files :
	   1. NXOpen.dll 
	   2. NXOpenUI.dll 
	   3. NXOpen.Utilities.dll
	   4. NXOpen.UF.dll.
	   To do this, right click on "References" under the project in Solution
	   Explorer. Pick Add Reference->Browse->Go to %UGII_BASE_DIR\nxbin%\managed,
	   select DLL ( since here there are multiple dll, press CTRL Key and then
	   start selecting DLLs).

6. In the Solution Explorer highlight the project name and use the 3rd mouse 
  button and drag to Add.  Choose Add Existing Item.  Navigate to and add any 
  of the *.vb file. (Please Note each VB file is a example, so add one at a time)
   		
7. Go to Project Menu -> Properties. If you see "Module1" in "Startup Project" push down list,
   select Startup Project as new Module name displayed into pull down menu. Click on Ok.

8. Go to Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right
   click on project name and select Build.

How to Run VB Examples
----------------------
NOTE : Some examples you need to execute in interactive mode and some in the batch mode.

Once you have successfully finished with "How to Build VB examples" steps, it will 
create executable called VB_NXOpen_UF_Examples.exe in bin dir of the project dir.

1. Thru File Menu :

	1. Start NX.
	2. Go to File Menu -> Execute ->NX Open.
	3. You will lead to window called "Execute User Function". 
	4. Navigate to the location of the exe file.  It will be in the <Project Folder>\bin 
	   directory under the directory named for VB project.
	5. Select .exe filename and Click ok.

How to Run VB example in the batch mode 
---------------------------------------
Here you have to choices : ( follow any one of these)

1. Executing this project thru Visual Studio :
	1. Click on Debug->Start or Start icon.
OR

2. Executing this project using executable :
	1. Execute exe file in an “Explorer” window or a command prompt 
	   (Go to <Project Folder>\bin to find exe file).

To Build another VB example
-----------------------------
1. You need to get into Visual Studio and remove the VB file that was just built from 
  the project.  Highlight the VB file in the Solution Explorer and use the 3rd mouse 
  button and pull to Delete it.  You will receive a pop-up that says it will be 
  permanently removed.  Hit OK.

2. In the Solution Explorer highlight the project name and use the 3rd mouse 
  button and drag to Add.  Choose Add Existing Item.  Navigate to and add any 
  of the *.vb file.

3. Go to Project -> Project Properties. Select Startup Project as new Module name displayed 
   into pull down menu. Click on Ok.

4. Go to Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right
   click on project name and select Build.

VB Examples
-----------

EX_Curve_CreateArc.vb :

	This example will create EX_Curve_CreateArc.prt, EX_Curve_CreateArc.log files 
	under <Project Folder>\bin folder and creates an Arc using theUfSession.Curve.CreateArc()
	method. The program prints the report to the log file called "EX_Curve_CreateArc.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build VB examples" section of this file if you 
	are creating this example as first example or follow "To build another VB example"
	section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin.
	
	If you are running the example in interactive mode mode, you will find generated log file 
	as well as part file at current working directory.
	
	Compare the contents of the log "EX_Curve_CreateArc.log"  file with the contents of 
	EX_Curve_CreateArc_vb.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>

EX_Curve_CreateFillet.vb: 

	This example will create EX_Curve_CreateFillet.prt, EX_Curve_CreateFillet.log files 
	under <Project Folder>\bin folder and creates fillet between Line and Arc 
	using theUfSession.Curve.CreateFillet()	method. 
	The program prints the report to the log file called "EX_Curve_CreateFillet.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build VB examples" section of this file if you 
	are creating this example as first example or follow "To build another VB example"
	section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Curve_CreateFillet.log"  file with the contents of 
	EX_Curve_CreateFillet_vb.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>

EX_Curve_CreateSpline.vb: 

	This example will create EX_Curve_CreateSpline.prt, EX_Curve_CreateSpline.log files 
	under <Project Folder>\bin folder and creates two planar B-curves and calculates 
	their inflection points	using theUfSession.Curve.AskCurveInflections().
	The program prints the report to the log file called "EX_Curve_CreateSpline.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build VB examples" section of this file if you 
	are creating this example as first example or follow "To build another VB example"
	section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Curve_CreateSpline.log"  file with the contents of 
	EX_Curve_CreateSpline_vb.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>

EX_Curve_CreateSplineThruPts.vb : 

	This example will create EX_Curve_CreateSplineThruPts.prt, EX_Curve_CreateSplineThruPts.log files 
	under <Project Folder>\bin folder and creates spline through points using 
	theUfSession.Curve.CreateSplineThruPts(().
	The program prints the report to the log file called "EX_Curve_CreateSplineThruPts.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build VB examples" section of this file if you 
	are creating this example as first example or follow "To build another VB example" 
	section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Curve_CreateSplineThruPts.log"  file with the contents of 
	EX_Curve_CreateSplineThruPts_vb.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>

EX_Curve_ProjCurves.vb: 

	This example will create EX_Curve_ProjCurves.prt, EX_Curve_ProjCurves.log files 
	under <Project Folder>\bin folder and demonstrates curve projection functionality 
	usung theUfSession.Curve.CreateProjCurves().
	The program prints the report to the log file called "EX_Curve_ProjCurves.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build VB examples" section of this file if you 
	are creating this example as first example or follow "To build another VB example"
	section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Curve_ProjCurves.log"  file with the contents of 
	EX_Curve_ProjCurves_vb.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>

EX_DirPath.vb: 

	This example will create EX_DirPath.prt, EX_DirPath.log files under 
	<Project Folder>\bin folder and queries directories at UGII_BASE_DIR and 
	directories created using theUfSession.Dirpath.CreateFromDirs(), 
	using theUfSession.Dirpath.AskDirs() method. The program prints the report to the 
	log file called "EX_DirPath.log".
	
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build VB examples" section of this file if you 
	are creating this example as first example or follow "To execute another VB example"
	section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_DirPath.log"  file with the contents of 
	EX_DirPath_vb.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>
	First, Dir Path: <Value of Environment var, UGII_BASE_DIR>


EX_Drf_AskPreferences.vb: 

	This example will create EX_Drf_AskPreferences.prt, EX_Drf_AskPreferences.log files under 
	<Project Folder>\bin folder and queries the current settings of the drafting 
	parameters using theUfSession.Drf.AskPreferences().
	The program prints the report to the log file called "EX_Drf_AskPreferences.log".

	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build VB examples" section of this file if you 
	are creating this example as first example or follow "To execute another VB example"
	section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Drf_AskPreferences.log"  file with the contents of 
	EX_Drf_AskPreferences_vb.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>

	
EX_Facet.vb: 
	
	This example will create EX_Facet.prt, EX_Facet.log files under 
	<Project Folder>\bin folder. 
	For each facet it prints the position, vertex 
   	normal, and vertex convexity for each vertex.The program prints the report to the 
	log file called "EX_Facet.log".
	
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build VB examples" section of this file if you 
	are creating this example as first example or follow "To execute another VB example"
	section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Facet.log"  file with the contents of 
	EX_Facet_vb.mstlog.

EX_Modl_AskBsurf.vb: 
	
	This example will create EX_Modl_AskBsurf.prt, EX_Modl_AskBsurf.log files 
	under <Project Folder>\bin folder and creates B-Surface and Spline, 
	and then queries its data. 
	The program prints the report to the log file called "EX_Modl_AskBsurf.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build VB examples" section of this file if you 
	are creating this example as first example or follow "To execute another VB example"
	section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Modl_AskBsurf.log"  file with the contents of 
	EX_Modl_AskBsurf_vb.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>


EX_Modl_Create.vb:

	This example will create EX_Modl_Create.prt, EX_Modl_Create.log files 
	under <Project Folder>\bin folder and creates rectangular groove
	using theUfSession.Modl.CreateRectGroove() method.
	The program prints the report to the log file called "EX_Modl_Create.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build VB examples" section of this file if you 
	are creating this example as first example or follow "To execute another VB example"
	section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Modl_Create.log"  file with the contents of 
	EX_Modl_Create_vb.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>


EX_Modl_CreateBlend.vb: 
	
	This example will create EX_Modl_CreateBlend.prt, EX_Modl_CreateBlend.log files 
	under <Project Folder>\bin folder and creates a block 1x2x3 units. 
	The four 3-unit edges are blended using method theUfSession.Modl.CreateBlend()
	with a variable radius.
	The program prints the report to the log file called "EX_Modl_CreateBlend.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build VB examples" section of this file if you 
	are creating this example as first example or follow "To execute another VB example"
	section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Modl_CreateBlend.log"  file with the contents of 
	EX_Modl_CreateBlend_vb.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>


EX_Modl_CreateExtruded.vb: 

	This example will create EX_Modl_CreateExtruded.prt, EX_Modl_CreateExtruded.log files 
	under <Project Folder>\bin folder. This example extrudes lines and arcs along 
	the z-axis. Three lines and two arcs are drawn. The center line is a reference line
	only, and is not included in the objects to be extruded.
	The program prints the report to the log file called "EX_Modl_CreateExtruded.log".
			
	This example can be run in batch mode as well as interactive mode. 

	Follow the steps given in "How to Build VB examples" section of this file if you 
	are creating this example as first example or follow "To execute another VB example"
	section of this file.

	The output should be as follows :
	
	If you are running the example in batch mode, you will find generated log file as well as
	part file at <Project Folder>\bin.
	
	If you are running the example in interactive mode, you will find generated log file as well as
	part file at current working directory.
	
	Compare the contents of the log "EX_Modl_CreateExtruded.log"  file with the contents of 
	EX_Modl_CreateExtruded_vb.mstlog.

	You may get difference for following strings :
	Loaded: <Location of part file>


EX_Modl_FeatureType.vb: 

	This example program requires a work part with at least one feature. The
	example extracts the feature information of a given solid body via 
	theUfSession.Modl.AskFeatType(), theUfSession.Modl.AskMaster(), 
	theUfSession.Modl.AskFeatRelatives() etc. The program  prints a report 
	to the listing window.
 
	This example should run in the interactive mode.

	1. Start NX.
	2. Open Part file, analyasisArclengthDistance.prt (This file is provided along
	   with CS files. You can use any other part file containing at least one feature,
	   but then, you will get different information into the log file).
	3. Follow, step nos. 2,3,4,5 in How to Run VB example in the interactive mode"
	   section of this file.
	4. See the information displayed into the Listing Window. Compare the contents 
	   of the Listing Window with the contents of EX_Modl_FeatureType_vb.mstlog.

EX_Ui_ListingWindow.vb: 
	
	This example demonstrates how to open Listing Window device in using,
	theUfSession.Ui.OpenListingWindow() and prints data using, 
	theUfSession.Ui.WriteListingWindow() method.
	The program will create EX_Ui_ListingWindow.prt file and prints
	the name of the feature created into the Listing Window device.
	 
	This example should run in the interactive mode.

	1. Start NX.
	2. Follow, step nos. 2,3,4,5 in "How to Run example in the interactive mode" 
	   section of this file.
	3. See the information displayed into the Listing Window. Compare the contents 
	   of the Listing Window with the contents of EX_Ui_ListingWindow_vb.mstlog.
