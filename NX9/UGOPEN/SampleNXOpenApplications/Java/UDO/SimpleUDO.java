//=============================================================================
//
//                   Copyright (c) 2012 Siemens PLM Solutions
//                    Unpublished - All rights reserved
//===============================================================================
// This program creates a very simple UDO example. 
// 
// It demonstrates each of the following callback reasons: 
// * Display 
// * Selection 
// * Attention Point 
// * Fit 
// * Edit 
// * Information 
// 
// In NX execute this program via: File -> Execute -> NX Open... 
// This program begins by opening a new part (if there were no open parts). 
// Next it will prompt you to select a position on the screen. 
// The screen position will be used as a reference point for the UDO. 
// The UDO will display as a triangle on that point with a name 
// "JAVA UDO" next to the triangle. 
// 
// This UDO is selectable. If you go to Information->Object and select 
// the UDO you will see custom information output to the listing window from 
// the function genericCallback defined in this program. 
// 
// You can also edit the location of the UDO. Start by right-clicking 
// on the UDO and selecting "Edit User Defined Object" from the MB3 popup menu. 
// Editing the UDO will invoke the genericCallback function defined in this program. 
// You will be prompted to select a new screen position, and after you make 
// the selection the UDO will move to the new location. 
//=============================================================================
//
//=============================================================================
import nxopen.*; 
import nxopen.userdefinedobjects.*; 
import java.io.*; 
import java.rmi.RemoteException;

