#ifndef NXOpen_IOMNAME_HXX_INCLUDED
#define NXOpen_IOMNAME_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     IOMName.ja
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
#include <NXOpen/libnxopenjamtestcpp_exports.hxx>
namespace NXOpen
{
    class IOMName;
    /**
    Test interface for interfaces
    */
    class NXOPENJAMTESTCPPEXPORT  IOMName
    {
        virtual void EnsureVtableExists() {}
        public: virtual ~IOMName() {}
        /** Returns the object name  @return   <br> License requirements : None */
        public: virtual NXString GetObjectName
        (
        ) = 0;
        /** Compare with  @return   <br> License requirements : None */
        public: virtual bool CompareWith
        (
            NXOpen::IOMName * other /** other */ 
        ) = 0;
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif
