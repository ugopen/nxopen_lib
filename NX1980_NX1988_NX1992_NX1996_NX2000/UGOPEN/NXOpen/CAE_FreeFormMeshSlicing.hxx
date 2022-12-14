#ifndef NXOpen_CAE_FREEFORMMESHSLICING_HXX_INCLUDED
#define NXOpen_CAE_FREEFORMMESHSLICING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FreeFormMeshSlicing.ja
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
#include <NXOpen/CAE_MeshSlicingData.hxx>
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
        class FreeFormMeshSlicing;
    }
    namespace CAE
    {
        class MeshSlicingData;
    }
    namespace Facet
    {
        class FacetedBody;
    }
    namespace CAE
    {
        class _FreeFormMeshSlicingBuilder;
        class FreeFormMeshSlicingImpl;

        /// \cond NX_NO_DOC 
        /**  @brief  Represents a 'MeshSlicingData' sub object, Free Form Mesh Slicing 

           <br> This is a sub object of Mesh Slicing Data  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  FreeFormMeshSlicing : public NXOpen::CAE::MeshSlicingData
        {
            private: FreeFormMeshSlicingImpl * m_freeformmeshslicing_impl;
            private: friend class  _FreeFormMeshSlicingBuilder;
            protected: FreeFormMeshSlicing();
            public: ~FreeFormMeshSlicing();

            /// \cond NX_NO_DOC 
            /** Get Freeform Surfaces 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void GetSurfaces
            (
                std::vector<NXOpen::Facet::FacetedBody *> & sufaces /** sufaces */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Set Freeform Surfaces 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetSurfaces
            (
                const std::vector<NXOpen::Facet::FacetedBody *> & surfaces /** surfaces */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get Maximum Distance To Mesh Boundaries 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: double GetMaximumDistanceToMeshBoundaries
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Set Maximum Distance To Mesh Boundaries 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMaximumDistanceToMeshBoundaries
            (
                double maximumDistanceToMeshBoundaries /** maximum distance to mesh boundaries */ 
            );

            /// \endcond 
        };

        /// \endcond 
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
