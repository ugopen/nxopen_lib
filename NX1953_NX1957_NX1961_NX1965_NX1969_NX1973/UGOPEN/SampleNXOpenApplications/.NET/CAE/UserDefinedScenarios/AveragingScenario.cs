/*==================================================================================================

              Copyright 2020 Siemens Product Lifecycle Management Software Inc.
                                    All Rights Reserved.

====================================================================================================
File description:
    Example User Defined Scenario for averaging (arithmetic and geometric) of the selected result data.
    The scenario demonstrates the usage of subviewports, allocating results to the different subviewports
    and the usage of the transformation function.

====================================================================================================

*/

using System;
using System.Collections.Generic;
using System.Linq;
using NXOpen;


public class AveragingScenario
{
    // class members
    private static Session theSession;
    private static ListingWindow lw;
    public static AveragingScenario averagingScenario;
    public static bool isDisposeCalled;

    static int registered = 0;
    static int idPartOpenedOrCreated = 0;

    //------------------------------------------------------------------------------
    // Constructor
    //------------------------------------------------------------------------------
    public AveragingScenario()
    {
        try
        {
            theSession = Session.GetSession();
            if (theSession != null)
            {
                lw = theSession.ListingWindow;
                lw.Open();
            }
            isDisposeCalled = false;
        }
        catch (NXOpen.NXException ex)
        {
            theSession.LogFile.WriteLine(String.Format("Unhandled exception occured when opening the listing window: {0}.", ex.Message));
        }
    }

    /*This is the implementation of the descriptor callback.
    The method has no parameters and returns a character string.*/
    public String MyDescriptionCallback()
    {
        return "This scenario exemplifies how to do the arithmetic and geometric means on the given data.";
    }


