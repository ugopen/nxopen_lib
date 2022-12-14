#ifndef NXOpen_TOOLING_COOLINGCONNECTBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_COOLINGCONNECTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_CoolingConnectBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/Tooling_CoolingConnectBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class CoolingConnectBuilder;
    }
    class Builder;
    class Direction;
    class Point;
    class SelectBody;
    namespace Tooling
    {
        class _CoolingConnectBuilderBuilder;
        class CoolingConnectBuilderImpl;
        /**The builder class for Cooling connection which assists you
               to create channel and connect it to other channels. <br> To create a new instance of this class, use @link Tooling::CoolingConnectCollection::CreateCoolingConnectBuilder Tooling::CoolingConnectCollection::CreateCoolingConnectBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        DefineConnectVector </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DefineStartPoint </td> <td> 
         
        0 </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  CoolingConnectBuilder : public Builder
        {
            private: CoolingConnectBuilderImpl * m_coolingconnectbuilder_impl;
            private: friend class  _CoolingConnectBuilderBuilder;
            protected: CoolingConnectBuilder();
            public: ~CoolingConnectBuilder();
            /**Returns  the first channel to be connected.  <br> License requirements : None */
            public: NXOpen::SelectBody * FirstChannel
            (
            );
            /**Returns  the second channel to be connected.  <br> License requirements : None */
            public: NXOpen::SelectBody * SecondChannel
            (
            );
            /**Returns  the value which specifies whether to define the start point or not. <br> License requirements : None */
            public: bool DefineStartPoint
            (
            );
            /**Sets  the value which specifies whether to define the start point or not. <br> License requirements : None */
            public: void SetDefineStartPoint
            (
                bool defineStartPoint /** definestartpoint */ 
            );
            /**Returns  the point for changing the start position of the connecting channel. <br> License requirements : None */
            public: NXOpen::Point * StartPoint
            (
            );
            /**Sets  the point for changing the start position of the connecting channel. <br> License requirements : None */
            public: void SetStartPoint
            (
                NXOpen::Point * startPoint /** startpoint */ 
            );
            /**Returns  the value which specifies whether to define the vector of the connect channel or not.  <br> License requirements : None */
            public: bool DefineConnectVector
            (
            );
            /**Sets  the value which specifies whether to define the vector of the connect channel or not.  <br> License requirements : None */
            public: void SetDefineConnectVector
            (
                bool defineConnectVector /** defineconnectvector */ 
            );
            /**Returns  the vector specified for creating connecting channel.  <br> License requirements : None */
            public: NXOpen::Direction * ConnectVector
            (
            );
            /**Sets  the vector specified for creating connecting channel.  <br> License requirements : None */
            public: void SetConnectVector
            (
                NXOpen::Direction * connectVector /** connectvector */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
