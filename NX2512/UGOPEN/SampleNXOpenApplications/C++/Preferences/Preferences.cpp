//===============================================================================
//
//                   Copyright (c) 2010 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//====================================================================================
//File description: NX/Open example for Changing Sketch and Grid Preferences
//====================================================================================
//

#include <uf_defs.h>
#include <NXOpen/NXException.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/FileNew.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Preferences_PartPreferences.hxx>
#include <NXOpen/Preferences_PartSketch.hxx>
#include <NXOpen/Preferences_SessionPreferences.hxx>
#include <NXOpen/Preferences_SessionSketch.hxx>
#include <NXOpen/Preferences_WorkPlane.hxx>
#include <NXOpen/Session.hxx>
using namespace NXOpen;

extern "C" DllExport int ufusr_ask_unload()
{
    return (int)Session::LibraryUnloadOptionImmediately;
}

extern "C" DllExport void ufusr(char *param, int *retCode, int paramLen)
{
    Session *theSession = Session::GetSession();

    //Creates New Part with name as Preferences.prt
    NXOpen::Part *part1;
    part1=theSession->Parts()->NewDisplay("Preferences",Part::UnitsMillimeters); 
    Part *workPart(theSession->Parts()->Work());
    Part *displayPart(theSession->Parts()->Display()); 



    // ----------------------------------------------
    //  Changing Sketch Prefix names
    // ----------------------------------------------   
      
    theSession->Preferences()->Sketch()->SetDefaultSketchNamePrefix("SKT_");

    theSession->Preferences()->Sketch()->SetDefaultVertexNamePrefix("VRT_");

    theSession->Preferences()->Sketch()->SetDefaultLineNamePrefix("LIN_");

    theSession->Preferences()->Sketch()->SetDefaultArcNamePrefix("ARC_");

    theSession->Preferences()->Sketch()->SetDefaultConicNamePrefix("CON_");

    theSession->Preferences()->Sketch()->SetDefaultSplineNamePrefix("SPL_");       
   
    
    // ----------------------------------------------
    //  Changing Grid values
    // ----------------------------------------------  
    
    Preferences::WorkPlane *workPlane1;
    workPlane1 = workPart->Preferences()->Workplane();
    
    workPlane1->SetGridType(Preferences::WorkPlane::GridPolar);
    
    Preferences::WorkPlane::PolarGridSize polarGridSize1;
    polarGridSize1.RadialGridSize.MajorGridSpacing = 75.0;
    polarGridSize1.RadialGridSize.MinorLinesPerMajor = 3;
    polarGridSize1.RadialGridSize.SnapPointsPerMinor = 5;
    polarGridSize1.AngularGridSize.MajorGridSpacing = 45.0;
    polarGridSize1.AngularGridSize.MinorLinesPerMajor = 4;
    polarGridSize1.AngularGridSize.SnapPointsPerMinor = 2;
    workPlane1->SetPolarGridSize(polarGridSize1);
    
    workPlane1->SetShowGrid(true);
    
    workPlane1->SetShowLabels(false);
    
    workPlane1->SetSnapToGrid(false);
    
    workPlane1->SetGridOnTop(false);
    
    workPlane1->SetRectangularShowMajorLines(false);
    
    workPlane1->SetPolarShowMajorLines(true);
    
    workPlane1->SetGridColor(130);
}
