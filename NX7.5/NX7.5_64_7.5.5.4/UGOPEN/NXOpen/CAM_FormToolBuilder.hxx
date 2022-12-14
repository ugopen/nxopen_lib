#ifndef NXOpen_CAM_FORMTOOLBUILDER_HXX_INCLUDED
#define NXOpen_CAM_FORMTOOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_FormToolBuilder.ja
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
#include <NXOpen/CAM_TurningToolBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class FormToolBuilder;
    }
    namespace CAM
    {
        class FormEdgesBuilder;
    }
    namespace CAM
    {
        class TurningToolBuilder;
    }
    namespace CAM
    {
        class _FormToolBuilderBuilder;
        class FormToolBuilderImpl;
        /** Represents a Form tool builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateFormToolBuilder CAM::NCGroupCollection::CreateFormToolBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  FormToolBuilder : public CAM::TurningToolBuilder
        {
            private: FormToolBuilderImpl * m_formtoolbuilder_impl;
            private: friend class  _FormToolBuilderBuilder;
            protected: FormToolBuilder();
            public: ~FormToolBuilder();
            /**Returns  the Form Edges Builder  <br> License requirements : None */
            public: NXOpen::CAM::FormEdgesBuilder * FormEdges
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
