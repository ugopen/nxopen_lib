#ifndef NXOpen_DRAWINGS_VIEWBREAK_HXX_INCLUDED
#define NXOpen_DRAWINGS_VIEWBREAK_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ViewBreak.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class ViewBreak;
    }
    namespace Drawings
    {
        class _ViewBreakBuilder;
        class ViewBreakImpl;
        /**  ViewBreak - defines the portion of a view that gets hidden to
                 produce a broken view  <br> use builder once available <br> */
        class NXOPENCPPEXPORT  ViewBreak : public TaggedObject
        {
            private: ViewBreakImpl * m_viewbreak_impl;
            private: friend class  _ViewBreakBuilder;
            protected: ViewBreak();
            public: ~ViewBreak();
        };
    }
}
#undef EXPORTLIBRARY
#endif