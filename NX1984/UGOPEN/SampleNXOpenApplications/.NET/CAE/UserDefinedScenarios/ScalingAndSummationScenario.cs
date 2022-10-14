/*==================================================================================================

                 Copyright (c) 2020 Siemens Product Lifecycle Management Software Inc.
                                      All Rights Reserved.

====================================================================================================
File description:
    Example User Defined Scenario for scaling and summation of plot data.

====================================================================================================
 
*/

using System;
using System.Collections.Generic;
using System.Linq;
using NXOpen;

public class MyScenario
{
    // class members
    private static Session theSession;
    private static ListingWindow lw;
    public static MyScenario myScenario;
    public static bool isDisposeCalled;

    static int registered = 0;
    static int idPartOpenedOrCreated = 0;

    //------------------------------------------------------------------------------
    // Constructor
    //------------------------------------------------------------------------------
    public MyScenario()
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
        catch (NXOpen.NXException e)
        {
            theSession.LogFile.WriteLine(String.Format("Unhandled exception occured when opening the listing window: {0}.", e.Message));
        }
    }

    /*This is the implementation of the descriptor callback.
    The method has no parameters and returns a character string.*/
    public String MyDescriptionCallback()
    {
        return "This scenario exemplifies how to do scaling and summation operations on the given data.";
    }

    /* This is the implementation of the sensitivity callback between the "Scaling" and "Scaling Value"
    configuration variables. From the xml of the scenario it can be seen that the "Scaling" configuration
    variable is boolean. If the "Scaling" variable has the value false then the "Scaling Value" node in the
    Scenario Based Data-Visualization Navigator will be editable, otherwise it will be uneditable and greyed out.
    The method has the following input parameters:
    part - NXOpen.BasePart
    ctx - NXOpen.CAE.PostScenarioConfigurationVariableCallbackContext
    collector - NXOpen.CAE.PostScenarioValueCollector
    The method returns a boolean value.*/
    public bool MySensitivityCallback(
        NXOpen.BasePart part,
        NXOpen.CAE.PostScenarioConfigurationVariableCallbackContext ctx,
        NXOpen.CAE.PostScenarioValueCollector collector)
    {
        var vals = collector.GetValues();
        if (vals.Length == 0)
            return false;
        return !vals[0].GetValueAsBoolean();
    }

    /*This is the implementation of the transformation callback. The method takes the data from the input query results,
    transforms the data accordingly, and stores the transformed data in the output query results.
    The method has the following input parameters:
    part - NXOpen.BasePart
    input - NXOpen.CAE.PostScenarioQueryResults
    ctx - NXOpen.CAE.PostScenarioQueryContext
    output - NXOpen.CAE.PostScenarioQueryResults
    The method doesn't have a return value.*/
    public void MyTransformationCallback(
        NXOpen.BasePart part,
        NXOpen.CAE.PostScenarioQueryResults input,
        NXOpen.CAE.PostScenarioQueryContext ctx,
        NXOpen.CAE.PostScenarioQueryResults output)
    {
        // Utility object that is used to write to the information window.
        NXOpen.CAE.PostScenarioMessageCollector mc = ctx.MessageCollector;

        try
        {

            // There should be only one result configuration group named "Default".
            var cfg = input.GetConfigurationGroups()[0];
            mc.AddInformationLine(String.Format("Configuration group name: {0}", cfg.Name));

            /* Retrieve the names of the existing configuration variables, that were defined in the xml scenario.
            There should be three: "Scaling", "Scaling Value", "Summation", in this order. */
            var keys = cfg.GetKeys();

            // Print the keys to the informtion window.
            mc.AddInformationLine("Available keys:");
            foreach (var key in keys)
                mc.AddInformationLine(String.Format("{0}", key));

            // Retrieve the value of the "Scaling" configuration variable.
            var hasScaling = cfg.GetValues(keys[0])[0];

            /* If the value for "Scaling" is true, retrieve the value of the "Scaling Value" configuration variable
            with which the data will be scaled. */
            double scalingFactor = 1.0;
            if (hasScaling.GetValueAsBoolean())
            {
                var scalingVal = cfg.GetValues(keys[1])[0];
                scalingFactor = scalingVal.GetValueAsDouble();
            }

            // Retrieve the value of the "Summation" configuration variable.
            var hasSumPlot = cfg.GetValues(keys[2])[0];

            // Assign a name for the output query results.
            output.Name = "Scaled and/or summed query results";

            // Create a default configuration group builder for the output query results.
            var cg = output.NewConfigurationGroupBuilder("Default");
            cg.Commit();
            cg.Dispose();

            // Initializet the lists where the summed data will be stored.
            List<double> sumIVals = new List<double>();
            List<double> sumIValsIntersection = new List<double>();
            List<double> sumDValsReal = new List<double>();
            List<double> sumDValsImag = new List<double>();

            // Copy the result groups to the output.
            foreach (var rg in input.GetResultGroups())
            {
                var rgOut = output.NewResultGroupBuilder(rg.Name);
                // Copy the independent variables to the output.
                foreach (var indepVar in rg.GetIndependentVariables())
                    rgOut.AddIndependentVariable(indepVar.Name, indepVar.DataType, indepVar.Domain);

                // Copy the dependent variables to the output.
                foreach (var depVar in rg.GetDependentVariables())
                    rgOut.AddDependentVariable(depVar.Name, depVar.DataType, NXOpen.CAE.PostScenarioComponentType.Scalar, depVar.Domain);

                rgOut.Commit();
                rgOut.Dispose();

                // Copy the plots to the ouput.
                foreach (var plot in rg.GetPlots())
                {
                    var outPb = output.NewPlotBuilder((String.IsNullOrEmpty(plot.Name) ? "PlotName" : plot.Name), rg.Name, "Default");

                    // Copy the metadata to the output.
                    outPb.SetMetadata(plot.Metadata);

                    // Copy the entries to the output.
                    foreach (var entry in plot.GetEntries())
                    {
                        var ebOut = outPb.NewPlotEntryBuilder();

                        // Copy the independent values with the given scaling value and give them to the output.
                        ebOut.SetIndependent(rg.GetIndependentVariables()[0].Name, entry.GetIndependentValues());

                        // Scale the dependent values with the given scaling value and give them to the output.
                        foreach (var depVar in rg.GetDependentVariables())
                            foreach (var comp in entry.GetAvailableComponents(depVar.Name))
                            {
                                List<double> realValues = new List<double>();
                                List<double> imagValues = new List<double>();

                                switch (depVar.DataType)
                                {
                                    case NXOpen.CAE.PostScenarioVariantType.Double:
                                        {
                                            realValues = entry.GetDependentValues(depVar.Name, comp).GetValueAsDouble().ToList<double>().
                                            ConvertAll<double>(val => scalingFactor * val);

                                            var vl = part.PostScenarioMgr.NewVariantList();
                                            vl.SetValueAsDouble(realValues.ToArray());
                                            ebOut.AssignDependent(depVar.Name, NXOpen.CAE.PostScenarioVariantComponent.Scalar, vl);
                                            vl.Dispose();
                                        }

                                        break;

                                    case NXOpen.CAE.PostScenarioVariantType.Complex:
                                        {
                                            realValues = entry.GetDependentValues(depVar.Name, comp).GetValueAsComplex().ToList<NXOpen.CAE.Complex>().
                                            ConvertAll<double>(val => scalingFactor * val.Real);
                                            imagValues = entry.GetDependentValues(depVar.Name, comp).GetValueAsComplex().ToList<NXOpen.CAE.Complex>().
                                                ConvertAll<double>(val => scalingFactor * val.Imag);

                                            var values = realValues.Zip(imagValues, (valRe, valImg) => new NXOpen.CAE.Complex(valRe, valImg)).ToArray<NXOpen.CAE.Complex>();

                                            var vl = part.PostScenarioMgr.NewVariantList();
                                            vl.SetValueAsComplex(values);
                                            ebOut.AssignDependent(depVar.Name, NXOpen.CAE.PostScenarioVariantComponent.Scalar, vl);
                                            vl.Dispose();
                                        }

                                        break;

                                    default:
                                        // According to the scenario xml the expected dependent data can be either real or complex.
                                        mc.AddInformationLine("Unexpected dependent data type.");
                                        break;
                                }

                                /* If the "Summation" configuration variable has a true value, populate lists with 
                                the summed values of the dependent variables. */
                                if (hasSumPlot.GetValueAsBoolean())
                                {
                                    var iValues = entry.GetIndependentValues().GetValueAsDouble().ToList();

                                    if (sumIValsIntersection.Any())
                                        sumIValsIntersection = iValues.Intersect<double>(sumIValsIntersection).ToList();
                                    else
                                        sumIValsIntersection = iValues;

                                    switch (depVar.DataType)
                                    {
                                        case NXOpen.CAE.PostScenarioVariantType.Double:

                                            foreach (var iVal in iValues)
                                            {
                                                if (sumIVals.Contains(iVal))
                                                {
                                                    sumDValsReal[sumIVals.IndexOf(iVal)] += realValues[iValues.IndexOf(iVal)];
                                                }
                                                else
                                                {
                                                    sumIVals.Add(iVal);
                                                    sumDValsReal.Add(realValues[iValues.IndexOf(iVal)]);
                                                }
                                            }

                                            break;

                                        case NXOpen.CAE.PostScenarioVariantType.Complex:

                                            foreach (var iVal in iValues)
                                            {
                                                if (sumIVals.Contains(iVal))
                                                {
                                                    sumDValsReal[sumIVals.IndexOf(iVal)] += realValues[iValues.IndexOf(iVal)];
                                                    sumDValsImag[sumIVals.IndexOf(iVal)] += imagValues[iValues.IndexOf(iVal)];
                                                }
                                                else
                                                {
                                                    sumIVals.Add(iVal);
                                                    sumDValsReal.Add(realValues[iValues.IndexOf(iVal)]);
                                                    sumDValsImag.Add(imagValues[iValues.IndexOf(iVal)]);
                                                }
                                            }

                                            break;

                                        default:
                                            // According to the scenario xml the expected dependent data can be either real or complex.
                                            mc.AddInformationLine("Unexpected dependent data type.");
                                            break;
                                    }
                                }
                            }

                        ebOut.Commit();
                        ebOut.Dispose();
                    }

                    outPb.Commit();
                    outPb.Dispose();
                }
            }

            /* If the "Summation" configuration variable has a true value, create an additional plot
            with the summed values of the dependent variables.*/
            if (hasSumPlot.GetValueAsBoolean())
            {
                // If there are no result groups in the input, there is nothing to plot.
                if (input.GetResultGroups().Length != 0)
                {
                    /* The same type of independent variable, dependent variable and plot can be created as
                    those in the first input result group, due to the xml scenario in this example. */
                    var rg = input.GetResultGroups()[0];

                    // Create a new result group in the output
                    var rgOut = output.NewResultGroupBuilder("Summed Group");

                    // Add the independent variable to the output.
                    var indepVar = rg.GetIndependentVariables()[0];
                    rgOut.AddIndependentVariable(indepVar.Name, indepVar.DataType, indepVar.Domain);

                    // Add the dependent variable to the output.
                    var depVar = rg.GetDependentVariables()[0];
                    rgOut.AddDependentVariable(depVar.Name, depVar.DataType, NXOpen.CAE.PostScenarioComponentType.Scalar, depVar.Domain);

                    rgOut.Commit();
                    rgOut.Dispose();

                    // Create a new plot in the output.
                    var pbOut = output.NewPlotBuilder("Summed Plot", "Summed Group", "Default");

                    if (rg.GetPlots().Length != 0)
                    {
                        var metadata = rg.GetPlots()[0].Metadata;
                        // The "summed" plot will be displayed with a thicker line.
                        metadata.HighlightedDisplay = true;
                        // Copy the metadata, as it should be the same.
                        pbOut.SetMetadata(metadata);
                    }

                    // Create a new entry in the output.
                    var ebOut = pbOut.NewPlotEntryBuilder();

                    // Assign the independent values.
                    var iVl = part.PostScenarioMgr.NewVariantList();
                    iVl.SetValueAsDouble(sumIValsIntersection.ToArray());
                    ebOut.SetIndependent(indepVar.Name, iVl);
                    iVl.Dispose();

                    // Assign the dependent values.
                    var dVl = part.PostScenarioMgr.NewVariantList();
                    if (!sumDValsImag.Any())
                    {
                        // Consider only the values from the intersection of the independent values.
                        List<double> sumDValsRealIntersection = new List<double>();
                        foreach (var iVal in sumIValsIntersection)
                        {
                            sumDValsRealIntersection.Add(sumDValsReal[sumIVals.IndexOf(iVal)]);
                        }

                        dVl.SetValueAsDouble(sumDValsRealIntersection.ToArray());
                    }
                    else
                    {
                        // Consider only the values from the intersection of the independent values.
                        List<double> sumDValsRealIntersection = new List<double>();
                        List<double> sumDValsImagIntersection = new List<double>();
                        foreach (var iVal in sumIValsIntersection)
                        {
                            sumDValsRealIntersection.Add(sumDValsReal[sumIVals.IndexOf(iVal)]);
                            sumDValsImagIntersection.Add(sumDValsImag[sumIVals.IndexOf(iVal)]);
                        }

                        var sumDVals = sumDValsRealIntersection.Zip(sumDValsImagIntersection, (reVal, imgVal) => new NXOpen.CAE.Complex(reVal, imgVal)).ToArray();
                        dVl.SetValueAsComplex(sumDVals);
                    }

                    ebOut.AssignDependent(depVar.Name, NXOpen.CAE.PostScenarioVariantComponent.Scalar, dVl);
                    dVl.Dispose();

                    ebOut.Commit();
                    ebOut.Dispose();

                    pbOut.Commit();
                    pbOut.Dispose();
                }
            }
        }
        catch (NXException e)
        {
            mc.AddInformationLine("Error occured in the transformation callback.");
            mc.AddInformationLine(String.Format("The exception had the following message attached: {0}.", e.Message));
        }
        catch (Exception e)
        {
            theSession.LogFile.WriteLine(String.Format("Unhandled exception occured in the transformation callbak: {0}.", e.Message));
        }
    }

    public void PartOpenedOrCreated(BasePart part)
    {
        theSession.LogFile.WriteLine("Inserting Scaling and Summation Scenario.");

        try
        {
            NXOpen.CAE.PostScenarioDescriptorBuilder builder = null;
            builder = part.PostScenarioMgr.PostScenarioDescriptors.NewPostScenarioDescriptorBuilder();

            // This is the scenario xml.
            builder.XmlText = @"<?xml version='1.0' encoding='utf-8'?> 
    <!DOCTYPE Scenario SYSTEM 'scenarios.dtd' >
    <Scenario name='Summation and Scaling Scenario' domainPath='Examples' trigram='SSS' >
        < InputDefinition name = 'My Definition' >
            <Slot name='My Slot'>
                <DependentSelector/>
                <IndependentVariable name='Abscissa'>
                    <AllowedDataTypes>
                        <DataType type='real'/>
                    </AllowedDataTypes>
                </IndependentVariable>
                <DependentVariable name='Ordinate'>
                    <AllowedDataTypes>
                        <DataType type='real'/>
                        <DataType type='complex'/>
                     </AllowedDataTypes>
                </DependentVariable>
            </Slot>
            <!--Configuration variables with which the data should be scaled.-->
            <ConfigurationVariable name='Scaling Value' type='real'>
                <DefaultValue>1.0</DefaultValue>
            </ConfigurationVariable>
            <!--Configuration variable that controls whether the data should be scaled or not.
            It controls the availability of the previous configuration variable in the UI through a callback.-->
            <ConfigurationVariable name='Scaling' type='boolean'>
                <DefaultValue>true</DefaultValue>
                <ControlsSensitivity callback='MySensitivityCallback'>
                    <VariableRef name='Scaling Value'/>
                </ControlsSensitivity>
            </ConfigurationVariable>
            <!--Configuration variable that controls the creation of a plot containing the summed data of multiple plots.-->
            <ConfigurationVariable name='Summation' type = 'boolean'></ConfigurationVariable>
            <Visualization name='XY Plot' layout='1X1'>
                <XYPlot name='Metadata Example' gridCell='1X1'></XYPlot>
            </Visualization>
        </InputDefinition>
    </Scenario>";

            // This callback is used to provide a short description of the user defined scenario.
            builder.AddDescriptionCallback(MyDescriptionCallback);
            /* This callback is used to create a relation between two configuration variables
            "Scaling" and "Scaling Value".*/
            builder.AddSensitivityCallback("MySensitivityCallback", MySensitivityCallback);
            /* This callback is used to transform the given data. For this particular scenario the
            data can be scaled and/or summed. */
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
            myScenario = new MyScenario();

            if (registered == 0)
            {
                idPartOpenedOrCreated = theSession.Parts.AddPartCreatedHandler(new NXOpen.PartCollection.PartCreatedHandler(myScenario.PartOpenedOrCreated));
                idPartOpenedOrCreated = theSession.Parts.AddPartOpenedHandler(new NXOpen.PartCollection.PartOpenedHandler(myScenario.PartOpenedOrCreated));

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
        catch (NXOpen.NXException e)
        {
            theSession.LogFile.WriteLine(String.Format("Unhandled exception occured when closing the listing window: {0}.", e.Message));
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
