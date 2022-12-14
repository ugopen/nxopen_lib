#ifndef NXOpen_FEATURES_PRINTCSYSBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_PRINTCSYSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_PrintCsysBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class PrintCsysBuilder;
    }
    class CoordinateSystem;
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    namespace Features
    {
        class _PrintCsysBuilderBuilder;
        class PrintCsysBuilderImpl;
        /**
            Represents a @link Features::Feature Features::Feature@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::PrintCsysFeatureCollection::CreatePrintCsysBuilder  NXOpen::Features::PrintCsysFeatureCollection::CreatePrintCsysBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Freedom </td> <td> 
         
        Free </td> </tr> 

        <tr><td> 
         
        MaxAngle </td> <td> 
         
        45 </td> </tr> 

        <tr><td> 
         
        Offset </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        Type </td> <td> 
         
        UserDefined </td> </tr> 

        </table>  

         <br>  Created in NX12.0.1.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  PrintCsysBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Types of methods which is used to create print CSYS  */
            public: enum Types
            {
                TypesUserDefined/** User defined method   */,
                TypesMinimumHeight/** Minimum height method */
            };

            /** Freedom type of the print CSYS*/
            public: enum FreedomType
            {
                FreedomTypeFree/** Parts are free to rotate and translate*/,
                FreedomTypeFixZDirection/** Parts are free to translate, rotate around z and rotate 180 degrees around other axes*/,
                FreedomTypeFixBottomPlane/** Parts are free to translate and to rotate around z only*/,
                FreedomTypeRotate180/** Parts are free to translate and rotate 180 degrees over any axis*/,
                FreedomTypeFixBottomandXY/** Parts are free to translate, rotate 180 degrees around z axis only*/,
                FreedomTypeFixRotation/** Parts are free to translate only*/,
                FreedomTypeFixed/** Parts are fixed in place and will not be optimized*/
            };

            private: PrintCsysBuilderImpl * m_printcsysbuilder_impl;
            private: friend class  _PrintCsysBuilderBuilder;
            protected: PrintCsysBuilder();
            public: ~PrintCsysBuilder();
            /**Returns  the type which used to create print CSYS 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::PrintCsysBuilder::Types Type
            (
            );
            /**Sets  the type which used to create print CSYS 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : nx_additive_design (" NX Additive Design") */
            public: void SetType
            (
                NXOpen::Features::PrintCsysBuilder::Types type /** type */ 
            );
            /**Returns  the bodies which are selected to create print CSYS 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * Bodies
            (
            );
            /**Returns  the coordinate system which is manually set for the print CSYS
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CoordinateSystem * CoordinateSystem
            (
            );
            /**Sets  the coordinate system which is manually set for the print CSYS
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : nx_additive_design (" NX Additive Design") */
            public: void SetCoordinateSystem
            (
                NXOpen::CoordinateSystem * coord /** coord */ 
            );
            /**Returns  the maximum overhang angle
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: double MaxAngle
            (
            );
            /**Sets  the maximum overhang angle
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : nx_additive_design (" NX Additive Design") */
            public: void SetMaxAngle
            (
                double maxAngle /** maxangle */ 
            );
            /**Returns  the freedom type of the print CSYS
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::PrintCsysBuilder::FreedomType Freedom
            (
            );
            /**Sets  the freedom type of the print CSYS
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : nx_additive_design (" NX Additive Design") */
            public: void SetFreedom
            (
                NXOpen::Features::PrintCsysBuilder::FreedomType freedom /** freedom */ 
            );
            /**Returns  the print csys offset in Z direction
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double Offset
            (
            );
            /**Sets  the print csys offset in Z direction
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_additive_design (" NX Additive Design") */
            public: void SetOffset
            (
                double offset /** offset */ 
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
