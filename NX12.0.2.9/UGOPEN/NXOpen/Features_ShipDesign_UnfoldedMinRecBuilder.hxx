#ifndef NXOpen_FEATURES_SHIPDESIGN_UNFOLDEDMINRECBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_UNFOLDEDMINRECBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_UnfoldedMinRecBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
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
            class UnfoldedMinRecBuilder;
        }
    }
    class Builder;
    class SelectDisplayableObjectList;
    namespace Features
    {
        namespace ShipDesign
        {
            class _UnfoldedMinRecBuilderBuilder;
            class UnfoldedMinRecBuilderImpl;
            /** 
                Represents the class Features.ShipDesign.UnfoldedMinRecBuilder which is used to 
                calculate the unfolded minimum rectangle of ship basic design plates or standard parts.
                 <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateUnfoldedMinRecBuilder  NXOpen::Features::ShipCollection::CreateUnfoldedMinRecBuilder @endlink  <br> 
             <br>  Created in NX10.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  UnfoldedMinRecBuilder : public NXOpen::Builder
            {
                private: UnfoldedMinRecBuilderImpl * m_unfoldedminrecbuilder_impl;
                private: friend class  _UnfoldedMinRecBuilderBuilder;
                protected: UnfoldedMinRecBuilder();
                public: ~UnfoldedMinRecBuilder();
                /**Returns  the ship basic design plate faces and standard part curves.
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: NXOpen::SelectDisplayableObjectList * SelectionObjects
                (
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
