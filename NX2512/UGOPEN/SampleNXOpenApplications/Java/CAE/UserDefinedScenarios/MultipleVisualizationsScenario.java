/*==================================================================================================

                 Copyright (c) 2020 Siemens Product Lifecycle Management Software Inc.
                                      All Rights Reserved.

====================================================================================================
File description:
    Example User Defined Scenario that presents the usage of subviewports and displays 
    the same data in different visualization types.

====================================================================================================

*/

import nxopen.*;
import nxopen.cae.*;
import java.io.*;

public class MultipleVisualizationsScenario implements nxopen.PartCollection.PartCreatedHandler, nxopen.PartCollection.PartOpenedHandler
{
    public static Session theSession = null;
    public static ListingWindow lw = null;
    
    static MultipleVisualizationsScenario the_MultipleVisualizationsScenario;
    
    public static int registered  = 0;
    
    public static int idPartCreated = 0;
    public static int idPartOpened = 0;
    
    private static void WriteToLog(String message)
    {
        try 
        {
            theSession.logFile().writeLine(message);
        }
        catch(Exception e)
        {
            // Handle log failure.
        }
    }
    
    public MultipleVisualizationsScenario()
    {
        try
        {
            theSession = (Session)SessionFactory.get("Session");
            
            lw = theSession.listingWindow();
        
            if (registered == 0)
            {
                idPartCreated = theSession.parts().addPartCreatedHandler(this);
                idPartOpened = theSession.parts().addPartOpenedHandler(this);
            
                registered = 1;
            }
        }
        catch(Exception e)
        {
            WriteToLog(String.format("Error occured when registering the part callbacks: %s", e.getMessage()));
        }
    }
     
    /*This is the implementation of the descriptor callback.
    The method has no parameters and retuns a character string.*/    
    public String MyDescriptionCallback() throws NXException, java.rmi.RemoteException
    {
        return "This scenario exemplifies how to create multiple visualizations.";
    }
    
    public void partCreatedHandler(BasePart part)
    {
        
        
        try
        { 
            WriteToLog("Inserting Multiple Visualizations Scenario.");
                
			PostScenarioDescriptorBuilder builder = null;
            builder = part.PostScenarioMgr().postScenarioDescriptors().newPostScenarioDescriptorBuilder();
                
            // This is the scenario xml.
            String xmlText = "<?xml version='1.0' encoding='utf-8'?>"+
"<!DOCTYPE Scenario SYSTEM 'scenarios.dtd'>"+
    "<Scenario name='Multiple Visualizations Scenario' trigram='MVS'>"+
        "<InputDefinition name='My Input Definition'>"+
            "<Slot name='My Slot'>"+
                "<DependentSelector/>"+
                "<IndependentVariable name='Abscissa'>"+
                    "<AllowedDataTypes>"+
                        "<DataType type='real'/>"+
                    "</AllowedDataTypes>"+
                "</IndependentVariable>"+
                "<DependentVariable name='Ordinate'>"+
                    "<AllowedDataTypes>"+
                        "<DataType type='complex'/>"+
                    "</AllowedDataTypes>"+
                "</DependentVariable>"+
            "</Slot>"+
            "<Visualization name='My Plots' layout='3X1'>"+
                "<XYPlot name='XY Plot' gridCell='1X1'/>"+
                "<VectorPlot name='Vector Plot' gridCell='2X1'/>"+
                "<BarChart name='Bar Chart Plot' gridCell='3X1'/>"+  
            "</Visualization>"+
            "<GridCellDataAllocation>"+
                "<AllocateResultGroup name='My Slot' gridCell='1X1'>"+
                    "<VisualizationRef name='XY Plot'/>"+
                "</AllocateResultGroup>"+
                "<AllocateResultGroup name='My Slot' gridCell='2X1'>"+
                    "<VisualizationRef name='Vector Plot'/>"+
                "</AllocateResultGroup>"+
                "<AllocateResultGroup name='My Slot' gridCell='3X1'>"+
                    "<VisualizationRef name='Bar Chart Plot'/>"+
                "</AllocateResultGroup>"+
            "</GridCellDataAllocation>"+
        "</InputDefinition>"+
    "</Scenario>";
            builder.setXmlText(xmlText);
                
            // This callback is used to provide a short description of the user defined scenario.
            builder.addDescriptionCallback(this::MyDescriptionCallback);
                
            builder.commit();
        }
        catch(Exception e)
        {
            WriteToLog(String.format("Error occured when creating the user defined scenario: %s", e.getMessage()));
        }
        finally
        {
            try
            {
                builder.destroy();
            }
            catch(Exception e)
            {
                // Nothing to handle.
            }
        }
    }
    
    public void partOpenedHandler(BasePart p)
    {
        partCreatedHandler(p);
    }
    
    //-----------------------------------------------------
    //  Main()
    //    Called manually from File->Execute->NX Open
    //-----------------------------------------------------
    public static void main(String[] args)
    {
        try
        {
            startup(args);
        }
        catch(Exception e)
        {
            // Nothing to handle.
        }
    }
    
    //-----------------------------------------------------
    // Called when NX starts up
    // registers the part callbacks with NX
    //-----------------------------------------------------
    public static void startup(String[] args) throws NXException, java.rmi.RemoteException
    {
        the_MultipleVisualizationsScenario = new MultipleVisualizationsScenario();
    }
    
    //-----------------------------------------------------
    //  GetUnloadOption()
    //
    //    Used to tell NX when to unload this library
    //
    //    Available options include: 
    //       Session.LibraryUnloadOption.Immediately
    //       Session.LibraryUnloadOption.Explicitly
    //       Session.LibraryUnloadOption.AtTermination
    //
    //    Any programs that register callbacks must use 
    //    AtTermination as the unload option.
    //-----------------------------------------------------
     public static int getUnloadOption()
    {
        return BaseSession.LibraryUnloadOption.AT_TERMINATION;
    }
}

