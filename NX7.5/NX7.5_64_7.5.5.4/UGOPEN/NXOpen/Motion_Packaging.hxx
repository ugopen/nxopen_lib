#ifndef NXOpen_MOTION_PACKAGING_HXX_INCLUDED
#define NXOpen_MOTION_PACKAGING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_Packaging.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class Packaging;
    }
    class NXObject;
    namespace Motion
    {
        class _PackagingBuilder;
        class PackagingImpl;
        /** This class is an abstract class and base class for @link  PackagingMeasure   PackagingMeasure @endlink , 
            @link  PackagingTrace   PackagingTrace @endlink  and @link  PackagingInterference   PackagingInterference @endlink  objects.  <br> This is an abstract class, and cannot be created. <br> */
        class NXOPENCPPEXPORT  Packaging : public NXObject
        {
            private: PackagingImpl * m_packaging_impl;
            private: friend class  _PackagingBuilder;
            protected: Packaging();
            public: ~Packaging();
        };
    }
}
#undef EXPORTLIBRARY
#endif
