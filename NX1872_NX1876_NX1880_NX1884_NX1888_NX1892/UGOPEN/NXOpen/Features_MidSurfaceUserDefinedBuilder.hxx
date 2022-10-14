#ifndef NXOpen_FEATURES_MIDSURFACEUSERDEFINEDBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_MIDSURFACEUSERDEFINEDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_MidSurfaceUserDefinedBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class MidSurfaceUserDefinedBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class SelectBody;
    class SelectBodyList;
    namespace Features
    {
        class _MidSurfaceUserDefinedBuilderBuilder;
        class MidSurfaceUserDefinedBuilderImpl;
        /**
            Represents a @link NXOpen::Features::MidSurfaceUserDefined NXOpen::Features::MidSurfaceUserDefined@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateMidSurfaceUserDefinedBuilder  NXOpen::Features::FeatureCollection::CreateMidSurfaceUserDefinedBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        MaxThickness.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        MinThickness.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        OutsideThickness.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        </table>  

         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  MidSurfaceUserDefinedBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: MidSurfaceUserDefinedBuilderImpl * m_midsurfaceuserdefinedbuilder_impl;
            private: friend class  _MidSurfaceUserDefinedBuilderBuilder;
            protected: MidSurfaceUserDefinedBuilder();
            public: ~MidSurfaceUserDefinedBuilder();
            /**Returns  the solid body for user defined midsurface 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBody * SolidBodySel
            (
            );
            /**Returns  the sheet bodies to be treated as user defined neutral sheets 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBodyList * SheetBodySelection
            (
            );
            /**Returns  the min element thickness allowed during Fem solve 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MinThickness
            (
            );
            /**Returns  the max thickness allowed during Fem solve 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MaxThickness
            (
            );
            /**Returns  the outside thickness to be used during Fem solve if the node falls outside of solid 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OutsideThickness
            (
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