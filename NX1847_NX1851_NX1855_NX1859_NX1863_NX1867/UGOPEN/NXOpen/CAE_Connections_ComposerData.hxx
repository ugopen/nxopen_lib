#ifndef NXOpen_CAE_CONNECTIONS_COMPOSERDATA_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_COMPOSERDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_ComposerData.ja
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
#include <NXOpen/CAE_Connections_ComponentData.hxx>
#include <NXOpen/CAE_Connections_ConnectionData.hxx>
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
        namespace Connections
        {
            class ComposerData;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class ComponentData;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class ConnectionData;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class _ComposerDataBuilder;
            class ComposerDataImpl;
            /** Composer connection. Use this interface to set/get/create properties and set/get parameters of the composer.  
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ComposerData : public NXOpen::TaggedObject
            {
                private: ComposerDataImpl * m_composerdata_impl;
                private: friend class  _ComposerDataBuilder;
                protected: ComposerData();
                public: ~ComposerData();
                /** Create component. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: NXOpen::CAE::Connections::ComponentData * CreateComponent
                (
                );
                /** Gets components. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::CAE::Connections::ComponentData *> GetComponents
                (
                );
                /** Sets components. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: void SetComponents
                (
                    const std::vector<NXOpen::CAE::Connections::ComponentData *> & components /** components */ 
                );
                /** Create component. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: NXOpen::CAE::Connections::ConnectionData * CreateConnection
                (
                );
                /** Gets connections 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::CAE::Connections::ConnectionData *> GetConnections
                (
                );
                /** Sets connections 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: void SetConnections
                (
                    const std::vector<NXOpen::CAE::Connections::ConnectionData *> & connections /** connections */ 
                );
                /**Returns  the assembly name  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString AssemblyName
                (
                );
                /**Sets  the assembly name  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: void SetAssemblyName
                (
                    const NXString & assemblyName /** assemblyname */ 
                );
                /**Sets  the assembly name  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                void SetAssemblyName
                (
                    const char * assemblyName /** assemblyname */ 
                );
                /**Returns  the input file direction  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString InputFileDir
                (
                );
                /**Sets  the input file direction  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: void SetInputFileDir
                (
                    const NXString & inputFileDir /** inputfiledir */ 
                );
                /**Sets  the input file direction  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                void SetInputFileDir
                (
                    const char * inputFileDir /** inputfiledir */ 
                );
                /**Returns  the output file direction  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString OutputFileDir
                (
                );
                /**Sets  the output file direction  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: void SetOutputFileDir
                (
                    const NXString & outputFileDir /** outputfiledir */ 
                );
                /**Sets  the output file direction  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                void SetOutputFileDir
                (
                    const char * outputFileDir /** outputfiledir */ 
                );
                /**Returns  the material file direction  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString MaterialDBDir
                (
                );
                /**Sets  the material file direction  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: void SetMaterialDBDir
                (
                    const NXString & materialDBDir /** materialdbdir */ 
                );
                /**Sets  the material file direction  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                void SetMaterialDBDir
                (
                    const char * materialDBDir /** materialdbdir */ 
                );
                /**Returns  the start node and element number  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: int StartNumNodeAndElement
                (
                );
                /**Sets  the start node and element number  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: void SetStartNumNodeAndElement
                (
                    int startNumNodeAndElement /** startnumnodeandelement */ 
                );
                /**Returns  the start properties number  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: int StartNumProperties
                (
                );
                /**Sets  the start properties number  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: void SetStartNumProperties
                (
                    int startNumProperties /** startnumproperties */ 
                );
                /**Returns  the start axis number  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: int StartNumAxisSystems
                (
                );
                /**Sets  the start axis number  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: void SetStartNumAxisSystems
                (
                    int startNumAxisSystems /** startnumaxissystems */ 
                );
            };
        }
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
