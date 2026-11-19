#==================================================================================================
#                Copyright (c) 2020 Siemens
#                All Rights Reserved.
#==================================================================================================
#
# File description:
#     Example User Defined Scenario that uses coordinate system transformations
#
#==================================================================================================
#

"""
Sample Scenario, which demonstrates how to use the Coordinate System Transformation utilities.

These utilities leverage Result Coordinate Systems from Data Sources, as well as Sim/Fem 
Coordinate Systems from the CSYS container, as well as ad-hoc definitions of coordinate systems.

Place this file in the `startup` subdirectory of your user dir. For more information, see 
    installation_dir/ugopen/SampleNXOpenApplications/Python/CAE/UserDefinedScenarios/Readme.txt
"""

import sys
import traceback
import math
import NXOpen

registered = 0

# List of choices for ConversionTypeProvider.
myConversionTypeValues = [
    "Native",
    "Absolute Rectangular",
    "Absolute Cylindrical",
    "Absolute Spherical",
    "Project Results To Faces",
    "Selected Coordinate Systems"]

def ConversionTypeSensitivity(mgr, ctx, collector):
    """
    Callback that determines the sensitivity of the Coordinate System Picker configuration variable.

    Args:
        mgr (CAE.PostScenarioManager): Input context
        ctx (CAE.PostScenarioConfigurationVariableCallbackContext): Input context
        collector (CAE.PostScenarioValueCollector): Input values of context variables

    Returns:
        bool: if the To variable will be disabled
    """
    values = collector.GetValues()
    selected = myConversionTypeValues[0]
    if len(values) > 0:
        selected = values[0].GetValueAsUnicodeString()
    return selected != myConversionTypeValues[-1]

def ConversionTypeProvider(part, choiceContext, valueCollector):
    """
    Callback that determines the available choices for this variable.

    Args:
        mgr (CAE.PostScenarioManager): Input context
        ctx (CAE.PostScenarioConfigurationVariableCallbackContext): Input context
        valueCollector (CAE.PostScenarioValueCollector): Place values here
    """
    for x in myConversionTypeValues:
        valueCollector.AddString(x)

def GenerateDomainPatterns(mgr):
    """
    Method that generates CAE.PostScenarioVariableDomain patterns to identify
    Frequency Repsonse Functions or Cross Power Functions, respectively.

    Args:
        mgr (CAE.PostScenarioManager): input context
    
    Returns:
        CAE.PostScenarioVariableDomain, CAE.PostScenarioVariableDomain
    """
    frfDomainPattern = mgr.NewVariableDomain()
    frfDomainPattern.AddComponent("rational_support", ["wildcard"])
    frfDomainPattern.AddComponent("rational_support", ["over"])
    frfDomainPattern.AddComponent("rational_support", ["wildcard"])
    crossPowerDomainPattern = mgr.NewVariableDomain()
    crossPowerDomainPattern.AddComponent("rational_support", ["wildcard"])
    crossPowerDomainPattern.AddComponent("rational_support", ["cross"])
    crossPowerDomainPattern.AddComponent("rational_support", ["wildcard"])

    return frfDomainPattern, crossPowerDomainPattern

