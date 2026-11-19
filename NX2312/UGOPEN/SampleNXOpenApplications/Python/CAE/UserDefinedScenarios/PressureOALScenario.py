#==================================================================================================

#                Copyright (c) 2020 Siemens Product Lifecycle Management Software Inc.

#                                     All Rights Reserved.

#==================================================================================================
#File description:
#    Example Overall Sound Pressure Level scenario.

#==================================================================================================
#   Date      Name                    Description of Change
#16-Oct-2020  Costin Nila             Initial version
#26-Jan-2021  Radu Pelin              Use the PostScenarioManager from BasePart
#27-Jan-2021  Alexandru Ciobanas      Extended scenario to compute loudness
#03-Mar-2021  Codrut Simandan         Added error handling for NXException
#$HISTORY$
#==================================================================================================

import sys
import traceback
import math
import bisect
import NXOpen


registered = 0

LEVEL_SPL_WEIGHTING_NONE = "SPL - No Weighting"
LEVEL_SPL_WEIGHTING_A_NETWORK = "SPL - A Weighting"
LEVEL_LOUDNESS = "Loudness"

A_NETWORK_FREQUENCIES = [    
        10.0,       12.5,       16.0,       20.0,       25.0,       31.5,       40.0,
        50.0,       63.0,       80.0,       100.0,      125.0,      160.0,      200.0,
        250.0,      315.0,      400.0,      500.0,      630.0,      800.0,      1000.0,
        1250.0,     1600.0,     2000.0,     2500.0,     3150.0,     4000.0,     5000.0,
        6300.0,     8000.0,     10000.0,    12500.0,    16000.0,    20000.0,    25000.0,
        31500.0,    40000.0,    50000.0,    63000.0,    80000.0,    100000.0
    ]
            
A_NETWORK_WEIGHTS = [
    -70.4,  -63.4,  -56.7,  -50.5,  -44.7,  -39.4,  -34.6,
    -30.2,  -26.2,  -22.5,  -19.1,  -16.1,  -13.4,  -10.9,
    -8.6,   -6.6,   -4.8,   -3.2,   -1.9,   -0.8,    0.0,
    0.6,    1.0,    1.2,    1.3,    1.2,    1.0,    0.5,
    -0.1,   -1.1,   -2.5,   -4.3,   -6.6,   -9.3,  -12.4,
    -15.8,  -19.3,  -23.1,  -26.9,  -30.8,  -34.7
]


# This is the implementation of the descriptor callback.
# The method has no parameters and returns a character string.
def MyDescriptionCallback():
    return "This scenario computes the Pressure Overall Level."

# This is the implementation of the choice provider callback for SPL weighting option
def MyChoiceProviderCallback(part, ctx, values):
    values.AddString(LEVEL_SPL_WEIGHTING_NONE)
    values.AddString(LEVEL_SPL_WEIGHTING_A_NETWORK)
    values.AddString(LEVEL_LOUDNESS)


# This is the implementation of the 1D interpolator
class IterpolatorOneD:
    def __init__(self, xValues, yValues):
        assert self.__ListIsSortedAscending(xValues), "The function to be interpolated needs to have ascending sorted abscissa values."
        assert len(xValues) == len(yValues), "The abscissa and ordinate need to have the same size."
        assert len(xValues) > 0, "The function needs to have a fine number of points."
        self.__xValues = xValues
        self.__yValues = yValues
        
    def Interpolate(self, value):
        if len(self.__xValues) == 1:
            return self.__yValues[0]
        
        # extrapolation constant
        if value <= self.__xValues[0]:
            return self.__yValues[0]
        elif value >= self.__xValues[len(self.__xValues) - 1]:
            return self.__yValues[len(self.__xValues) - 1]
        
        # find insertion index and interpolate
        insertionIndex = bisect.bisect_left(self.__xValues, value)
        if (insertionIndex > 0): # should always happen since value > xValues[0]
            return self.__InterpolateLinear(self.__xValues[insertionIndex - 1], self.__xValues[insertionIndex], self.__yValues[insertionIndex - 1], self.__yValues[insertionIndex], value)

        return None
    
    def __InterpolateLinear(self, x1, x2, y1, y2, xi):
        if x1 == x2: # should not happen since validation is done on the constructor
            return y1
        return y1 + (y2 - y1)/(x2 - x1)*(xi - x1)

    def __ListIsSortedAscending(self, values):
        if len(values) < 2:
            return True
        
        for (i, j) in zip(range(0,len(values) - 1), range(1, len(values))):
            if values[i] >= values[j]: # if not ascending or duplicate
                return False
        
        return True

