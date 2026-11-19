-------------------------------------------------------------------------------
          .Net      RemotingExample 
-------------------------------------------------------------------------------

Description:
------------
This example demonstrates the use of one way to setup Remoting for .Net.  This example consists of two C# projects.  One if the Server and one is for the Client.

Note about Example code:
The examples shows a .NET server program that uses the HTTP protocol. This sample program uses hardcoded values. In practice, this would be specified on the command line or by using .NET configuration files.


To build this example:
---------------------
Server:
- Open up the Server C# project (Server\Server.csproj) in Visual Studio.
- Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilitie
s.dll.
  To do this, right click on
  "References" under the AssemblyViewer project in Solution Explorer. Pick "Add
  Reference..." and then navigate to the location of the dlls. These dlls
  can be found in %UGII_ROOT_DIR%\managed.
- Build the project using Build - Build Solution and hit OK.
- The default location for the newly created Server.dll that is created
is in a
  subdirectory called Server\obj\Debug.


Client:
- Open up the Client C# project (Client\Client.csproj) in Visual Studio.
- Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilitie
s.dll.
  To do this, right click on
  "References" under the AssemblyViewer project in Solution Explorer. Pick "Add
  Reference..." and then navigate to the location of the dlls. These dlls
  can be found in %UGII_ROOT_DIR%\managed.
- Build the project using Build - Build Solution and hit OK.
- The default location for the newly created Client.exe that is created
is in a
  subdirectory called Client\obj\Debug.


To run this example:
-------------------
Note: you will need a .NET authoring license to run the example. See
the online documentation for details of licensing.

- Start NX.
- Type Ctrl-U to open the "Execute NXOpen" dialog.
- Navigate to Server.dll and press OK.

- In the Client C# project, run the Client.exe.  This will create a new part and with some simple curves.


