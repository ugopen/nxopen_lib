====================================================================================================
                 Copyright 2017 Siemens Product Lifecycle Management Software Inc.
====================================================================================================

        	        	Routing Callbacks, Plugins, and Design Rule Examples

----------------------------------------------------------------------------------------------------

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

----------------------------------------------------------------------------------------------------
EXAMPLE DESCRIPTION

Callbacks are NX Open code Routing will call after a command has run. Refer to the NX Open 
documentation in the Custom Manager for the list of callback reasons and the commands 
associated with them.

Plugins are NX Open code Routing typically will call instead of the core Routing code. For example,
if you want to calculate the diameter of a bundle of wires using your own method, register your 
own Bundle plugin.

Design Rules are NX Open code Routing will call after a command has run to give customers a 
chance to verify the objects just created or changed meet their design rules. Refer to the NX Open 
documentation in the Custom Manager for the list of Design Rule reasons and the commands 
associated with them.

These examples demonstrate how to write Callbacks, Plugins, and Design Rules to be executed by
various Routing commands. Each of the files contains just of few of the many ways Callbacks, 
Plugins, and Design Rules can be written for Routing commands.

You can register more than one Callback or Design Rule using the same reason. Routing will call
every Callback and Design Rule you register for a given reason one after the other. If a Callback
or Design Rule throws an error, Routing will write the error to the log file and continue to the
next registered Callback or Design Rule.

However, you can only register one plugin. If a Plugin throws an error, Routing will write 
the error to the log file.

Callbacks, Plugins, and Design Rules configured in the Application View (APV) file take precedence
over those that you register. In fact, you will see a note in the log file if you try to register 
Callbacks, Plugins, and Design Rules which already have an APV-configured program. If there is
an APV-configured program, Routing will call that one and ignore any registered Callbacks, Plugins,
and Design Rules. In a future NX release, the APV-configured Callbacks, Plugins, and Design Rules
will no longer be supported.

----------------------------------------------------------------------------------------------------
FILES REQUIRED

    1. Routing_Example_Callbacks.java
    2. Routing_Example_DesignRules.java
    3. Routing_Example_Plugins.java
	
The above listed files are located at $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/Java/Routing.

----------------------------------------------------------------------------------------------------
BUILD STEPS

The build steps vary depending on the language in which you write your Callbacks, Plugins, and
Design Rules. However you build the examples, you need to end up with a .class file.

----------------------------------------------------------------------------------------------------
SETUP BEFORE LAUNCHING NX

The output file built (e.g. .class) must be placed in one of the following locations:
   1. $UGII_SITE_DIR/startup
   2. $UGII_GROUP_DIR/startup
   3. $UGII_USER_DIR/startup
   4. For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
        recommended. This variable is set to a full directory path to a file 
        containing a list of root directories for all custom applications.
        e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
        
----------------------------------------------------------------------------------------------------
EXAMPLE EXECUTION STEPS

Routing executes the Callbacks, Plugins, and Design Rules from various commands within the Routing
applications. The following steps show how to execute the Create Path Design Rule in the DesignRules.java
file.

	  1. Create a new Routing Electrical file using File->New.
      2. Launch the Spline Path and click several points in the Graphics Window until you have a
         spline that is longer than 1,000 millimeters.
      3. Hit OK.

At this point, you should see a Design Rule Violation displayed that says the segment is too long.
This violation was created by the example Design Rule.

----------------------------------------------------------------------------------------------------
NOTES

NX Open application must be signed before its release. If not signed the application may not get executed.
For more details on signing the application refer to NX Open Programmer's Guide.


