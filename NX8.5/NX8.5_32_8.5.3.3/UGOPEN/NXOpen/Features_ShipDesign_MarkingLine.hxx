#ifndef NXOpen_FEATURES_SHIPDESIGN_MARKINGLINE_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_MARKINGLINE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_MarkingLine.ja
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
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace ShipDesign
        {
            class MarkingLine;
        }
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class _MarkingLineBuilder;
            class MarkingLineImpl;
            /** Represents a marking line feature.  <br> To create or edit an instance of this class, use @link Features::ShipDesign::MarkingLineBuilder  Features::ShipDesign::MarkingLineBuilder @endlink  <br> 
             <br>  Created in NX8.0.1.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  MarkingLine : public Features::Feature
            {
                private: MarkingLineImpl * m_markingline_impl;
                private: friend class  _MarkingLineBuilder;
                protected: MarkingLine();
                public: ~MarkingLine();
            };
        }
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

#undef EXPORTLIBRARY
#endif
