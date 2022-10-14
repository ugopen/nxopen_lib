#ifndef NXOpen_CAE_DURSPECIALISTDURWELDBUILDER_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTDURWELDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistDurWeldBuilder.ja
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
#include <NXOpen/CAE_Connections_IConnection.hxx>
#include <NXOpen/CAE_DurSpecialistDurWeldSet.hxx>
#include <NXOpen/CAE_DurSpecialistSimulationObjectTable.hxx>
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
        class DurSpecialistDurWeldBuilder;
    }
    class Builder;
    namespace CAE
    {
        namespace Connections
        {
            class IConnection;
        }
    }
    namespace CAE
    {
        class DurSpecialistDurWeldSet;
    }
    namespace CAE
    {
        class DurSpecialistSimulationObjectTable;
    }
    namespace CAE
    {
        class _DurSpecialistDurWeldBuilderBuilder;
        class DurSpecialistDurWeldBuilderImpl;
        /** Represents the abstract builder class for all @link CAE::DurSpecialistDurWeld CAE::DurSpecialistDurWeld@endlink .  <br> This is an abstract class, and cannot be created.  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistDurWeldBuilder : public NXOpen::Builder
        {
            private: DurSpecialistDurWeldBuilderImpl * m_durspecialistdurweldbuilder_impl;
            private: friend class  _DurSpecialistDurWeldBuilderBuilder;
            protected: DurSpecialistDurWeldBuilder();
            public: ~DurSpecialistDurWeldBuilder();
            /**Returns  the name 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXString NameString
            (
            );
            /**Sets  the name 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetNameString
            (
                const NXString & nameString /** namestring */ 
            );
            /**Sets  the name 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void SetNameString
            (
                const char * nameString /** namestring */ 
            );
            /** Returns the description multi string 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetDescriptionMultiString
            (
            );
            /** Sets the description multi string 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetDescriptionMultiString
            (
                const std::vector<NXString> & descriptionMultiString /** descriptionmultistring */ 
            );
            /**Returns  the weld connection 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::Connections::IConnection * WeldConnection
            (
            );
            /**Sets  the weld connection 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetWeldConnection
            (
                NXOpen::CAE::Connections::IConnection * weldConnection /** weld connection to assign */
            );
            /**Returns  the recovery simulation object 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSimulationObjectTable * RecoverySimulationObject
            (
            );
            /**Sets  the recovery simulation object 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetRecoverySimulationObject
            (
                NXOpen::CAE::DurSpecialistSimulationObjectTable * recoverySimulationObject /** recovery simulation object to assign  */
            );
            /**Returns  the durability weld set 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistDurWeldSet * DurWeldSet
            (
            );
            /**Sets  the durability weld set 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetDurWeldSet
            (
                NXOpen::CAE::DurSpecialistDurWeldSet * durWeldSet /** set the weld set which the durability weld belongs to  */
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