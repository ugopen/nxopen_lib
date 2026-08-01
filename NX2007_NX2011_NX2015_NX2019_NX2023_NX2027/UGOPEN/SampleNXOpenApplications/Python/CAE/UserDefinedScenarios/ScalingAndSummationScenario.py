#==================================================================================================

#                Copyright (c) 2020 Siemens Product Lifecycle Management Software Inc.
#                                     All Rights Reserved.

#==================================================================================================
#File description:
#    Example User Defined Scenario for scaling and summation of plot data.

#==================================================================================================
#

import sys
import traceback
import math
import NXOpen

registered = 0

# This is the implementation of the descriptor callback.
# The method has no parameters and returns a character string.
def MyDescriptionCallback():
    return "This scenario exemplifies how to do scaling and summation operations on the given data."

# This is the implementation of the sensitivity callback between the "Scaling" and "Scaling Value"
# configuration variables. From the xml of the scenario it can be seen that the "Scaling" configuration
# variable is boolean. If the "Scaling" variable has the value false then the "Scaling Value" node in the
# Scenario Based Data-Visualization Navigator will be editable, otherwise it will be uneditable and greyed out.
# The method has the following input parameters:
# part - NXOpen.BasePart
# ctx - NXOpen.CAE.PostScenarioConfigurationVariableCallbackContext
# collector - NXOpen.CAE.PostScenarioValueCollector
# The method returns a boolean value.
def MySensitivityCallback(part, ctx, collector):
    vals = collector.GetValues()
    if len(vals) == 0:
        return False
    return not vals[0].GetValueAsBoolean()

# This function intersects two array and returns another array containing intersection elements
# The method has the following input parameters:
# list1 - 1st array to be intersected.
# list2 - 2nd array to be intersected.
# The method returns array containing intersection elements.
def ListIntersect(list1, list2):
    return list(set(list1).intersection(set(list2)))
       
