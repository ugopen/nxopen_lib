#==================================================================================================

#                Copyright (c) 2020 Siemens Product Lifecycle Management Software Inc.
#                                     All Rights Reserved.

#==================================================================================================
#File description:

#    Example User Defined Scenario to creat a 3D Plot with results on elements or nodes.

#==================================================================================================
#

import sys
import traceback
import math
import NXOpen

registered = 0

# This method is used as a callback to described the scenario
def Description():
    return "This is a user defined scenario used to display results as a contour plot on a 3D model."

#This method is used as a callback to:
        # - be sure that only one result group is added to the output query result
        # - create a single plot with a dynamic plot name based to the selected component
def Transformation(part, input, ctx, output):
    # part: NXOpen.BasePart
    # input: NXOpen.CAE.PostScenarioQueryResults
    # ctx: NXOpen.CAE.PostScenarioQueryContext
    # outout: NXOpen.CAE.PostScenarioQueryResults

    try:
        ### Set the output query results name ###
        output.Name = input.Name
        
        ### Check to see if the input is a valid object for this transformation function ###
        inputResultGroups = input.GetResultGroups()  # list of NXOpen.CAE.PostScenarioResultGroup
       
        ### Get the variables (NXOpen.CAE.PostScenarioResultGroupVariable) from the expected result group (only one result group is expected) ###  
            # Only one independent and dependent is expected
        independentVariables = inputResultGroups[0].GetIndependentVariables()  
        dependentVariables = inputResultGroups[0].GetDependentVariables()
        selectionVariables = inputResultGroups[0].GetSelectionVariables()
        
        ### Create a result group (NXOpen.CAE.PostScenarioResultGroupBuilder) for the output ###
        outputResultGroup = output.NewResultGroupBuilder("3D Results")
            # Attach the independent variable
        outputResultGroup.AddIndependentVariable(independentVariables[0].Name, independentVariables[0].DataType, independentVariables[0].Domain)
            # Attach the dependent variable
        outputResultGroup.AddDependentVariable(dependentVariables[0].Name, dependentVariables[0].DataType, dependentVariables[0].ComponentType, dependentVariables[0].Domain)
            # Attach the selection variables
        for selectionVariable in selectionVariables:
            outputResultGroup.AddSelectionVariable(selectionVariable.Name, selectionVariable.DataType, selectionVariable.Domain)
        
            # Add the result group
        outputResultGroup.Commit()
            # Clean up
        outputResultGroup.Dispose()
        
        ### Add a new configuration group for the output ###
        configurationVariable = output.NewConfigurationGroupBuilder("Default")
            # Add the configuration group
        configurationVariable.Commit()
            # Clean up
        configurationVariable.Dispose()
         
        ### Create a single plot (NXOpen.CAE.PostScenarioPlotBuilder) attached to the new result group ###
            # Get the plot (NXOpen.CAE.PostScenarioPlotData) from the first result group (only one plot is expected)
        inputPlot = inputResultGroups[0].GetPlots()[0];
        
            # Make sure that the second parameter is the name of the new result group and the third one is the name of the new configuration group.
        outputPlot = output.NewPlotBuilder("3D Results", "3D Results", "Default")
            
            ### Assign values ###
                # Assign independent values (NXOpen.CAE.PostScenarioVariantList) taken from the first entry (NXOpen.CAE.PostScenarioPlotDataEntry)
        entryBuilder = outputPlot.NewPlotEntryBuilder()  # NXOpen.CAE.PostScenarioPlotEntryBuilder)
        entryBuilder.SetIndependent(independentVariables[0].Name, 
                                    inputPlot.GetEntries()[0].GetIndependentValues())
            
                # Assign dependent values for each available component (NXOpen.CAE.PostScenarioVariantComponent) taken from the first entry
        for component in inputPlot.GetEntries()[0].GetAvailableComponents(dependentVariables[0].Name):
            entryBuilder.AssignDependent(dependentVariables[0].Name, 
                                     component, 
                                     inputPlot.GetEntries()[0].GetDependentValues(dependentVariables[0].Name, component))                   
                # Add the entry builder
        entryBuilder.Commit()

                # Assign selections (NXOpen.CAE.PostScenarioVariant) values 
        for selectionVariable in selectionVariables:
            outputPlot.SetSelectionValue(selectionVariable.Name, 
                                         inputPlot.GetSelectionVariableValue(selectionVariable.Name),
                                         inputPlot.GetSelectionVariableMetadata(selectionVariable.Name))
            
            # Set additional metadata (NXOpen.CAE.PostScenarioMetadata)
        outputPlot.SetMetadata(inputPlot.Metadata)
        
            # Generate the correct plot name 
        name = outputPlot.GeneratePlotName(outputPlot.GetPlotNameComponent())
        if name == "":
            name = "Plot"
        outputPlot.Name = name
       
            # Add the plot
        outputPlot.Commit()
        
        # Clean up
        inputPlot.Dispose()
        entryBuilder.Dispose()
        outputPlot.Dispose()
        for var in independentVariables + dependentVariables + selectionVariables + inputResultGroups:
            var.Dispose()
    except AttributeError as err:
        ctx.MessageCollector.AddInformationLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        ctx.MessageCollector.AddInformationLine(tb)
    except TypeError as err:
        ctx.MessageCollector.AddInformationLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        ctx.MessageCollector.AddInformationLine(tb)
    except Exception as err:
        ctx.MessageCollector.AddInformationLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        ctx.MessageCollector.AddInformationLine(tb)

