#ifndef NXOpen_CAE_FTK_ARRAYRECORD2DWITHZVALUE_HXX_INCLUDED
#define NXOpen_CAE_FTK_ARRAYRECORD2DWITHZVALUE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FTK_ArrayRecord2DWithZValue.ja
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
#include <NXOpen/CAE_FTK_BaseUnit.hxx>
#include <NXOpen/CAE_FTK_ArrayRecord2D.hxx>
#include <NXOpen/CAE_FTK_IRecordWithZValue.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        namespace FTK
        {
            class ArrayRecord2DWithZValue;
        }
    }
    namespace CAE
    {
        namespace FTK
        {
            class ArrayRecord2D;
        }
    }
    namespace CAE
    {
        namespace FTK
        {
            class BaseUnit;
        }
    }
    namespace CAE
    {
        namespace FTK
        {
            class IRecordWithZValue;
        }
    }
    namespace CAE
    {
        namespace FTK
        {
            class _ArrayRecord2DWithZValueBuilder;
            class ArrayRecord2DWithZValueImpl;
            /** Manages the @link CAE::FTK::ArrayRecord2D CAE::FTK::ArrayRecord2D@endlink  with Z value  <br> Not support KF.  <br> 
             <br>  Created in NX1926.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ArrayRecord2DWithZValue : public NXOpen::CAE::FTK::ArrayRecord2D, public virtual NXOpen::CAE::FTK::IRecordWithZValue
            {
                private: ArrayRecord2DWithZValueImpl * m_arrayrecord2dwithzvalue_impl;
                private: friend class  _ArrayRecord2DWithZValueBuilder;
                protected: ArrayRecord2DWithZValue();
                public: ~ArrayRecord2DWithZValue();
                /**Returns  the Z unit 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::FTK::BaseUnit * Unit
                (
                );
                /**Sets  the Z unit 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual void SetUnit
                (
                    NXOpen::CAE::FTK::BaseUnit * zValueUnit /** zvalueunit */ 
                );
                /**Returns  the Z value 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual double Value
                (
                );
                /**Sets  the Z value 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual void SetValue
                (
                    double zValue /** zvalue */ 
                );
            };
        }
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
