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
#include <NXOpen/Tooling_DefineNeutralFactorBuilder.hxx>
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
        class DefineNeutralFactorBuilder;
    }
    namespace Tooling
    {
        class _UniversalUnformBuilderBuilder;
        class UniversalUnformBuilderImpl;
        /**Represents a @link NXOpen::Tooling::UniversalUnformBuilder NXOpen::Tooling::UniversalUnformBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::ToolingCollection::CreateUniversalUnformBuilder  NXOpen::Features::ToolingCollection::CreateUniversalUnformBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        BendType </term> <description> 
         
        StraightBend </description> </item> 

        <item><term> 
         
        DefineNeutralFactor.BendDevelopedLength </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DefineNeutralFactor.NeutralFactor </term> <description> 
         
        0.40 </description> </item> 

        <item><term> 
         
        DefineNeutralFactor.NeutralFactorFormula </term> <description> 
         
        General </description> </item> 

        <item><term> 
         
        DefineNeutralFactor.PartMaterial </term> <description> 
         
        08 </description> </item> 

        <item><term> 
         
        UnformNeutralFactor (deprecated) </term> <description> 
         
        0.4 </description> </item> 

        </list> 

         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  UniversalUnformBuilder : public NXOpen::Features::FeatureBuilder
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
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link Tooling::DefineNeutralFactorBuilder::NeutralFactor Tooling::DefineNeutralFactorBuilder::NeutralFactor@endlink  instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  Use Tooling::DefineNeutralFactorBuilder::NeutralFactor instead.") double UnformNeutralFactor
            (
            );
            /**Sets  the operation of neutral factor for univeral unform. 
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link Tooling::DefineNeutralFactorBuilder::SetNeutralFactor Tooling::DefineNeutralFactorBuilder::SetNeutralFactor@endlink  instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  Use Tooling::DefineNeutralFactorBuilder::SetNeutralFactor instead.") void SetUnformNeutralFactor
            (
                double kFactor /** kfactor */ 
            );
            /**Returns  the define neutral factor builder which contains new neutral factor, part material and bend developed length 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::DefineNeutralFactorBuilder * DefineNeutralFactor
            (
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