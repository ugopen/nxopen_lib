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

    See Routing_Example_Plugins.hpp for the interface.


==================================================================================================*/
#include "Routing_Example_Bundle_Plugin.hpp"
#include <cmath>
#include <sstream>
#include <uf_ugopenint.h>

#include <NXOpen/Arc.hxx>
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/LogFile.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Routing_Anchor.hxx>
#include <NXOpen/Routing_CrossSection.hxx>
#include <NXOpen/Routing_CrossSectionCollection.hxx>
#include <NXOpen/Routing_CustomManager.hxx>
#include <NXOpen/Routing_RouteManager.hxx>
#include <NXOpen/Routing_Wire.hxx>
#include <NXOpen/Session.hxx>

using namespace NXOpen;
using namespace NXOpen::Routing;

Tyco* NXOpen::Routing::thePlugin;

using StlCrossSectionVector  = std::vector<CrossSection *>;
using StlCurveVector         = std::vector<NXOpen::Curve *>;

//--------------------------------------------------------------------------------------------------
Tyco::Tyco()
{
    CustomManager* customManager = Session::GetSession()->RouteCustomManager();

    customManager->SetBundlePlugin( make_callback( this, &Tyco::BundlePlugin ) );
};

//--------------------------------------------------------------------------------------
double Tyco::BundlePlugin
(
    StlStockDataVector stockDatas
)
{
    const double tolerance = 0.000001;

    // This table is used if all the wires are the same diameter.
    static const double bundleFactorTable[] =
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

    static int sizeOfBundleFactorTable = sizeof( bundleFactorTable ) / sizeof( bundleFactorTable[0] );

    double sumOfDiameters =  0.0;
    double sumOfSquares   =  0.0;
    double commonDiameter = -1.0;
    bool   equalDiameters = true;

    for ( auto stockData : stockDatas )
    {
        StlCrossSectionVector wireCrossSections = stockData->GetCrossSections();
        for ( auto wireCrossSection : wireCrossSections )
        {
            StlCurveVector wireCrossSectionCurves = wireCrossSection->GetCrossCurves();
            if ( wireCrossSectionCurves.empty() )
                continue;

            // Assume all the cross sections of this stock have the same diameter.
            Arc* crossSectionArc = dynamic_cast<Arc*>( wireCrossSectionCurves[0] );
            if ( crossSectionArc == nullptr )
                continue;

            double arcDiameter = crossSectionArc->Radius() * 2.0;

            sumOfDiameters += arcDiameter;
            sumOfSquares   += arcDiameter * arcDiameter;

            if ( commonDiameter < 0.0 )
            {
                commonDiameter = arcDiameter;
            }
            else if ( equalDiameters && fabs( commonDiameter - arcDiameter ) > tolerance )
            {
                equalDiameters = false;
            }
        }
    }

    double diameter =  0.0;
    if ( equalDiameters && stockDatas.size() < sizeOfBundleFactorTable )
    {
        // If all the wires are the same size, use the Tyco table.
        diameter = bundleFactorTable[ stockDatas.size() ] * commonDiameter;
    }
    else
    {
        // Otherwise use the the formula.
        diameter = 1.2 * sqrt( sumOfSquares );
    }

    return diameter;
}

//--------------------------------------------------------------------------------------------------
// Called when NX starts up to register the plugins using the Plugins class constructor.
extern "C" DllExport void ufsta
(
    char* /*param*/,
    int*  retcod,
    int   /*param_len*/
)
{
    *retcod = 0;

    thePlugin = new Tyco();
}

//--------------------------------------------------------------------------------------------------
// Tells NX when to unload your application.
// For Routing callbacks, plugins, and Design Rules, this MUST return UF_UNLOAD_UG_TERMINATE.
extern int ufusr_ask_unload()
{
    return( UF_UNLOAD_UG_TERMINATE );
}
