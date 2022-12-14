------------------------------------------------------------------------------------

       Copyright 2014 Siemens Product Lifecycle Management Software Inc. 
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
    the number of browseable features in the work part. This example uses a journal 
    recorded using the Python programming language.

--------------
Files required
--------------
    ExecuteCheckerAndGetResults.py
    
    You can use the sample part file ExecuteCheckerAndGetResults.prt located at 
    $UGII_BASE_DIR/ugopen/SampleNXOpenApplications/C++/CheckMate/ExecuteCheckerAndGetResults
    or any part file with modeling features.

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

    7. Execute the checker by the following method:

        7.1 Journal execution
            -----------------
            Invoke ExecuteCheckerAndGetResults.py file
            using Tools->Journal->Play... (Alt+F8).

-----
Note:
-----
    1. A Check-Mate license  is required to run the example. See the 
       online documentation for details of licensing.

    2. This example was generated by recording this workflow:

       2.1 Open Check-Mate on the HD3D Tools. Click the Set Up Tests button to open Set Up Tests dialog.
       2.2 Click Tests to load all checkers. Notice that there will be a tree structure in the Categories area.
       2.3 Select the Check-Mate checker Get Information->Modeling->Number of browseable features. Click the Add to Selected button.
       2.4 The checker will appear in the Chosen Tests area. Click Execute Check-Mate button to execute the chosen checker.
       2.5 Notice four features will be reported in the Results area of the Check-Mate.

-----------
CAVEATS
-----------

    None

