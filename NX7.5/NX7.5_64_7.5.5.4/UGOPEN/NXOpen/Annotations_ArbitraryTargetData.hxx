#ifndef NXOpen_ANNOTATIONS_ARBITRARYTARGETDATA_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_ARBITRARYTARGETDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_ArbitraryTargetData.ja
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
#include <NXOpen/Annotations_DatumTargetData.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class ArbitraryTargetData;
    }
    namespace Annotations
    {
        class DatumTargetData;
    }
    namespace Annotations
    {
    }
    namespace Annotations
    {
        class ArbitraryTargetDataImpl;
        /** Represents arbitrary datum target data */
        class NXOPENCPPEXPORT  ArbitraryTargetData : public Annotations::DatumTargetData
        {
            private: ArbitraryTargetDataImpl * m_arbitrarytargetdata_impl;
            public: explicit ArbitraryTargetData(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~ArbitraryTargetData();
            /**Returns  the upper text  <br> License requirements : None */
            public: NXString UpperText
            (
            );
            /**Sets  the upper text  <br> License requirements : None */
            public: void SetUpperText
            (
                const NXString & upperText /** New upper text */
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
