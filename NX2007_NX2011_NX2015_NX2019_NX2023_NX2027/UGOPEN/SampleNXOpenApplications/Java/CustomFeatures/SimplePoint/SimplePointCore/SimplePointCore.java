//=============================================================================
//
//                   Copyright (c) 2018 Siemens Industry Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Custom feature 
//=============================================================================
//

//==============================================================================
//  Purpose:  This TEMPLATE file contains JAVA source to guide you in the
//  construction of core library for custom feature.
//
//  1.  Help on how to write Core library for custom feature
//      using APIs provided in NXOpen
//==============================================================================
//------------------------------------------------------------------------------
//These imports are needed for the following template code
//------------------------------------------------------------------------------


import java.rmi.RemoteException;
import nxopen.*;
import nxopen.features.TrackingData;
import nxopen.BaseSession;
import nxopen.NXException;
import nxopen.Part;
import nxopen.Session;
import nxopen.SessionFactory;
import nxopen.UFSession;
import nxopen.UI;
import nxopen.features.CustomFeatureClass;
import nxopen.features.CustomFeatureClassManager;
import nxopen.features.CustomFeatureCreateFeatureGeometryEvent;
import nxopen.features.CustomFeatureInformationEvent;
import nxopen.features.CustomDoubleAttribute;


public class SimplePointCore implements 
CustomFeatureClass.CreateFeatureGeometryCallback
{
    // Class Members    
    private static Session        theSession        = null;
    private static UFSession      theUFSession      = null;
    public static UI              theUI             = null;
    
    /**
         * This method specifies how a shared image is unloaded from memory within
         * NX. This method gives you the capability to unload an internal NX Open
         * application or user exit from NX. Specify any two of the three constants
         * as a return value to determine the type of unload to perform:
         *
         * Explicitly : unload the library from the "Unload Shared Image" dialog
         * AtTermination : unload the library when the NX session terminates
         *
         * NOTE: Custom feature core library must not use unload option immediately 
         * as this will unload image too early to be used by NX.
         *
         * @return Unload Option
         */
    public static final int getUnloadOption()
    {
         return BaseSession.LibraryUnloadOption.EXPLICITLY; // Recommanded during development.
         //return BaseSession.LibraryUnloadOption.AT_TERMINATION; // Recommanded during production.
    }
    
    /**
     * Main Entry Point of the application
     *
     * @param args
     *            input arguments
     * @throws NXException 
     * @throws RemoteException 
     */
    public static void main(final String[] args) throws RemoteException, NXException
    {
        
        try
        {
            if(SimplePointCore.theSession == null)
                SimplePointCore.theSession = (Session) SessionFactory.get("Session");
            
            if(SimplePointCore.theUFSession == null)
                SimplePointCore.theUFSession = (UFSession) SessionFactory.get("UFSession");
            
            new SimplePointCore();
            
        }
        catch(final Exception thisException)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, thisException.getMessage());
        }
    }
    
    SimplePointCore() throws RemoteException, NXException
    {
        try
        {
            theSession = (Session) SessionFactory.get("Session");
            theUFSession = (UFSession) SessionFactory.get("UFSession");
            theUI = (UI) SessionFactory.get("UI");
            
            Part workPart = theSession.parts().work();
            
            // Get custom feature manager from session.
            CustomFeatureClassManager cfClassManager = theSession.customFeatureClassManager();
            CustomFeatureClass cfClass = cfClassManager.getClassFromName("NXOpen::CustomFeature::SimplePoint");
    
            // Registration of callback functions
            cfClass.addCreateFeatureGeometryHandler(this);
        }
        catch(final Exception thisException)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, thisException.getMessage());
        }
    }
    
    /**
     * Following method cleanup any housekeeping chores that may be needed. This
     * method is automatically called by NX.
     * @throws NXException 
     * @throws RemoteException 
     */
    public static void onUnload() throws RemoteException, NXException
    {
        try
        {
            // If necessary clean up code here
        }
        catch(final Exception thisException)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, thisException.getMessage());
        }
    }
    
    /* (non-Javadoc)
     * @see nxopen.features.CustomFeatureClass.CreateFeatureGeometryCallback#createFeatureGeometryCallback(nxopen.features.CustomFeatureCreateFeatureGeometryEvent)
     */
    @Override
    public int createFeatureGeometryCallback(CustomFeatureCreateFeatureGeometryEvent eventObject) throws NXException, RemoteException
    {
        try
        {
            // Get the attributes of custom feature for which callback is invoked
            nxopen.features.CustomFeature theCustomFeature = eventObject.getCustomFeature();
            nxopen.features.CustomFeatureData cfData = theCustomFeature.featureData();
            
            CustomDoubleAttribute pointXAttribute = cfData.customDoubleAttributeByName("PointX");
                
            CustomDoubleAttribute pointYAttribute = cfData.customDoubleAttributeByName("PointY");
                
            CustomDoubleAttribute pointZAttribute = cfData.customDoubleAttributeByName("PointZ");
            
            // Let's create Point from input coordinates
            Point3d point3d = new Point3d();
            point3d.x = pointXAttribute.value();
            point3d.y = pointYAttribute.value();
            point3d.z = pointZAttribute.value();
            
            Part workPart = theSession.parts().work();
            Point point = workPart.points().createPoint(point3d);
            point.setVisibility(SmartObject.VisibilityOption.VISIBLE);
            
            // Track the created point by creating tracking data for it
            TrackingData[] trackData =  new TrackingData[1];
            TrackingData track = eventObject.createTrackingDataForNXObject (point);
            
            // Since this simple point application only creates single point we
            // Track it here with integer.
            track.addIntSourceEntity(1); 
            trackData[0] = track;
            
            eventObject.appendOutputTrackingData (trackData);
            
        }
        catch (Exception thisException) 
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, thisException.getMessage());
        }
        
        return 0;
    }

}
