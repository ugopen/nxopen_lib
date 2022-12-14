#ifndef NXOpen_FEATURES_SHIPDESIGN_EXCESSMATERIALBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_EXCESSMATERIALBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_ExcessMaterialBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_ShipDesign_ExcessMaterialBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
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
            class ExcessMaterialBuilder;
        }
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    class SelectFace;
    namespace Features
    {
        namespace ShipDesign
        {
            class _ExcessMaterialBuilderBuilder;
            class ExcessMaterialBuilderImpl;
            /**
                    Represents a @link Features::ShipDesign::ExcessMaterial Features::ShipDesign::ExcessMaterial@endlink  builder.
                    The Excess Material feature adds excess manufacturing material to the end of plate.
                     <br> To create a new instance of this class, use @link Features::ShipCollection::CreateExcessMaterialBuilder  Features::ShipCollection::CreateExcessMaterialBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            OffsetDistance.Value </td> <td> 
             
            10 (millimeters part), 10 (inches part) </td> </tr> 

            </table>  

             <br>  Created in NX7.5.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ExcessMaterialBuilder : public Features::FeatureBuilder
            {
                private: ExcessMaterialBuilderImpl * m_excessmaterialbuilder_impl;
                private: friend class  _ExcessMaterialBuilderBuilder;
                protected: ExcessMaterialBuilder();
                public: ~ExcessMaterialBuilder();
                /**Returns  the selection face.  The selected face will be offset by the specified distance. 
                 <br>  @deprecated Deprecated in NX8.0.0.  Use @link Features::ShipDesign::ExcessMaterialBuilder::SelectFaces Features::ShipDesign::ExcessMaterialBuilder::SelectFaces@endlink  instead. <br>  

                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Use Features::ShipDesign::ExcessMaterialBuilder::SelectFaces instead.") NXOpen::SelectFace * SelectFace
                (
                );
                /**Returns  the faces that need to have excess material. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * SelectFaces
                (
                );
                /**Returns  the offset distance 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * OffsetDistance
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
