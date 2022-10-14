-------------------------------------------------------------------------------

           Copyright 2008 Siemens PLM Software Inc.
                   All Rights Reserved.
                   
   
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
                 Managed Cpp Example
-------------------------------------------------------------------------------

-----------
Description
-----------
This NX Open example demonstrates the use of NX Open using Managed C++ (.NET).  
The example opens a listing window with a text line.

There are two entry points Main() and ufget() in the automation file. The Main() function gets
executed through the menu option File -> Execute -> NX Open, and ufget() is executed through File -> Open.


--------------
Files required
--------------

      1.ManagedCpp.vcxproj
      2.ManagedCpp.cpp
      3.NXSigningResource.res
      
 All the above files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/.NET/ManagedCpp
            
-----------
Build Steps
-----------      
    1. Open up the project ManagedCpp.vcxproj in Visual Studio.
    
    2. Add references to NXOpen.dll, NXOpen.UF.dll,and NXOpen.Utilities.dll. 
       To do this, right click on
       "References" under the ManagedCpp project in Solution Explorer. Pick "Add
       Reference..." and then navigate to the location of the dlls. These dlls
       can be found in %UGII_BASE_DIR%\nxbin\managed.  Set the copy local attribute
       for these DLLs to be false so you always use the versions from the NX install.
       
    3. Set "Common Language Runtime Support" option to Common Language Runtime Support (/clr:safe).
    4. Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

   This will create an executable called ManagedCpp.dll in the Debug directory.
   
   
----------------------------
Settings before Launching NX
----------------------------
 There are two Entry points Main() and ufget() in the automation file. To execute ufget(),
 the environment variable USER_RETRIEVE should be defined to the complete path of ManagedCpp.dll.
 
 No settings required to execute the Main() function.
    
----------------------------
Settings after Launching NX
----------------------------

1. Change the Role to Advanced.    
    
--------------------------
Example execution steps
--------------------------

To execute Main() function:

        1. Start NX.
        
        2. Go to File -> Execute -> NX Open through Menu or type Ctrl+U to open the "Execute User Function" dialog.
        
        3. Navigate to ManagedCpp.dll and press OK. 
        
        4. An Information window containing the text, "Running Managed C++ Sample Application. Executed through the function: Main" will
           appear.

To execute ufget() function:

        1. Start NX

        2. Go to File->Open through Menu option.

        3. An Information window containing the text, "Running Managed C++ Sample Application. Executed through the function: ufget" will
           appear.

--------------------------                   
Signing the example:
--------------------------  
"NXOpen application must be signed before its release. If not signed the application may not get executed.
 For more details on signing the application refer to NXOpen Programmer's Guide."  
 
You will need a .NET authoring license to run the example. See the online documentation for details of licensing.


The NXSigningResource.res has been setup to be embedded into the dll.  So after building this example you can run the %UGII_BASE_DIR%\nxbin\SignLibrary.exe utility to sign this DLL.

To set this up for generic managed C++ solution, go to the project property pages and add the path to 'NXSigningResource.res' in: Configuration Properties -> Linker -> Input -> Embed Managed Resource File (the equivalent command-line option is /ASSEMBLYRESOURCE:file).
        





 
