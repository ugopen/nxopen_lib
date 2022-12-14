#ifndef NXOpen_PRESSLINESIMULATION_AXISCONTROLDATA_HXX_INCLUDED
#define NXOpen_PRESSLINESIMULATION_AXISCONTROLDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PressLineSimulation_AxisControlData.ja
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
#include <NXOpen/libpresslinesimulopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PressLineSimulation
    {
        class AxisControlData;
    }
    class NXObject;
    namespace PressLineSimulation
    {
        class _AxisControlDataBuilder;
        class AxisControlDataImpl;
        /** This class is the base class for axis data representations in Press Line Simulation  <br> This class is abstract and cannot be instanciated  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class PRESSLINESIMULOPENCPPEXPORT  AxisControlData : public NXOpen::NXObject
        {
            private: AxisControlDataImpl * m_axiscontroldata_impl;
            private: friend class  _AxisControlDataBuilder;
            protected: AxisControlData();
            public: ~AxisControlData();
            /**Returns  the name of the axis, with which it is displayed in the UI. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DisplayName
            (
            );
            /**Returns  the external status of the axis control column 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool External
            (
            );
            /**Sets  the external status of the axis control column 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_pls_line_setup (" NX Press Line Setup") */
            public: void SetExternal
            (
                bool external /** external */ 
            );
        };
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
