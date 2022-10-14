'===================================================================================
'
'          Copyright (c) 2020 Siemens Product Lifecycle Management Software Inc.
'                               All rights reserved
'
' 
'  
'===================================================================================

------------------------------------------------------------------------------------
                        User Defined Scenarios
------------------------------------------------------------------------------------


User Defined Scenarios are a new plugin mechanism for Simcenter users that allows them to extend post processing capabilities via
NXOpen.
Its main purpose is to allow users to create and register customised scenarios in Scenario Based Data Visualization context and 
apply them onto selected data.
That way the scenario descriptor, transformation function and other available callback functions can be personalised to match and
model selected data according to your needs.


-------------------------
How does the system work?
-------------------------

The scenario descriptor is defined using XML by strictly complying with scenarios.dtd type definition file that can be 
found at %UGII_BASE_DIR%\simulation\PostScenario.
A scenario descriptor specifies default styles, layouts, and instructs the system to only provide the data that you asked for.
The XML scenario descriptor can be inlined within the language specific (C++, Python, .NET or Java) scripting file or kept as a 
separate file and referenced in the scripting.
The scenario registration relies on the part created/opened callbacks that are getting registered at Simcenter startup.
When there is a positive data-scenario match, the scenario can be found under Scenario Based Data Visualisation -> Scenarios ->
User Defined.
A number of existing functions can be overriden and behaviour customised as required through an existing mechanism of callbacks, 
such as the data transformation, choice provider, deformation transformation, data aggregation, orientation transformation, 
override default data set match, override data set selection and sensitivity function callbacks.


---------------------------------
Deploying User Defined Scenarios
---------------------------------

Depending on the scripting language used Post Scenario uses preexisting functionality to allow users to register their scenarios 
at Simcenter startup.

There are currently two ways of loading your scenarios at Simcenter startup by using any of the two environment variables
and placing files at the chosen path
	I. UGII_CUSTOM_DIRECTORY_FILE
		- this variable should be set to point to a text file. 
		- the text file should contain one directory path per line
		- the name of the directories doesn't matter
			Path examples in .txt file pointed by environment variable:
				D:\UserScenarios
				D:\MyScenarios
		- for each directory, a subdirectory named "startup" is searched for
			Path examples:
				D:\UserScenarios\startup
				D:\MyScenarios\startup
		- the <custom_directory>\startup should contain a script, which implements a startup method 

	II. UGII_USER_DIR
		- similar to UGII_CUSTOM_DIRECTORY_FILE, but it should be set to point to the path where your scenario files are located
			Path example:
				D:\UserScenarios
		- at the set path the scenarios should be stored in a folder named "startup"
			Path example:
				D:\UserScenarios\startup

1. Python
Python scenario scripts should be dropped in the startup folder as indicated by the environment variable used.

2. C++, .NET(VB, C#), and Java
For C++, .Net, and Java, you have to create a project that builds a dynamically linked library or -- in Java's case --
Java archives (*.jar) or java classes (*.class).
All these final products should then be added in the startup folders as indicated by the environment variable used.

If the XML Scenario Descriptor is kept as a separate file, it should be dropped in the same startup folder as the scripting file.

If a scenario will have a successful match with the selected data, then the Scenario will be available under
Scenario Based Data Visualisation -> Scenarios -> User Defined.


-------------------------------------
How do you use the example scenarios?
-------------------------------------

Some examples of user defined scenarios that illustrate the functionality are available in:
%UGII_BASE_DIR%\ugopen\SampleNXOpenApplications\<language_specific_folder>\CAE\UserDefinedScenarios
where language_specific_folder stands for Python, DotNet, CPP or Java.
To load the example scenarios refer to the previous section "Deploying User Defined Scenarios".
Example data files can be found in the same folder as the scenarios and you can use them when trying the example scenarios. The
data files will have to be added as external data files in the Scenario Based Data Visualization navigator to have a successful
match with examples given.

-----
Java
-----
1. Multiple Visualizations Scenario
    Scenario:  MultipleVisualizationsScenario.java
    Data file: FunctionDataSample.unv

	This scenario exemplifies viewing of the same data in multiple visualisation types, in our case a XY plot, a vector plot and a
	bar chart plot.

-----------
Build Steps
-----------
    Windows
    -------
    Preconditions:
        i.  Have the Java JDK installed on your machine.
        ii. For optimal results have the NXOpen.jar, NXOpenUF.jar in the same folder as the java example scenario.
            The required jars can be found at %UGII_BASE_DIR%\kits\nxbin\.

    1. Make sure you have me the pre-requisites

    2. Open a command prompt window as administrator: WinKey->cmd

    3. In the command prompt window navigate to your folder where the scenario and libraries are available

    4. When at the right path in the command prompt window run the following command:
       javac -cp ./* MultipleVisualizationsScenario.java
       or for the last part of the commnad the name of the java file to be built

    7. This will create a .class file in the same folder that can be loaded in Simcenter thereafter

    At this point the resulting .class can be added in the startup folder indicated by the UGII_USER_DIR or a startup folder as pointed
    in the paths from the text file specified by UGII_CUSTOM_DIRECTORY_FILE.

    Note: 
    The Java installation can be checked to see if it meets the Simcenter requirements.
    That can be done by launching File->Execute->Check Java for Simcenter 3D

