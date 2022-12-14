#ifndef NXOpen_ANNOTATIONS_RECTANGULARTARGETDATA_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_RECTANGULARTARGETDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_RectangularTargetData.ja
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
#include <NXOpen/Annotations.hxx>
#include <NXOpen/Annotations_DatumTargetData.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class RectangularTargetData;
    }
    namespace Annotations
    {
        class DatumTargetData;
    }
    class Expression;
    namespace Annotations
    {
    }
    namespace Annotations
    {
        class RectangularTargetDataImpl;
        /** Represents rectangular datum target data */
        class NXOPENCPPEXPORT  RectangularTargetData : public Annotations::DatumTargetData
        {
            private: RectangularTargetDataImpl * m_rectangulartargetdata_impl;
            public: explicit RectangularTargetData(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~RectangularTargetData();
            /** Returns the length  @return  Length data   <br> License requirements : None */
            public: NXOpen::Annotations::Value GetLength
            (
            );
            /** Sets the length  <br> License requirements : None */
            public: void SetLength
            (
                const NXOpen::Annotations::Value & length /** New length data */
            );
            /** Returns the width  @return  Width data  <br> License requirements : None */
            public: NXOpen::Annotations::Value GetWidth
            (
            );
            /** Sets the width  <br> License requirements : None */
            public: void SetWidth
            (
                const NXOpen::Annotations::Value & width /** New width data */
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
