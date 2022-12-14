#ifndef NXOpen_ROUTING_FORMBOARDFRAMERECTANGLE_HXX_INCLUDED
#define NXOpen_ROUTING_FORMBOARDFRAMERECTANGLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_FormboardFrameRectangle.ja
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
        class FormboardFrameRectangle;
    }
    namespace Routing
    {
        class FormboardFrame;
    }
    namespace Routing
    {
        class _FormboardFrameRectangleBuilder;
        class FormboardFrameRectangleImpl;
        /**Represents a Formboard Frame Rectangle. */
        class NXOPENCPPEXPORT  FormboardFrameRectangle : public Routing::FormboardFrame
        {
            private: FormboardFrameRectangleImpl * m_formboardframerectangle_impl;
            private: friend class  _FormboardFrameRectangleBuilder;
            protected: FormboardFrameRectangle();
            public: ~FormboardFrameRectangle();
        };
    }
}
#undef EXPORTLIBRARY
#endif