// SimpleUDO class used to demo a UDO in the java language 
public class SimpleUDO implements 
nxopen.userdefinedobjects.UserDefinedClass.DisplayCallback, 
nxopen.userdefinedobjects.UserDefinedClass.GenericCallback 
{ 
// class members
     public static Session theSession = null; 
    public static UI theUI = null; 
    public static UFSession theUFSession = null; 
    public static UserDefinedClass myUDOclass = null; 

    static SimpleUDO theSimpleJavaUDO; 

    //------------------------------------------------------------------------------ 

    // Callback Name: displayCallback 
    // This is a callback method associated with displaying a UDO. 
    // This same callback is registered for display, select, fit, and attention point 
    //------------------------------------------------------------------------------ 

    public int displayCallback(nxopen.userdefinedobjects.UserDefinedDisplayEvent e) 
    { 
        int retValue = 0; 
        try 
        { 
            // all display reasons (DISPLAY, SELECTION, FIT, and ATTENTION_POINT) 
            // should do the same thing so we don't need to figure out the 
            // reason we're in this displayCallback 

            //Get the doubles used to define the selected screen position for this UDO. 

            double[] myUDOdoubles = e.userDefinedObject().getDoubles(); 

            // Use the doubles to define points of a triangle 
            Point3d[] myPoints = new Point3d[]
                              { new Point3d( myUDOdoubles[0] + 0, 
                                             myUDOdoubles[1] + 0, 
                                             myUDOdoubles[2] + 0), 
                                new Point3d( myUDOdoubles[0] + 100, 
                                             myUDOdoubles[1] + 0, 
                                             myUDOdoubles[2] + 0), 
                                new Point3d( myUDOdoubles[0] + 0, 
                                             myUDOdoubles[1] + 100, 
                                             myUDOdoubles[2] + 0), 
                                             new Point3d(myUDOdoubles[0] + 0, 
                                             myUDOdoubles[1] + 0, 
                                             myUDOdoubles[2] + 0)}; 
            // Display the triangle 
            e.displayContext().displayPolyline(myPoints); 

            // Display the text next to the triangle 
            Point3d myPt = new Point3d(); 
            myPt.x = myUDOdoubles[0] + 100; 
            myPt.y = myUDOdoubles[1] + 0; 
            myPt.z = myUDOdoubles[2] + 0; 
            e.displayContext().displayText("JAVA UDO", myPt, UserDefinedObjectDisplayContext.TextRef.BOTTOM_LEFT); 
        } 
        catch(Exception ex) 
        { 
            System.out.println("Error Message"); 
            System.out.println(ex.getMessage()); 
        } 
        return retValue; 
    } 
//------------------------------------------------------------------------------ 

  // Callback Name: genericCallback 
  // This is a callback method associated with editing a UDO, or querying the UDO 
  // for information. Because one callback is used to do two completely different 
  // things (with different functionality for each thing) we must first check the 
  // reason stored in the event object to see which piece of functionality we need 
  // to execute. 
  //------------------------------------------------------------------------------ 
  public int genericCallback(nxopen.userdefinedobjects.UserDefinedEvent e) 
  { 
   int retValue = 0; 
   try 
   { 
    if(e.eventReason() == nxopen.userdefinedobjects.UserDefinedEvent.Reason.EDIT ) 
    { 
     // highlight the current udo we are about to edit 
     // this is helpful if multiple udo's were on the selection 
     // list when the user decided to edit them 
     e.userDefinedObject().highlight(); 

     // ask the user to select a new origin for this UDO 
     Selection.SelectScreenPositionData mySelectionData = theUI.selectionManager().selectScreenPosition("Select Origin of Java UDO"); 
     // we are done asking the user for input... unhighlight the udo 
     e.userDefinedObject().unhighlight(); 

     // use the new screen position (if the user picked one) 
     if( mySelectionData.response == Selection.DialogResponse.PICK ) 
     { 
      double[] 
      myUDOdoubles = new double[3]; 
      myUDOdoubles[0] = mySelectionData.screenPosition.x; 
      myUDOdoubles[1] = mySelectionData.screenPosition.y; 
      myUDOdoubles[2] = mySelectionData.screenPosition.z; 
      // store the newly selected origin with the udo 
      e.userDefinedObject().setDoubles(myUDOdoubles); 

      // add the udo to the display list manually 
      // this will force the udo display to regenerate 
      // immediately and show the changes we just made 
      theUFSession.disp().addItemToDisplay(e.userDefinedObject().tag()); 
     } 
    } 
    else if(e.eventReason() == nxopen.userdefinedobjects.UserDefinedEvent.Reason.INFO ) 
    { 
     // print information for the udo here 
     ListingWindow 
     theLW = theSession.listingWindow(); 
     theLW.open(); theLW.writeLine(" "); 
     theLW.writeLine("------------------------------------------------------------"); 
     theLW.writeLine("Begin Custom Information"); 
     theLW.writeLine(" "); 
     theLW.writeLine("UDO Class Name: '" + e.userDefinedObject().userDefinedClass().className() + "'"); 
     theLW.writeLine("UDO Friendly Name: '" + e.userDefinedObject().userDefinedClass().friendlyName() + "'"); 
     double[] myUDOdoubles = e.userDefinedObject().getDoubles(); 
     theLW.writeLine("myUDOdoubles(0) = " + myUDOdoubles[0]); 
     theLW.writeLine("myUDOdoubles(1) = " + myUDOdoubles[1]); 
     theLW.writeLine("myUDOdoubles(2) = " + myUDOdoubles[2]); 
     theLW.writeLine(" "); theLW.writeLine("End Custom Information"); 
    } 
   } 
   catch(Exception ex) 
   { 
    System.out.println("Error Message"); 
    System.out.println(ex.getMessage()); 
   } 
   return retValue; 
  } 
  //------------------------------------------------------------------------------ 

  // initUDO 
  // Checks to see which (if any) of the application's static variables are 
  // uninitialized, and sets them accordingly. 
  // Initializes the UDO class and registers all of its callback methods. 
  //------------------------------------------------------------------------------ 
  private void initUDO() throws Exception, RemoteException
  { 
   try 
   { 
    if (theSession == null) 
    { 
     theSession = (Session)SessionFactory.get("Session"); 
    } 
    if( theUI == null ) 
    { 
     theUI = (UI)SessionFactory.get("UI"); 
    } 
    if( theUFSession == null ) 
    { 
     theUFSession = (UFSession)SessionFactory.get("UFSession"); 
    }
     
    theUFSession.ui().openListingWindow();
    theUFSession.ui().writeListingWindow("Session and UFSession are created \n");
    if (myUDOclass == null) 
    { 
     // Define your custom UDO class 
     myUDOclass = theSession.userDefinedClassManager().createUserDefinedObjectClass("Sample_Java_UDO", "Sample Java UDO" ); 
      theUFSession.ui().writeListingWindow("UDU object is created \n");
     // Setup properties on the custom UDO class 
     myUDOclass.setAllowQueryClassFromName( nxopen.userdefinedobjects.UserDefinedClass.AllowQueryClass.ON ); 
     // Register callbacks for the UDO class 
     myUDOclass.addDisplayHandler(this); 
     myUDOclass.addAttentionPointHandler(this); 
     myUDOclass.addFitHandler(this); 
     myUDOclass.addSelectionHandler(this); 
     myUDOclass.addEditHandler(this); 
     myUDOclass.addInformationHandler(this); 
     // Add this class to the list of object types available for selection in NX. 
     // If you skip this step you won't be able to select UDO's of this class,
     // even though you registered a selection callback. 
     theUI.selectionManager().setSelectionStatusOfUserDefinedClass(myUDOclass, true); 
   } 
        } 
        catch(Exception ex) 
        { 
            System.out.println("Error Message"); 
            System.out.println(ex.getMessage()); 
            throw new Exception(ex);
        } 
    } 
    // constructor 
    public SimpleUDO() throws Exception, RemoteException
    { 
        try 
        { 
            initUDO(); 
        } 
        catch(Exception ex) 
        { 
            System.out.println("Caught Exception"); 
            System.out.println(ex.getMessage()); 
            throw new Exception(ex);
        } 
    } 

    //------------------------------------------------------------------------------ 

    // main (Explicit Activation) 
    // This entry point is used to activate the application explicitly, as in 
    // "File->Execute UG/Open->NX Open..." 
    //------------------------------------------------------------------------------ 

    public static void main(String[] args) 
    { 
        try 
        { 
            theSimpleJavaUDO = new SimpleUDO(); 
            // if we don't have any parts open create one 
            BasePart myBasePart = theSession.parts().baseDisplay(); 
            if( myBasePart == null) 
            { 
                myBasePart = theSession.parts().newBaseDisplay("test_java_udo.prt", BasePart.Units.MILLIMETERS); 
            } 

            // ask the user to select an origin for this UDO 
            Selection.SelectScreenPositionData mySelectionData = theUI.selectionManager().selectScreenPosition("Select Origin of Java UDO"); 
            if( mySelectionData.response == Selection.DialogResponse.PICK ) 
            { 
                // The user selected a point - go ahead and create the udo 
                UserDefinedObjectManager myUDOmanager = myBasePart.userDefinedObjectManager(); 
                UserDefinedObject firstUDO = myUDOmanager.createUserDefinedObject(myUDOclass); 
                // set the color property of the udo - just for fun :) 
                firstUDO.setColor(36); 
                // store the origin selected by the user with the udo 
                double[] myUDOdoubles = new double[3]; 
                myUDOdoubles[0] = mySelectionData.screenPosition.x; 
                myUDOdoubles[1] = mySelectionData.screenPosition.y; 
                myUDOdoubles[2] = mySelectionData.screenPosition.z;     
                firstUDO.setDoubles(myUDOdoubles); 
                // add the udo to the display list manually 
                // this will force the udo to display immediately 
                theUFSession.disp().addItemToDisplay(firstUDO.tag()); 
                theUFSession.ui().writeListingWindow("Test Completed Successfully.");
            } 
        } 
        catch(Exception ex) 
        { 
            System.out.println("Caught Exception"); 
            System.out.println(ex.getMessage()); 
            try
            {
                theUFSession.ui().writeListingWindow(ex.getMessage());
            }
            catch(Exception ex1)
            {
                System.out.println("Caught Exception"); 
                System.out.println(ex1.getMessage()); 
            }
        } 
    } 
    //------------------------------------------------------------------------------ 

    // startup 
    // Entrypoint used when program is loaded automatically 
    // as NX starts up. Note this application must be placed in a 
    // special folder for NX to find and load it during startup. 
    // Refer to the NX Open documentation for more details on how 
    // NX finds and loads applications during startup. 
    //------------------------------------------------------------------------------ 
    public static void startup (String [] args)throws NXException, java.rmi.RemoteException 
    { 
        try 
        { 
            theSimpleJavaUDO = new SimpleUDO(); 
    } 
    catch(Exception ex) 
    { 
        System.out.println("Caught Exception"); 
        System.out.println(ex.getMessage()); 
    } 
    } 
    //------------------------------------------------------------------------------ 

    // getUnloadOption 
    // Make sure you specify AtTermination for the unload option. 
    // If you unload the library before the NX Session Terminates 
    // bad things could happen when we try to execute a udo 
    // callback that no longer exists in the session. 
    //------------------------------------------------------------------------------ 

    public static final int getUnloadOption() 
    { 
        //return BaseSession.LibraryUnloadOption.AT_TERMINATION; 
         return BaseSession.LibraryUnloadOption.IMMEDIATELY; 
        //return BaseSession.LibraryUnloadOption.AT_TERMINATION;
    } 
}
