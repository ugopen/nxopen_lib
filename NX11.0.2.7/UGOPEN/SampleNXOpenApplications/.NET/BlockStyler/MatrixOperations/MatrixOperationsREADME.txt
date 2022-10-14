'=============================================================================
'
'                   Copyright (c) 2010 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'
'  
'=============================================================================

------------------------------------------------------------------------------
        		Block Styler Matrix Operations Example
------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates usage of Block Styler Application in NX.
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
   2. MatrixOperations.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/MatrixOperations)

------------
Build steps
------------
   Windows
   -------
   1. Open Microsoft Visual Studio .Net.

   2. Create new project as:
      2.1. File->New->Project.
      2.2. Select Visual Basic Projects using the NX Open AppWizard, Class Library Application, Enter
           name as 'MatrixOperations'. Click Next
      2.3. Under Application Settings, select 'An Internal application that can be activated from an NX session (DLL)'
           and select 'NXOpen.UI API'. 
      2.4. Select to activate the application explicitly and to unload the application when NX session terminates. Click Finish.

   3. Remove the Module1.vb file from the project. Highlight it in the Solution Explorer and use the 3rd mouse button
      and pull to Delete it. You will receive a pop-up that says it will be deleted permanently. Hit OK.
   
   4. In the Solution Explorer highlight the project name and use the 3rd mouse 
      button and drag to Add.  Choose 'Add-> Existing Item'. Navigate to and add the MatrixOperations.vb file.
   		
   5. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project 
      name and select Build.

   6. This will create an executable called MatrixOperations.dll in the \bin\Release directory.

    Linux
   -------
    -NA-

----------------------------
Settings before Launching NX
----------------------------
The MatrixOperations.dlx file must be placed in one of the following locations:
	
   1. From where NX session is launched
   2. $UGII_USER_DIR/application
   3. For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
       recommended. This variable is set to a full directory path to a file 
       containing a list of root directories for all custom applications.
       e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat

----------------------------
Settings after Launching NX
----------------------------
1. Change the Role to Advanced.

-----------------------
Example execution steps
-----------------------
     Journal execution
     ------------------
      1. Open new part.
      2. Using Tools->Journal->Play or (ALT+F8)
      3. Select MatrixOperations.vb and Run
      4. This will pop-up Matrix operation dailog box.
      5. Under Matrix operations you can do the following operations.

           a) Multiplication
           b) Addition
           c) Deteminant
           d) Transpose
           e) Orthonormalize
           f) RotateAboutAxis
           g) VectorMultiply
           h) X-direction Vector
           i) Y-direction Vector
           j) Z-direction Vector

         Enter the matrix values under the INPUT fields and based on the matrix
         operation, The resultant matrix will be displayed under RESULT fields.
        
     Shared Library execution
     ------------------------
      1. Open new part.
      2. File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.
      3. Browse and select the MatrixOperations.dll and execute.
      4. Under Matrix operations you can do the following operations.

           a) Multiplication
           b) Addition
           c) Deteminant
           d) Transpose
           e) Orthonormalize
           f) RotateAboutAxis
           g) VectorMultiply
           h) X-direction Vector
           i) Y-direction Vector
           j) Z-direction Vector

         Enter the matrix values under the INPUT fields and based on the matrix
         operation, The resultant matrix will be displayed under RESULT fields.

------
Notes
------
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."

'=================================End=========================================
