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
	   name as UistylerSelectionMaskExample(you can specify name of your choice). 
	3. Click on Ok. 
3. Remove the Class1.vb file from the project.  Highlight it in the Solution Explorer and use the 3rd mouse button
   and pull to Delete it. You will receive a pop-up that says it will be deleted permanently. Hit OK.
 
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
   		
6. Go to, Build Menu -> Build Solution or Ctrl + Shift + B or go to Solution Explorer, right click on project 
   name and select Build.

--------------------------------------
How to Run VB Examples
--------------------------------------

Once you have successfully finished with "How to Build VB examples" steps, it will create executable called 
UistylerSelectionMaskExample.dll in bin dir of the project dir.

	1. Start NX.
	2. Open UistylerSelectionMaskExample.prt file.
	2. Go to File -> Execute -> NX Open.
	3. This will lead to a window called "Execute User Function". 
	4. Navigate to the location of the dll file.  It will be in the <Project      
         Folder>\bin\Debug\ directory under the directory named for VB project.
	5. Select UistylerSelectionMaskExample.dll file and Click ok. The "Move To Layer" dialog pops up.
	6. Set the Toggle ON for all the entities for which you need to set the Mask and hit the SetFilter button. 
	   Now, you will be able to select only those entities for which the Toggle is ON. Everytime you change the
	   filter items you need to hit Set Filter button in order to change the Selection Mask.
	7. If you Hit on the Layer Setting button, this pops up an information window showing the layer categories, 
	   the layers in each category and the object count in each layer.
	8. After selection, change the layer number in "Move to Layer" field to the layer to which you would like to 
	   move the entities to, and Hit Apply or OK. This will move the selected entities to the desired layer. You can
	   check the number of objects in the layers thru the "Layer Setting Information" button.
	   
