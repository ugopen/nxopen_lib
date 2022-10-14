#ifndef NXOpen_MOTION_GRAPHLEGENDDATA_HXX_INCLUDED
#define NXOpen_MOTION_GRAPHLEGENDDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_GraphLegendData.ja
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
#include <NXOpen/CAE_FTK_IApplicationData.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class GraphLegendData;
    }
    namespace CAE
    {
        namespace FTK
        {
            class IApplicationData;
        }
    }
    class NXObject;
    namespace Motion
    {
        class _GraphLegendDataBuilder;
        class GraphLegendDataImpl;
        /** Represents a motion graph legend data  <br> Not support KF.  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  GraphLegendData : public NXOpen::NXObject, public virtual NXOpen::CAE::FTK::IApplicationData
        {
            private: GraphLegendDataImpl * m_graphlegenddata_impl;
            private: friend class  _GraphLegendDataBuilder;
            protected: GraphLegendData();
            public: ~GraphLegendData();
            /** Asks the count of attributes which could be showed on legend table  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual int AskNumberOfDisplayableAttributes
            (
            );
            /** Asks the name of a displayable attribute  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXString AskNthDisplayableAttributeName
            (
                int nth /** nth */ 
            );
            /** Asks the value of a displayable attribute  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXString AskNthDisplayableAttributeValue
            (
                int nth /** nth */ 
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