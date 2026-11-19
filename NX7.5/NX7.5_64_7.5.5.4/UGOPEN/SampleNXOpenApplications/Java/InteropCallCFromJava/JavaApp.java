/*=============================================================================
                  Copyright (c) 2009 Siemens
                      All rights reserved
===============================================================================
UFapp.cxx

Description: Sample code showing interactions with a Java applications 

 
=============================================================================*/


import java.util.*;
import nxopen.*;
class JavaApp 
{
    //Native method declarations
    private native int nativeUFappFunction1();
    private native int nativeUFappFunction2( int value, String name );
    
    //Load the native library, the library should be in your environment
    //path 
    //On non-Windows - LD_LIBRARY_PATH, on windows PATH
    static {
        System.loadLibrary("UFapp");
    }
    
    // Accessor methods used by our other Java classes . By hiding 
    //  the actual calls to the native methods, we can change the 
    //  implementation without affecting the classes calling in. 
    
    public int UFappFunction1()
    {
        return(this.nativeUFappFunction1());
    }
    
    public int UFappFunction2( int value, String name )
    {
        return(this.nativeUFappFunction2( value, name ));
    }
    //Main functions
    public static void main (String args[]) {
        
      try
      {
        Session theSession = (Session)SessionFactory.get("Session");
        theSession.logFile().writeLine("BEGIN Java app (Running from File->Execute)");
        //Create class instance
        JavaApp app = new JavaApp();
        //Call native methods
        int ret1 = app.UFappFunction1();
        int ret2 = app.UFappFunction2(88, "This is string from Java");
        //Now we are back in Java
        theSession.logFile().writeLine("function1:" + Integer.toString(ret1) );
      }
      catch (Exception ex)
      {
        System.out.println("Failed"); 
      }
    }
    public static int getUnloadOption() { 
        return BaseSession.LibraryUnloadOption.EXPLICITLY;
    }
}

