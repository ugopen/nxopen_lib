#ifndef NXOpen_CAE_SIMBCXYPLOTBUILDER_HXX_INCLUDED
#define NXOpen_CAE_SIMBCXYPLOTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimBcXyPlotBuilder.ja
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
#include <NXOpen/CAE_Xyplot_Plot.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class SimBcXyPlotBuilder;
    }
    class Builder;
    namespace CAE
    {
        class FEElemEdge;
    }
    namespace CAE
    {
        class FEElemFace;
    }
    namespace CAE
    {
        class FEElement;
    }
    namespace CAE
    {
        class FENode;
    }
    namespace CAE
    {
        class SimBC;
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class Plot;
        }
    }
    namespace CAE
    {
        class _SimBcXyPlotBuilderBuilder;
        class SimBcXyPlotBuilderImpl;
        /** Represents a @link NXOpen::CAE::SimBcXyPlotBuilder NXOpen::CAE::SimBcXyPlotBuilder@endlink  builder 
            which can be used to generate a XY plot of a @link NXOpen::CAE::SimBC NXOpen::CAE::SimBC@endlink  
            in the graphics area. This is limited to @link NXOpen::CAE::SimBC NXOpen::CAE::SimBC@endlink  objects 
            in the active solution.  <br> To create a new instance of this class, use @link NXOpen::CAE::SimSimulation::CreateSimBcXyPlotBuilder  NXOpen::CAE::SimSimulation::CreateSimBcXyPlotBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SimBcXyPlotBuilder : public NXOpen::Builder
        {
            /** Resolve multiple matches when the location specified matches multiple items in the boundary condition's target set */
            public: enum ResolveMultipleMatches
            {
                ResolveMultipleMatchesAdd/** add */ ,
                ResolveMultipleMatchesAverage/** average */ ,
                ResolveMultipleMatchesMinimum/** minimum */ ,
                ResolveMultipleMatchesMaximum/** maximum */ ,
                ResolveMultipleMatchesMultipleCurves/** multiple curves */ 
            };

            private: SimBcXyPlotBuilderImpl * m_simbcxyplotbuilder_impl;
            private: friend class  _SimBcXyPlotBuilderBuilder;
            protected: SimBcXyPlotBuilder();
            public: ~SimBcXyPlotBuilder();
            /** Returns all available @link NXOpen::CAE::SimBC NXOpen::CAE::SimBC@endlink  to plot  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<NXOpen::CAE::SimBC *> GetAvailableBcsToPlot
            (
            );
            /** Returns all available property names that can be plotted for the specified @link NXOpen::CAE::SimBC NXOpen::CAE::SimBC@endlink   @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<NXString> GetAvailablePropertyNamesToPlot
            (
                NXOpen::CAE::SimBC * tBc /** tbc */ 
            );
            /** Sets @link NXOpen::CAE::SimBC NXOpen::CAE::SimBC@endlink  objects to plot. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetBcsToPlot
            (
                const std::vector<NXOpen::CAE::SimBC *> & bcs /** boundary conditions to plot */,
                std::vector<NXString> & propertyNames /** property names to plot */
            );
            /** Sets @link NXOpen::CAE::SimBC NXOpen::CAE::SimBC@endlink  objects to plot. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetBcsToPlot
            (
                const std::vector<NXOpen::CAE::SimBC *> & bcs /** boundary conditions to plot */
            );
            /** Sets property name to plot. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPropertyNameToPlot
            (
                const NXString & pPropertyName /** ppropertyname */ 
            );
            /** Sets property name to plot. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetPropertyNameToPlot
            (
                const char * pPropertyName /** ppropertyname */ 
            );
            /**Returns  a @link NXOpen::CAE::SimBcXyPlotBuilder::ResolveMultipleMatches NXOpen::CAE::SimBcXyPlotBuilder::ResolveMultipleMatches@endlink  used in plot to resolve multiple values 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::SimBcXyPlotBuilder::ResolveMultipleMatches MultipleMatches
            (
            );
            /**Sets  a @link NXOpen::CAE::SimBcXyPlotBuilder::ResolveMultipleMatches NXOpen::CAE::SimBcXyPlotBuilder::ResolveMultipleMatches@endlink  used in plot to resolve multiple values 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMultipleMatches
            (
                NXOpen::CAE::SimBcXyPlotBuilder::ResolveMultipleMatches resolveMultipleMatches /** resolvemultiplematches */ 
            );
            /** Creates XY plot  @return  Created plot 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::Xyplot::Plot * Plot
            (
                int deviceIndex /** device index */,
                int viewIndex /** view index */
            );
            /** Sets location at a node 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetLocationNode
            (
                NXOpen::CAE::FENode * node /** node */
            );
            /** Sets location at an element 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetLocationElement
            (
                NXOpen::CAE::FEElement * element /** element */
            );
            /** Sets location at an element edge
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetLocationElementEdge
            (
                NXOpen::CAE::FEElemEdge * elementEdge /** element edge */
            );
            /** Sets location at an element face 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetLocationElementFace
            (
                NXOpen::CAE::FEElemFace * elementFace /** element face */
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
