#ifndef NXOpen_CAE_DURSPECIALISTTRANSIENTEVENTBUILDER_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTTRANSIENTEVENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistTransientEventBuilder.ja
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
#include <NXOpen/CAE_DurSpecialistDataSources.hxx>
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
        class DurSpecialistTransientEventBuilder;
    }
    class Builder;
    namespace CAE
    {
        class DurSpecialistDataSources;
    }
    namespace CAE
    {
        class DurSpecialistTemperatureSource;
    }
    namespace CAE
    {
        class _DurSpecialistTransientEventBuilderBuilder;
        class DurSpecialistTransientEventBuilderImpl;
        /** Represents a @link NXOpen::CAE::DurSpecialistTransientEvent NXOpen::CAE::DurSpecialistTransientEvent@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::CAE::DurSpecialistEventCollection::CreateTransientEventBuilder  NXOpen::CAE::DurSpecialistEventCollection::CreateTransientEventBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistTransientEventBuilder : public NXOpen::Builder
        {
            /** Type of move operations for the increment list */
            public: enum MoveOperation
            {
                MoveOperationReverseOrder/** Reverse order of selected increments */,
                MoveOperationMoveUp/** Move selected increments up */,
                MoveOperationMoveDown/** Move selected increments down */
            };

            /** Type of edit operations for the increments in the list */
            public: enum EditOperation
            {
                EditOperationActive/** Set Active property for selected increments */,
                EditOperationVisible/** Set Visible property for selected increments */,
                EditOperationOutput/** Set Output (for solver use) property for selected increments */
            };

            /** The resolution strategy for overlapping groups */
            public: enum OverlapResolution
            {
                OverlapResolutionMaximum/** Use the maximum value */,
                OverlapResolutionMinimum/** Use the minimum value */,
                OverlapResolutionAverage/** Calculate the average value */
            };

            private: DurSpecialistTransientEventBuilderImpl * m_durspecialisttransienteventbuilder_impl;
            private: friend class  _DurSpecialistTransientEventBuilderBuilder;
            protected: DurSpecialistTransientEventBuilder();
            public: ~DurSpecialistTransientEventBuilder();
            /**Returns  the name. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns  the description. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Description
            (
            );
            /**Sets  the description. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetDescription
            (
                const NXString & description /** description */ 
            );
            /**Sets  the description. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void SetDescription
            (
                const char * description /** description */ 
            );
            /**Returns  the time increment. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: int TimeIncrement
            (
            );
            /**Sets  the time increment. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetTimeIncrement
            (
                int timeIncrement /** timeincrement */ 
            );
            /**Returns  the FE results. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistDataSources * FeResults
            (
            );
            /** Tag as output the transient increments selected for solver use. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void TagOutputTransientIncrements
            (
            );
            /** Move items of the transient increment list. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void MoveSelectedTransientSubcases
            (
                const std::vector<int> & subcaseToMoveIndices /** subcasetomoveindices */ ,
                NXOpen::CAE::DurSpecialistTransientEventBuilder::MoveOperation operation /** operation */ 
            );
            /** Edit items of the transient increment list. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void EditSelectedTransientIncrements
            (
                const std::vector<int> & incrementToEditIndices /** incrementtoeditindices */ ,
                const std::vector<int> & parentSubcaseIndices /** parentsubcaseindices */ ,
                NXOpen::CAE::DurSpecialistTransientEventBuilder::EditOperation operation /** operation */ ,
                bool value /** value */ 
            );
            /** Edit items scale of the transient increment list. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void EditSelectedTransientIncrementsScale
            (
                const std::vector<int> & incrementToEditIndices /** incrementtoeditindices */ ,
                const std::vector<int> & parentSubcaseIndices /** parentsubcaseindices */ ,
                const std::vector<double> & scales /** scale values*/
            );
            /** Give the number of transient increments.  @return  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: int GetNumTransientIncrements
            (
            );
            /**Returns  the case sensitive comparison. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: bool TemperatureSourceInherited
            (
            );
            /**Sets  the case sensitive comparison. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetTemperatureSourceInherited
            (
                bool temperatureSourceInherited /** temperaturesourceinherited */ 
            );
            /**Returns  the temperature data source. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistTemperatureSource * TemperatureSource
            (
            );
            /**Sets  the temperature data source. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetTemperatureSource
            (
                NXOpen::CAE::DurSpecialistTemperatureSource * theTemperatureSource /** thetemperaturesource */ 
            );
            /**Returns  the temperature date source overlap resolution. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistTransientEventBuilder::OverlapResolution TemperatureSourceOverlapResolution
            (
            );
            /**Sets  the temperature date source overlap resolution. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetTemperatureSourceOverlapResolution
            (
                NXOpen::CAE::DurSpecialistTransientEventBuilder::OverlapResolution temperatureSourceOverlapResolution /** temperaturesourceoverlapresolution */ 
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