# This is the implementation of the transformation callback. The method takes the data from the input query results,
# transforms the data accordingly, and stores the transformed data in the output query results.
# The method has the following input parameters:
# part - NXOpen.BasePart
# input - NXOpen.CAE.PostScenarioQueryResults
# ctx - NXOpen.CAE.PostScenarioQueryContext
# output - NXOpen.CAE.PostScenarioQueryResults
# The method doesn't have a return value.
def MyTransformationCallback(part, input, ctx, output):

    # NXOpen.CAE.PostScenarioMessageCollector utility object that is used to write to the information window.
    mc = ctx.MessageCollector

    try:

        # There should be only one result configuration group named "Default".
        cfg = input.GetConfigurationGroups()[0]
        mc.AddInformationLine("Configuration group name: {}".format(cfg.Name))
        
        # Retrieve the names of the existing configuration variables, that were defined in the xml scenario.
        # There should be three: "Scaling", "Scaling Value", "Summation", in this order.
        keys = cfg.GetKeys()

        # Print the keys to the information window.
        mc.AddInformationLine("Available keys:")
        for key in keys:
            mc.AddInformationLine("{}".format(key))

        # Retrieve the value of the "Scaling" configuration variable.
        hasScaling = cfg.GetValues(keys[0])[0]

        # If the value for "Scaling" is true, retrieve the value of the "Scaling Value" configuration variable
        # with which the data will be scaled.
        scalingFactor = 1.0
        if hasScaling.GetValueAsBoolean():
            scalingVal = cfg.GetValues(keys[1])[0]     
            scalingFactor = scalingVal.GetValueAsDouble()

        # Retrieve the value of the "Summation" configuration variable.
        hasSumPlot = cfg.GetValues(keys[2])[0]

        

        # Assign a name for the output query results.
        output.Name = "Scaled and/or summed query results"

        # Create a default configuration group builder for the output query results.
        cg = output.NewConfigurationGroupBuilder("Default")
        cg.Commit()
        cg.Dispose()

        # Initialize the lists where the summed data will be stored.
        sumIVals = []
        sumIValsIntersection = []
        sumDValsReal = []
        sumDValsImag = []

        # Copy the result groups to the output.
        for rg in input.GetResultGroups():
            
            rgOut = output.NewResultGroupBuilder(rg.Name)

            # Copy the independent variables to the output.
            for indepVar in rg.GetIndependentVariables():
                rgOut.AddIndependentVariable(indepVar.Name, indepVar.DataType, indepVar.Domain)

            # Copy the depedent variables to the output.
            for depVar in rg.GetDependentVariables():
                rgOut.AddDependentVariable(depVar.Name, depVar.DataType, NXOpen.CAE.PostScenarioComponentType.Scalar, depVar.Domain)

            rgOut.Commit()
            rgOut.Dispose()

            # Copy the plots to the output.
            for plot in rg.GetPlots():
               
                outPb = output.NewPlotBuilder("Plot Name" if not plot.Name else plot.Name, rg.Name, "Default")

                # Copy the metadata to the output.
                outPb.SetMetadata(plot.Metadata)

                # Copy the entries to the output.
                for entry in plot.GetEntries():
                    ebOut = outPb.NewPlotEntryBuilder()

                    # Copy the independent values to the output.
                    ebOut.SetIndependent(rg.GetIndependentVariables()[0].Name, entry.GetIndependentValues())

                    # Scale the dependent values with the given scaling value and give them to the output.
                    for depVar in rg.GetDependentVariables():
                        for comp in entry.GetAvailableComponents(depVar.Name):
                            
                            realValues = []
                            imagValues = []

                            if depVar.DataType == NXOpen.CAE.PostScenarioVariantType.Double:

                                realValues = [scalingFactor * value for value in entry.GetDependentValues(depVar.Name, comp).GetValueAsDouble()]

                                vl = part.PostScenarioMgr.NewVariantList()
                                vl.SetValueAsDouble(realValues)
                                ebOut.AssignDependent(depVar.Name, NXOpen.CAE.PostScenarioVariantComponent.Scalar, vl)
                                vl.Dispose()

                            elif depVar.DataType == NXOpen.CAE.PostScenarioVariantType.Complex:

                                realValues = [scalingFactor * value.Real for value in entry.GetDependentValues(depVar.Name, comp).GetValueAsComplex()]
                                imagValues = [scalingFactor * value.Imag for value in entry.GetDependentValues(depVar.Name, comp).GetValueAsComplex()]

                                values = []
                                for r, i in zip(realValues, imagValues):
                                    values.append(NXOpen.CAE.Complex(r,i))

                                vl = part.PostScenarioMgr.NewVariantList()
                                vl.SetValueAsComplex(values)
                                ebOut.AssignDependent(depVar.Name, NXOpen.CAE.PostScenarioVariantComponent.Scalar, vl)
                                vl.Dispose()

                            else:
                                # According to the scenario xml the expected dependent data can be either real or complex.
                                mc.AddInformationLine("Unexpected dependent data type")

                            # If the "Summation" configuration variable has a true value, populate lists with 
                            # the summed values of the dependent variables.
                            if hasSumPlot.GetValueAsBoolean():

                                iValues = entry.GetIndependentValues().GetValueAsDouble()

                                if sumIValsIntersection:
                                    sumIValsIntersection = ListIntersect(sumIValsIntersection, iValues)
                                else:
                                    sumIValsIntersection = iValues

                                if depVar.DataType == NXOpen.CAE.PostScenarioVariantType.Double:

                                    for iVal in iValues:
                                        if iVal in sumIVals:
                                            sumDValsReal[sumIVals.index(iVal)] += realValues[iValues.index(iVal)]
                                        else:
                                            sumIVals.append(iVal)
                                            sumDValsReal.append(realValues[iValues.index(iVal)])
                                
                                elif depVar.DataType == NXOpen.CAE.PostScenarioVariantType.Complex:

                                        for iVal in iValues:
                                            if iVal in sumIVals:
                                                sumDValsReal[sumIVals.index(iVal)] += realValues[iValues.index(iVal)]
                                                sumDValsImag[sumIVals.index(iVal)] += imagValues[iValues.index(iVal)]
                                            else:
                                                sumIVals.append(iVal)
                                                sumDValsReal.append(realValues[iValues.index(iVal)])
                                                sumDValsImag.append(imagValues[iValues.index(iVal)])
                                else:
                                    # According to the scenario xml the expected dependent data can be either real or complex.
                                    mc.AddInformationLine("Unexpected dependent data type")

                    ebOut.Commit()
                    ebOut.Dispose()

                outPb.Commit()
                outPb.Dispose()

        # If the "Summation" configuration variable has a true value, create an additional plot
        # with the summed values of the dependent variables.
        if hasSumPlot.GetValueAsBoolean():
            # If there are no result groups in the input, there is nothing to plot.
            if len(input.GetResultGroups()) != 0:

                # The same type of independent variable, dependent variable and plot can be created as
                # those in the first input result group, due to the xml scenario in this example.
                rg = input.GetResultGroups()[0]

                # Create a new result group in the output.
                rgOut = output.NewResultGroupBuilder("Summed Group")

                # Add the independent variable to the output.
                indepVar = rg.GetIndependentVariables()[0]
                rgOut.AddIndependentVariable(indepVar.Name, indepVar.DataType, indepVar.Domain)

                # Add the dependent variable to the output.
                depVar = rg.GetDependentVariables()[0]
                rgOut.AddDependentVariable(depVar.Name, depVar.DataType, NXOpen.CAE.PostScenarioComponentType.Scalar, depVar.Domain)

                rgOut.Commit()
                rgOut.Dispose()

                # Create a new plot in the output.
                pbOut = output.NewPlotBuilder("Summed Plot", "Summed Group", "Default")

                if len(rg.GetPlots()) != 0:
                    metadata = rg.GetPlots()[0].Metadata
                    # The "summed" plot will be displayed with a thicker line.
                    metadata.HighlightedDisplay = True
                    # Copy the metadata, as it should be the same.
                    pbOut.SetMetadata(metadata)
               
                # Create a new entry in the output.
                ebOut = pbOut.NewPlotEntryBuilder()

                # Assign the independent values.
                iVl = part.PostScenarioMgr.NewVariantList()

                iVl.SetValueAsDouble(sumIValsIntersection)
                
                ebOut.SetIndependent(indepVar.Name, iVl)

                iVl.Dispose()

                # Assign the dependent values.
                dVl = part.PostScenarioMgr.NewVariantList()

                if not sumDValsImag:
                    # Consider only the values from the intersection of the independent values.
                    sumDValsRealIntersection = []
                    for iVal in sumIValsIntersection:
                        sumDValsRealIntersection.append(sumDValsReal[sumIVals.index(iVal)])

                    dVl.SetValueAsDouble(sumDValsRealIntersection)
                else:
                    # Consider only the values from the intersection of the independent values.
                    sumDValsRealIntersection = []
                    sumDValsImagIntersection = []
                    for iVal in sumIValsIntersection:
                        sumDValsRealIntersection.append(sumDValsReal[sumIVals.index(iVal)])
                        sumDValsImagIntersection.append(sumDValsImag[sumIVals.index(iVal)])

                    sumDVals = []
                    for r, i in zip(sumDValsRealIntersection, sumDValsImagIntersection):
                        sumDVals.append(NXOpen.CAE.Complex(r, i))

                    dVl.SetValueAsComplex(sumDVals)

                ebOut.AssignDependent(depVar.Name, NXOpen.CAE.PostScenarioVariantComponent.Scalar, dVl)

                dVl.Dispose()

                ebOut.Commit()
                ebOut.Dispose()

                pbOut.Commit()
                pbOut.Dispose()

    except AttributeError as err:
        mc.AddInformationLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        mc.AddInformationLine(tb)
    except TypeError as err:
        mc.AddInformationLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        mc.AddInformationLine(tb)
    except Exception as err:
        mc.AddInformationLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        mc.AddInformationLine(tb)

