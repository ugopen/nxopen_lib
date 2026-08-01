#===================================================================================================
#
#        Copyright (c) 2018 Siemens Product Lifecycle Management Software Inc. 
#                            All Rights Reserved.
#
#===================================================================================================
#
#
#    Code Description:
#
#    A simple NX Open Python application program that prints the full version number of installed 
#    Siemens NX software in the system log file and the listing window. If the messages are
#    successfully printed, then NX Open software automation setup is validated.
#===================================================================================================
#
#    Note:
#  
#    NX Development provides programming examples for illustration only.
#    NX Development assumes you are familiar with the programming language
#    demonstrated in these examples, and the tools used to create and debug NX/Open
#    programs. GTAC support professionals can help explain the functionality of
#    a particular procedure, but neither GTAC nor NX Development will modify
#    these examples to provide added functionality or construction procedures.
#===================================================================================================

import math
import NXOpen
def main() : 

    # Get the NXOpen Session
    theSession  = NXOpen.Session.GetSession( )
	
    # Get the listing window for this session
    lw = theSession.ListingWindow
	
    # Open the listing window
    lw.Open( )
	
    # Get the name of the system log file
    logFileName = theSession.LogFile.FileName
	
    # Write a line to the listing window
    lw.WriteLine( "Log File Name: " + logFileName + " created." )

    # Get the full version name of the installed Siemens NX
    NXFullVersion = theSession.GetEnvironmentVariableValue( "NX_FULL_VERSION" )
	
    if NXFullVersion:
	
        # Write a string to the system log file
        theSession.LogFile.WriteLine( "NX Open software automation setup is validated for release: " + NXFullVersion + "." )
		
        # Write a line to the listing window
        lw.WriteFullline( "NX Open software automation setup is validated for release: " + NXFullVersion + "." )
    
    else:
	
        # Write a string to the system log file
        theSession.LogFile.WriteLine( "Siemens NX installation not verified." )
		
        # Write a line to the listing window
        lw.WriteFullline( "Siemens NX installation not verified." )		
	
	
    # Close the stream to the listing window.
    lw.Close( )
	
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()
