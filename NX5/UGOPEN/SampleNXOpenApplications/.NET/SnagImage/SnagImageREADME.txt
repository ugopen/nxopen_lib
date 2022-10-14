-------------------------------------------------------------------------------
		SnagImage Example
-------------------------------------------------------------------------------


Description:
------------
This example demonstrates the use of the NXOpen.UF (.NET Wrapper of UF)API in 
conjunction with Winforms.

The example uses .NET Wrapped UG/Open (NXOpen.UF) API 'Disp.CreateImage' to 
capture the NX Graphics Window in different image formats with different 
background color

To build this example in VB.NET:
- Open up the VB .NET project (SnagImageVB.vbproj) in Visual Studio.
- Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll. 
  To do this, right click on
  "References" under the SnagImage project in Solution Explorer. Pick "Add
  Reference..." and then navigate to the location of the dlls. These dlls
  can be found in %UGII_ROOT_DIR%\managed.
- Build the project using Build - Build Solution and hit OK.
- The default location for the newly created SnagImageVB.dll that is created is in a 
  subdirectory called bin\Debug.


To build this example in C#:
- Open up the C# project (SnagImage.csproj) in Visual Studio.
- Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll. 
  To do this, right click on
  "References" under the SnagImage project in Solution Explorer. Pick "Add
  Reference..." and then navigate to the location of the dlls. These dlls
  can be found in %UGII_ROOT_DIR%\managed.
- Build the project using Build - Build Solution and hit OK.
- The default location for the newly created SnagImage.dll that is created is in a 
  subdirectory called bin\Debug.

--------------------------------------

To run this example:
- Start NX.
- Open a any part
- Type Ctrl-U to open the "Execute NXOpen" dialog.
- Navigate to SnagImage.dll or SnagImageVB.dll and press OK. 
  You should see the "SnagImage" form appear.
- While the form is up, Select the file format, background color and 
  name/location of the image file
- Click SnagIt button.
- When the image is generated, you will receive a pop-up telling you so.
- By default, this image file will be created in the directory where NX was stared.