def PartOpenedOrCreated(part):
    theSession  = NXOpen.Session.GetSession()
    theSession.LogFile.WriteLine("Inserting Scaling and Summation Scenario")

    try:
        # Create a new NXOpen.CAE.PostScenarioDescriptorBuilder
        builder = part.PostScenarioMgr.PostScenarioDescriptors.NewPostScenarioDescriptorBuilder()
        try:
            # This is the scenario xml.
            builder.XmlText = r"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE Scenario SYSTEM "scenarios.dtd">
<Scenario name="Summation and Scaling Scenario" domainPath="Examples" trigram="SSS">
  <InputDefinition name="My Definition">
    <Slot name="Real Data Only">
      <DependentSelector/>
      <IndependentVariable name="Abscissa">
        <AllowedDataTypes>
          <DataType type="real"/>
        </AllowedDataTypes>
      </IndependentVariable>
      <DependentVariable name="Ordinate">
        <AllowedDataTypes>
          <DataType type="real"/>
          <DataType type="complex"/>
        </AllowedDataTypes>
      </DependentVariable>
    </Slot>
    <!--Configuration variables with which the data should be scaled.-->
    <ConfigurationVariable name="Scaling Value" type="real">
        <DefaultValue>1.0</DefaultValue>
    </ConfigurationVariable>
    <!--Configuration variable that controls whether the data should be scaled or not. 
    It controls the availability of the previous configuration variable in the UI through a callback.-->
    <ConfigurationVariable name="Scaling" type="boolean">
        <DefaultValue>true</DefaultValue>
        <ControlsSensitivity callback="MySensitivityCallback">
            <VariableRef name="Scaling Value"/>
        </ControlsSensitivity>
    </ConfigurationVariable>
    <!--Configuration variable that controls the creation of a plot containing the summed data of multiple plots.-->
    <ConfigurationVariable name="Summation" type="boolean"></ConfigurationVariable>
    <Visualization name="XY Plot" layout="1X1">
      <XYPlot name="Metadata Example" gridCell="1X1"></XYPlot>
    </Visualization>
  </InputDefinition> 
