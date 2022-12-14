#ifndef NXOpen_CAE_MESHPOINTONFACEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MESHPOINTONFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_MeshPointOnFaceBuilder.ja
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
#include <NXOpen/CAE_MeshPointOnFaceBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class MeshPointOnFaceBuilder;
    }
    class Builder;
    class Expression;
    class SelectIParameterizedSurfaceList;
    namespace CAE
    {
        class _MeshPointOnFaceBuilderBuilder;
        class MeshPointOnFaceBuilderImpl;
        /**
            Represents a @link CAE::MeshPointOnFaceBuilder CAE::MeshPointOnFaceBuilder@endlink 
             <br> To create a new instance of this class, use @link CAE::MeshPointCollection::CreateMeshpointOnFaceBuilder  CAE::MeshPointCollection::CreateMeshpointOnFaceBuilder @endlink  <br> 
         <br>  Created in NX5.0.2.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  MeshPointOnFaceBuilder : public Builder
        {
            private: MeshPointOnFaceBuilderImpl * m_meshpointonfacebuilder_impl;
            private: friend class  _MeshPointOnFaceBuilderBuilder;
            protected: MeshPointOnFaceBuilder();
            public: ~MeshPointOnFaceBuilder();
            /**Returns  the node 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectIParameterizedSurfaceList * Face
            (
            );
            /**Returns  the u parameter 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * UParameter
            (
            );
            /**Returns  the v parameter 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * VParameter
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
