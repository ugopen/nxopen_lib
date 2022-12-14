#ifndef NXOpen_FEATURES_SHIPDESIGN_ANCHORPOINT_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_ANCHORPOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_AnchorPoint.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
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
            class AnchorPoint;
        }
    }
    class Builder;
    class SelectPoint;
    namespace Features
    {
        namespace ShipDesign
        {
            class _AnchorPointBuilder;
            class AnchorPointImpl;
            /**
                Represents a @link NXOpen::Features::ShipDesign::AnchorPoint NXOpen::Features::ShipDesign::AnchorPoint@endlink  builder.
                 <br> To create a new instance of this class, use @link NXOpen::Features::ShipDesign::QualifySketchBuilder::CreateNewAnchorPoint  NXOpen::Features::ShipDesign::QualifySketchBuilder::CreateNewAnchorPoint @endlink  <br> 
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  AnchorPoint : public NXOpen::Builder
            {
                private: AnchorPointImpl * m_anchorpoint_impl;
                private: friend class  _AnchorPointBuilder;
                protected: AnchorPoint();
                public: ~AnchorPoint();
                /**Returns  the anchor point. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectPoint * Point
                (
                );
                /**Returns  the anchor name. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString Name
                (
                );
                /**Sets  the anchor name. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design") */
                public: void SetName
                (
                    const NXString & name /** name */ 
                );
                /**Sets  the anchor name. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design") */
                void SetName
                (
                    const char * name /** name */ 
                );
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