</Scenario>"""
            # This callback is used to provide a short description of the user defined scenario.
            builder.AddDescriptionCallback(MyDescriptionCallback)
            # This callback is used to create a relation between two configuration variables
            # "Scaling" and "Scaling Value".
            builder.AddSensitivityCallback("MySensitivityCallback", MySensitivityCallback)
            # This callback is used to transform the given data. For this particular scenario the
            # data can be scaled and/or summed.
            builder.AddTransformationCallback(MyTransformationCallback)

            descriptor = builder.Commit()
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
	
    # Get the listing window for this session
    lw = theSession.ListingWindow
	
    # Open the listing window
    lw.Open()
	
    # Get the name of the system log file
    logFileName = theSession.LogFile.FileName
	
    # Write a line to the listing window
    lw.WriteLine( "Log File Name: " + logFileName + " created." )

    global registered
    if registered == 0:
        registered = 1
        idPartOpenedOrCreated = theSession.Parts.AddPartOpenedHandler(PartOpenedOrCreated)
        idPartOpenedOrCreated = theSession.Parts.AddPartCreatedHandler(PartOpenedOrCreated)
    else:
        theSession.LogFile.WriteLine("Already registered.")

    # Close the stream to the listing window.
    lw.Close()
	
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    return 0

def main(): 
    return startup(0, [])
    
if __name__ == '__main__':
    main()
