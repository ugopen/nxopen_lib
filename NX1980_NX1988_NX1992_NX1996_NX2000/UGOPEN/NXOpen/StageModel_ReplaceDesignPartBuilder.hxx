#ifndef NXOpen_STAGEMODEL_REPLACEDESIGNPARTBUILDER_HXX_INCLUDED
#define NXOpen_STAGEMODEL_REPLACEDESIGNPARTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     StageModel_ReplaceDesignPartBuilder.ja
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
#include <NXOpen/libstagemodelopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace StageModel
    {
        class ReplaceDesignPartBuilder;
    }
    class Builder;
    class Part;
    namespace StageModel
    {
        class _ReplaceDesignPartBuilderBuilder;
        class ReplaceDesignPartBuilderImpl;

        /// \cond NX_NO_DOC 
        /** Represents a @link StageModel::ReplaceDesignPartBuilder StageModel::ReplaceDesignPartBuilder@endlink . <br> To create a new instance of this class, use @link NXOpen::StageModel::Manager::CreateReplaceDesignPartBuilder  NXOpen::StageModel::Manager::CreateReplaceDesignPartBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        EnumDesignReference </term> <description> 
         
        DesignPart </description> </item> 

        </list> 

         <br>  Created in NX1980.0.0.  <br>  
        */
        class STAGEMODELOPENCPPEXPORT  ReplaceDesignPartBuilder : public NXOpen::Builder
        {
            /** Represents the two options the user can have. Either replacing the Design Part or another referenced part by the StageSet*/
            public: enum DesignPartTypes
            {
                DesignPartTypesDesignPart/** design part */ ,
                DesignPartTypesReferencePart/** reference part */ 
            };

            private: ReplaceDesignPartBuilderImpl * m_replacedesignpartbuilder_impl;
            private: friend class  _ReplaceDesignPartBuilderBuilder;
            protected: ReplaceDesignPartBuilder();
            public: ~ReplaceDesignPartBuilder();

            /// \cond NX_NO_DOC 
            /** Set reference part. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : stage_model (" Stage Model") */
            public: void SetReferencePart
            (
                NXOpen::Part * part /** part */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Set replacement part. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : stage_model (" Stage Model") */
            public: void SetReplacementPart
            (
                NXOpen::Part * part /** part */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the enum design reference 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : stage_model (" Stage Model") */
            public: NXOpen::StageModel::ReplaceDesignPartBuilder::DesignPartTypes EnumDesignReference
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the enum design reference 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : stage_model (" Stage Model") */
            public: void SetEnumDesignReference
            (
                NXOpen::StageModel::ReplaceDesignPartBuilder::DesignPartTypes enumDesignReference /** enumdesignreference */ 
            );

            /// \endcond 
        };

        /// \endcond 
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
