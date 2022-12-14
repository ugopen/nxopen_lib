#ifndef NXOpen_FEATURES_SHIPDESIGN_DELETESEAMBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_DELETESEAMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_DeleteSeamBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_ShipDesign_DeleteSeamBuilder.hxx>
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
            class DeleteSeamBuilder;
        }
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class SelectTaggedObjectList;
    namespace Features
    {
        namespace ShipDesign
        {
            class _DeleteSeamBuilderBuilder;
            class DeleteSeamBuilderImpl;
            /**
                Used to create a @link Features::ShipDesign::DeleteSeamBuilder Features::ShipDesign::DeleteSeamBuilder@endlink  which
                is used to delete the seams from the ship structural components.
                 <br> To create a new instance of this class, use @link Features::ShipCollection::CreateDeleteSeamBuilder  Features::ShipCollection::CreateDeleteSeamBuilder @endlink  <br> 
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  DeleteSeamBuilder : public Features::FeatureBuilder
            {
                private: DeleteSeamBuilderImpl * m_deleteseambuilder_impl;
                private: friend class  _DeleteSeamBuilderBuilder;
                protected: DeleteSeamBuilder();
                public: ~DeleteSeamBuilder();
                /**Returns  the seams to delete from the ship structural components 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectTaggedObjectList * Seams
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
