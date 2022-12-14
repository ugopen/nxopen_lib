#ifndef NXOpen_CAE_SHELL2SOLIDBUILDER_HXX_INCLUDED
#define NXOpen_CAE_SHELL2SOLIDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Shell2SolidBuilder.ja
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
#include <NXOpen/CAE_ElementTypeBuilder.hxx>
#include <NXOpen/CAE_Shell2SolidBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class Shell2SolidBuilder;
    }
    class Builder;
    namespace CAE
    {
        class ElementTypeBuilder;
    }
    class SelectDisplayableObjectList;
    namespace CAE
    {
        class _Shell2SolidBuilderBuilder;
        class Shell2SolidBuilderImpl;
        /** Represents 3D Tet Mesh
             *  Used to create a @link CAE::Mesh3d CAE::Mesh3d@endlink 
             <br> To create a new instance of this class, use @link CAE::MeshManager::CreateShell2solidBuilder CAE::MeshManager::CreateShell2solidBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  Shell2SolidBuilder : public Builder
        {
            private: Shell2SolidBuilderImpl * m_shell2solidbuilder_impl;
            private: friend class  _Shell2SolidBuilderBuilder;
            protected: Shell2SolidBuilder();
            public: ~Shell2SolidBuilder();
            /**Returns  the selection objects  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::SelectDisplayableObjectList * SelectionList
            (
            );
            /**Returns  the element type builder.   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementTypeBuilder * ElementType
            (
            );
            /**Returns  the mesh size variation  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: double MeshSizeVariation
            (
            );
            /**Sets  the mesh size variation  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMeshSizeVariation
            (
                double dSizeVaration /** dsizevaration */ 
            );
            /**Returns  the mesh size variation  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: bool FillHolesOption
            (
            );
            /**Sets  the mesh size variation  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetFillHolesOption
            (
                bool fFillHoles /** ffillholes */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
