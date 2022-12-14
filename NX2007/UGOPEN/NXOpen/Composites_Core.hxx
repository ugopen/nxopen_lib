#ifndef NXOpen_COMPOSITES_CORE_HXX_INCLUDED
#define NXOpen_COMPOSITES_CORE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Composites_Core.ja
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
#include <NXOpen/Composites_Base.hxx>
#include <NXOpen/libcompositesopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Composites
    {
        class Core;
    }
    namespace Composites
    {
        class Base;
    }
    namespace Composites
    {
        class _CoreBuilder;
        class CoreImpl;

        /// \cond NX_NO_DOC 
        /** Represents a solid piece of material to be placed within a composite part  <br> To create or edit an instance of this class, use @link NXOpen::Composites::CoreBuilder  NXOpen::Composites::CoreBuilder @endlink  <br> 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class COMPOSITESOPENCPPEXPORT  Core : public NXOpen::Composites::Base
        {
            private: CoreImpl * m_core_impl;
            private: friend class  _CoreBuilder;
            protected: Core();
            public: ~Core();
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
