This file describes how to build and run CAE batch meshing application
as a standalone module (without UI).

HOW TO COMPILE
==============
  
   -  It is assumed that user has license to ugopen. Has access to
      proper version of C/C++ compilers.

   -  Take all the files (except the readme file) to your working directory.
      

   -  The files that are must are :  
    
          ufx_batchmeshing.cxx
          ufx_batchmeshing_paramreader.cxx
          ufx_batchmeshing_paramreader.hxx
          ufx_geomassignmodule.cxx
          ufx_geomassignmodule.hxx

-----------
Build Steps
-----------

   Windows
   -------
   1. Using Visual Studio - create a new project using the NXOpen AppWizard.
      This is described in the Automation -> NXOpen -> Open for C/C++ -> 
	  Open C Reference Guide -> Overview -> Setting up your system -> Windows Operating System Setup. 
      When setting the Application Settings, select "An external application that runs independent of NX (EXE)" 
      and select C++ as the language. 

   2. Remove all the existing files from project.
   
   3. Add the files from above to Source Files
      by selecting the Project pulldown and select "Add Existing Item...". Select the file 
      using the popup window.

   4. Build the internal image by going to the Build menu and selecting either 
      "Build Solution" or "Rebuild Solution".
 
   This will create an executable called ufx_batchmeshing.exe in the Debug directory.   

   Linux
   ----
   1. Start up an NX command prompt window then start up ufmenu ($UGII_BASE_DIR/ugopen/ufmenu).
   2. Compile the program accepting the defaults.
   3. Link an internal user function program.
   4. Answer the first question for linking with an "i" (Link internal/external user function (i/e):) 
      Select "y" for the next input to create an application with user interface code
      Select "y" for the next input to Link a UG/Open++ Image (y/n).
   5. Take the default linking options.
   6. Provide the name of the program to link => Selection
   7. Do not add any subroutines or libraries.
       
   This will create ufx_batchmeshing.so in the current directory.

   Exit out of ufmenu.
   



HOW TO RUN
==========

   ufx_batchmeshing  -?  -h or -H 
                     -part=<Partname> -p=<Parameter file name> -t=<Template file name>
                     -c=<Criteria file name> -no_idealize  
                     -fem -dat=<extension> -key_word=<some keyword string> 

   Gives complete usage.  
   
   For help on detailed options : ufx_batchmeshing  -?
   
   Note the command line parameters do not need to be in the above listed 
   order.
   
   All parameters must have "-" preceeding the parameter name.  Example
   "-part" and not "part"
   
   The individual parameters that take values must not have any blanks 
   between parameter name and "=" and value following "=". For example
   "part = <part_name>" or "-part = <part_name>" are not allowed. 

 
 
NX SUPPLIED EXECUTABLE
======================

   NX supplies a default build executable.  The executable is located in
   nxbin directory and is named "ugnx_batchmesher" (with appropriate platform
   specific extension).
   
   

SAMPLE PARAM AND CRITERIA FILES
===============================
  
  Sample param and criteria files are provided.
     ufx_batchmeshing_sample_param.txt
     ufx_batchmeshing_sample_criteria.txt

  These may be edited in text editor to change only the numerical values.
