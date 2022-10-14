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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAE_MeshPointOnFaceBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /**
            Represents a @link CAE::MeshPointOnFaceBuilder CAE::MeshPointOnFaceBuilder@endlink 
             <br> To create a new instance of this class, use @link CAE::MeshPointCollection::CreateMeshpointOnFaceBuilder CAE::MeshPointCollection::CreateMeshpointOnFaceBuilder@endlink  <br> */
        class NXOPENCPPEXPORT MeshPointOnFaceBuilder : public Builder
        {
            private: friend class  _MeshPointOnFaceBuilderBuilder;
            protected: MeshPointOnFaceBuilder();
            /**Returns  the node  <br> License requirements : None */
            public: NXOpen::SelectIParameterizedSurfaceList * Face
            (
            );
            /**Returns  the u parameter  <br> License requirements : None */
            public: NXOpen::Expression * UParameter
            (
            );
            /**Returns  the v parameter  <br> License requirements : None */
            public: NXOpen::Expression * VParameter
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif