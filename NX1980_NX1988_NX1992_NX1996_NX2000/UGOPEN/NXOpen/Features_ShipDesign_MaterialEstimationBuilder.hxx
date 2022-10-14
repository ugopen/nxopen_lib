#ifndef NXOpen_FEATURES_SHIPDESIGN_MATERIALESTIMATIONBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_MATERIALESTIMATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_MaterialEstimationBuilder.ja
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
            class MaterialEstimationBuilder;
        }
    }
    class Builder;
    class Part;
    class SelectBody;
    class SelectDisplayableObjectList;
    namespace Features
    {
        namespace ShipDesign
        {
            class _MaterialEstimationBuilderBuilder;
            class MaterialEstimationBuilderImpl;
            /** 
                Represents the class Features.ShipDesign.MaterialEstimationBuilder which is used to 
                calculate the material estimation information.
                 <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateMaterialEstimationBuilder  NXOpen::Features::ShipCollection::CreateMaterialEstimationBuilder @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            SelectionMethod </term> <description> 
             
            Volume </description> </item> 

            </list> 

             <br>  Created in NX10.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  MaterialEstimationBuilder : public NXOpen::Builder
            {
                /** Settings to indicate how the objects are selected. */
                public: enum SelectionMethods
                {
                    SelectionMethodsVolume/** Selection by volume. */,
                    SelectionMethodsFrame/** Selection by Frame. */,
                    SelectionMethodsShipStructure/** Selection by ship structure. */
                };

                private: MaterialEstimationBuilderImpl * m_materialestimationbuilder_impl;
                private: friend class  _MaterialEstimationBuilderBuilder;
                protected: MaterialEstimationBuilder();
                public: ~MaterialEstimationBuilder();
                /**Returns  the selection method. 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: NXOpen::Features::ShipDesign::MaterialEstimationBuilder::SelectionMethods SelectionMethod
                (
                );
                /**Sets  the selection method. 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetSelectionMethod
                (
                    NXOpen::Features::ShipDesign::MaterialEstimationBuilder::SelectionMethods enumSelectionType /** enumselectiontype */ 
                );
                /**Returns  the selected volume body. 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: NXOpen::SelectBody * VolumeBody
                (
                );
                /**Returns  the selected ship structures. 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: NXOpen::SelectDisplayableObjectList * ShipStructures
                (
                );
                /** Sets the selected frame parts.   @return  ship basic design structure component.
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: NXOpen::Part * SetFrameParts
                (
                    int nPartCount /** npartcount */ 
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