def SetOutputMetadata(metadata, part, soundLevelScale):
    #Set the function class to spectrum
    functionClassSpectrum = part.PostScenarioMgr.NewVariant()
    functionClassSpectrum.SetValueAsUnicodeString("Spectrum")
    metadata.SetKeyValue("FunctionClass", functionClassSpectrum)

    #Set the spectrum format to linear
    spectrumFormatLinear = part.PostScenarioMgr.NewVariant()
    spectrumFormatLinear.SetValueAsUnicodeString("Linear")
    metadata.SetKeyValue("SpectrumFormat", spectrumFormatLinear)

    #Set the spectrum scaling to peak
    spectrumScalingPeak = part.PostScenarioMgr.NewVariant()
    spectrumScalingPeak.SetValueAsUnicodeString("Peak")
    metadata.SetKeyValue("SpectrumScaling", spectrumScalingPeak)

    vizSpectrumScalingValue = "RMS"
    dbOptionValue = "dbOptionDB"
    if soundLevelScale == LEVEL_LOUDNESS:
        vizSpectrumScalingValue = "Peak"
        dbOptionValue = "dbOptionLinear"
        
    #Set the visualization scaling ot rms
    vizSpectrumScalingRms = part.PostScenarioMgr.NewVariant()
    vizSpectrumScalingRms.SetValueAsUnicodeString(vizSpectrumScalingValue)
    metadata.SetKeyValue("VisualizationSpectrumScaling", vizSpectrumScalingRms)

    #Set the visualization in dB
    dbOptionDB = part.PostScenarioMgr.NewVariant()
    dbOptionDB.SetValueAsUnicodeString(dbOptionValue)
    metadata.SetKeyValue("dBOption", dbOptionDB)

def ComputeOverallSoundPressureLevel(rg, plot, frequencyIndepVariableName, pressureConversionFactor, soundLevelScale, interpolator):

    sumOfSquaresOnNodes = []
    
    # Compute SPLs over frequencies for all nodes
    for entry in plot.GetEntries():

        depVar = rg.GetDependentVariables()[0]                  # we know that there is only one dependent variable (enforced by scenario desciptor)
        comp = entry.GetAvailableComponents(depVar.Name)[0]     # we know that there is only one component (scalar) (enforced by scenario desciptor)
                    
        frequencyVariant = entry.GetHighOrderIndependentVariableValue(frequencyIndepVariableName)
        assert frequencyVariant is not None, "Unexpected independent data type."
                    
        currentFrequency = frequencyVariant.GetValueAsDouble()  # we know frequencies are double values

        squaredAmplitudes = [abs(complex(value.Real, value.Imag))**2 for value in entry.GetDependentValues(depVar.Name, comp).GetValueAsComplex()]
                    
        squareFactor = pressureConversionFactor
        if soundLevelScale == LEVEL_SPL_WEIGHTING_A_NETWORK:
            assert interpolator is not None, "Interpolator 1D has not been initialized." # should never happen, it is initialized at the begining of the transformation function
            weightFactorDB = interpolator.Interpolate(currentFrequency)
            assert weightFactorDB is not None, "Interpolation of A weight coefficient failed."
            squareFactor = pressureConversionFactor * math.pow(10., weightFactorDB/10.)
                    
        squaredAmplitudes = map(lambda x: x*squareFactor, squaredAmplitudes)

        if depVar.DataType == NXOpen.CAE.PostScenarioVariantType.Complex:
            if len(sumOfSquaresOnNodes) == 0:      
                sumOfSquaresOnNodes.extend(squaredAmplitudes)                              
            else:
                sumOfSquaresOnNodes = [a + b for a, b in zip(sumOfSquaresOnNodes, squaredAmplitudes)]
        else:
            # According to the scenario xml the expected dependent data can be only complex.
            mc.AddInformationLine("Unexpected dependent data type")

    values = []
    for v in sumOfSquaresOnNodes:
        values.append(math.sqrt(v))

    return values