def CoordinateSystemPickerProvider(part, ctx, collector):
  """
  Callback that determines how many coordinate systems need to be defined for this scenario, given the context.

  If we're showing native, or converting to absolute coordinate systems, then none are required.

  If we're converting to a target coordinate system, the user needs to select one (Responses) or two (FRFs, XPowers).

  Args:
      part (BasePart): input context part
      ctx (CAE.PostScenarioConfigurationVariableCallbackContext): input context
      collector (CAE.PostScenarioValueCollector): output values
  """
  theSession  = NXOpen.Session.GetSession()
  lw = theSession.ListingWindow
  values = []
  disposables = []
  try:
    lw.Open()
    postScenarioSelectionParameters = ctx.SelectionParameters
    postScenarioConfigurationVariableCollection = postScenarioSelectionParameters.ConfigurationVariables
    postScenarioConfigurationVariable = postScenarioConfigurationVariableCollection.Find("Conversion Type")
    values = postScenarioConfigurationVariable.GetAssignedValues()
    value = next((value.GetValueAsUnicodeString() for value in values), myConversionTypeValues[0])
    lw.WriteLine("ConversionType: {0} {1}".format(len(values), repr(value)))
    if value != myConversionTypeValues[-1]:
        # no pickers necessary for native, absolute conversions or face normal projectsion
        pass
    else:
        mgr = part.PostScenarioMgr
        postScenarioDataMatch = ctx.GetSlotDataMatch("Data")
        variables = postScenarioDataMatch.GetMatchedDependentVariables()

        postScenarioVariableDomain = variables[0].Domain
        disposables.append(postScenarioVariableDomain)

        frfDomainPattern, crossPowerDomainPattern = GenerateDomainPatterns(mgr)
        disposables.append(frfDomainPattern)
        disposables.append(crossPowerDomainPattern)

        if postScenarioVariableDomain.MatchDomainPattern(frfDomainPattern):
            collector.AddString("Excitation")
            collector.AddString("Response")
        elif postScenarioVariableDomain.MatchDomainPattern(crossPowerDomainPattern):
            collector.AddString("Left")
            collector.AddString("Right")
        else:
            collector.AddString("Coordinate System")
  finally:
    for v in values:
        v.Dispose()
    for v in disposables:
        v.Dispose()

def toAbsolute(queryResults, mgr, ctx, type):
    """
    Helper function to convert the input queryResults to an absolute coordinate system, determined by type,
    regardless of data shape.

    Args:
        queryResults (CAE.PostScenarioQueryResults): input data
        mgr (CAE.PostScenarioManager): input context
        ctx (CAE.PostScenarioQueryContext): input context
        type (CAE.PostScenarioCoordinateSystemType): absolute csys type

    Returns:
        CAE.PostScenarioQueryResults: transformed data
    """
    plots = []
    for rg in queryResults.GetResultGroups():
        for plot in rg.GetPlots():        
            plots.append(plot)
    postScenarioCoordinateSystemTransformation = ctx.NewCoordinateSystemTransformation(NXOpen.CAE.PostScenarioCoordinateSystemTransformationType.ToAbsolute)
    postScenarioCoordinateSystemTransformation.AssumeResultsAreInGlobal = True
    postScenarioCoordinateSystemTransformation.SetCoordinateSystemType(type)
    try:
        return postScenarioCoordinateSystemTransformation.Convert(plots)
    finally:
        postScenarioCoordinateSystemTransformation.Dispose()

def toFaceNormal(queryResults, mgr, ctx):
    """
    Helper function to project the input queryResults to face normals,
    regardless of data shape.

    Args:
        queryResults (CAE.PostScenarioQueryResults): input data
        mgr (CAE.PostScenarioManager): input context
        ctx (CAE.PostScenarioQueryContext): input context

    Returns:
        CAE.PostScenarioQueryResults: transformed data
    """

    plots = []
    for rg in queryResults.GetResultGroups():
        for plot in rg.GetPlots():        
            plots.append(plot)
    postScenarioCoordinateSystemTransformation = ctx.NewCoordinateSystemTransformation(NXOpen.CAE.PostScenarioCoordinateSystemTransformationType.ToFaceNormal)
    postScenarioCoordinateSystemTransformation.AssumeResultsAreInGlobal = True
    try:
        return postScenarioCoordinateSystemTransformation.Convert(plots)
    finally:
        postScenarioCoordinateSystemTransformation.Dispose()

