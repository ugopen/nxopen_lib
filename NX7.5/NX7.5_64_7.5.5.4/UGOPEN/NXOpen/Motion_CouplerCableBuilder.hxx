#ifndef NXOpen_MOTION_COUPLERCABLEBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_COUPLERCABLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_CouplerCableBuilder.ja
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
#include <NXOpen/Motion_CouplerBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class CouplerCableBuilder;
    }
    namespace Motion
    {
        class CouplerBuilder;
    }
    namespace Motion
    {
        class _CouplerCableBuilderBuilder;
        class CouplerCableBuilderImpl;
        /** Represents a @link Motion::CouplerCableBuilder Motion::CouplerCableBuilder@endlink   <br> To create a new instance of this class, use @link Motion::CouplerCollection::CreateCouplerCableBuilder Motion::CouplerCollection::CreateCouplerCableBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Ratio </td> <td> 
         
        1.0 </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  CouplerCableBuilder : public Motion::CouplerBuilder
        {
            private: CouplerCableBuilderImpl * m_couplercablebuilder_impl;
            private: friend class  _CouplerCableBuilderBuilder;
            protected: CouplerCableBuilder();
            public: ~CouplerCableBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
