#ifndef NXOpen_DISPLAY_BOUNDEDGRID_HXX_INCLUDED
#define NXOpen_DISPLAY_BOUNDEDGRID_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_BoundedGrid.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Display_Grid.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Display
    {
        class BoundedGrid;
    }
    namespace Display
    {
        class Grid;
    }
    namespace Display
    {
        class _BoundedGridBuilder;
        /** Represents a bounded grid  <br> Bounded grids are not supported in KF. <br> */
        class NXOPENCPPEXPORT BoundedGrid : public Display::Grid
        {
            private: friend class  _BoundedGridBuilder;
            protected: BoundedGrid();
        };
    }
}
#undef EXPORTLIBRARY
#endif
