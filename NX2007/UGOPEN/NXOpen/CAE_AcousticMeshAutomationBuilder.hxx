#ifndef NXOpen_CAE_ACOUSTICMESHAUTOMATIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_ACOUSTICMESHAUTOMATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AcousticMeshAutomationBuilder.ja
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
#include <NXOpen/CAE_ElementTypeBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class AcousticMeshAutomationBuilder;
    }
    class Builder;
    namespace CAE
    {
        class ElementTypeBuilder;
    }
    namespace CAE
    {
        class PropertyTable;
    }
    class Plane;
    class SelectDisplayableObjectList;
    namespace CAE
    {
        class _AcousticMeshAutomationBuilderBuilder;
        class AcousticMeshAutomationBuilderImpl;
        /**  
                Represents a @link CAE::AcousticMeshAutomationBuilder CAE::AcousticMeshAutomationBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::CAE::MeshManager::CreateAcousticMeshAutomationBuilder  NXOpen::CAE::MeshManager::CreateAcousticMeshAutomationBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  AcousticMeshAutomationBuilder : public NXOpen::Builder
        {
            private: AcousticMeshAutomationBuilderImpl * m_acousticmeshautomationbuilder_impl;
            private: friend class  _AcousticMeshAutomationBuilderBuilder;
            protected: AcousticMeshAutomationBuilder();
            public: ~AcousticMeshAutomationBuilder();
            /**Returns  the selection objects 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * SelectionList
            (
            );
            /**Returns  the element type builder.  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ElementTypeBuilder * SurfaceWrapElementType
            (
            );
            /**Returns  the element type builder.  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ElementTypeBuilder * Shell2SolidElementType
            (
            );
            /**Returns  the property table associated with the mesh. 
                        The property table contains the parameters needed for the generation
                        of the mesh.  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::PropertyTable * PropertyTable
            (
            );
            /** The creation of automatic element size
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling"), nx_adv_fluid_mod ("NX Advanced Fluid Modeling - Basic") OR sc_acou_meshing (" SC Acoustic Meshing") */
            public: void AutomaticElementSize
            (
            );
            /** The Infinite planes 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling"), nx_adv_fluid_mod ("NX Advanced Fluid Modeling - Basic") OR sc_acou_meshing (" SC Acoustic Meshing") */
            public: void SetInfinitePlanes
            (
                const std::vector<NXOpen::Plane *> & pPlaneTags /** pplanetags */ 
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