-------------------------------------------------------------------------------
		UIStyler Selection Example
-------------------------------------------------------------------------------


Description:
------------
This example demonstrates the Selection capability of NXOpen UIStyler.
Running this example will launch a dialog which creates Edge Blend on the selected edges.


---------------------------------------
How to Build VB examples
---------------------------------------
1. Open Microsoft Visual Studio .Net 2005.

2. Create new project as :
	1. File->New->Project.
	2. Select Visual Basic Projects, Class Library Application, Enter
	   name as UIStylerselectionExample(you can specify name of your choice). 
	3. Click on Ok. 
3. Remove the Class1.vb file from the project.  Highlight it in the Solution Explorer and use the 3rd mouse button and pull to Delete it.  You will receive a pop-up that says it will be deleted permanently. Hit OK.
 
4. Add the following references,
	   1. NXOpen.dll 
	   2. NXOpenUI.dll 
	   3. NXOpen.Utilities.dll
	   4. NXOpen.UF.dll.

	   To do this, right click on "References" under the project in Solution
	   Explorer. Pick Add Reference->Browse->Go to %UGII_ROOT_DIR%\out\ugac,
	   select DLL.

5. In the Solution Explorer highlight the project name and use the 3rd mouse 
  button and drag to Add.  Choose Add Existing Item.  Navigate to and add any 
  of the *.vb file.
   		
6. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project name and select Build.

--------------------------------------
How to Run VB Examples
--------------------------------------

Once you have successfully finished with "How to Build VB examples" steps, it will create executable called UistylerselectionExample.dll in bin dir of the project dir.
	1. Start NX.
	2. Open Block.prt file
	2. Go to File -> Execute ->NX Open.
	3. You will lead to window called "Execute User Function". 
	4. Navigate to the location of the dll file.  It will be in the <Project      
         Folder>\bin\Debug\ directory under the directory named for VB project.
	5. Select UistylerselectionExample.dll file and Click ok.


---------------------------------------
How to Build C# examples
---------------------------------------
1. Open Microsoft Visual Studio .Net 2005.

2. Create new project as :
	1. File->New->Project.
	2. Select Visual C# Projects, Class Library Application, Enter
	   name as UIStylerselectionExample(you can specify name of your choice). 
	3. Click on Ok. 
3. Remove the Class1.cs file from the project.  Highlight it in the Solution Explorer and use the 3rd mouse button and pull to Delete it.  You will receive a pop-up that says it will be deleted permanently. Hit OK.
 
4. Add the following references,
	   1. NXOpen.dll 
	   2. NXOpenUI.dll 
	   3. NXOpen.Utilities.dll
	   4. NXOpen.UF.dll.

	   To do this, right click on "References" under the project in Solution
	   Explorer. Pick Add Reference->Browse->Go to %UGII_ROOT_DIR%\out\ugac,
	   select DLL.

5. In the Solution Explorer highlight the project name and use the 3rd mouse 
  button and drag to Add.  Choose Add Existing Item.  Navigate to and add any 
  of the *.cs file.
   		
6. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project name and select Build.

--------------------------------------
How to Run C# Examples
--------------------------------------

Once you have successfully finished with "How to Build C# examples" steps, it will create executable called UistylerselectionExample.dll in bin dir of the project dir.
	1. Start NX.
	2. Open Block.prt file
	2. Go to File -> Execute ->NX Open.
	3. You will lead to window called "Execute User Function". 
	4. Navigate to the location of the .dll file.  It will be in the <Project      
         Folder>\bin\Debug\ directory under the directory named for CS project.
	5. Select UistylerselectionExample.dll file and Click ok.