    /*This is the implementation of the transformation callback.
    This callback is calculating the arithmetical and geometrical mean of the plots.
    It does the means separately for the real and the imaginary parts of the complex values.
    The method has the following input parameters:
    part - NXOpen.CAE.CaePart
    input - NXOpen.CAE.PostScenarioQueryResults
    ctx - NXOpen.CAE.PostScenarioQueryContext
    output - NXOpen.CAE.PostScenarioQueryResults
    The method doesn't have a return value.*/
    public void MyTransformationCallback(
        NXOpen.CAE.CaePart part,
        NXOpen.CAE.PostScenarioQueryResults input,
        NXOpen.CAE.PostScenarioQueryContext ctx,
        NXOpen.CAE.PostScenarioQueryResults output)
    {
        // Utility object that is used to write to the information window.
        NXOpen.CAE.PostScenarioMessageCollector mc = ctx.MessageCollector;

        try
        {
            // Assign a name for the output query results.
            output.Name = "Averaged query results";

            // Create a default configuration group builder for the output query results.
            var cg = output.NewConfigurationGroupBuilder("Default");
            cg.Commit();
            cg.Dispose();

            // Initialize the lists where the data will be stored.
            // Independent values
            List<double> sumIVals = new List<double>();
            List<double> sumIValsIntersection = new List<double>();
            // Summing and multiplication of dependent values counters
            Dictionary<double, int> counterSumMult = new Dictionary<double, int>();
            // Summation lists
            List<double> sumDValsReal = new List<double>();
            List<double> sumDValsImag = new List<double>();
            // Multiplication lists
            List<double> multipliedDValsReal = new List<double>();
            List<double> multipliedDValsImag = new List<double>();


            // Go through input's result groups.
            foreach (var rg in input.GetResultGroups())
            {
                // Go through plots.
                foreach (var plot in rg.GetPlots())
                {
                    // Go through entries.
                    foreach (var entry in plot.GetEntries())
                    {
                        // Sum, multiply and count plot values in preparation for further calculating the means
                        foreach (var depVar in rg.GetDependentVariables())
                            foreach (var comp in entry.GetAvailableComponents(depVar.Name))
                            {
                                List<double> realValues = new List<double>();
                                List<double> imagValues = new List<double>();

                                if (depVar.DataType == NXOpen.CAE.PostScenarioVariantType.Complex)
                                {
                                    realValues = entry.GetDependentValues(depVar.Name, comp).GetValueAsComplex().ToList<NXOpen.CAE.Complex>().
                                        ConvertAll<double>(val => val.Real);
                                    imagValues = entry.GetDependentValues(depVar.Name, comp).GetValueAsComplex().ToList<NXOpen.CAE.Complex>().
                                        ConvertAll<double>(val => val.Imag);

                                    var values = realValues.Zip(imagValues, (valRe, valImg) => new NXOpen.CAE.Complex(valRe, valImg)).ToArray<NXOpen.CAE.Complex>();

                                    var vl = part.PostScenarioMgr.NewVariantList();
                                    vl.SetValueAsComplex(values);
                                    vl.Dispose();

                                    // Intersecting independent values in separate container
                                    var iValues = entry.GetIndependentValues().GetValueAsDouble().ToList();
                                    if (sumIValsIntersection.Any())
                                        sumIValsIntersection = iValues.Intersect<double>(sumIValsIntersection).ToList();
                                    else
                                        sumIValsIntersection = iValues;

                                    foreach (var iVal in iValues)
                                    {
                                        // Dependents are summed and multiplied for each independent.
                                        if (sumIVals.Contains(iVal))
                                        {
                                            sumDValsReal[sumIVals.IndexOf(iVal)] += realValues[iValues.IndexOf(iVal)];
                                            sumDValsImag[sumIVals.IndexOf(iVal)] += imagValues[iValues.IndexOf(iVal)];

                                            multipliedDValsReal[sumIVals.IndexOf(iVal)] *= Math.Abs(realValues[iValues.IndexOf(iVal)]);
                                            multipliedDValsImag[sumIVals.IndexOf(iVal)] *= Math.Abs(imagValues[iValues.IndexOf(iVal)]);

                                            counterSumMult[iVal]++;
                                        }
                                        else
                                        {
                                            sumIVals.Add(iVal);
                                            counterSumMult[iVal] = 1;

                                            sumDValsReal.Add(realValues[iValues.IndexOf(iVal)]);
                                            sumDValsImag.Add(imagValues[iValues.IndexOf(iVal)]);

                                            multipliedDValsReal.Add(Math.Abs(realValues[iValues.IndexOf(iVal)]));
                                            multipliedDValsImag.Add(Math.Abs(imagValues[iValues.IndexOf(iVal)]));
                                        }
                                    }
                                }
                                else
                                {
                                    mc.AddInformationLine("Unexpected dependent data type.");
                                }
                            }
                    }
                }
            }


            // If there are no result groups in the input, there is nothing to plot.
            if (input.GetResultGroups().Length != 0)
            {
                /* The same type of independent variable, dependent variable and plot can be created as
                those in the first input result group, due to the xml scenario in this example. */
                var rg = input.GetResultGroups()[0];

                // Create a new result group in the output
                var rgAmOut = output.NewResultGroupBuilder("ArithmeticMean");
                var rgGmOut = output.NewResultGroupBuilder("GeometricMean");

                // Add the independent variable to the output.
                var indepVar = rg.GetIndependentVariables()[0];
                rgAmOut.AddIndependentVariable(indepVar.Name, indepVar.DataType, indepVar.Domain);
                rgGmOut.AddIndependentVariable(indepVar.Name, indepVar.DataType, indepVar.Domain);

                // Add the dependent variable to the output.
                var depVar = rg.GetDependentVariables()[0];
                rgAmOut.AddDependentVariable(depVar.Name, depVar.DataType, NXOpen.CAE.PostScenarioComponentType.Scalar, depVar.Domain);
                rgGmOut.AddDependentVariable(depVar.Name, depVar.DataType, NXOpen.CAE.PostScenarioComponentType.Scalar, depVar.Domain);

                rgAmOut.Commit();
                rgAmOut.Dispose();
                rgGmOut.Commit();
                rgGmOut.Dispose();

                // Create a new plot in the output.
                var pbAmOut = output.NewPlotBuilder("Arithmetic Mean", "ArithmeticMean", "Default");
                var pbGmOut = output.NewPlotBuilder("Geometric Mean", "GeometricMean", "Default");

                if (rg.GetPlots().Length != 0)
                {
                    var metadata = rg.GetPlots()[0].Metadata;

                    // Copy the metadata, as it should be the same.
                    pbAmOut.SetMetadata(metadata);
                    pbGmOut.SetMetadata(metadata);
                }

                // Create a new entry in the output.
                var ebAmOut = pbAmOut.NewPlotEntryBuilder();
                var ebGmOut = pbGmOut.NewPlotEntryBuilder();

                // Assign the independent values.
                var iVl = part.PostScenarioMgr.NewVariantList();
                iVl.SetValueAsDouble(sumIValsIntersection.ToArray());
                ebAmOut.SetIndependent(indepVar.Name, iVl);
                ebGmOut.SetIndependent(indepVar.Name, iVl);
                iVl.Dispose();

                // Average intersetion dependent values stoarge lists
                List<double> arithMeanIntersectedDValsReal = new List<double>();
                List<double> arithMeanIntersectedDValsImag = new List<double>();
                List<double> geoMeanIntersectedDValsReal = new List<double>();
                List<double> geoMeanIntersectedDValsImag = new List<double>();
                // The arithmetic and geometric mean of the intersected summed/multiplied dependents is obtained
                foreach (var iVal in sumIValsIntersection)
                {
                    arithMeanIntersectedDValsReal.Add(sumDValsReal[sumIVals.IndexOf(iVal)] / counterSumMult[iVal]);
                    arithMeanIntersectedDValsImag.Add(sumDValsImag[sumIVals.IndexOf(iVal)] / counterSumMult[iVal]);
                    geoMeanIntersectedDValsReal.Add(Math.Pow(multipliedDValsReal[sumIVals.IndexOf(iVal)], 1.0 / counterSumMult[iVal]));
                    geoMeanIntersectedDValsImag.Add(Math.Pow(multipliedDValsImag[sumIVals.IndexOf(iVal)], 1.0 / counterSumMult[iVal]));
                }

                // Assign the dependent values.
                var dAmVl = part.PostScenarioMgr.NewVariantList();
                var dGmVl = part.PostScenarioMgr.NewVariantList();

                var AmDVals = arithMeanIntersectedDValsReal.Zip(arithMeanIntersectedDValsImag, (reVal, imgVal) => new NXOpen.CAE.Complex(reVal, imgVal)).ToArray();
                dAmVl.SetValueAsComplex(AmDVals);
                var GmDVals = geoMeanIntersectedDValsReal.Zip(geoMeanIntersectedDValsImag, (reVal, imgVal) => new NXOpen.CAE.Complex(reVal, imgVal)).ToArray();
                dGmVl.SetValueAsComplex(GmDVals);

                ebAmOut.AssignDependent(depVar.Name, NXOpen.CAE.PostScenarioVariantComponent.Scalar, dAmVl);
                ebGmOut.AssignDependent(depVar.Name, NXOpen.CAE.PostScenarioVariantComponent.Scalar, dGmVl);
                dAmVl.Dispose();
                dGmVl.Dispose();

                ebAmOut.Commit();
                ebAmOut.Dispose();

                ebGmOut.Commit();
                ebGmOut.Dispose();

                pbAmOut.Commit();
                pbAmOut.Dispose();

                pbGmOut.Commit();
                pbGmOut.Dispose();
            }
        }
        catch (NXException e)
        {
            mc.AddInformationLine("Error occured in the transformation callback.");
            mc.AddInformationLine(String.Format("The exception had the following message attached: {0}.", e.Message));
        }
        catch (Exception e)
        {
            theSession.LogFile.WriteLine(String.Format("Unhandled exception occured in the transformation callback: {0}.", e.Message));
        }
    }