def ComputeLoudness(simSimulation, rg, plot, frequencyIndepVariableName, lengthUnitFactor):
    
    numberOfFrequencies = len(plot.GetEntries())
    assert numberOfFrequencies > 0, "The number of frequencies should be > 0."
    
    frequencyAxis = [0.] * numberOfFrequencies
    frequencyIndex = 0
    functionsData = []

    # transform data from SORT1 to SORT2
    for entry in plot.GetEntries():

        frequencyVariant = entry.GetHighOrderIndependentVariableValue(frequencyIndepVariableName)
        assert frequencyVariant is not None, "Unexpected independent data type."
        frequencyAxis[frequencyIndex] = frequencyVariant.GetValueAsDouble()  # we know frequencies are double values

        depVar = rg.GetDependentVariables()[0]                  # we know that there is only one dependent variable (enforced by scenario desciptor)
        comp = entry.GetAvailableComponents(depVar.Name)[0]     # we know that there is only one component (scalar) (enforced by scenario desciptor)
        depValues = entry.GetDependentValues(depVar.Name, comp).GetValueAsComplex()

        # init functions data
        if len(functionsData) == 0:
            functionsData = [[0.] * 2 * numberOfFrequencies for i in range(len(depValues))]
        else:
            assert len(functionsData) == len(depValues), "The size of the dependent variable varies from one frequency to another."

        for depValueIndex, depValue in enumerate(depValues):
            functionsData[depValueIndex][frequencyIndex * 2] = depValue.Real * lengthUnitFactor
            functionsData[depValueIndex][frequencyIndex * 2 + 1] = depValue.Imag * lengthUnitFactor

        frequencyIndex += 1

    values = [simSimulation.Acoustics.ComputeLoudness(frequencyAxis, pressureFunctionData) for pressureFunctionData in functionsData]
    return values


