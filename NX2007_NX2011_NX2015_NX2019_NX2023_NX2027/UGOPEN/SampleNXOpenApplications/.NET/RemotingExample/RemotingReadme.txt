-------------------------------------------------------------------------------


          Copyright 2010 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                           .Net Remoting Example 
-------------------------------------------------------------------------------

Description:
------------
This example demonstrates the use of one way to setup Remoting for .Net.  This 
example consists of two C# projects.  One is the Server and one is for the 
Client.

Note about Example code:
The examples shows a .NET server program that uses the HTTP protocol. This 
sample program uses hardcoded values.In practice, this would be specified on 
the command line or by using .NET configuration files.

Please note for the server code:  the Run method (which is put in infinite 
sleep state) should only perform the following operations:
     - Setting up Remoting 
     - Obtaining the session
     - Exporting the session
     
If you make other calls especially NXOpen calls that may involve the UI (such 
as ListingWindow).  This may put NX in a state of an infinite loop.  Calls to
the LogFile API are acceptable though.

Additionally, the methods GetUnloadOption and UnloadLibrary are implemented.  This server
is setup so that it can be unloaded using the File->Utilities->Unload Shared Images 
functionality.  The server can be stopped by explicitly unloading it using the
Unload Shared Images functionality.  This will stop the infinite loop and disconnect
the session.


--------------
Files required
--------------
	1. Client.csproj
	2. NXOpenRemotingClient.cs
	The above listed files are located at $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\RemotingExample\Client

	3. NXOpenRemotingService.cs
	4. Server.csproj
	The above listed files are located at $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\RemotingExample\Server

	
-------------------------
Build steps
-------------------------

	Windows
	-------
	Server:
	1. Open up the Server C# project (Server\Server.csproj) in Visual Studio.
	
	2. Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll.
	   To do this, right click on "References" under the Server project in Solution Explorer. 
	   Pick "Add Reference..." and then navigate to the location of the dlls. 
	   These dlls can be found in %UGII_BASE_DIR%\nxbin\managed.
	   
	3. Build the project using Build - Build Solution and hit OK.
	
	4. The default location for the newly created Server.dll that is created is in a subdirectory called Server\obj\Debug.

	Client:
	1. Open up the Client C# project (Client\Client.csproj) in Visual Studio.

	2. Add references to NXOpen.dll, NXOpen.UF.dll,NXOpen.UI.dll, and NXOpen.Utilities.dll.
	   To do this, right click on "References" under the Client project in Solution Explorer. 
	   Pick "Add Reference..." and then navigate to the location of the dlls. 
	   These dlls can be found in %UGII_BASE_DIR%\nxbin\managed.
	   
	3. Build the project using Build - Build Solution and hit OK.
	
	4. The default location for the newly created Client.exe that is created is in a subdirectory called Client\obj\Debug.
  
	Linux
	-------
    -N/A-
   

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

Note: you will need a .NET authoring license to run the example. See
the online documentation for details of licensing.

	1. Start NX through the NX command prompt.
	
	2. Type Ctrl-U to open the "Execute NXOpen" dialog.
	
	3. Navigate to Server.dll(Server\obj\Debug\Server.dll) and press OK.
	
	4. Using the same NX command prompt, run the Client.exe(Client\obj\Debug\Client.exe).
       This will create a new part with some simple curves. You may need to zoom out to see the curves created.

------
Notes
------
    1. "NXOpen application must be signed before its release. If not signed the application may not get executed.
       For more details on signing the application refer to NXOpen Programmer's Guide."

    2. The server can be shutdown by using the File->Utilities->Unload Shared Images functionality.

    3. After the server is shutdown, you can start up the server again by using the "Execute NXOpen" dialog.
