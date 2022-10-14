#ifndef NXOpen_AME_PRIMITIVESHEETELEMENTTYPES_HXX_INCLUDED
#define NXOpen_AME_PRIMITIVESHEETELEMENTTYPES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_PrimitiveSheetElementTypes.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        /** Represents lettering angle of annotation */
        enum PrimitiveSheetElementBuilderOfNoteLetteringangle
        {
            PrimitiveSheetElementBuilderOfNoteLetteringangleInvalid/** invalid */  = -1,
            PrimitiveSheetElementBuilderOfNoteLetteringangleNoValue/** no value */ ,
            PrimitiveSheetElementBuilderOfNoteLetteringangleDegree0/** degree0 */ ,
            PrimitiveSheetElementBuilderOfNoteLetteringangleDegree45/** degree45 */ ,
            PrimitiveSheetElementBuilderOfNoteLetteringangleDegree90/** degree90 */ ,
            PrimitiveSheetElementBuilderOfNoteLetteringangleDegree135/** degree135 */ ,
            PrimitiveSheetElementBuilderOfNoteLetteringangleDegree180/** degree180 */ ,
            PrimitiveSheetElementBuilderOfNoteLetteringangleDegree225/** degree225 */ ,
            PrimitiveSheetElementBuilderOfNoteLetteringangleDegree270/** degree270 */ ,
            PrimitiveSheetElementBuilderOfNoteLetteringangleDegree315/** degree315 */ 
        };

        /** Represents anchor of annotation */
        enum PrimitiveSheetElementBuilderOfNoteAnchor
        {
            PrimitiveSheetElementBuilderOfNoteAnchorInvalid/** invalid */  = -1,
            PrimitiveSheetElementBuilderOfNoteAnchorNoValue/** no value */ ,
            PrimitiveSheetElementBuilderOfNoteAnchorTopLeft/** top left */ ,
            PrimitiveSheetElementBuilderOfNoteAnchorTopCenter/** top center */ ,
            PrimitiveSheetElementBuilderOfNoteAnchorTopRight/** top right */ ,
            PrimitiveSheetElementBuilderOfNoteAnchorMiddleLeft/** middle left */ ,
            PrimitiveSheetElementBuilderOfNoteAnchorMiddleCenter/** middle center */ ,
            PrimitiveSheetElementBuilderOfNoteAnchorMiddleRight/** middle right */ ,
            PrimitiveSheetElementBuilderOfNoteAnchorBottomLeft/** bottom left */ ,
            PrimitiveSheetElementBuilderOfNoteAnchorBottomCenter/** bottom center */ ,
            PrimitiveSheetElementBuilderOfNoteAnchorBottomRight/** bottom right */ 
        };

    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#endif