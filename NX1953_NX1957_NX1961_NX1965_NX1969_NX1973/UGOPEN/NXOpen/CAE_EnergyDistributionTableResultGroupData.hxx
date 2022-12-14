#ifndef NXOpen_CAE_ENERGYDISTRIBUTIONTABLERESULTGROUPDATA_HXX_INCLUDED
#define NXOpen_CAE_ENERGYDISTRIBUTIONTABLERESULTGROUPDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_EnergyDistributionTableResultGroupData.ja
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
#include <NXOpen/CAE_EnergyDistributionTableResultPIDData.hxx>
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
        class EnergyDistributionTableResultGroupData;
    }
    namespace CAE
    {
        class EnergyDistributionTableResultPIDData;
    }
    namespace CAE
    {
        class _EnergyDistributionTableResultGroupDataBuilder;
        class EnergyDistributionTableResultGroupDataImpl;
        /** Retrieve Energy table group data calculation per PID and per group. <br> To obtain result data see @link CAE::EnergyDistributionTableBuilder CAE::EnergyDistributionTableBuilder@endlink .  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  EnergyDistributionTableResultGroupData : public NXOpen::TaggedObject
        {
            private: EnergyDistributionTableResultGroupDataImpl * m_energydistributiontableresultgroupdata_impl;
            private: friend class  _EnergyDistributionTableResultGroupDataBuilder;
            protected: EnergyDistributionTableResultGroupData();
            public: ~EnergyDistributionTableResultGroupData();
            /** Get energy result per PID. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::CAE::EnergyDistributionTableResultPIDData *> GetResultPIDDatas
            (
            );
            /**Returns  the group name  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Returns  the energy value (unit - Joule)
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: double Energy
            (
            );
            /**Returns  the number of elements in group  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: int Elements
            (
            );
            /**Returns  the group relative energy in percentage 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: double RelativeEnergyPercentage
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
