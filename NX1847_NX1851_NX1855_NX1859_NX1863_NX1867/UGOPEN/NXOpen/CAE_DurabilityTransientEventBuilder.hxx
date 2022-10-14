#ifndef NXOpen_CAE_DURABILITYTRANSIENTEVENTBUILDER_HXX_INCLUDED
#define NXOpen_CAE_DURABILITYTRANSIENTEVENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurabilityTransientEventBuilder.ja
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
#include <NXOpen/CAE_DurabilityDataControlBuilder.hxx>
#include <NXOpen/CAE_DurabilityEventBuilder.hxx>
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
        class DurabilityTransientEventBuilder;
    }
    namespace CAE
    {
        class DurabilityDataControlBuilder;
    }
    namespace CAE
    {
        class DurabilityEventBuilder;
    }
    class NXObject;
    namespace CAE
    {
        class _DurabilityTransientEventBuilderBuilder;
        class DurabilityTransientEventBuilderImpl;
        /** Represents the builder for the transient durability event.  <br> There is no kf creator for this.  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurabilityTransientEventBuilder : public NXOpen::CAE::DurabilityEventBuilder
        {
            private: DurabilityTransientEventBuilderImpl * m_durabilitytransienteventbuilder_impl;
            private: friend class  _DurabilityTransientEventBuilderBuilder;
            protected: DurabilityTransientEventBuilder();
            public: ~DurabilityTransientEventBuilder();
            /**Returns  the subcase index. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: int Subcase
            (
            );
            /**Sets  the subcase index. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetSubcase
            (
                int subcase /** subcase */ 
            );
            /**Returns  the data control. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: NXOpen::CAE::DurabilityDataControlBuilder * DataControl
            (
            );
            /**Returns  the sort2 access. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool Sort2Access
            (
            );
            /**Sets  the sort2 access. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetSort2Access
            (
                bool sort2Access /** sort2access */ 
            );
            /**Returns  the mdfFileName. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: NXString MdfFileName
            (
            );
            /**Sets  the mdfFileName. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetMdfFileName
            (
                const NXString & filename /** filename */ 
            );
            /**Sets  the mdfFileName. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            void SetMdfFileName
            (
                const char * filename /** filename */ 
            );
            /**Returns  the static offset for the event.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: NXOpen::NXObject * StaticOffset
            (
            );
            /**Sets  the static offset for the event.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetStaticOffset
            (
                NXOpen::NXObject * staticOffset /** staticoffset */ 
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