def toUserDefined(queryResults, mgr, ctx, coordinateSystems):
    """
    Helper function to convert the input queryResults to user selected coordinate systems.

    Args:
        queryResults (CAE.PostScenarioQueryResults): input data
        mgr (CAE.PostScenarioManager): input context
        ctx (CAE.PostScenarioQueryContext): input context
        coordinateSystems ([CAE.PostScenarioCoordinateSystem]): value of coordinate system picker configuration variable

    Returns:
        CAE.PostScenarioQueryResults: transformed data
    """

    if len(queryResults.GetResultGroups()) == 0:
        return queryResults
    rg = queryResults.GetResultGroups()[0]
    if len(rg.GetDependentVariables()) > 1:
        ctx.MessageCollector.Warning("Internal Error", "Multiple dependent variables are not supported by this scenario, check descriptor has single selection enabled on the dependent selector")
        return queryResults
    postScenarioVariable = rg.GetDependentVariables()[0]
    postScenarioVariableDomain = postScenarioVariable.Domain
    frfDomainPattern, crossPowerDomainPattern = GenerateDomainPatterns(mgr)
    plots = []
    for rg in queryResults.GetResultGroups():
        for plot in rg.GetPlots():        
            plots.append(plot)
    try:
        # based on data shape, we populate the appropriate coordinate system fields using the data we got from the user
        # user input is automatically converted to CAE.PostScenarioCoordinateSystem
        if postScenarioVariableDomain.MatchDomainPattern(frfDomainPattern):
            postScenarioCoordinateSystemTransformation = ctx.NewCoordinateSystemTransformation(NXOpen.CAE.PostScenarioCoordinateSystemTransformationType.ResponseFunction)
            if len(coordinateSystems) == 2:
                postScenarioCoordinateSystemTransformation.SetExcitationCoordinateSystem("User Defined", coordinateSystems[0])
                postScenarioCoordinateSystemTransformation.SetResponseCoordinateSystem("User Defined", coordinateSystems[1])
        elif postScenarioVariableDomain.MatchDomainPattern(crossPowerDomainPattern):
            postScenarioCoordinateSystemTransformation = ctx.NewCoordinateSystemTransformation(NXOpen.CAE.PostScenarioCoordinateSystemTransformationType.CrossPower)
            if len(coordinateSystems) == 2:
                postScenarioCoordinateSystemTransformation.SetLeftCoordinateSystem("User Defined", coordinateSystems[0])
                postScenarioCoordinateSystemTransformation.SetRightCoordinateSystem("User Defined", coordinateSystems[1])
        else:
            postScenarioCoordinateSystemTransformation = ctx.NewCoordinateSystemTransformation(NXOpen.CAE.PostScenarioCoordinateSystemTransformationType.UserDefined)
            if len(coordinateSystems) == 1:
                postScenarioCoordinateSystemTransformation.SetCoordinateSystem("User Defined", coordinateSystems[0])
        postScenarioCoordinateSystemTransformation.AssumeResultsAreInGlobal = True
        return postScenarioCoordinateSystemTransformation.Convert(plots)
    finally:
        postScenarioCoordinateSystemTransformation.Dispose()
        postScenarioVariableDomain.Dispose()
        frfDomainPattern.Dispose()
        crossPowerDomainPattern.Dispose()

