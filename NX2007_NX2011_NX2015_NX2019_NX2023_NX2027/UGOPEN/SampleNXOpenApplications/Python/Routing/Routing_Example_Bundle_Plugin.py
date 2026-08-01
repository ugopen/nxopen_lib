#===================================================================================================
#               Copyright 2017 Siemens Product Lifecycle Management Software Inc.
#===================================================================================================
#
#    NOTE:  NX Development provides programming examples for illustration only.
#    NX Development assumes you are familiar with the programming language
#    demonstrated in these examples, and the tools used to create and debug NX/Open
#    programs. GTAC support professionals can help explain the functionality of
#    a particular procedure, but neither GTAC nor NX Development will modify
#    these examples to provide added functionality or construction procedures.
#
#File description:
#
#
#   This file implements a Routing Plugin that implements Tyco's Entry Size new bundling algorithm
#   for routing wires in Routing Electrical.  The algorithm is taken from a PDF titled
#   AdapterEntrySizeSelection.pdf on the Tyco Electronics' Raychem web site.
#
#   ALGORITHM:
#
#   For 61 or fewer wires of all the same size, use the Tyco table data to look up a bundle factor (F).
#   The bundle diameter is computed as D = F * d, where d is the wire diameter.
#
#   Otherwise use the formula,
#
#       D = 1.2 * SQRT( SUM( d[i] * d[i] )
#
#   where d[i] is the diameter for each wire in the bundle.
#
#
#===================================================================================================
import NXOpen
import NXOpen.Routing
import math

#---------------------------------------------------------------------------------------------------
def bundlePlugin( stockDatas ):
    try:

        tolerance = 0.000001

        bundleFactorTable = [0.00, 1.00, 1.64, 2.00, 2.41,
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
                             9.00, 9.00]
        
        sizeOfBundleFactorTable = len( bundleFactorTable )

        sumOfDiameters = 0.0
        sumOfSquares   = 0.0
        commonDiameter = -1.0
        equalDiameters = True

        for stockData in stockDatas:

            wireCrossSections = stockData.GetCrossSections()
            for wireCrossSection in wireCrossSections:
                
                wireCrossSectionCurves = wireCrossSection.GetCrossCurves()

                if len( wireCrossSectionCurves ) == 0:
                    continue

                arcDiameter = wireCrossSectionCurves[0].Radius * 2.0
                                    
                sumOfDiameters += arcDiameter
                sumOfSquares   += arcDiameter * arcDiameter

                
                if commonDiameter < 0.0:
                    commonDiameter = arcDiameter;
                elif equalDiameters and abs(commonDiameter - arcDiameter) > tolerance:
                    equalDiameters = False;


        diameter = 0.0

        if equalDiameters and len( stockDatas ) < sizeOfBundleFactorTable:
            # If all the wires are the same size, use the Tyco table.
            diameter = bundleFactorTable[ len(stockDatas) ] * commonDiameter
        else:
            # Otherwise use the the formula.
            diameter = 1.2 * math.sqrt(sumOfSquares)

        return diameter
        
    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#---------------------------------------------------------------------------------------------------
def startup( argc, args ):
    try:

        customManager = NXOpen.Session.GetSession().RouteCustomManager

        customManager.SetBundlePlugin( bundlePlugin )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

    return 0 # No errors.