# This is the implementation of the transformation callback. The method takes the data from the input query results,
# transforms the data accordingly, and stores the transformed data in the output query results.
# The method has the following input parameters:
# part - NXOpen.BasePart
# input - NXOpen.CAE.PostScenarioQueryResults
# ctx - NXOpen.CAE.PostScenarioQueryContext
# output - NXOpen.CAE.PostScenarioQueryResults
# The method doesn't have a return value.
def MyTransformationCallback(part, input, ctx, output):
    
    theSession  = NXOpen.Session.GetSession()
    assert theSession is not None, "The session is not valid."

    workSimPart = theSession.Parts.BaseWork
    assert workSimPart is not None, "Work sim part is not valid."

    simSimulation = workSimPart.FindObject("Simulation")
    assert simSimulation is not None, "Simulation object cannot be found."

    # NXOpen.CAE.PostScenarioMessageCollector utility object that is used to write to the information window.
    mc = ctx.MessageCollector

    lengthUnitFactor = 1.
    if part.PartUnits == NXOpen.BasePartUnits.Inches:
        lengthUnitFactor = (1000. / 25.4)
    elif part.PartUnits == NXOpen.BasePartUnits.Millimeters:
        lengthUnitFactor = 1000.
    else:
        assert False, "The part has mix units. The current scenario does not support mix units."

    try:
        # There should be only one result configuration group named "Default".
        cfg = input.GetConfigurationGroups()[0]
        keys = cfg.GetKeys()

        soundLevelScale = None
        if len(keys) > 0:
            soundLevelScaleVariant = cfg.GetValues(keys[0])[0]
            soundLevelScale = soundLevelScaleVariant.GetValueAsUnicodeString() # we know that the values of the weighting option are strings
        
        interpolator = None
        if soundLevelScale == LEVEL_SPL_WEIGHTING_A_NETWORK:
            interpolator = IterpolatorOneD(A_NETWORK_FREQUENCIES, A_NETWORK_WEIGHTS)

        # Assign a name for the output query results.
        output.Name = "Overall Level query results"

        # Create a default configuration group builder for the output query results.
        cg = output.NewConfigurationGroupBuilder("Overall Sound Presure Level")
        cg.Commit()
        cg.Dispose()

        # Copy the result groups to the output.
        for rg in input.GetResultGroups():
            rgOut = output.NewResultGroupBuilder(rg.Name)

            # Copy the independent variables to the output (except for the frequency, because we're consuming it).
            frequencyIndepVariableName = None
            for indepVar in rg.GetIndependentVariables():
                if indepVar.Domain.GetMeasure() != "Frequency":
                    rgOut.AddIndependentVariable(indepVar.Name, indepVar.DataType, indepVar.Domain)
                else:
                    frequencyIndepVariableName = indepVar.Name
            
            assert frequencyIndepVariableName is not None, "Unexpected independent data type"
            
            # Copy the depedent variables to the output (but change the type from complex to double).
            depVariables = rg.GetDependentVariables()
            assert len(depVariables) == 1, "The current scenario supports only one dependent variable."
            
            depVar = depVariables[0]
            
            varDomain = None
            if soundLevelScale == LEVEL_LOUDNESS:
                varDomain = part.PostScenarioMgr.NewVariableDomain()
                varDomain.AddComponent("unitless", [])
            else:
                varDomain = depVar.Domain
            
            assert varDomain is not None, "Unexpected dependent variable domain"

            rgOut.AddDependentVariable(depVar.Name, NXOpen.CAE.PostScenarioVariantType.Double, NXOpen.CAE.PostScenarioComponentType.Scalar, varDomain)

            rgOut.Commit()
            rgOut.Dispose()

            # Copy the plots to the output.
            for plot in rg.GetPlots():
               
                outPb = output.NewPlotBuilder("Plot Name" if not plot.Name else plot.Name, rg.Name, "Overall Sound Presure Level")
                metadata = plot.Metadata

                # verify if input plot scaling is peak or rms
                pressureConversionFactor = 1.
                if metadata.SpectrumFormat == NXOpen.CAE.PostScenarioSpectrumFormat.Linear and metadata.SpectrumMode == NXOpen.CAE.PostScenarioSpectrumMode.Rms:
                    pressureConversionFactor = math.sqrt(2.) # convert rms to peak
                
                SetOutputMetadata(metadata, part, soundLevelScale)
                
                outPb.SetMetadata(metadata)

                # Create a new entry that will contains the OAL
                ebOut = outPb.NewPlotEntryBuilder()
                ebOut.SetIndependent(rg.GetIndependentVariables()[0].Name, plot.GetEntries()[0].GetIndependentValues())

                values = None
                if soundLevelScale == LEVEL_LOUDNESS:
                    values = ComputeLoudness(simSimulation, rg, plot, frequencyIndepVariableName, lengthUnitFactor)
                else:
                    values = ComputeOverallSoundPressureLevel(rg, plot, frequencyIndepVariableName, pressureConversionFactor, soundLevelScale, interpolator)

                vl = part.PostScenarioMgr.NewVariantList()
                vl.SetValueAsDouble(values)
                ebOut.AssignDependent(rg.GetDependentVariables()[0].Name, NXOpen.CAE.PostScenarioVariantComponent.Scalar, vl)
                vl.Dispose()         

                ebOut.Commit()
                ebOut.Dispose()

                outPb.Commit()
                outPb.Dispose()        

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
<Scenario name="Pressure Overall Level" domainPath="Acoustics" trigram="OAL">
  <InputDefinition name="Pressure Overall Level">
    <Slot name="Pressure Data">
      <DependentSelector/>
      <IndependentVariable name="Abscissa">
        <AllowedDataTypes>
          <DataType type="integer"/>
        </AllowedDataTypes>
        <AllowedDomains>
            <VariableDomain type="node"/>
        </AllowedDomains>
      </IndependentVariable>
      <IndependentVariable name="Frequency">
        <AllowedDataTypes>
          <DataType type="real"/>
        </AllowedDataTypes>
        <AllowedDomains>
            <VariableDomain type="frequency"/>
        </AllowedDomains>
      </IndependentVariable>
      <DependentVariable name="Ordinate">
        <AllowedDataTypes>
          <DataType type="complex"/>
        </AllowedDataTypes>
        <AllowedDomains>
            <VariableDomain type="pressure"/>
            <VariableDomain not="true" type="pressure" subTypes="pressure_psd"/>
        </AllowedDomains>
      </DependentVariable>      
    </Slot>    
    <MeshDefinition name="Mesh" meshType="post_model"/>
    <ConfigurationVariable name="Sound Level Scale" type="choice">
        <ChoiceProvider callback="MyChoiceProviderCallback"></ChoiceProvider>
    </ConfigurationVariable>
    <Visualization name="Contour Plot" layout="1X1">
      <PostView name="Overall Level" gridCell="1X1"></PostView>
    </Visualization>
  </InputDefinition> 
</Scenario>"""
            # This callback is used to provide a short description of the user defined scenario.
            builder.AddDescriptionCallback(MyDescriptionCallback)

            # This callback is used to provide the values for the SPL weighting option dropdown list.
            builder.AddChoiceProviderCallback("MyChoiceProviderCallback", MyChoiceProviderCallback)

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
    lw.Close( )
	
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    return 0

def main() : 
    return startup(0, [])
    
if __name__ == '__main__':
    main()
