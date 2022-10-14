#ifndef NXOpen_DRAWINGS_DRAWINGREGION_HXX_INCLUDED
#define NXOpen_DRAWINGS_DRAWINGREGION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_DrawingRegion.ja
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
#include <NXOpen/DisplayableObject.hxx>
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
        class DrawingRegion;
    }
    class DisplayableObject;
    namespace Drawings
    {
        class _DrawingRegionBuilder;
        class DrawingRegionImpl;
        /** Represents a Drawing Region  <br> To create or edit an instance of this class, use @link NXOpen::Drawings::DrawingRegionBuilder  NXOpen::Drawings::DrawingRegionBuilder @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  DrawingRegion : public NXOpen::DisplayableObject
        {
            private: DrawingRegionImpl * m_drawingregion_impl;
            private: friend class  _DrawingRegionBuilder;
            protected: DrawingRegion();
            public: ~DrawingRegion();
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