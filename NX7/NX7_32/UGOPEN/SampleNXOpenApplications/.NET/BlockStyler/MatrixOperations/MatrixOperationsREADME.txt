-------------------------------------------------------------------------------
		Block Styler MatrixOperations Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstartes usage of Block Styler Application in NX.
The set of APIs designed for Block Styler application are property based. While using 
these APIs one must be aware about the Block, its associated properties and their datatype.
This program uses UI Blocks like 
- DoubleTable,    - Enumuration,    - Double, 
- Toggle,         - SpecifyVector,  - AngularDim.

Executing this example will launch a dialog which allows you to perform Matrix operations like
- Multiplication       - Addition            - Determinant   -Transpose   
 - OrthoNormalize       - RotateAboutAxis     - VectorMultiply
- X-direction Vector   - Y-direction Vector  - Z-direction Vector

This sample program uses UFwrappers (NXOpen.UF APIs) to perform matrix operations. 

--------------
Files required
--------------
1. MatrixOperations.vb
2. MatrixOperations.dlx : The dlx file must be placed in one of the following locations:
	
	1.) From where NX session is launched
	2.) $UGII_USER_DIR/application
	3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
	    recommended. This variable is set to a full directory path to a file 
	    containing a list of root directories for all custom applications.
	    e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat

----------------------
How to run the example
----------------------

1. Using Tools->Journal->Play 

	1. Start NX.
	2. Create new part.
	3. Read the instruction under DIALOG LAUNCHING section of MatrixOperations.vb
	   in order to understand where to keep the MatrixOperations.dlx file.
	4. Invoke MatrixOperations.vb file using Tools->Journal->Play.
	
2. By creating Shared Library and invoke it through File->Execute->NX Open Menu. 
   
   Once you have successfully finished with "How to Build VB/C# example" steps, 
   follow the steps below:

	1. Start NX.
	2. Create new part.
	3. Read the instruction under DIALOG LAUNCHING section of MatrixOperations.vb
	   in order to understand where to keep the MatrixOperations.dlx file.
	4. Invoke Shared Library through  File->Execute->NX Open  Menu.
	
--------------------------
How to Build VB/C# example
--------------------------
1. Open Microsoft Visual Studio .Net.

2. Create a new VB/C# project using the NX Open AppWizard. This is described in the 
   NX Open Programmers Guide -> Wizard Setup.
   Also information under Creating NX Open Automation -> Applications will be helpful.
   When setting the Application Settings, select "Create an Internal application"
   and select NXOpen.UI API. 
   Select to activate the application Explicitly and to unload when NX terminates.
   Then pick Finish.

3.  Add the MatrixOperations.vb to the project by selecting the Project pulldown and select 
    "Add Existing Item...". Select the file using the popup window.

4. Build the internal image by going to the Build menu and selecting either "Build" or "Rebuild".

This will create an executable called MatrixOperations.dll in the Release directory.

