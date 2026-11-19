------------------------------------------------------------------------------------

          Copyright 2012 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.

------------------------------------------------------------------------------------



------------------------------------------------------------------------------------
                        ExecuteCheckerAndGetResults Example
------------------------------------------------------------------------------------

-----------
Description
-----------
    This example demonstrates how to record the journal of executing a Check-Mate checker,
    and how to get the executing result of a Check-Mate checker by playing the journal in NX.

    This example uses the Check-Mate checker %mqc_report_browseable_features whose
    display name is "Number of browseable features", and this Check-Mate checker reports
    the number of browseable features in the work part. This example records journal
    using C Sharp and VB.Net languages.

--------------
Files required
--------------
    1. ExecuteCheckerAndGetResults.prt
    2. ExecuteCheckerAndGetResults.cs
    3. ExecuteCheckerAndGetResults.vb

    The above listed files are located at
    $UGII_BASE_DIR\ugopen\SampleNXOpenApplications\.NET\CheckMate\ExecuteCheckerAndGetResults

-----------
Build Steps
-----------

Windows
-------
For VB.Net:

    1. Open Microsoft Visual Studio.

    2. Create a new Vb project using the NX Open AppWizard.
       Create new project as:

        2.1 File->New->Project.

        2.2 Select Vb Project using the NX Open AppWizard, Class Library Application,
            Enter name as ExecuteCheckerAndGetResults. Click Next.

        2.3 Under Application Settings, select 'An Internal application that can be
            activated from an NX session (DLL)'.

        2.4 Select to activate the application explicitly and to unload the
            application when NX session terminates. Click Finish.

    3. Remove all *.vb files from created project by clicking MB3 on respective file and
       clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be
       deleted permanently. Hit OK.

    4. Add the ExecuteCheckerAndGetResults.vb to the project by selecting the Project
       pull down and select "Add Existing Item...". Select the file using the popup window.

    5. Confirm following four references are added into this project:

        $UGII_BASE_DIR\nxbin\managed\NXOpen.dll
        $UGII_BASE_DIR\nxbin\managed\NXOpen.UF.dll
        $UGII_BASE_DIR\nxbin\managed\NXOpen.Utilities.dll
        $UGII_BASE_DIR\nxbin\managed\NXOpenUI.dll

       Confirm the version of target framework is .NET Framework 4:

        Right-click this project in the Solution Explorer and select Properties on the popup menu.
        Go to Compile tab page, click Advanced Compile Options... button at the bottom of this page.
        On the Advanced Compiler Settings dialog, select .NET Framework 4 for Target
        framework, and select AnyCPU or X64 for Target CPU if 64 bit NX is used.

       Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

    This will create an executable called ExecuteCheckerAndGetResults.dll in the Debug directory.

For C Sharp:

    1. Open Microsoft Visual Studio.

    2. Create a new VC# project using the NX Open AppWizard.
       Create new project as:

        2.1 File->New->Project.

        2.2 Select VC# Project using the NX Open AppWizard, Class Library Application,
            Enter name as ExecuteCheckerAndGetResults. Click Next.

        2.3 Under Application Settings, select 'An Internal application that can be
            activated from an NX session (DLL)'.

        2.4 Select to activate the application explicitly and to unload the
            application when NX session terminates. Click Finish.

    3. Remove all *.cs files from created project by clicking MB3 on respective file and
       clicking 'Delete' on pop-up menu. You will receive a pop-up that says it will be
       deleted permanently. Hit OK.

    4. Add the ExecuteCheckerAndGetResults.cs to the project by selecting the Project
       pull down and select "Add Existing Item...". Select the file using the popup window.

    5. Confirm following four references are added into this project:

        $UGII_BASE_DIR\nxbin\managed\NXOpen.dll
        $UGII_BASE_DIR\nxbin\managed\NXOpen.UF.dll
        $UGII_BASE_DIR\nxbin\managed\NXOpen.Utilities.dll
        $UGII_BASE_DIR\nxbin\managed\NXOpenUI.dll

       Confirm the version of target framework is .NET Framework 4:

        Right-click this project in the Solution Explorer and select Properties on the popup menu.
        Select .NET Framework 4 for Target framework on the Application tab page.

       Build the internal image by going to the Build menu and selecting either "Build Solution" or "Rebuild Solution".

    This will create an executable called ExecuteCheckerAndGetResults.dll in the Debug directory.

Linux
-------
    -N/A-

----------------------------
Settings before Launching NX
----------------------------
    None

----------------------------
Settings after Launching NX
----------------------------
    None

--------------------------
Example execution steps
--------------------------

    1. Start NX.

    2. Open the part file ExecuteCheckerAndGetResults.prt.

    3. Change the Role to Advanced if not set.

    4. Find the four features in the Part Navigator in the work part.

    5. Open Check-Mate on the HD3D Tools. Click the Set Up Tests button to open Set Up Tests dialog.

    6. Click Tests to load all checkers. Notice that there will be a tree structure in the Categories area.

    7. Execute the example to execute checker by one of following two ways:

        7.1 Journal execution
            -----------------
            Invoke ExecuteCheckerAndGetResults.vb file or ExecuteCheckerAndGetResults.cs file
            using Tools->Journal->Play... (Alt+F8).

        7.2 Library execution
            -----------------
            Invoke ExecuteCheckerAndGetResults.dll coming from the VB.Net or C Sharp project
            using File->Execute->NX Open... (Ctrl+U).

-----
Note:
-----
    1. "NXOpen application must be signed before its release. If not signed the application may not get executed.
       For more details on signing the application refer to NXOpen Programmer's Guide."

    2. A Check-Mate license and a .NET authoring license is required to run the
       example. See the online documentation for details of licensing.

    3. This example was generated by recording this workflow:

       3.1 Open Check-Mate on the HD3D Tools. Click the Set Up Tests button to open Set Up Tests dialog.
       3.2 Click Tests to load all checkers. Notice that there will be a tree structure in the Categories area.
       3.3 Select the Check-Mate checker Get Information->Modeling->Number of browseable features. Click the Add to Selected button.
       3.4 The checker will appear in the Chosen Tests area. Click Execute Check-Mate button to execute the chosen checker.
       3.5 Notice four features will be reported in the Results area of the Check-Mate.

-----------
CAVEATS
-----------

    None

