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


   -  For build using ugmenu
      ----------------------
          
         - run ugmenu.
         - select version of ug (if asked to)
         - This will open "Unigraphics NX Activity Menu" application dialog
         - Select the option "UGOPEN-API  (User function)"  option and hit apply.
         - You are in "USER FUNCTION DEVELOPMENT ENVIRONMENT" menu.
         - Choose option "2-Compile"
             - Select all default options (i.e, hit return to all prompts).
             - You are back to "USER FUNCTION DEVELOPMENT ENVIRONMENT" menu.
         - Choose option "3-Link"
             - Specify option "e" for question on :
               "Link internal/external user function (i/e)".
             - Hit return to all other questions except the last question 
               on "Enter program to link=>"
               For that give executable name in this case "ufx_batchmeshing"
         - If there are no compile or link error check the working directory
           for the executable "ufx_batchmeshing"
           As a test try "ufx_batchmeshing -?" at the command prompt.  If help
           on usage is dumped out the build is fine!



HOW TO RUN
==========

   ufx_batchmeshing  -?  -h or -H 
                     -part=<Partname> -p=<Parameter file name> 
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

 
 
UG SUPPLIED EXECUTABLE
======================

   UG supplies a default build executable.  The executable is located in
   ugii directory and is named "ugnx_batchmesher" (with appropriate platform
   specific extension).
   
   

SAMPLE PARAM AND CRITERIA FILES
===============================
  
  Sample param and criteria files are provided.
     ufx_batchmeshing_sample_param.txt
     ufx_batchmeshing_sample_criteria.txt

  These may be edited in text editor to change only the numerical values.
