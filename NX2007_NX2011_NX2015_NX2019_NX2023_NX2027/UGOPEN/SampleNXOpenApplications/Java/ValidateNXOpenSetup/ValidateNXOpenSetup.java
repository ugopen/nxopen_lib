/*===================================================================================================
  
          Copyright (c) 2018 Siemens Product Lifecycle Management Software Inc. 
                              All Rights Reserved.
  
=====================================================================================================

  
      Code Description:
  
      A simple NX Open Java application program that prints the full version number of installed  
      Siemens NX software in the system log file and the listing window. If the messages are 
      successfully printed, then NX Open software automation setup is validated.   
=====================================================================================================
  
      Note:  
     
      NX Development provides programming examples for illustration only.
      NX Development assumes you are familiar with the programming language
      demonstrated in these examples, and the tools used to create and debug NX/Open
      programs. GTAC support professionals can help explain the functionality of
      a particular procedure, but neither GTAC nor NX Development will modify
      these examples to provide added functionality or construction procedures.
=====================================================================================================
*/

import nxopen.*;
public class ValidateNXOpenSetup
{
  public static void main( String [ ] args ) throws NXException, java.rmi.RemoteException
  {
    // Get the session  
    nxopen.Session theSession = ( nxopen.Session )nxopen.SessionFactory.get( "Session" );
    
    // Get the listing window for this session
    nxopen.ListingWindow lw = theSession.listingWindow( );
    
    // Open the listing window
    lw.open( );
    
    // Get the system log file for this session    
    nxopen.LogFile logFile = theSession.logFile( );
    
    // Get the name of the system log file
    String logFileName = logFile.fileName( );
    
    // Write a line to the listing window
    lw.writeFullline( "Log File Name: " + logFileName + " created." );
    
    // Get the full version name of the installed Siemens NX
    String NXFullVersion = theSession.getEnvironmentVariableValue( "NX_FULL_VERSION" );
    
    if ( NXFullVersion != null )
    {
        // Write a string to the system log file
        logFile.writeLine( "NX Open software automation setup is validated for release: " + NXFullVersion + "." );
        
        // Write a line to the listing window
        lw.writeFullline( "NX Open software automation setup is validated for release: " + NXFullVersion + "." );
    }
    else
    {
        // Write a string to the system log file
        logFile.writeLine( "Siemens NX installation not verified." );
        
        // Write a line to the listing window
        lw.writeFullline( "Siemens NX installation not verified." );        
    }

    // Close the stream to the listing window
    lw.close( );
        
    // ----------------------------------------------
    //   Menu: Tools->Journal->Stop Recording
    // ----------------------------------------------
  
  }
  
  public static final int getUnloadOption() { return nxopen.BaseSession.LibraryUnloadOption.IMMEDIATELY; }
  
}