    public void PartOpenedOrCreated(BasePart part)
    {
        theSession.LogFile.WriteLine("Inserting the Averaging Scenario.");

        NXOpen.CAE.CaePart caePart = part as NXOpen.CAE.CaePart;
        if (caePart != null)
        {
            NXOpen.CAE.PostScenarioDescriptorBuilder builder = null;
            try
            {
                builder = caePart.PostScenarioMgr.PostScenarioDescriptors.NewPostScenarioDescriptorBuilder();

                // This is the scenario xml.
                builder.XmlText = @"<?xml version='1.0' encoding='utf-8'?>
    <!DOCTYPE Scenario SYSTEM 'scenarios.dtd' >
    <Scenario name='Averaging Scenario' domainPath='Example Scenarios' trigram='AVG' >
        <InputDefinition name = 'My Definition' >
            <Slot name='My Slot'>
                <DependentSelector/>
                <IndependentVariable name='Abscissa'>
                    <AllowedDataTypes>
                        <DataType type='real'/>
                    </AllowedDataTypes>
                </IndependentVariable>
                <DependentVariable name='Ordinate'>
                    <AllowedDataTypes>
                        <DataType type='complex'/>
                     </AllowedDataTypes>
                </DependentVariable>
            </Slot>
            <Visualization name='XY Plot' layout='1X2'>
                <XYPlot name='Arithmetic Mean' gridCell='1X1'></XYPlot>
                <XYPlot name='Geometric Mean' gridCell='1X2'></XYPlot>
            </Visualization>
            <GridCellDataAllocation>
                <AllocateResultGroup name='ArithmeticMean' gridCell ='1X1'>
                    <VisualizationRef name='Arithmetic Mean' />
                </AllocateResultGroup>
                <AllocateResultGroup name='GeometricMean' gridCell ='1X2'>
                    <VisualizationRef name='Geometric Mean'/>
                </AllocateResultGroup>
            </GridCellDataAllocation>
        </InputDefinition>
    </Scenario>";

                // This callback is used to provide a short description of the user defined scenario.
                builder.AddDescriptionCallback(MyDescriptionCallback);

                /* This callback is used to transform the given data. For this particular scenario the
                data will be arithmetically and geometrically averaged. */
                builder.AddTransformationCallback(MyTransformationCallback);

                builder.Commit();
            }
            catch (NXException e)
            {
                if (lw != null)
                {
                    lw.WriteLine("Error occured when creating the user defined scenario.");
                    lw.WriteLine(String.Format("The exception had the following message attached: {0}.", e.Message));
                }
            }
            catch (Exception e)
            {
                theSession.LogFile.WriteLine(String.Format("Unhandled exception occured when creating the user defined scenario: {0}.", e.Message));
            }
            finally
            {
                builder.Destroy();
            }
        }
        else
        {
            lw.WriteLine("Not a cae part.");
        }
    }

