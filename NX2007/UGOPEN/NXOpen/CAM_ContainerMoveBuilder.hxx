#ifndef NXOpen_CAM_CONTAINERMOVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_CONTAINERMOVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ContainerMoveBuilder.ja
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
#include <NXOpen/CAM_MoveBuilder.hxx>
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class ContainerMoveBuilder;
    }
    namespace CAM
    {
        class MoveBuilder;
    }
    namespace CAM
    {
        class _ContainerMoveBuilderBuilder;
        class ContainerMoveBuilderImpl;

        /// \cond NX_NO_DOC 
        /** Represents the container move  <br> To create a new instance of this class, use @link NXOpen::CAM::MoveCollection::CreateContainerMoveBuilder  NXOpen::CAM::MoveCollection::CreateContainerMoveBuilder @endlink  <br> 
         <br>  Created in NX11.0.2.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ContainerMoveBuilder : public NXOpen::CAM::MoveBuilder
        {
            private: ContainerMoveBuilderImpl * m_containermovebuilder_impl;
            private: friend class  _ContainerMoveBuilderBuilder;
            protected: ContainerMoveBuilder();
            public: ~ContainerMoveBuilder();
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