========================================================================
    NX_OPEN : [!output PROJECT_NAME] Project Overview
========================================================================

NX11 Open C# Wizard has created this [!output PROJECT_NAME] project for you as a starting point.

This file contains a summary of what you will find in each of the files that make up your project.

[!output PROJECT_NAME].vbproj
    This is the main project file for projects generated using an Application Wizard. 
    It contains information about the version of the product that generated the file, and 
    information about the platforms, configurations, and project features selected with the
    Application Wizard.
    
    Executing User Exit Functions
    -----------------------------
    
    For execution of each user exit, corresponding Environment Variable need to be set with the full path 
    of the dll.     
    
    The following environment variables are used to point to user exit executables. 
    Alternatively a single Environment Variable USER_DEFAULT can be set for all the Entry point. 

User Exit		        Environment Variable		Entry Point

Open Part		        USER_RETRIEVE 			ufget

New Part	 	        USER_CREATE 		        ufcre

Save Part 		        USER_FILE 		        ufput

Save Part As 		        USER_SAVEAS 		        ufsvas

Import Part 		        USER_MERGE 		        ufmrg

Execute GRIP Program 	        USER_GRIP 		        ufgrp

Add Existing Part 	        USER_RCOMP 		        ufrcp
 
Export Part 		        USER_FCOMP 		        uffcp

Component Where-used 	        USER_WHERE_USED                 ufusd

Plot File 		        USER_PLOT 		        ufplt

2D Analysis Using 
Curves                          USER_AREAPROPCRV 	        uf2da

User Defined Symbols 	        USER_UDSYMBOL 		        ufuds

Open CLSF 		        USER_CLS_OPEN 		        ufclso

Save CLSF 		        USER_CLS_SAVE 	   	        ufclss

Rename CLSF 		        USER_CLS_RENAME 	        ufclsr

Generate CLF 		        USER_CL_GEN 		        ufclg

Postprocess CLSF 	        USER_POST 		        ufpost

Create Component 	        USER_CCOMP 		        ufccp

Change Displayed Part 	        USER_CDISP 		        ufcdp

Change Work Part 	        USER_CWORK 		        ufcwp

Remove Component 	        USER_DCOMP 		        ufdcp

Reposition Component 	        USER_MCOMP 		        ufmcp

Substitute Component 
Out                             USER_SCOMP1 		        ufscpo

Substitute Component In         USER_SCOMP2 		        ufscpi

Open Spreadsheet                USER_SPRD_OPN                   ufspop

Close Spreadsheet	        USER_SPRD_CLO		        ufspcl
   
Update Spreadsheet	        USER_SPRD_UPD		        ufspup

Finish Updating 
Spreadsheet                     USER_SPRD_UPF		        ufspuf

Replace Reference Set 	        USER_RRSET 		        ufrrs

Rename Component 	        USER_NCOMP 		        ufncp

NX Startup 		        USER_STARTUP 		        ufsta

Access Genius Library 
Management System		USER_GENIUS	      	        ufgen

Execute Debug GRIP   	        USER_GRIPDEBUG 		        ufgrpd

Execute User Function 	        USER_UFUN 		        ufufun

Initialize new operation   
Re-initialize an 
existing operation              USER_CREATE_OPER                ufnopr

CAM Startup      		USER_CAM_STARTUP                ufcams
    
