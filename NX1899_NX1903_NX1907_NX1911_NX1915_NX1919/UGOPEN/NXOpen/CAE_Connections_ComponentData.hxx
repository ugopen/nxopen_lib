#ifndef NXOpen_CAE_CONNECTIONS_COMPONENTDATA_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_COMPONENTDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_ComponentData.ja
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
        namespace Connections
        {
            class ComponentData;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class _ComponentDataBuilder;
            class ComponentDataImpl;
            /** Composer connection. Use this interface to set/get properties and parameters of the spot weld connection.  
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ComponentData : public NXOpen::TaggedObject
            {
                private: ComponentDataImpl * m_componentdata_impl;
                private: friend class  _ComponentDataBuilder;
                protected: ComponentData();
                public: ~ComponentData();
                /**Returns  the component name  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString ComponentName
                (
                );
                /**Sets  the component name  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: void SetComponentName
                (
                    const NXString & name /** name */ 
                );
                /**Sets  the component name  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                void SetComponentName
                (
                    const char * name /** name */ 
                );
                /**Returns  the file path  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString FilePath
                (
                );
                /**Sets  the file path  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: void SetFilePath
                (
                    const NXString & path /** path */ 
                );
                /**Sets  the file path  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                void SetFilePath
                (
                    const char * path /** path */ 
                );
                /**Returns  the mesh path  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString MeshPath
                (
                );
                /**Sets  the mesh path  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: void SetMeshPath
                (
                    const NXString & meshPath /** meshpath */ 
                );
                /**Sets  the mesh path  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                void SetMeshPath
                (
                    const char * meshPath /** meshpath */ 
                );
                /**Returns  the mass path 
                 <br>  @deprecated Deprecated in NX1847.0.0.  Component Mass Trim functionality has been deprecated without replacement. <br>  

                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Component Mass Trim functionality has been deprecated without replacement.") NXString MassPath
                (
                );
                /**Sets  the mass path 
                 <br>  @deprecated Deprecated in NX1847.0.0.  Component Mass Trim functionality has been deprecated without replacement. <br>  

                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Component Mass Trim functionality has been deprecated without replacement.") void SetMassPath
                (
                    const NXString & massPath /** masspath */ 
                );
                /**Sets  the mass path 
                 <br>  @deprecated Deprecated in NX1847.0.0.  Component Mass Trim functionality has been deprecated without replacement. <br>  

                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                void SetMassPath
                (
                    const char * massPath /** masspath */ 
                );
                /**Returns  the connection points path  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString ConnectionPointsPath
                (
                );
                /**Sets  the connection points path  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: void SetConnectionPointsPath
                (
                    const NXString & connectionPointsPath /** connectionpointspath */ 
                );
                /**Sets  the connection points path  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                void SetConnectionPointsPath
                (
                    const char * connectionPointsPath /** connectionpointspath */ 
                );
                /**Returns  the imported connection points path  
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString ImportedConnectionPointsPath
                (
                );
                /**Sets  the imported connection points path  
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                public: void SetImportedConnectionPointsPath
                (
                    const NXString & importedConnPointsPath /** importedconnpointspath */ 
                );
                /**Sets  the imported connection points path  
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : sc_nv_comp (" Simcenter NVH Composer") OR sc_gso_comp (" Simcenter NVH Composer") */
                void SetImportedConnectionPointsPath
                (
                    const char * importedConnPointsPath /** importedconnpointspath */ 
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
