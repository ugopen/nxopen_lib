
/*==================================================================================================
               Copyright 2017 Siemens Product Lifecycle Management Software Inc.
====================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    A Java class that implements Maximum Height Violation Routing Design Rule.


==================================================================================================*/
import java.rmi.RemoteException;
import java.util.List;
import java.util.Vector;

import nxopen.ListingWindow;
import nxopen.LogFile;
import nxopen.NXException;
import nxopen.NXObject;
import nxopen.Session;
import nxopen.SessionFactory;
import nxopen.routing.CustomManager;
import nxopen.routing.ISegment;
import nxopen.routing.Overstock;
import nxopen.routing.OverstockApplication;
import nxopen.routing.OverstockApplicationCollection;
import nxopen.routing.RouteManager;
import nxopen.routing.StockDefinition;
import nxopen.routing.Wire;
import nxopen.routing.electrical.*;
import nxopen.routing.StockDevice; 
import nxopen.routing.CustomManager.DesignRuleReason;

class MaxHeightDesignRules implements nxopen.routing.CustomManager.DesignRule
{
    static MaxHeightDesignRules theMaxHeightDesignRules = null;
    static Session theSession = null;
    static ListingWindow listingWindow = null;
    
    //------------------------------------------------------------------------------------------
    // Called when NX starts.
    // Creates a new instance of this Callback class.
    public static void startup( String [] args ) throws NXException, java.rmi.RemoteException
    {     
     
        if (theSession == null)
            theSession = (Session)SessionFactory.get((String)"Session");

        if (listingWindow == null)
            listingWindow = theSession.listingWindow();
        
        theMaxHeightDesignRules = new MaxHeightDesignRules();
    
    }
    
    //------------------------------------------------------------------------------------------
    // The constructor for this class.
    // Registers the Design Rules.
    public MaxHeightDesignRules() throws RemoteException, NXException
    {        
        try
        {
            CustomManager customManager = theSession.routeCustomManager();  
            String shortDescription = "Maximum Height Violation";
            String longDescription = "The Maximum Height design rule makes sure the diameter of each individual connection is within the permissible limit of value specified by attribute CABLETRAY_MAXHEIGHT."; 
            customManager.addDesignRule(DesignRuleReason.CREATE_PATH,shortDescription,longDescription , this);
            customManager.addDesignRule(DesignRuleReason.HEAL_PATH,shortDescription,longDescription , this);
            customManager.addDesignRule(DesignRuleReason.ASSIGN_CORNER,shortDescription,longDescription , this);
            customManager.addDesignRule(DesignRuleReason.REMOVE_PART,shortDescription,longDescription , this);
            customManager.addDesignRule(DesignRuleReason.AUTO_ROUTE_PIN_LEVEL,shortDescription,longDescription , this);
            customManager.addDesignRule(DesignRuleReason.MANUAL_ROUTE_PIN_LEVEL,shortDescription,longDescription , this);
            customManager.addDesignRule(DesignRuleReason.AUTO_ROUTE_COMPONENT_LEVEL,shortDescription,longDescription , this);
            customManager.addDesignRule(DesignRuleReason.MANUAL_ROUTE_COMPONENT_LEVEL,shortDescription,longDescription , this);
            customManager.addDesignRule(DesignRuleReason.INTERACTIVE,shortDescription,longDescription , this);
            customManager.addDesignRule(DesignRuleReason.TRANSFORM_PATH,shortDescription,longDescription , this);            
            customManager.addDesignRule(DesignRuleReason.EDIT_CHARACTERISTIC,shortDescription,longDescription , this);
        }
        catch ( NXException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***Error in Routing_MaximumHeight_DR constructor: " + ex.getMessage() );
        }
        catch (RemoteException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***RemoteException in Routing_MaximumHeight_DR constructor: " + ex.getMessage() );
        }        
    }
    
