#ifndef NXOpen_DRAWINGS_BASESTEPPEDSECTIONLINE_HXX_INCLUDED
#define NXOpen_DRAWINGS_BASESTEPPEDSECTIONLINE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_BaseSteppedSectionLine.ja
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
#include <NXOpen/Drawings_SectionLine.hxx>
#include <NXOpen/libnxopencpp_drawings_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drawings
    {
        class BaseSteppedSectionLine;
    }
    namespace Drawings
    {
        class SectionLine;
    }
    namespace Drawings
    {
        class _BaseSteppedSectionLineBuilder;
        class BaseSteppedSectionLineImpl;
        /** Represents a Base Stepped Section Line. <br> This is an abstract class that cannot be instantiated  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  BaseSteppedSectionLine : public NXOpen::Drawings::SectionLine
        {
            private: BaseSteppedSectionLineImpl * m_basesteppedsectionline_impl;
            private: friend class  _BaseSteppedSectionLineBuilder;
            protected: BaseSteppedSectionLine();
            public: ~BaseSteppedSectionLine();
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