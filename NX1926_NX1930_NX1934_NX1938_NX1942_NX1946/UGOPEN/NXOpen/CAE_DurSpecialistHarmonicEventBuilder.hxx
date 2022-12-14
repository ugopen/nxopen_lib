#ifndef NXOpen_CAE_DURSPECIALISTHARMONICEVENTBUILDER_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTHARMONICEVENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistHarmonicEventBuilder.ja
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
#include <NXOpen/CAE_DurSpecialistLoadLengthBuilder.hxx>
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
        class DurSpecialistHarmonicEventBuilder;
    }
    class Builder;
    namespace CAE
    {
        class DurSpecialistLoadLengthBuilder;
    }
    class Expression;
    class NXObject;
    namespace CAE
    {
        class _DurSpecialistHarmonicEventBuilderBuilder;
        class DurSpecialistHarmonicEventBuilderImpl;
        /** Represents a @link NXOpen::CAE::DurSpecialistHarmonicEvent NXOpen::CAE::DurSpecialistHarmonicEvent@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::CAE::DurSpecialistEventCollection::CreateHarmonicEventBuilder  NXOpen::CAE::DurSpecialistEventCollection::CreateHarmonicEventBuilder @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistHarmonicEventBuilder : public NXOpen::Builder
        {
            private: DurSpecialistHarmonicEventBuilderImpl * m_durspecialistharmoniceventbuilder_impl;
            private: friend class  _DurSpecialistHarmonicEventBuilderBuilder;
            protected: DurSpecialistHarmonicEventBuilder();
            public: ~DurSpecialistHarmonicEventBuilder();
            /**Returns  the name. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns  the description. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Description
            (
            );
            /**Sets  the description. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetDescription
            (
                const NXString & description /** description */ 
            );
            /**Sets  the description. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void SetDescription
            (
                const char * description /** description */ 
            );
            /**Returns  the load length. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistLoadLengthBuilder * LoadLength
            (
            );
            /**Returns  the harmonic data source. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * DataSource
            (
            );
            /**Sets  the harmonic data source. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetDataSource
            (
                NXOpen::NXObject * theDataSource /** thedatasource */ 
            );
            /**Returns  the scaling factor. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Scaling
            (
            );
            /**Sets  the scaling factor. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetScaling
            (
                NXOpen::Expression * scalingTag /** scalingtag */ 
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
