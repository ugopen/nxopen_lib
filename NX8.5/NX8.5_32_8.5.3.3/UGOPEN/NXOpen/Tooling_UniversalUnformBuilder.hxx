#ifndef NXOpen_TOOLING_UNIVERSALUNFORMBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_UNIVERSALUNFORMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_UniversalUnformBuilder.ja
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
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/Tooling_UniversalUnformBuilder.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class UniversalUnformBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    class SelectNXObject;
    namespace Tooling
    {
        class _UniversalUnformBuilderBuilder;
        class UniversalUnformBuilderImpl;
        /**Represents a @link Tooling::UniversalUnformBuilder Tooling::UniversalUnformBuilder@endlink  builder.  <br> To create a new instance of this class, use @link Features::ToolingCollection::CreateUniversalUnformBuilder  Features::ToolingCollection::CreateUniversalUnformBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        BendType </td> <td> 
         
        StraightBend </td> </tr> 

        <tr><td> 
         
        UnformNeutralFactor </td> <td> 
         
        0.4 </td> </tr> 

        </table>  

         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  UniversalUnformBuilder : public Features::FeatureBuilder
        {
            /** The types of bend  */
            public: enum BendTypes
            {
                BendTypesStraightBend/** straight bend type */,
                BendTypesContourFlange/** contour flange type */,
                BendTypesBurring/** burring type */
            };

            private: UniversalUnformBuilderImpl * m_universalunformbuilder_impl;
            private: friend class  _UniversalUnformBuilderBuilder;
            protected: UniversalUnformBuilder();
            public: ~UniversalUnformBuilder();
            /**Returns  the reference face edge 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * ReferenceFaceEdge
            (
            );
            /**Returns  the bend faces 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * BendFaces
            (
            );
            /**Returns  the blend faces 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * BlendFaces
            (
            );
            /**Returns  the bend type 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::UniversalUnformBuilder::BendTypes BendType
            (
            );
            /**Sets  the bend type 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBendType
            (
                NXOpen::Tooling::UniversalUnformBuilder::BendTypes bendType /** bendtype */ 
            );
            /**Returns  the operation of neutral factor for univeral unform. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: double UnformNeutralFactor
            (
            );
            /**Sets  the operation of neutral factor for univeral unform. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetUnformNeutralFactor
            (
                double kFactor /** kfactor */ 
            );
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

#undef EXPORTLIBRARY
#endif