def PartOpenedOrCreated(part):
    theSession  = NXOpen.Session.GetSession()
    theSession.LogFile.WriteLine("Inserting Contour Plot Scenario")
    
    try:
        builder = part.PostScenarioMgr.PostScenarioDescriptors.NewPostScenarioDescriptorBuilder()
        try:
            # Add the scenario descriptor 
            builder.XmlText = r"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE Scenario SYSTEM "scenarios.dtd">
<Scenario name="Contour Plot Scenario" domainPath="Examples" trigram="3D">
    <InputDefinition name="3D Results" defaultSelectionWidgetStyle="list_with_checkbox">
        <Slot name="Data">
            <DependentSelector componentName="Component" componentBehavior="inferred">
                <CardinalityRestriction type="equals" value="1"/>
            </DependentSelector>
            <IndependentVariable name="Target">
                <AllowedDataTypes>
                    <DataType type="integer"/>
                </AllowedDataTypes>
                <AllowedDomains>
                    <VariableDomain type="node"/>
                    <VariableDomain type="element"/>
                    <VariableDomain type="panel"/>
                </AllowedDomains>
            </IndependentVariable>
            <DependentVariable name="Value">
                <AllowedDataTypes>
                    <DataType type="integer"/>
                    <DataType type="real"/>
                    <DataType type="complex"/>
                    <DataType type="real_on_nodes_of_elements"/>
                    <DataType type="complex_on_nodes_of_elements"/>
                </AllowedDataTypes>
                <AllowedDomains>
                    <VariableDomain not="true" type="ppt_label"/>
                </AllowedDomains>
            </DependentVariable>
        </Slot>
        <MeshDefinition name="Mesh" meshType="post_model"/>
        <Visualization name="3D PostView" layout="1X1">
            <PostView name="Contour Plots" gridCell="1X1"/>
        </Visualization>
    </InputDefinition>
</Scenario>"""
            ### Attach callbacks ###

            # Add Description
            builder.AddDescriptionCallback(Description)
            # Add Transformation to create the correct result group and a plot with a generated name
            builder.AddTransformationCallback(Transformation)
            builder.Commit()
        finally:
            builder.Destroy()
    except AttributeError as err:
        lw = theSession.ListingWindow
        lw.Open()
        lw.WriteLine(str(err))
        lw.Close()
    except NXOpen.NXException as err:
        lw = theSession.ListingWindow
        lw.Open()
        lw.WriteLine("The user defined scenario could not be added.")
        lw.WriteLine("The following error was raised: {}".format(err.GetMessage()))
        lw.Close()

def startup(argc, args):
    # Get the NXOpen Session
    theSession  = NXOpen.Session.GetSession()

    global registered
    try:
        if registered == 0:
            registered = 1
            idPartCreated1 = theSession.Parts.AddPartCreatedHandler(PartOpenedOrCreated)
            idPartOpened1 = theSession.Parts.AddPartOpenedHandler(PartOpenedOrCreated)
        else:
            theSession.LogFile.WriteLine("Already registered!")
    except AttributeError as err:
        # Get the listing window for this session
        lw = theSession.ListingWindow
	
        # Open the listing window
        lw.Open()

        # Add a line in the listing window
        lw.WriteLine(str(err))

        # Close the listing window
        lw.Close()
       
    return 0

def main(): 
    return startup(0, [])
    
if __name__ == '__main__':
    main()