    //------------------------------------------------------------------------------
    //  NX Startup
    //      This entry point activates the application at NX startup

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_STARTUP or USER_DEFAULT

    //OR

    //Will also work if dll is at folder named "startup" under any folder listed in the 
    //text file pointed to by the environment variable UGII_CUSTOM_DIRECTORY_FILE.
    //------------------------------------------------------------------------------
    public static int Startup()
    {
        int retValue = 0;
        try
        {
            // Create an instance of the MyScenario class.
            averagingScenario = new AveragingScenario();

            if (registered == 0)
            {
                idPartOpenedOrCreated = theSession.Parts.AddPartCreatedHandler(new NXOpen.PartCollection.PartCreatedHandler(averagingScenario.PartOpenedOrCreated));
                idPartOpenedOrCreated = theSession.Parts.AddPartOpenedHandler(new NXOpen.PartCollection.PartOpenedHandler(averagingScenario.PartOpenedOrCreated));

                registered = 1;
            }
        }
        catch (NXOpen.NXException e)
        {
            if (lw != null)
            {
                lw.WriteLine(String.Format("Unhandled exception occured when creating the user defined scenario: {0}.", e.Message));
            }
        }
        catch (Exception e)
        {
            theSession.LogFile.WriteLine(String.Format("Unhandled exception occured when creating the user defined scenario: {0}.", e.Message));
        }
        return retValue;
    }

    //------------------------------------------------------------------------------
    // Following method disposes all the class members
    //------------------------------------------------------------------------------
    public void Dispose()
    {
        try
        {
            if (isDisposeCalled == false)
            {
                lw.Close();
            }
            isDisposeCalled = true;
        }
        catch (NXOpen.NXException ex)
        {
            theSession.LogFile.WriteLine(String.Format("Unhandled exception occured when closing the listing window: {0}.", ex.Message));
        }
    }

    public static int GetUnloadOption(string arg)
    {
        //Unloads the image explicitly, via an unload dialog
        //return System.Convert.ToInt32(Session.LibraryUnloadOption.Explicitly);

        //Unloads the image immediately after execution within NX
        // return System.Convert.ToInt32(Session.LibraryUnloadOption.Immediately);

        //Unloads the image when the NX session terminates
        return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);
    }

}

