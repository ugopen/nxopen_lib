#ifndef NXOpen_FEATURES_SHIPDESIGN_ADDDATASETBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_ADDDATASETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_AddDataSetBuilder.ja
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
            class AddDataSetBuilder;
        }
    }
    class Builder;
    class SelectDisplayableObject;
    namespace Features
    {
        namespace ShipDesign
        {
            class _AddDataSetBuilderBuilder;
            class AddDataSetBuilderImpl;
            /**
                    This class is used to add a dataset to an item in Teamcenter
                     <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateAddDataSetBuilder  NXOpen::Features::ShipCollection::CreateAddDataSetBuilder @endlink  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  AddDataSetBuilder : public NXOpen::Builder
            {
                private: AddDataSetBuilderImpl * m_adddatasetbuilder_impl;
                private: friend class  _AddDataSetBuilderBuilder;
                protected: AddDataSetBuilder();
                public: ~AddDataSetBuilder();
                /**Returns  the data set file 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString DataSetFile
                (
                );
                /**Sets  the data set file 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                public: void SetDataSetFile
                (
                    const NXString & fileName /** filename */ 
                );
                /**Sets  the data set file 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                void SetDataSetFile
                (
                    const char * fileName /** filename */ 
                );
                /**Returns  the component to add the data set to
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectDisplayableObject * Component
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