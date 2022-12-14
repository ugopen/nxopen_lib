#ifndef NXOpen_PCBEXCHANGE_IDXCOMPAREBUILDER_HXX_INCLUDED
#define NXOpen_PCBEXCHANGE_IDXCOMPAREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PcbExchange_IdxCompareBuilder.ja
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
#include <NXOpen/libnxopencpp_pcbexchange_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PcbExchange
    {
        class IdxCompareBuilder;
    }
    class Builder;
    namespace PcbExchange
    {
        class _IdxCompareBuilderBuilder;
        class IdxCompareBuilderImpl;
        /** Represents a @link NXOpen::PcbExchange::IdxCompareBuilder NXOpen::PcbExchange::IdxCompareBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateIdxCompareBuilder  NXOpen::PcbExchange::Manager::CreateIdxCompareBuilder @endlink  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_PCBEXCHANGEEXPORT  IdxCompareBuilder : public NXOpen::Builder
        {
            /** This enum defines the type of source model. */
            public: enum SourceTypeEnum
            {
                SourceTypeEnumNx/** nx */ ,
                SourceTypeEnumIdx/** idx */ 
            };

            private: IdxCompareBuilderImpl * m_idxcomparebuilder_impl;
            private: friend class  _IdxCompareBuilderBuilder;
            protected: IdxCompareBuilder();
            public: ~IdxCompareBuilder();
            /**Returns  the type of source model 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PcbExchange::IdxCompareBuilder::SourceTypeEnum SourceType
            (
            );
            /**Sets  the type of source model 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetSourceType
            (
                NXOpen::PcbExchange::IdxCompareBuilder::SourceTypeEnum sourceType /** sourcetype */ 
            );
            /**Returns  the Source File 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString SourceFile
            (
            );
            /**Sets  the Source File 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetSourceFile
            (
                const NXString & sourceFile /** sourcefile */ 
            );
            /**Sets  the Source File 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            void SetSourceFile
            (
                const char * sourceFile /** sourcefile */ 
            );
            /**Returns  the Target File 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString TargetFile
            (
            );
            /**Sets  the Target File 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetTargetFile
            (
                const NXString & targetFile /** targetfile */ 
            );
            /**Sets  the Target File 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            void SetTargetFile
            (
                const char * targetFile /** targetfile */ 
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
