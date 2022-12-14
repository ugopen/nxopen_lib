#ifndef NXOpen_CAE_DURABILITYDATACONTROLBUILDER_HXX_INCLUDED
#define NXOpen_CAE_DURABILITYDATACONTROLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurabilityDataControlBuilder.ja
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
        class DurabilityDataControlBuilder;
    }
    class Expression;
    namespace CAE
    {
        class _DurabilityDataControlBuilderBuilder;
        class DurabilityDataControlBuilderImpl;
        /** Represents a builder class for the transient event data control.
                The data control helps choose the start and ending time for the
                transient loading. It also allows for a decimation order and a 
                peak valley tolerance control.
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurabilityDataControlBuilder : public NXOpen::TaggedObject
        {
            /** the time extents enum.*/
            public: enum TimeExtentsEnum
            {
                TimeExtentsEnumFromParentResult/** From Parent Result*/,
                TimeExtentsEnumSpecify/** Specify */
            };

            private: DurabilityDataControlBuilderImpl * m_durabilitydatacontrolbuilder_impl;
            private: friend class  _DurabilityDataControlBuilderBuilder;
            protected: DurabilityDataControlBuilder();
            public: ~DurabilityDataControlBuilder();
            /**Returns  the output start time. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OutputStartTime
            (
            );
            /**Returns  the output end time. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: NXOpen::Expression * OutputEndTime
            (
            );
            /**Returns  the decimation order. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: int DecimationOrder
            (
            );
            /**Sets  the decimation order. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetDecimationOrder
            (
                int decimationOrder /** decimationorder */ 
            );
            /**Returns  the peak valley tolerance. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double PeakValleyTolerance
            (
            );
            /**Sets  the peak valley tolerance. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetPeakValleyTolerance
            (
                double peakValleyTolerance /** peakvalleytolerance */ 
            );
            /**Returns  the time extents. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurabilityDataControlBuilder::TimeExtentsEnum TimeExtents
            (
            );
            /**Sets  the time extents. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetTimeExtents
            (
                NXOpen::CAE::DurabilityDataControlBuilder::TimeExtentsEnum timeExtents /** timeextents */ 
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
