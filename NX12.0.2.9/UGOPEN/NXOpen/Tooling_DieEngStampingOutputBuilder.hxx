#ifndef NXOpen_TOOLING_DIEENGSTAMPINGOUTPUTBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_DIEENGSTAMPINGOUTPUTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_DieEngStampingOutputBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class DieEngStampingOutputBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class SelectBody;
    class SelectBodyList;
    namespace Tooling
    {
        class _DieEngStampingOutputBuilderBuilder;
        class DieEngStampingOutputBuilderImpl;
        /**
            Represents a Stamping Output builder
             <br> To create a new instance of this class, use @link NXOpen::Tooling::AutoDieCollection::CreateDieEngStampingOutputBuilder  NXOpen::Tooling::AutoDieCollection::CreateDieEngStampingOutputBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        SewTolerance </td> <td> 
         
        0.0254 </td> </tr> 

        <tr><td> 
         
        SpringbackMethod </td> <td> 
         
        None </td> </tr> 

        </table>  

         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  DieEngStampingOutputBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Types of product display. */
            public: enum DisplayProductType
            {
                DisplayProductTypeOriginalProduct/** original product */ ,
                DisplayProductTypeNewProduct/** new product */ ,
                DisplayProductTypeBoth/** both */ 
            };

            /** Types of springback method */
            public: enum SpringbackMethodType
            {
                SpringbackMethodTypeNone/** none */ ,
                SpringbackMethodTypeUniformMembraneExpansion/** uniform membrane expansion */ ,
                SpringbackMethodTypeOvercrownbyFunction/** overcrownby function */ ,
                SpringbackMethodTypeOvercrownbySurface/** overcrownby surface */ 
            };

            private: DieEngStampingOutputBuilderImpl * m_dieengstampingoutputbuilder_impl;
            private: friend class  _DieEngStampingOutputBuilderBuilder;
            protected: DieEngStampingOutputBuilder();
            public: ~DieEngStampingOutputBuilder();
            /**Returns  the select die engineering sheet bodies 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::SelectBodyList * SourceBody
            (
            );
            /**Returns  the select target body 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBody * TargetBody
            (
            );
            /**Returns  the springback method 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::DieEngStampingOutputBuilder::SpringbackMethodType SpringbackMethod
            (
            );
            /**Sets  the springback method 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetSpringbackMethod
            (
                NXOpen::Tooling::DieEngStampingOutputBuilder::SpringbackMethodType springbackMethod /** springbackmethod */ 
            );
            /** The define springback method 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void DefineSpringback
            (
            );
            /** The set stamping output display property method 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetProperty
            (
            );
            /**Returns  the sew tolerance 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double SewTolerance
            (
            );
            /**Sets  the sew tolerance 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetSewTolerance
            (
                double sewTolerance /** sewtolerance */ 
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