def MyCallback(part, xinput, ctx, output):
    """
    Implementation of MyTransformation
    """
    mgr = part.PostScenarioMgr
    finalIvals = []
    finalDvals = []
    numPlots = 0

    theSession  = NXOpen.Session.GetSession()
    lw = theSession.ListingWindow

    configurationGroups = xinput.GetConfigurationGroups()
    if len(configurationGroups) == 0:
        return

    inputConfigurationGroup = configurationGroups[0]
    conversionType = next((x.GetValueAsUnicodeString() for x in inputConfigurationGroup.GetValues("Conversion Type")), myConversionTypeValues[0])

    # map converter choices to a lambda that will perform the transformation
    # while here, bind invariant data to the callbacks' argument lists
    converters = {
        myConversionTypeValues[0]: lambda x: x, # native
        myConversionTypeValues[1]: lambda x: toAbsolute(x, mgr, ctx, NXOpen.CAE.PostScenarioCoordinateSystemType.Rectangular),
        myConversionTypeValues[2]: lambda x: toAbsolute(x, mgr, ctx, NXOpen.CAE.PostScenarioCoordinateSystemType.Cylindrical),
        myConversionTypeValues[3]: lambda x: toAbsolute(x, mgr, ctx, NXOpen.CAE.PostScenarioCoordinateSystemType.Spherical),
        myConversionTypeValues[4]: lambda x: toFaceNormal(x, mgr, ctx),
        myConversionTypeValues[5]: lambda x: toUserDefined(x, mgr, ctx, [x.GetValueAsCoordinateSystem() for x in inputConfigurationGroup.GetValues("Coordinate System")])
    }

    # perform conversion
    input = converters.get(conversionType, lambda x: x)(xinput)
    # if errors were encountered, one could check the "Converted" and "ConvertedError" plot metadata
    # if an error did occur, the input data was left untouched (save for those two metadata mentioned above)
    # See CAE.PostScenarioMetadata, CAE.PostScenarioPlotData.Metadata

    # Need a new object here...
    cg = output.NewConfigurationGroupBuilder("Default")

    cg.Commit()
    cg.Dispose()

    zz_i = 0

    # populate scenario output
    for rg in input.GetResultGroups():

        # Need a new object here...
        newRG = output.NewResultGroupBuilder("Converted")

        for independent in rg.GetIndependentVariables():
            newRG.AddIndependentVariable(independent.Name, independent.DataType, independent.Domain)

        for selection in rg.GetSelectionVariables():
            newRG.AddSelectionVariable(selection.Name, selection.DataType, selection.Domain)

        for dependent in rg.GetDependentVariables():
            newRG.AddDependentVariable(dependent.Name, dependent.DataType, dependent.ComponentType, dependent.Domain)

        newRG.Commit()
        newRG.Dispose()

        lw.WriteLine("Result Group " + rg.Name)
        for dvar in rg.GetDependentVariables():
            q = dvar.DataType
            a = dvar.Name
            lw.WriteLine(a)
            lw.WriteLine("Variable " + dvar.Name)
            lw.WriteLine(" measure " + dvar.Domain.GetMeasure())
            for plot in rg.GetPlots():
                newPlot = output.NewPlotBuilder("plot", "Converted", "Default")
                for selectionVariable in rg.GetSelectionVariables():
                    newPlot.SetSelectionValue(selectionVariable.Name, 
                                              plot.GetSelectionVariableValue(selectionVariable.Name), 
                                              plot.GetSelectionVariableMetadata(selectionVariable.Name))

                newPlot.SetMetadata(plot.Metadata)
                
                lw.WriteLine("Printing " + plot.Name)
                lw.WriteLine("Number of entries: " + str(sum(1 for e in plot.GetEntries())))
                i = 0
                for entry in plot.GetEntries():
                    newEntry = newPlot.NewPlotEntryBuilder()

                    i = i + 1
                    lw.WriteLine("Entry #" + str(i))
                    for component in entry.GetAvailableComponents(dvar.Name):
                        ivalues = entry.GetIndependentValues().GetValueAsDouble()
                        if dvar.DataType == NXOpen.CAE.PostScenarioVariantType.Double:
                            dvalues = entry.GetDependentValues(dvar.Name, component).GetValueAsDouble()
                        elif dvar.DataType == NXOpen.CAE.PostScenarioVariantType.Complex:
                            dvalues = entry.GetDependentValues(dvar.Name, component).GetValueAsComplex()

                        newEntry.SetIndependent(rg.GetIndependentVariables()[0].Name, entry.GetIndependentValues())
                        newEntry.AssignDependent(dvar.Name, component, entry.GetDependentValues(dvar.Name, component))

                        numPlots = numPlots + 1

                    newEntry.Commit()
                    newEntry.Dispose()

                newName = newPlot.GeneratePlotName(NXOpen.CAE.PostScenarioVariantComponent.Scalar)
                newPlot.Name = newName if len(newName) > 0 else "Plot {0}".format(zz_i)
                zz_i += 1
                
                newPlot.Commit()
                newPlot.Dispose()
    return

def MyDescription():
    """
    Callback that displays a short description for this scenario.
    """
    return "Testing coordinate system transformations for graph data"

