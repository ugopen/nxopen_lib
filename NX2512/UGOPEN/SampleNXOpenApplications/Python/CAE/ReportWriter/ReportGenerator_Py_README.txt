------------------------------------------------------------------------------------

       Unpublished work Copyright 2021 Siemens

------------------------------------------------------------------------------------



------------------------------------------------------------------------------------
                        ReportGenerator.py Example
------------------------------------------------------------------------------------

DESCRIPTION
    Generates report documents for reports in input simulation parts.
    The report document name would be "part name + solution name + report name.docx"

--------------
Files required
--------------
    
    1.  ReportGenerator.py
    2.  ReportGeneratorCmdLineParser.py
    
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
    
    ReportGenerator
  <-h or -help> [sim part names]
  [-d= input folder] <-sw= "xxxx"> <-rw= "yyy"> <-o= folder> <-or= skip|replace|new>
  
        -h or - help
  -- Prints the command help information.
  
        Simulation part names
  
  – The input simulation part names which must be full name.
  
        -d
  – Optional. When it is specified, it is to generate report documents for simulation parts in this folder
  
        -sw
  – Optional. The wildcard of filtered solution name
  
        -rw
  – Optional. The wildcard of filtered report name
  
        -o
  – Optional. The output folder of published report documents. If it is not provided, the report documents will be generated in same location of simulation part.
  
        -or
  --Optional. The option tells the tool how to generate report document if the document with default name is existing. If it is not specified, the default option is "skip“
  
       There are 3 options:
  
                       skip - Not generate report document
  
                       replace - replace the existing one by a new document with same name
  
                       new - generate a new document which name appends index number in the default name
    
-----------------------
Notes
-----------------------
    
    If part name or folder name contains white spaces,
    quotation marks must be used.
    
-----------------------
Example execution steps
-----------------------
    
    1,open cmd window, change the root to xx/nxbin, "cd xx/nxbin"
    
    2,use run_journal.exe to execute ReportGenerator.py, use -args to pass paramters to ReportGenerator.py
        
-----------------------
Example commands
-----------------------
    
    1, Generates for all reports in my part.sim
    run_journal.exe ReportGenerator.py -args "c:\my folder\my part.sim"
    
   2, Generates for all reports in my part.sim and my_part2.sim
    run_journal.exe ReportGenerator.py -args "c:\my folder\my part.sim" "c:\my folder\my part2.sim"
    
   3, Generates for report in solutions which name is matched to the wildcard "*mysol" in my part.sim
    run_journal.exe ReportGenerator.py -args "c:\my folder\my part.sim" -sw="*mysol"
    
   4, Generates for report which name is matched to the wildcard "*myreport" in my part.sim
    run_journal.exe ReportGenerator.py -args "c:\my folder\my part.sim" -rw="*myreport"
    
   5, Generates for report which name is matched to the wildcard "*myreport"
    and which solution name is matched to wildcard "*mysol" in my part.sim
    run_journal.exe ReportGenerator.py -args "c:\my folder\my part.sim" -rw= "*myreport"  -sw= "*mysol"
    
   6, Generates documents in folder myreports for all reports in my part.sim
    run_journal.exe ReportGenerator.py -args "c:\my folder\my part.sim"   -o=myreports
    
   7 ,Generates all reports in my part.sim, if the document with default name existing, replace it with new docu
    run_journal.exe ReportGenerator.py -args "c:\my folder\my part.sim"   -or=replace
    
   8, Generates report documents to output folder myreports for all simulation parts in "my simparts" folder,
    , only those report which name is matched to the wildcard will be exported. If the report document in output
    folder is existing, skip it.
    run_journal.exe ReportGenerator.py -args -d="c:\my simparts"   -o=myreports -rw= "*myreport" -or=skip
