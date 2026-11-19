------------------------------------------------------------------------------------

       Unpublished work Copyright 2022 Siemens

------------------------------------------------------------------------------------



------------------------------------------------------------------------------------
                        SnapShot.py Example
------------------------------------------------------------------------------------

DESCRIPTION
    Generates image for all the snapshots in the file.
    The image name would be "snapshot name" + .png

--------------
Files required
--------------
    
    1.  SnapShot.py

----------------------------
Settings before Running journal
----------------------------
    
    set NX_ENABLE_HEADLESS_GRAPHICS=1
    
----------------------------
Settings after Running journal
----------------------------
    
----------------------------
Usage
----------------------------
    
    SnapShot
  
    
-----------------------
Notes
-----------------------
    
    If part name or folder name contains white spaces,
    quotation marks must be used.
    
-----------------------
Example execution steps
-----------------------
    
    1,open cmd window, change the root to xx/nxbin, "cd xx/nxbin" (run_journal.exe is located here)
    
    2,use run_journal.exe to execute SnapShot.py (use the path of SnapShot.py), use -args to pass paramters to SnapShot.py
        
-----------------------
Example commands
-----------------------
    
    1, Generates images for all the snapshots my part.sim in location c:\my folder\ with snapshot name 
    run_journal.exe SnapShot.py(need full path) -args "c:\my folder\my part.sim" "c:\my folder\"

