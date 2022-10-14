PolygonTool Example

Description:

This example demonstrates the use of the NX Automation API in conjunction with
Winforms. The example uses sketcher functionality to create constrained
polygons based on parameter data supplied by the user via a Winform.

To build this example:

- Open up the VB .NET project (PolygonTool.vbproj) in Visual Studio.
- Set the reference path to the NXOpen* dlls. To do this, MB3 on the
  PolygonTool project in Solution Explorer and pick Properties. Under Common
  Properties, pick Reference Path. Add the directory for the managed dlls to
  the Reference Path (enter the location and click Add Folder).
  Note: The dlls are located at %UGII_ROOT_DIR%\managed but you will need to
  enter the value of %UGII_ROOT_DIR% instead of the variable directly because
  Visual Studio does not accept environment variables in the Reference Path.
- Build the project.

To run this example:

- Start NX.
- Open a new part, go into Modeling, and then into Sketcher.
- Type Ctrl-U to open the "Execute User Function" dialog.
- Navigate to PolygonTool.dll and press OK. You should see the "Create
  Polygon" form appear.
- Enter in the number of sides, diameter, and set the inscribed/circumscribed
  option. Press OK to create the constrained polygon.

