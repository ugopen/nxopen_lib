#ifndef NXOpen_CAE_IMESHCOLLECTOR_HXX_INCLUDED
#define NXOpen_CAE_IMESHCOLLECTOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_IMeshCollector.ja
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
    namespace CAE
    {
        class IMeshCollector;
    }
    class NXObject;
    namespace CAE
    {
        class _IMeshCollectorBuilder;
        /**  @brief  Represents the base IMeshCollector class for MeshCollector and
                          MeshCollectorOccurrence classes  

           <br> Base Class for MeshCollector and MeshCollectorOccurrence classes <br> */
        class NXOPENCPPEXPORT IMeshCollector : public NXObject
        {
            private: friend class  _IMeshCollectorBuilder;
            protected: IMeshCollector();
        };
    }
}
#undef EXPORTLIBRARY
#endif