def MyTransformation(part, input, ctx, output):
    """
    Scenario transformation function, called to filter/transform data.

    Args:
        part (BasePart): input context
        xinput (CAE.PostScenarioQueryResults): input data
        ctx (CAE.PostScenarioQueryContext): input context
        output (CAE.PostScenarioQueryResults): output data
    """
    theSession  = NXOpen.Session.GetSession()
    lw = theSession.ListingWindow
    lw.Open()

    # assign QueryResults name
    output.Name = "Coordinate System Transformations"

    try:
        MyCallback(part, input, ctx, output)
    except AttributeError as err:
        lw.WriteLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        lw.WriteLine(tb)
    except TypeError as err:
        lw.WriteLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        lw.WriteLine(tb)
    except Exception as err:
        lw.WriteLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        lw.WriteLine(tb)

def PartOpenedOrCreated(part):
    """
    Callback invoked whenever a part is open or created, in order to inject our scenario plugin at runtime.
    """
    theSession  = NXOpen.Session.GetSession()
    lw = theSession.ListingWindow
    lw.Open()

    try:
        builder = part.PostScenarioMgr.PostScenarioDescriptors.NewPostScenarioDescriptorBuilder()
        try:
            builder.XmlText = r"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE Scenario SYSTEM "scenarios.dtd">
<Scenario name="CSYS Converter" domainPath="Examples/Feature" trigram="CSX">
  <InputDefinition name="My Definition">
    <Slot name="Data">
      <DependentSelector/>
      <IndependentVariable name="Abscissa">
        <AllowedDataTypes>
          <DataType type="real"/>
        </AllowedDataTypes>
      </IndependentVariable>
      <SelectionVariable name="Location">
        <AllowedDomains>
          <VariableDomain type="node"/>
        </AllowedDomains>
      </SelectionVariable>
      <SelectionVariable name="DOF">
        <AllowedDomains>
          <VariableDomain type="dof_name"/>
        </AllowedDomains>
      </SelectionVariable>
      <DependentVariable name="Ordinate">
        <AllowedDataTypes>
          <DataType type="real"/>
          <DataType type="complex"/>
        </AllowedDataTypes>
      </DependentVariable>
    </Slot>
    <ConfigurationVariable type="choice" name="Conversion Type">
      <ChoiceProvider callback="ConversionTypeProvider"/>
      <ControlsSensitivity callback="ConversionTypeSensitivity">
        <VariableRef name="Coordinate System"/>
      </ControlsSensitivity>
    </ConfigurationVariable>
    <ConfigurationVariable type="coordinate_system_picker" name="Coordinate System">
      <CoordinateSystemPickerProvider callback="CoordinateSystemPickerProvider"/>
    </ConfigurationVariable>
    <Visualization name="XY Plot" layout="1X1">
      <XYPlot name="Result" gridCell="1X1"></XYPlot>
    </Visualization>
  </InputDefinition> 
</Scenario>"""

            builder.AddDescriptionCallback(MyDescription)
            builder.AddTransformationCallback(MyTransformation)
            builder.AddChoiceProviderCallback("ConversionTypeProvider", ConversionTypeProvider)
            builder.AddSensitivityCallback("ConversionTypeSensitivity", ConversionTypeSensitivity)
            builder.AddCoordinateSystemPickerProviderCallback("CoordinateSystemPickerProvider", CoordinateSystemPickerProvider)

            descriptor = builder.Commit()
            lw.WriteLine("loaded ExampleCsysFunctionPlots")
        finally:
            builder.Destroy()
    except AttributeError as err:
        lw.WriteLine("not a cae part -> " + str(err))
    except Exception as err:
        lw.WriteLine(str(err))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb = repr(traceback.format_tb(exc_traceback))
        lw.WriteLine(tb)


def startup(argc, args):
    """
    Entrypoint, invokd when an NXOpen program is loaded from USER_DIR/startup
    """
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
        idPartOpened1 = theSession.Parts.AddPartOpenedHandler(PartOpenedOrCreated)
        idPartOpened2 = theSession.Parts.AddPartCreatedHandler(PartOpenedOrCreated)
    else:
        theSession.LogFile.WriteLine("Already registered!")

    # Close the stream to the listing window.
    lw.Close()

    return 0


def main(): 
    """
    Entrypoint invoked when run as a standalone NXOpen program
    """
    return startup(0, [])
    

if __name__ == '__main__':
    main()
