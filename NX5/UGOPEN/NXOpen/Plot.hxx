#ifndef NXOpen_PLOT_HXX_INCLUDED
#define NXOpen_PLOT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Plot.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class Plot;
    class NXObject;
    class _PlotBuilder;
    /** Represents a plot */
    class NXOPENCPPEXPORT Plot : public NXObject
    {
        private: friend class  _PlotBuilder;
        protected: Plot();
    };
}
#undef EXPORTLIBRARY
#endif
