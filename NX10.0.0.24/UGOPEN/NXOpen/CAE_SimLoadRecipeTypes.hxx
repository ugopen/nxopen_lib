#ifndef NXOpen_CAE_SIMLOADRECIPETYPES_HXX_INCLUDED
#define NXOpen_CAE_SIMLOADRECIPETYPES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimLoadRecipeTypes.ja
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
        class SimLoadRecipeTypes;
    }
    namespace CAE
    {
        class SimLoadRecipeTypesImpl;
        /**  @brief  The class handles the enum definitions needed by load recipes  

           <br> No Creator this holds an enum  shared by other classes  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SimLoadRecipeTypes
        {
            /** This enum defines the Data Type options */
            public: enum DataTypes
            {
                DataTypesTimeData/** Time Data */,
                DataTypesFrequencySpectra/** Frequency Spectra */,
                DataTypesWaterfallofTimeData/** Waterfall of Time Data */,
                DataTypesWaterfallofFrequencySpectra/** Waterfall of Frequency Spectra */,
                DataTypesOrderCut/** Order Cut */
            };

            /** This enum defines the types of Data Source handling */
            public: enum LoadConditionHandling
            {
                LoadConditionHandlingSingle/** Treat all sources as a single load condition */,
                LoadConditionHandlingPerDataSource/** Treat each source as a load condition */
            };

            private: SimLoadRecipeTypesImpl * m_simloadrecipetypes_impl;
            public: ~SimLoadRecipeTypes();
        }; //lint !e1712 default constructor not defined for class  

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
