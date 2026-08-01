-------------------------------------------------------------------------------

          Copyright 2014 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.


-------------------------------------------------------------------------------

------------------------------------------------------------------------------
        		Block Styler Matrix Operations Example
------------------------------------------------------------------------------

-----------
Description
-----------
This example demonstrates the usage of a Block Styler Application in NX.
The set of APIs designed for Block Styler application are property based. While using 
these APIs one must be aware about the Block, its associated properties and their datatypes.
This program uses UI Blocks like 
- DoubleTable,    - Enumeration,    - Double, 
- Toggle,         - SpecifyVector,  - AngularDim.

Executing this example will launch a dialog which allows you to perform Matrix operations like
- Multiplication       - Addition            - Determinant   -Transpose   
- OrthoNormalize       - RotateAboutAxis     - VectorMultiply
- X-direction Vector   - Y-direction Vector  - Z-direction Vector

This sample program uses UFwrappers (NXOpen.UF APIs) to perform matrix operations. 

--------------
Files required
--------------
   1. MatrixOperations.py
   2. MatrixOperations.dlx (This file is located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/BlockStyler/MatrixOperations)

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
      3. Select MatrixOperations.py and Run
      4. This will pop-up the Matrix operation dialog box.
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
         operation, the resultant matrix will be displayed under RESULT fields.
        

