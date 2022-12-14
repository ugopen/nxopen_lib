#ifndef NXOpen_FEATURES_SHIPDESIGN_MANUFACTURINGOUTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_MANUFACTURINGOUTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_ManufacturingOutBuilder.ja
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
#include <NXOpen/Section.hxx>
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
            class ManufacturingOutBuilder;
        }
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class NXObject;
    class Section;
    class SelectDisplayableObject;
    namespace Features
    {
        namespace ShipDesign
        {
            class _ManufacturingOutBuilderBuilder;
            class ManufacturingOutBuilderImpl;
            /**
                    Represents a @link NXOpen::Features::ShipDesign::ManufacturingOut NXOpen::Features::ShipDesign::ManufacturingOut@endlink  builder
                     <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateManufacturingOutBuilder  NXOpen::Features::ShipCollection::CreateManufacturingOutBuilder @endlink  <br> 
             <br>  Created in NX5.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ManufacturingOutBuilder : public NXOpen::Features::FeatureBuilder
            {
                private: ManufacturingOutBuilderImpl * m_manufacturingoutbuilder_impl;
                private: friend class  _ManufacturingOutBuilderBuilder;
                protected: ManufacturingOutBuilder();
                public: ~ManufacturingOutBuilder();
                /**Returns  the output spreadsheet file 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString OutputFile
                (
                );
                /**Sets  the output spreadsheet file 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetOutputFile
                (
                    const NXString & fileName /** filename */ 
                );
                /**Sets  the output spreadsheet file 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                void SetOutputFile
                (
                    const char * fileName /** filename */ 
                );
                /**Returns  the XML confiuration file 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString ConfigFile
                (
                );
                /**Sets  the XML confiuration file 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetConfigFile
                (
                    const NXString & fileName /** filename */ 
                );
                /**Sets  the XML confiuration file 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                void SetConfigFile
                (
                    const char * fileName /** filename */ 
                );
                /**Returns  the component to validate
                 <br>  Created in NX9.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectDisplayableObject * Component
                (
                );
                /**Returns  the mark only section 
                 <br>  Created in NX9.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Section * MarkOnlySection
                (
                );
                /**The parts to be processed 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetParts
                (
                    const std::vector<NXOpen::NXObject *> & parts /** parts */ 
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
