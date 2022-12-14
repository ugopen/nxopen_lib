#ifndef NXOpen_ROUTING_FORMBOARDFRAMECGM_HXX_INCLUDED
#define NXOpen_ROUTING_FORMBOARDFRAMECGM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_FormboardFrameCGM.ja
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
#include <NXOpen/Routing_FormboardFrame.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class FormboardFrameCGM;
    }
    namespace Routing
    {
        class FormboardFrame;
    }
    namespace Routing
    {
        class _FormboardFrameCGMBuilder;
        class FormboardFrameCGMImpl;
        /**Represents a Formboard Frame CGM. */
        class NXOPENCPPEXPORT  FormboardFrameCGM : public Routing::FormboardFrame
        {
            private: FormboardFrameCGMImpl * m_formboardframecgm_impl;
            private: friend class  _FormboardFrameCGMBuilder;
            protected: FormboardFrameCGM();
            public: ~FormboardFrameCGM();
        };
    }
}
#undef EXPORTLIBRARY
#endif
