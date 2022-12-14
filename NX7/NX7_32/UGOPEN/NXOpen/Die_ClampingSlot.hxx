#ifndef NXOpen_DIE_CLAMPINGSLOT_HXX_INCLUDED
#define NXOpen_DIE_CLAMPINGSLOT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_ClampingSlot.ja
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
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        class ClampingSlot;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Die
    {
        class _ClampingSlotBuilder;
        /** Represents a clamping slot feature */
        class NXOPENCPPEXPORT ClampingSlot : public Features::BodyFeature
        {
            private: friend class  _ClampingSlotBuilder;
            protected: ClampingSlot();
        };
    }
}
#undef EXPORTLIBRARY
#endif
