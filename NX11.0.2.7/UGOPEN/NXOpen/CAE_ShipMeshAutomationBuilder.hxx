#ifndef NXOpen_CAE_SHIPMESHAUTOMATIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_SHIPMESHAUTOMATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ShipMeshAutomationBuilder.ja
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
#include <NXOpen/CAE_ShipMeshAutomationBuilder.hxx>
#include <NXOpen/Expression.hxx>
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
        class ShipMeshAutomationBuilder;
    }
    class Builder;
    class Expression;
    namespace CAE
    {
        class _ShipMeshAutomationBuilderBuilder;
        class ShipMeshAutomationBuilderImpl;
        /** Represents Ship Mesh Automation
             *  Used to create a @link NXOpen::CAE::ShipMeshAutomation NXOpen::CAE::ShipMeshAutomation@endlink 
             <br> To create a new instance of this class, use @link NXOpen::CAE::MeshManager::CreateShipMeshAutomationBuilder  NXOpen::CAE::MeshManager::CreateShipMeshAutomationBuilder @endlink  <br> 
         <br>  Created in NX11.0.2.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ShipMeshAutomationBuilder : public NXOpen::Builder
        {
            /** the meshing method type */
            public: enum MeshingMethodType
            {
                MeshingMethodTypeSubdivision/** Subdivision*/,
                MeshingMethodTypePaver/** Paver */
            };

            private: ShipMeshAutomationBuilderImpl * m_shipmeshautomationbuilder_impl;
            private: friend class  _ShipMeshAutomationBuilderBuilder;
            protected: ShipMeshAutomationBuilder();
            public: ~ShipMeshAutomationBuilder();
            /**Returns  the method type of creating mesh elements 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling"), nx_ship_basic ("Ship Basic Design") */
            public: NXOpen::CAE::ShipMeshAutomationBuilder::MeshingMethodType MethodType
            (
            );
            /**Sets  the method type of creating mesh elements 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling"), nx_ship_basic ("Ship Basic Design") */
            public: void SetMethodType
            (
                NXOpen::CAE::ShipMeshAutomationBuilder::MeshingMethodType methodType /** methodtype */ 
            );
            /**Returns  the flag to indicate whether to use the default mesh element size which is evaluated automatically 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling"), nx_ship_basic ("Ship Basic Design") */
            public: bool DefaultElementSize
            (
            );
            /**Sets  the flag to indicate whether to use the default mesh element size which is evaluated automatically 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling"), nx_ship_basic ("Ship Basic Design") */
            public: void SetDefaultElementSize
            (
                bool fDefaultElementSize /** fdefaultelementsize */ 
            );
            /**Returns  the value of meshing element size 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling"), nx_ship_basic ("Ship Basic Design") */
            public: NXOpen::Expression * ElementSize
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
