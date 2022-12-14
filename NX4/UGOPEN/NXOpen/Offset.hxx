#ifndef NXOpen_OFFSET_HXX_INCLUDED
#define NXOpen_OFFSET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Offset.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/SmartObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class Offset;
    class SmartObject;
    class _OffsetBuilder;
    /**
    Represents a @link Offset Offset@endlink . 
    */
    class NXOPENCPPEXPORT Offset : public SmartObject
    {
        private: friend class  _OffsetBuilder;
        protected: Offset();
    };
}
#undef EXPORTLIBRARY
#endif
