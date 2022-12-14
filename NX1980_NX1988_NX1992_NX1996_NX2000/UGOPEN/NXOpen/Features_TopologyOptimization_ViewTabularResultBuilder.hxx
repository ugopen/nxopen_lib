#ifndef NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_VIEWTABULARRESULTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_VIEWTABULARRESULTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TopologyOptimization_ViewTabularResultBuilder.ja
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
#include <NXOpen/Features_TopologyOptimization_Study.hxx>
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
        namespace TopologyOptimization
        {
            class ViewTabularResultBuilder;
        }
    }
    class Builder;
    namespace Features
    {
        namespace TopologyOptimization
        {
            class Study;
        }
    }
    class SelectTaggedObjectList;
    namespace Features
    {
        namespace TopologyOptimization
        {
            class _ViewTabularResultBuilderBuilder;
            class ViewTabularResultBuilderImpl;

            /// \cond NX_NO_DOC 
            /**
                    Represents a builder to specify tabular result contents and list tabular results according to the contents
                     <br> To create a new instance of this class, use @link NXOpen::Features::TopologyOptimization::PostManager::CreateViewTabularResultBuilder  NXOpen::Features::TopologyOptimization::PostManager::CreateViewTabularResultBuilder @endlink  <br> 
             <br>  Created in NX1980.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ViewTabularResultBuilder : public NXOpen::Builder
            {
                /** Report contents option */
                public: enum ReportContentOption
                {
                    ReportContentOptionOptimizationObjective/** optimization objective */ ,
                    ReportContentOptionOptimizationConstraint/** optimization constraint */ ,
                    ReportContentOptionAll/** all */ 
                };

                private: ViewTabularResultBuilderImpl * m_viewtabularresultbuilder_impl;
                private: friend class  _ViewTabularResultBuilderBuilder;
                protected: ViewTabularResultBuilder();
                public: ~ViewTabularResultBuilder();

                /// \cond NX_NO_DOC 
                /** Gets the selected studies. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::Features::TopologyOptimization::Study *> GetStudies
                (
                );

                /// \endcond 

                /// \cond NX_NO_DOC 
                /** Sets the selected studies. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : des_top_opt ("TOPOLOGY OPTIMIZATION FOR DESIGNERS") */
                public: void SetStudies
                (
                    const std::vector<NXOpen::Features::TopologyOptimization::Study *> & studies /** studies */ 
                );

                /// \endcond 

                /// \cond NX_NO_DOC 
                /**Returns  the report content choice 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::TopologyOptimization::ViewTabularResultBuilder::ReportContentOption ReportContent
                (
                );

                /// \endcond 

                /// \cond NX_NO_DOC 
                /**Sets  the report content choice 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : des_top_opt ("TOPOLOGY OPTIMIZATION FOR DESIGNERS") */
                public: void SetReportContent
                (
                    NXOpen::Features::TopologyOptimization::ViewTabularResultBuilder::ReportContentOption reportContent /** reportcontent */ 
                );

                /// \endcond 

                /// \cond NX_NO_DOC 
                /**Returns  the selected solid bodies for scenery bodies or design spaces 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectTaggedObjectList * Bodies
                (
                );

                /// \endcond 
            };

            /// \endcond 
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
