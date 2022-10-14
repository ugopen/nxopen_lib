#ifndef NXOpen_FEATURES_SHIPDESIGN_TRANSFRAMELISTITEMBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_TRANSFRAMELISTITEMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_TransFrameListItemBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/NXObject.hxx>
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
            class TransFrameListItemBuilder;
        }
    }
    class Expression;
    class NXObject;
    namespace Features
    {
        namespace ShipDesign
        {
            class _TransFrameListItemBuilderBuilder;
            class TransFrameListItemBuilderImpl;
            /**
                    Represents a @link NXOpen::Features::ShipDesign::TransFrameListItemBuilder NXOpen::Features::ShipDesign::TransFrameListItemBuilder@endlink 
                    
             <br>  Created in NX5.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  TransFrameListItemBuilder : public NXOpen::NXObject
            {
                private: TransFrameListItemBuilderImpl * m_transframelistitembuilder_impl;
                private: friend class  _TransFrameListItemBuilderBuilder;
                protected: TransFrameListItemBuilder();
                public: ~TransFrameListItemBuilder();
                /**Returns  the expression containing the frame spacing value. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * FrameSpacing
                (
                );
                /**Returns  the end frame index. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: int EndFrame
                (
                );
                /**Sets  the end frame index. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetEndFrame
                (
                    int endFrame /** endframe */ 
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