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

    This file implements a Routing Plugin that implements Tyco's Entry Size new bundling algorithm
    for routing wires in Routing Electrical.  The algorithm is taken from a PDF titled
    AdapterEntrySizeSelection.pdf on the Tyco Electronics' Raychem web site.

    ALGORITHM:

    For 61 or fewer wires of all the same size, use the Tyco table data to look up a bundle factor (F).
    The bundle diameter is computed as D = F * d, where d is the wire diameter.

    Otherwise use the formula,

        D = 1.2 * SQRT( SUM( d[i] * d[i] )

    where d[i] is the diameter for each wire in the bundle.


==================================================================================================*/
using NXOpen;
using NXOpen.Routing;
using System;

namespace Routing
{
    public class Tyco
    {
        // Static class members
        static CustomManager customManager = null;

        //------------------------------------------------------------------------------------------
        // Called when NX starts up to register the plugins.
        public static int Startup()
        {
            if (customManager == null)
                customManager = Session.GetSession().RouteCustomManager;

            customManager.SetBundlePlugin(BundlePlugin);

            return 0;
        }

        //------------------------------------------------------------------------------------------
        // Called from File->Execute->NX Open. Useful for testing.
        public static void Main()
        {
            if (customManager == null)
                customManager = Session.GetSession().RouteCustomManager;

            customManager.SetBundlePlugin(BundlePlugin);
        }

        //------------------------------------------------------------------------------------------
        public static double BundlePlugin
        (
            StockData[] stockDatas
        )
        {
            const double tolerance = 0.000001;

            // This table is used if all the wires are the same diameter.
            double[] bundleFactorTable = new double[]
            {
                0.00, 1.00, 1.64, 2.00, 2.41,
                2.70, 3.00, 3.00, 3.60, 4.00,
                4.00, 4.00, 4.00, 4.41, 4.41,
                4.70, 4.70, 5.00, 5.00, 5.00,
                5.31, 5.31, 5.61, 5.61, 5.61,
                6.00, 6.00, 6.00, 6.41, 6.41,
                6.41, 6.70, 6.70, 6.70, 7.00,
                7.00, 7.00, 7.00, 7.31, 7.31,
                7.31, 7.61, 7.61, 7.61, 7.61,
                8.00, 8.00, 8.00, 8.00, 8.41,
                8.41, 8.41, 8.41, 8.70, 8.70,
                8.70, 8.70, 9.00, 9.00, 9.00,
                9.00, 9.00
            };

            int sizeOfBundleFactorTable = bundleFactorTable.Length;

            double sumOfDiameters = 0.0;
            double sumOfSquares = 0.0;
            double commonDiameter = -1.0;
            bool equalDiameters = true;

            foreach (StockData stockData in stockDatas)
            {
                CrossSection[] wireCrossSections = stockData.GetCrossSections();
                foreach (CrossSection wireCrossSection in wireCrossSections)
                {
                    Curve[] wireCrossSectionCurves = wireCrossSection.GetCrossCurves();
                    if (wireCrossSectionCurves.Length == 0)
                        continue;

                    if (wireCrossSectionCurves[0].GetType() != typeof(Arc))
                        continue;

                    // Assume all the cross sections of this stock have the same diameter.
                    Arc crossSectionArc = (Arc)wireCrossSectionCurves[0];

                    double arcDiameter = crossSectionArc.Radius * 2.0;

                    sumOfDiameters += arcDiameter;
                    sumOfSquares += arcDiameter * arcDiameter;

                    if (commonDiameter < 0.0)
                    {
                        commonDiameter = arcDiameter;
                    }
                    else if (equalDiameters && Math.Abs(commonDiameter - arcDiameter) > tolerance)
                    {
                        equalDiameters = false;
                    }
                }
            }

            double diameter = 0.0;
            if (equalDiameters && stockDatas.Length < sizeOfBundleFactorTable)
            {
                // If all the wires are the same size, use the Tyco table.
                diameter = bundleFactorTable[stockDatas.Length] * commonDiameter;
            }
            else
            {
                // Otherwise use the the formula.
                diameter = 1.2 * Math.Sqrt(sumOfSquares);
            }

            return diameter;
        }

        //------------------------------------------------------------------------------------------
        // Tells NX when to unload your application.
        // For Routing callbacks, plugins, and Design Rules, this MUST return AtTermination.
        public static int GetUnloadOption(string arg)
        {
            return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);
        }
    }
}
