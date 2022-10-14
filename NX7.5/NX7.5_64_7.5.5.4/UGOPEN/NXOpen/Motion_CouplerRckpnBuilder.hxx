#ifndef NXOpen_MOTION_COUPLERRCKPNBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_COUPLERRCKPNBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_CouplerRckpnBuilder.ja
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
        class CouplerRckpnBuilder;
    }
    namespace Motion
    {
        class CouplerBuilder;
    }
    namespace Motion
    {
        class _CouplerRckpnBuilderBuilder;
        class CouplerRckpnBuilderImpl;
        /** Represents a @link Motion::CouplerRckpnBuilder Motion::CouplerRckpnBuilder@endlink   <br> To create a new instance of this class, use @link Motion::CouplerCollection::CreateCouplerRckpnBuilder Motion::CouplerCollection::CreateCouplerRckpnBuilder@endlink  <br> 
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
        class NXOPENCPPEXPORT  CouplerRckpnBuilder : public Motion::CouplerBuilder
        {
            private: CouplerRckpnBuilderImpl * m_couplerrckpnbuilder_impl;
            private: friend class  _CouplerRckpnBuilderBuilder;
            protected: CouplerRckpnBuilder();
            public: ~CouplerRckpnBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif