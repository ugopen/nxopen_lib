/*=============================================================================
                       Copyright (c) 2004 UGS
                   Unpublished - All rights reserved
===============================================================================
File description: Interoperability example : Uses Open C, Open C++, and NX
Open C++ APIs.


=============================================================================*/

//NXOpen header files
#include <NXOpen/Session.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Line.hxx>
#include <NXOpen/CurveCollection.hxx>
#include <NXOpen/Arc.hxx>
#include <NXOpen/NXObjectManager.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/ListingWindow.hxx>

//UFunc Headers
#include <uf_curve.h>
#include <uf.h>
#include <uf_csys.h>
#include <uf_part.h>

// UGOpen headers
#include <ug_session.hxx>
#include <ug_exception.hxx>
#include <ug_part.hxx>
#include <ug_line.hxx>
#include <ug_arc.hxx>
#include <ug_coord_sys.hxx>
#include <coord_sys.hxx>

int main(int argc, char* argv[])
{

    int errorCode;

    /* Here, we can initialize session using :
        1. Open C API environment
        2. Open C++ API environment
        3. NX Open C++ APIs.

        User has to initialize, UG Session using Open C++ as well as NX Open C++, session
        also.
    */

    /* Using Open C API, we can initialize UGSession as follows */
    /*
       errorCode = UF_initialize();
       if ( 0 != errorCode )
       {
            return errorCode;
       }
    */

    NXOpen::Part *part1;

    /* Using Open C++ API, we can initialize UGSession as follows */
    UgSession::initialize();

    /* Using NX Open C++ API, we can initialize UGSession as follows */
    NXOpen::Session *theSession = NXOpen::Session::GetSession();

    /* Create a new part.
       To create new part one can use :
        1. Open C API environment
        2. Open C++ API environment
        3. NX Open C++ APIs.
    */
    char* partName = "InteropWithOpenCOpenCPPAndNXOpenCPP.prt";
    /* Using Open C API, we can create new part as follows */
    /*
    tag_t UF_partTag;
    UF_PART_new(partName,2,&UF_partTag);
    */
    try
    {
        /* Using Open C++ API, we can create new part as follows */
        UgPart *UGPart = UgPart::create(partName, Inches );

        /* Using NX Open C++ API, we can create new part as follows */
        /*
        NXOpen::NXString partName = "InteropWithOpenCOpenCPPAndNXOpenCPP.prt";
        part1 = theSession->GetParts()->NewDisplay(partName, NXOpen::Part::UnitsInches);
        */

        //--------------------------------------------------------------------------
        //          Interop between NX Open C++ APIs and Open C
        /* Create a line using NX Open C++ APIs*/
        NXOpen::Point3d point3d1(-2.17019791346668, 1.13935390457001, 0);
        NXOpen::Point3d point3d2(-0.714356813182783, 1.13935390457001, 0);
        NXOpen::Line *line1;
        line1 = theSession->Parts()->Work()->Curves()->CreateLine(point3d1, point3d2);

        /* Retrieve line coordinates using Open C API */
        tag_t line_tag=line1->Tag();

        UF_CURVE_line_t line_coords;

        errorCode=UF_CURVE_ask_line_data(line_tag, &line_coords);

        /* Using NXException we can catch the error as follows*/
        if (errorCode) throw NXOpen::NXException::Create(errorCode);

        /* Using UgException we can catch the error as follows*/
//      UgException::throwOnFailure(UF_CURVE_ask_line_data(line_tag, &line_coords));


        //--------------------------------------------------------------------------
        //          Interop between Open C++ and NX Open C++ APIs
        Point3 UGPt1(line_coords.start_point[0]+5,line_coords.start_point[1]+5, line_coords.start_point[2]+5);
        Point3 UGPt2(line_coords.end_point[0]+5,line_coords.end_point[1], line_coords.end_point[2]);

        UgLine* UGLine;
        UGLine = UgLine::create(UGPt1, UGPt2);

        UgCoordSys *UGCoordsys;
        UGCoordsys = UgSession::getWCS();
        CoordSys Sys = UGCoordsys->getCoordSys();

        // Creating Arc
        UgArc* OpenCPPArc = UgArc::create(5.0, 0.25, 3.14, Sys);
        tag_t arc_tag = OpenCPPArc->getTag();

        NXOpen::Arc *nxArc = (NXOpen::Arc*)NXOpen::NXObjectManager::Get(arc_tag);

        double nxArc_radius = nxArc->Radius();
        double nxArc_start_angle = nxArc->StartAngle();
        double nxArc_end_angle = nxArc->EndAngle();

        //------------------------------------------------------------------------------------

        /* Save this work part.
           To save this work part one can use :
            1. Open C API environment
            2. Open C++ API environment
            3. NX Open C++ APIs.
        */

        /* Using Open C API, we can save this part as follows */
        /*
        UF_PART_save();
        */

        /* Using Open C++ API, we can save this part as follows */
        /*
        UGPart->save();
        */

        /* Using NX Open C++ API, we can save this part as follows */
        /* To get the part from the Part tag */
        part1 = (NXOpen::Part*)NXOpen::NXObjectManager::Get(UGPart->getTag());
        /* To save work part using NXOpen automation APIs */
        NXOpen::PartSaveStatus *partSaveStatus = part1->Save(NXOpen::Part::SaveComponentsTrue, NXOpen::Part::CloseAfterSaveTrue);
        /* To close all parts using NXOpen automation APIs */
        theSession->Parts()->CloseAll(NXOpen::BasePart::CloseModifiedCloseModified, NULL);
    }
    catch ( UgException &exception )      // Start of exception handler
    {
        exception.processError();
    }
    catch ( NXOpen::NXException &exception )      // Start of exception handler
    {
        theSession->ListingWindow()->Open();
        theSession->ListingWindow()->WriteLine("Error::");
        theSession->ListingWindow()->WriteLine(exception.Message());
    }


    /* Terminate the session using Open C API */
    UF_terminate();

    return 0;
}

