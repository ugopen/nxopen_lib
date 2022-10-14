#ifndef NXOpen_CAE_DURSPECIALISTDATASOURCES_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTDATASOURCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistDataSources.ja
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
        class DurSpecialistDataSources;
    }
    namespace CAE
    {
        class _DurSpecialistDataSourcesBuilder;
        class DurSpecialistDataSourcesImpl;

        /// \cond NX_NO_DOC 
        /** Represents a @link NXOpen::CAE::DurSpecialistDataSources NXOpen::CAE::DurSpecialistDataSources@endlink  
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistDataSources : public NXOpen::TaggedObject
        {
            /** the unit system */
            public: enum UnitSystem
            {
                UnitSystemImplicit/** use from file */,
                UnitSystemMillinewtonMillimeter/** mN mm kg */,
                UnitSystemNewtonMeter/** N m kg */,
                UnitSystemNewtonMillimeter/** N mm tonne */,
                UnitSystemCentinewtonCentimeter/** cN cm kg */,
                UnitSystemKgfMeter/** kgf m kgf-s^2/m */,
                UnitSystemKgfMillimeter/** kgf mm kgf-s^2/mm */,
                UnitSystemLbfFoot/** lbf ft slug */,
                UnitSystemLbfInch/** lbf in lbf-s^2/in */,
                UnitSystemPoundalFoot/** poundal ft lbm */
            };

            private: DurSpecialistDataSourcesImpl * m_durspecialistdatasources_impl;
            private: friend class  _DurSpecialistDataSourcesBuilder;
            protected: DurSpecialistDataSources();
            public: ~DurSpecialistDataSources();

            /// \cond NX_NO_DOC 
            /** Add a file  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: int AddDataSource
            (
                const NXString & fileName /** filename */ ,
                int driver /** driver */ 
            );
            /** Add a file  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            int AddDataSource
            (
                const char * fileName /** filename */ ,
                int driver /** driver */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Remove a file 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void RemoveDataSource
            (
                int fileIndex /** fileindex */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Opens the Information window. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void InformationWindow
            (
                int fileIndex /** fileindex */ 
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