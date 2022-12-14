#ifndef NXOpen_MARKUP_FREEHAND_HXX_INCLUDED
#define NXOpen_MARKUP_FREEHAND_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Markup_Freehand.ja
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
#include <NXOpen/Markup_Element.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_markup_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Markup
    {
        class Freehand;
    }
    namespace Markup
    {
        class Element;
    }
    namespace Markup
    {
        class _FreehandBuilder;
        class FreehandImpl;
        /**
                Represents a @link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink 
             <br> To create or edit an instance of this class, use @link NXOpen::Markup::ElementBuilder  NXOpen::Markup::ElementBuilder @endlink  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_MARKUPEXPORT  Freehand : public NXOpen::Markup::Element
        {
            private: FreehandImpl * m_freehand_impl;
            private: friend class  _FreehandBuilder;
            protected: Freehand();
            public: ~Freehand();
            /** Gets a list of points 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void GetPoints
            (
                std::vector<NXOpen::Point3d> & points /** points */ 
            );
            /** Sets a list of points 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: void SetPoints
            (
                const std::vector<NXOpen::Point3d> & points /** points */ 
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
