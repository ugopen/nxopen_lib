#ifndef NXOpen_FALCON_CALCULATIONBUILDER_HXX_INCLUDED
#define NXOpen_FALCON_CALCULATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Falcon_CalculationBuilder.ja
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
#include <NXOpen/libnxopencpp_falcon_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Falcon
    {
        class CalculationBuilder;
    }
    class Builder;
    namespace Falcon
    {
        class _CalculationBuilderBuilder;
        class CalculationBuilderImpl;
        /** the Class for creating Calculation  <br> To create a new instance of this class, use @link NXOpen::Falcon::FalconManager::CreateCalculationBuilder  NXOpen::Falcon::FalconManager::CreateCalculationBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        CalculationType </term> <description> 
         
        Euclidean </description> </item> 

        </list> 

         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_FALCONEXPORT  CalculationBuilder : public NXOpen::Builder
        {
            /** This enum is providing  which calculation type to be performed*/
            public: enum CalculationTypeOption
            {
                CalculationTypeOptionEuclidean/** euclidean */ ,
                CalculationTypeOptionRectilinear/** rectilinear */ 
            };

            private: CalculationBuilderImpl * m_calculationbuilder_impl;
            private: friend class  _CalculationBuilderBuilder;
            protected: CalculationBuilder();
            public: ~CalculationBuilder();
            /**Returns  the calculation type 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Falcon::CalculationBuilder::CalculationTypeOption CalculationType
            (
            );
            /**Sets  the calculation type 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetCalculationType
            (
                NXOpen::Falcon::CalculationBuilder::CalculationTypeOption calculationType /** calculationtype */ 
            );
            /**Returns  the name of calculation
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXString CalculationName
            (
            );
            /**Sets  the name of calculation
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetCalculationName
            (
                const NXString & calculationName /** calculationname */ 
            );
            /**Sets  the name of calculation
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            void SetCalculationName
            (
                const char * calculationName /** calculationname */ 
            );
            /**Returns  the calculate activity point utilization flag 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool CalculateActivityPointUtilization
            (
            );
            /**Sets  the calculate activity point utilization flag 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetCalculateActivityPointUtilization
            (
                bool calculateUtilization /** calculateutilization */ 
            );
            /**Returns  the calculate container stacking unstacking flag 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool CalculateContainerStacking
            (
            );
            /**Sets  the calculate container stacking unstacking flag 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetCalculateContainerStacking
            (
                bool calculateStacking /** calculatestacking */ 
            );
            /**Returns  the use scrap rate flag 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseScrapRate
            (
            );
            /**Sets  the use scrap rate flag 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetUseScrapRate
            (
                bool useScrapRate /** usescraprate */ 
            );
            /**Returns  the create calculation log file flag 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool CreateCalculationLog
            (
            );
            /**Sets  the create calculation log file flag 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetCreateCalculationLog
            (
                bool createLog /** createlog */ 
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