    //---------------------------------------------------------------------------------------------
    // This is the Create Path Design Rule.
    //
    // It simply prints the tags of the given object to the Listing Window and Log File.
    public void designRule(DesignRuleReason reason, NXObject[] objects) throws NXException, RemoteException 
    {
        CustomManager customManager = theSession.routeCustomManager();
        
        // For interactive checks, check all the segments in the work part.
        if (reason == CustomManager.DesignRuleReason.INTERACTIVE)
        {
            nxopen.TaggedObjectCollection.Iterator objectCollectionItr = theSession.parts().work().segmentManager().segments().iterator();

             while(objectCollectionItr.hasNext())
             {
              ISegment segment = (ISegment) objectCollectionItr.next();
              checkForMaximumHeightViolation(theSession.parts().work().routeManager(),customManager,segment, reason);
             }
             return;
        }
        
        // Otherwise, check the segments in the given list of objects.
        for (NXObject nxObject : objects)
        {                
            if(nxObject instanceof ISegment)
            {
                ISegment segment = (ISegment)nxObject;
                checkForMaximumHeightViolation(theSession.parts().work().routeManager(), customManager, segment, reason);
            }
        }
    }
    //--------------------------------------------------------------------------------------------------
    // Get the the double value from attribute
    //
    // \param[in]
    //      attributeInfo
    //         Attribute information from which double needs to be queried
    //
    // \return
    //      Value of attribute as Double
    private double convertToReal
    (
        NXObject.AttributeInformation attributeInfo
    )throws RemoteException, NXException
    {
        switch(attributeInfo.type.ordinal())
        {
            case    NXObject.AttributeType._REAL:
                    return attributeInfo.realValue;
                    
            case    NXObject.AttributeType._INTEGER:
                return (double)attributeInfo.integerValue;
                
            case    NXObject.AttributeType._STRING:
                return Double.parseDouble(attributeInfo.stringValue);
                
            default:
                NXException.create("Unknown attribute type");            
        }
        return 0;
    }
    //--------------------------------------------------------------------------------------------------
    // Gets the real value of the attribute on the given object, if any.
    //
    // \param[in]
    //      object
    //          The object to check for the attribute.
    //
    // \param[in]
    //      attributeName
    //          The name (a.k.a. title) of the attribute for which to look.
    //
    // \return
    //      Value of attribute as Double
    //
    private double getAttributeValue
    (
        ISegment              segment,
        String                attributeNameString
    ) throws RemoteException, NXException
    {        
        NXObject.AttributeInformation[] attributeInformationArray = ((NXObject) segment).getUserAttributes();
        
        for(NXObject.AttributeInformation attributeInfo : attributeInformationArray)
        {
            if(attributeInfo.title.equals(attributeNameString))
            {                
                return convertToReal(attributeInfo);
            }
        }
        return 0;
    }
    //--------------------------------------------------------------------------------------------------
    // Queries the list of stock devices routing through the segment
    //
    // \param[in]
    //      segment
    //          Segment through which stock devices are routed.
    //
    // \param[in]
    //      routeManager
    //          RouteManager from the current work part
    //
    // \return
    //          List of stock stock devices referencing the segment
    //
    private List<StockDevice> getStockDevicesRoutedThroughSegment
    (
        ISegment              segment,
        RouteManager          routeManager
    ) throws RemoteException, NXException
    {        
        List<StockDevice> stockDeviceList = new Vector<StockDevice>();
        ElectricalStockDeviceCollection stockDevices = routeManager.electricalStockDevice();

        nxopen.TaggedObjectCollection.Iterator stockDevicesItr = stockDevices.iterator();
        
        while(stockDevicesItr.hasNext())
        {
            StockDevice stockDevice = (StockDevice) stockDevicesItr.next();
            
            Wire wire = null;
            wire = (Wire)stockDevice.nxEquivalent();
            
            if (wire == null) continue;
            
            ISegment[] stockDeviceSegments = wire.getSegmentList();

            for(ISegment singleSegment : stockDeviceSegments)
            {                
                if (! singleSegment.equals(segment))
                {
                    continue;
                }
                
                if(!stockDeviceList.contains(stockDevice))
                {
                    stockDeviceList.add(stockDevice);
                }
            }
        }
        
        return stockDeviceList;
    }    
    //-----------------------------------------------------------------------------------------------
    // This method gives diameter of maximum size connection amongst the stock devices routing through the segment
    //
    // \param[in]
    //      segment
    //          Segment through which connections are routed
    // \param[in]
    //      stockDevicesOnSegment
    //          List of stock devices routed through the segment
    // \param[out]
    //      largestDiameter
    //          Maximum size diameter 
    private double getValueToCheckMaxHeightViolationForStockDevice
    (
        ISegment                      segment,
        List <StockDevice>            stockDevicesOnSegment
    ) throws RemoteException, NXException
    {
        double valueToCheck = 0;
        
        for (StockDevice stockDevice :stockDevicesOnSegment)
        {
            double maxValue = 0.0;
            
            StockDefinition stockDef = null;
            ElectricalStockDevice electricalStockDevice = null;
            
            if(stockDevice instanceof ElectricalStockDevice)
            {
                electricalStockDevice = (ElectricalStockDevice)stockDevice;
            }

            if(electricalStockDevice == null)
            {
                continue;
            }

            CableDefinition cableDefinition = electricalStockDevice.findTopmostCableDefinition();
            if (cableDefinition != null)
            {             
                CableDevice cableDevice = null;
                
                if(cableDefinition.getReferencingDevice() instanceof CableDevice)
                {
                    cableDevice = (CableDevice)cableDefinition.getReferencingDevice();
                }
                
                if (cableDevice == null)
                {
                    continue;
                }
                stockDef = cableDevice.stockDefinition();
            }
            else
            {
                stockDef = stockDevice.stockDefinition();
            }

            maxValue = stockDef.outerDiameter();
            
            if (Double.compare(maxValue, valueToCheck) > 0)
            {
                valueToCheck = maxValue;
            }
        }        
        return valueToCheck;        
    }    
    //-----------------------------------------------------------------------------------------------
    // Queries the overstock referencing the segment
    //
    // \param[in]
    //      segment
    //         Segment from which referencing overstock needs to be queried.
    // \param[in]
    //      routeManager
    //          RouteManager from the current work part
    // \return
    //          Set of overstocks referencing the segment
    private List<Overstock> getOverstocksPresentOnTheSegment
    (
        ISegment                     segment,
        RouteManager                 routeManager
    ) throws RemoteException, NXException
    {
         List<Overstock> overstockList = new Vector<Overstock>();
         
         OverstockApplicationCollection overstockApplications = routeManager.overstockApplications();
         nxopen.TaggedObjectCollection.Iterator overstockApplicationsItr = overstockApplications.iterator();
         
         while(overstockApplicationsItr.hasNext())
         {
             OverstockApplication overstockApplication = (OverstockApplication) overstockApplicationsItr.next();
             ISegment[] overstockApplicationSegments = overstockApplication.getSegments();

             for (ISegment currentSegment : overstockApplicationSegments)
             {
                 if (currentSegment != segment)
                 {
                     continue;
                 }

                 Overstock[] overstocks = overstockApplication.getOverstocks();
                 overstockList.add(overstocks[0]);
             }
         }
         return overstockList;
    }
    //------------------------------------------------------------------------------------------
    // Check the maximum diameter of connection routing through given segment against the maximum allowed height.
    //
    // Creates a violation for the given reason if connection diameter exceeds specified Maximum Height value.
    //
    // \param[in]
    //      routeManager
    //          RouteManager from current work part
    //
    // \param[in]
    //      customManager
    //          CustomManager to create design Rule violation.
    //
    // \param[in]
    //      segment
    //          Routing Segment to be check for Maximum Height violation
    //
    // \param[in]
    //      reason
    //          Design Rule reason for which Maximum Height Violation needs to be checked.
    private void checkForMaximumHeightViolation
    ( 
        RouteManager                    routeManager, 
        CustomManager                   customManager, 
        ISegment                        segment, 
        CustomManager.DesignRuleReason  reason
    ) throws RemoteException, NXException
    {
        // Get value of allowed Maximum Height or Specified Maximum Height
        String maxHeightAttributeName = "CABLETRAY_MAXHEIGHT";
        double specifiedMaxHeightValue = getAttributeValue(segment,maxHeightAttributeName);     
        if(Math.abs(specifiedMaxHeightValue) < 1e-5)
        {
         return;
        }    
     
        // Get list of Stock Devices routing through the segment
        List<StockDevice> stockDeviceList =  getStockDevicesRoutedThroughSegment(segment,routeManager);
       
        if(stockDeviceList.isEmpty())
        {
             return;
        }
        
        // Get max value diameter of connection routing through the segment
        double valueToCompare = getValueToCheckMaxHeightViolationForStockDevice(segment,stockDeviceList);
        
        // Get Overstocks referencing the segment
        List<Overstock> overstockList = getOverstocksPresentOnTheSegment(segment,routeManager);
        
        
        // If Overstocks are present on segment, get maximum value of diameter including overstock
        if(overstockList.size() > 0)
        {
            double totalOverstockThickness = 0.0;
            for(Overstock overstock : overstockList)
            {
                totalOverstockThickness += overstock.getThickness().value();
            }
            valueToCompare += (2 * totalOverstockThickness);
        }
        
        // If current value of diameter is greater than specified maximum height value then raise violation.
        if (Double.compare(valueToCompare, specifiedMaxHeightValue) > 0)
        { 
            String description = "The stock exceeds the maximum height allowed for this segment. The current height is " + valueToCompare + ".The allowed height is " + specifiedMaxHeightValue + ".";

            NXObject[] objects = {(NXObject)segment };
            customManager.createViolationForReason(reason,"The segment violates Maximum Height Rule", description, objects);
        }

        stockDeviceList.clear();
        overstockList.clear();     
    }
    //------------------------------------------------------------------------------------------
    // Tells NX when to unload your application.
    // For Routing callbacks, plugins, and Design Rules, this MUST return AtTermination.
    public static int getUnloadOption(String arg)
    {
        return Session.LibraryUnloadOption.AT_TERMINATION;
    }
}
