#ifndef NXOpen_TOOLING_COOLINGFITTINGDATA_HXX_INCLUDED
#define NXOpen_TOOLING_COOLINGFITTINGDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_CoolingFittingData.ja
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
#include <NXOpen/Tooling_CoolingFittingData.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class CoolingFittingData;
    }
    class Point;
    namespace Tooling
    {
        class CoolingFittingDataImpl;
        /** Represents the cooling fitting data in Add Channel Fitting Builder. 
              <br> To create an instance of this object use @link Tooling::ChannelFittingBuilder::CreateCoolingFittingData Tooling::ChannelFittingBuilder::CreateCoolingFittingData@endlink  <br> */
        class NXOPENCPPEXPORT  CoolingFittingData : public TransientObject
        {
            private: CoolingFittingDataImpl * m_coolingfittingdata_impl;
            public: explicit CoolingFittingData(void *ptr);
            /** Dispose the part infomation to be cloned.  <br> License requirements : None */
            public: virtual ~CoolingFittingData();
            /**Add cooling fitting points to the fitting data.  <br> License requirements : None */
            public: void AddFittingPoints
            (
                NXOpen::Point * fittingPoint /**the fitting point to be added. */
            );
            /**Clear cooling fitting points from the fitting data.  <br> License requirements : None */
            public: void ClearFittingPoints
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
