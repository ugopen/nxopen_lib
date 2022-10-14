#ifndef NXOpen_CAE_FREEBODYRESULTSBUILDER_HXX_INCLUDED
#define NXOpen_CAE_FREEBODYRESULTSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FreeBodyResultsBuilder.ja
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
#include <NXOpen/CAE_Result.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ugmath.hxx>
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
        class FreeBodyResultsBuilder;
    }
    class Builder;
    namespace CAE
    {
        class BaseIteration;
    }
    class NXColor;
    namespace CAE
    {
        class _FreeBodyResultsBuilderBuilder;
        class FreeBodyResultsBuilderImpl;
        /** Represents a @link NXOpen::CAE::FreeBodyResultsBuilder NXOpen::CAE::FreeBodyResultsBuilder@endlink   <br> To obtain an instance of this class use @link NXOpen::Session::ResultManager NXOpen::Session::ResultManager@endlink .  <br> 
         <br>  Created in NX7.5.1.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  FreeBodyResultsBuilder : public NXOpen::Builder
        {
            /** Location definition method */
            public: enum LocationMethod
            {
                LocationMethodId/** location is defined by node id */,
                LocationMethodCoords/** location is defined by coordinates */,
                LocationMethodCsysorigin/** location is defined by coordinate system origin */
            };

            /** User Specified output units */
            public: enum OutputUnits
            {
                OutputUnitsDefault/** same as Solver Deck Unit*/,
                OutputUnitsMilliNewton/** Load unit = "N", Moment unit N-mm*/,
                OutputUnitsMilliMillinewton/** Load unit = "mN", Moment unit N-mm*/,
                OutputUnitsMeterNewton/** Load unit = "N", Moment unit N-m*/,
                OutputUnitsFtPoundForce/** Load unit = "lbf", Moment unit lbf-ft*/,
                OutputUnitsInPoundForce/** Load unit = "lbf", Moment unit lbf-in*/
            };

            /** Vector display option */
            public: enum VectorDisplay
            {
                VectorDisplayMagnitude/** display single magnitude vector */,
                VectorDisplayComponents/** display individual components */
            };

            private: FreeBodyResultsBuilderImpl * m_freebodyresultsbuilder_impl;
            private: friend class  _FreeBodyResultsBuilderBuilder;
            protected: FreeBodyResultsBuilder();
            public: ~FreeBodyResultsBuilder();
            /** The iteration containing the grid point force results  @return  Ask Iteration 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::BaseIteration * GetIteration
            (
            );
            /** The iteration containing the grid point force results 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetIteration
            (
                NXOpen::CAE::BaseIteration * iteration /** Set Iteration */
            );
            /** The view where graphics will be displayed  @return  Ask View 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: int GetPostview
            (
            );
            /** The view where graphics will be displayed 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetPostview
            (
                int postviewId /** Set View */
            );
            /** The free body elements  @return  Ask Elements 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: std::vector<int> GetElements
            (
            );
            /** The free body elements 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetElements
            (
                const std::vector<int> & elements /** Set Elements */
            );
            /** The interface nodes  @return  Ask Nodes 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: std::vector<int> GetNodes
            (
            );
            /** The interface nodes 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetNodes
            (
                const std::vector<int> & nodes /** Set Nodes */
            );
            /** The location definition method  @return  Ask Method 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::FreeBodyResultsBuilder::LocationMethod GetLocationMethod
            (
            );
            /** The location definition method 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetLocationMethod
            (
                NXOpen::CAE::FreeBodyResultsBuilder::LocationMethod method /** Set Method */
            );
            /** The location definition method by node id  @return  Ask Node ID 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: int GetLocationId
            (
            );
            /** The location definition method by node id 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetLocationId
            (
                int nodeId /** Set Node ID */
            );
            /** The location definition method by coordinates  @return  Ask Coordinates 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::Point3d GetLocationCoords
            (
            );
            /** The location definition method by coordinates 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetLocationCoords
            (
                const NXOpen::Point3d & coordinates /** Set Coordinates */
            );
            /** The location definition method by coordinate system origin  @return  Ask Coordinate System 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: int GetLocationCsys
            (
            );
            /** The location definition method by coordinate system origin 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetLocationCsys
            (
                int id /** Set Node Coordinate System */
            );
            /** The source for the location coordinate system  @return  Ask Source 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::Result::CoordinateSystemSource GetLocationCsysSource
            (
            );
            /** The source for the location coordinate system 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetLocationCsysSource
            (
                NXOpen::CAE::Result::CoordinateSystemSource source /** Set Source */
            );
            /** The reference coordinate system  @return  Ask Coordinate System 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::Result::CoordinateSystem GetReferenceCsys
            (
            );
            /** The reference coordinate system 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetReferenceCsys
            (
                NXOpen::CAE::Result::CoordinateSystem csys /** Set Coordinate System */
            );
            /** The selected reference coordinate system  @return  Ask Coordinate System 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: int GetSelectedReferenceCsys
            (
            );
            /** The selected reference coordinate system 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetSelectedReferenceCsys
            (
                int id /** Set Coordinate System */
            );
            /** The source for the selected reference coordinate system  @return  Ask Source 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::Result::CoordinateSystemSource GetSelectedReferenceCsysSource
            (
            );
            /** The source for the selected reference coordinate system 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetSelectedReferenceCsysSource
            (
                NXOpen::CAE::Result::CoordinateSystemSource source /** Set Source */
            );
            /** Print Output  @return  Ask Print 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: bool GetPrintOutput
            (
            );
            /** Print Output 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetPrintOutput
            (
                bool print /** Set Print */
            );
            /** Display Force  @return  Ask Display 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: bool GetDisplayForce
            (
            );
            /** Display Force 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetDisplayForce
            (
                bool display /** Set Display */
            );
            /** Display Moment  @return  Ask Moment 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: bool GetDisplayMoment
            (
            );
            /** Display Moment 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetDisplayMoment
            (
                bool display /** Set Moment */
            );
            /** Force vector display  @return  Ask force vector display 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::FreeBodyResultsBuilder::VectorDisplay GetForceVectorDisplay
            (
            );
            /** Force vector display 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetForceVectorDisplay
            (
                NXOpen::CAE::FreeBodyResultsBuilder::VectorDisplay vectorDisplay /** Set force vector display */
            );
            /** Moment vector display  @return  Ask moment vector display 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::FreeBodyResultsBuilder::VectorDisplay GetMomentVectorDisplay
            (
            );
            /** Moment vector display 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetMomentVectorDisplay
            (
                NXOpen::CAE::FreeBodyResultsBuilder::VectorDisplay vectorDisplay /** Set moment vector display */
            );
            /** Force Color  @return  Ask Color 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::NXColor * GetForceColor
            (
            );
            /** Force Color 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetForceColor
            (
                NXOpen::NXColor * display /** Set Color */
            );
            /** Moment Color  @return  Ask Color 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::NXColor * GetMomentColor
            (
            );
            /** Moment Color 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetMomentColor
            (
                NXOpen::NXColor * color /** Set Color */
            );
            /** Output Units  @return  Ask Units 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::FreeBodyResultsBuilder::OutputUnits GetOutputUnits
            (
            );
            /** Output Units 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetOutputUnits
            (
                NXOpen::CAE::FreeBodyResultsBuilder::OutputUnits units /** Set Units */
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