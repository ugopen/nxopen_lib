#ifndef NXOpen_DRAWINGS_REVOLVEDSECTIONLINE_HXX_INCLUDED
#define NXOpen_DRAWINGS_REVOLVEDSECTIONLINE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_RevolvedSectionLine.ja
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
        class RevolvedSectionLine;
    }
    namespace Drawings
    {
        class SectionLine;
    }
    namespace Drawings
    {
        class _RevolvedSectionLineBuilder;
        class RevolvedSectionLineImpl;
        /** Revolved Section Line is used to create section views which are
                revolved about an axis.  A revolved section line can contain a
                single revolved cut, or it can contain steps to form multiple cuts.
                In either case, all cut planes resulting from the section line cuts
                are revolved into a common plane for the Revolved Section View.  <br> To create or edit an instance of this class, use @link NXOpen::Drawings::SectionViewBuilder  NXOpen::Drawings::SectionViewBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  RevolvedSectionLine : public NXOpen::Drawings::SectionLine
        {
            private: RevolvedSectionLineImpl * m_revolvedsectionline_impl;
            private: friend class  _RevolvedSectionLineBuilder;
            protected: RevolvedSectionLine();
            public: ~RevolvedSectionLine();
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