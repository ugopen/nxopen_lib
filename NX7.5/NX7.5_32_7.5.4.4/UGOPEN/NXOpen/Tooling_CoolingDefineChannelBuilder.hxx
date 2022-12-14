#ifndef NXOpen_TOOLING_COOLINGDEFINECHANNELBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_COOLINGDEFINECHANNELBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_CoolingDefineChannelBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/GeometricUtilities_ModlMotion.hxx>
#include <NXOpen/Tooling_CoolingDefineChannelBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class CoolingDefineChannelBuilder;
    }
    class Builder;
    namespace GeometricUtilities
    {
        class ModlMotion;
    }
    class Point;
    namespace Tooling
    {
        class _CoolingDefineChannelBuilderBuilder;
        class CoolingDefineChannelBuilderImpl;
        /**The builder class for Cooling Define Channel which assists you
               to create channels directly. <br> To create a new instance of this class, use @link Tooling::CoolingDefineChannelCollection::CreateCoolingDefineChannelBuilder Tooling::CoolingDefineChannelCollection::CreateCoolingDefineChannelBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ChannelDiameter </td> <td> 
         
        10 </td> </tr> 

        <tr><td> 
         
        Motion.DeltaEnum </td> <td> 
         
        ReferenceWcsWorkPart </td> </tr> 

        <tr><td> 
         
        Motion.DeltaXc.Value </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        Motion.DeltaYc.Value </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        Motion.DeltaZc.Value </td> <td> 
         
        0.0 </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  CoolingDefineChannelBuilder : public Builder
        {
            private: CoolingDefineChannelBuilderImpl * m_coolingdefinechannelbuilder_impl;
            private: friend class  _CoolingDefineChannelBuilderBuilder;
            protected: CoolingDefineChannelBuilder();
            public: ~CoolingDefineChannelBuilder();
            /**Returns  the point as the start position of the channel.  <br> License requirements : None */
            public: NXOpen::Point * StartPoint
            (
            );
            /**Sets  the point as the start position of the channel.  <br> License requirements : None */
            public: void SetStartPoint
            (
                NXOpen::Point * startPoint /** startpoint */ 
            );
            /**Returns  the object which defines the transformation from start point to end point.  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::ModlMotion * Motion
            (
            );
            /**Returns  the channel diameter  <br> License requirements : None */
            public: double ChannelDiameter
            (
            );
            /**Sets  the channel diameter  <br> License requirements : None */
            public: void SetChannelDiameter
            (
                double channelDiameter /** channeldiameter */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
