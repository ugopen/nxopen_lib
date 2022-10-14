#ifndef NXOpen_ANNOTATIONS_OFFSETCENTERPOINT_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_OFFSETCENTERPOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_OffsetCenterPoint.ja
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
#include <NXOpen/Annotations_DraftingAid.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class OffsetCenterPoint;
    }
    namespace Annotations
    {
        class DraftingAid;
    }
    namespace Annotations
    {
        class _OffsetCenterPointBuilder;
        /** Represents a offset center point */
        class NXOPENCPPEXPORT OffsetCenterPoint : public Annotations::DraftingAid
        {
            private: friend class  _OffsetCenterPointBuilder;
            protected: OffsetCenterPoint();
        };
    }
}
#undef EXPORTLIBRARY
#endif