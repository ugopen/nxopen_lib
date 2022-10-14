#ifndef NXOpen_CAE_RESULTSEXTRACTIONOUTPUTSETTINGS_HXX_INCLUDED
#define NXOpen_CAE_RESULTSEXTRACTIONOUTPUTSETTINGS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResultsExtractionOutputSettings.ja
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
#include <NXOpen/CAE_NumberFormat.hxx>
#include <NXOpen/CAE_ResultsManipulationErrorHandling.hxx>
#include <NXOpen/CAE_ResultsManipulationUnitsSystem.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class ResultsExtractionOutputSettings;
    }
    namespace CAE
    {
        class NumberFormat;
    }
    namespace CAE
    {
        class ResultsManipulationErrorHandling;
    }
    namespace CAE
    {
        class ResultsManipulationUnitsSystem;
    }
    namespace CAE
    {
        class _ResultsExtractionOutputSettingsBuilder;
        class ResultsExtractionOutputSettingsImpl;

        /// \cond NX_NO_DOC 
        /** Represents a @link NXOpen::CAE::ResultsExtractionOutputSettings NXOpen::CAE::ResultsExtractionOutputSettings@endlink   <br> This is a sub object  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ResultsExtractionOutputSettings : public NXOpen::TaggedObject
        {
            /** Results extraction output types */

            /// \cond NX_NO_DOC 
            public: enum Type
            {
                TypeExportToCSV/** export to csv */ ,
                TypeExportToSCD5/** Extracting to SCD5 file is under development with development feature toggle. */
            };


            /// \endcond 
            /** Results extraction output variable format */

            /// \cond NX_NO_DOC 
            public: enum VariableFormat
            {
                VariableFormatInRow/** variable is outputted in row */,
                VariableFormatInColumn/** variable is outputted in column */
            };


            /// \endcond 
            private: ResultsExtractionOutputSettingsImpl * m_resultsextractionoutputsettings_impl;
            private: friend class  _ResultsExtractionOutputSettingsBuilder;
            protected: ResultsExtractionOutputSettings();
            public: ~ResultsExtractionOutputSettings();

            /// \cond NX_NO_DOC 
            /**Returns  the output type for results extraction 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::ResultsExtractionOutputSettings::Type OutputType
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the output type for results extraction 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetOutputType
            (
                NXOpen::CAE::ResultsExtractionOutputSettings::Type outputType /** outputtype */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the output units system 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::ResultsManipulationUnitsSystem * UnitsSystem
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the output error handling 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::ResultsManipulationErrorHandling * ErrorHandling
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the output file name with full path when output type is set as exporting to file (Currently CSV only) 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXString FileName
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the output file name with full path when output type is set as exporting to file (Currently CSV only) 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetFileName
            (
                const NXString & fileName /** filename */ 
            );
            /**Sets  the output file name with full path when output type is set as exporting to file (Currently CSV only) 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            void SetFileName
            (
                const char * fileName /** filename */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Gets the output raw and column format when output type is set as exporting to file (Currently CSV only) 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void GetRowColumnFormat
            (
                NXOpen::CAE::ResultsExtractionOutputSettings::VariableFormat* entityFormat /** node or element */,
                NXOpen::CAE::ResultsExtractionOutputSettings::VariableFormat* loadcaseFormat /** including result file, subcase, iteration, sub iteration */,
                NXOpen::CAE::ResultsExtractionOutputSettings::VariableFormat* resulttypeFormat /** including result type, ply, layer, component, shell section, beam section */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Sets the output raw and column format when output type is set as exporting to file (Currently CSV only) 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetRowColumnFormat
            (
                NXOpen::CAE::ResultsExtractionOutputSettings::VariableFormat entityFormat /** node or element */,
                NXOpen::CAE::ResultsExtractionOutputSettings::VariableFormat loadcaseFormat /** including result file, subcase, iteration, sub iteration */,
                NXOpen::CAE::ResultsExtractionOutputSettings::VariableFormat resulttypeFormat /** including result type, ply, layer, component, shell section, beam section */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the number format option 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::NumberFormat * NumberFormat
            (
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