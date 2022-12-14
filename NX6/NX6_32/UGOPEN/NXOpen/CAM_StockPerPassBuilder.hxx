#ifndef NXOpen_CAM_STOCKPERPASSBUILDER_HXX_INCLUDED
#define NXOpen_CAM_STOCKPERPASSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_StockPerPassBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAM_StockPerPassBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class StockPerPassBuilder;
    }
    class Builder;
    namespace CAM
    {
        class _StockPerPassBuilderBuilder;
        /** Represents a Builder which holds the data for a set of individual stock per pass.  <br> This is an abstract class and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT StockPerPassBuilder : public Builder
        {
            private: friend class  _StockPerPassBuilderBuilder;
            protected: StockPerPassBuilder();
            /** Add a new item  <br> License requirements : cam_base ("CAM BASE") */
            public: void Add
            (
                int passAfter /** the pass which new pass will be added after */,
                double stock /** the stock for new pass */
            );
            /** Modify item  <br> License requirements : cam_base ("CAM BASE") */
            public: void Modify
            (
                int pass /** the pass on which stock will be modified */,
                double stock /** the new value of stock */
            );
            /** Delete a item  <br> License requirements : cam_base ("CAM BASE") */
            public: void Delete
            (
                int pass /** the pass to be deleted */
            );
            /** Move up a item  <br> License requirements : cam_base ("CAM BASE") */
            public: void MoveUp
            (
                int pass /** the pass to be moved up */
            );
            /** Move down a item  <br> License requirements : cam_base ("CAM BASE") */
            public: void MoveDown
            (
                int pass /** the pass to be moved down */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
