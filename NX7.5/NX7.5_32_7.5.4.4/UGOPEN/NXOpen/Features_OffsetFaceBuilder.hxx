#ifndef NXOpen_FEATURES_OFFSETFACEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_OFFSETFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_OffsetFaceBuilder.ja
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
#include <NXOpen/Features_OffsetFaceBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class OffsetFaceBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    namespace Features
    {
        class _OffsetFaceBuilderBuilder;
        class OffsetFaceBuilderImpl;
        /** Represents a @link Features::OffsetFace Features::OffsetFace@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateOffsetFaceBuilder Features::FeatureCollection::CreateOffsetFaceBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Direction </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        Distance.Value </td> <td> 
         
        10 (millimeters part), 0.4 (inches part) </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  OffsetFaceBuilder : public Features::FeatureBuilder
        {
            private: OffsetFaceBuilderImpl * m_offsetfacebuilder_impl;
            private: friend class  _OffsetFaceBuilderBuilder;
            protected: OffsetFaceBuilder();
            public: ~OffsetFaceBuilder();
            /**Returns  the face collector  <br> License requirements : None */
            public: NXOpen::ScCollector * FaceCollector
            (
            );
            /**Returns  the distance  <br> License requirements : None */
            public: NXOpen::Expression * Distance
            (
            );
            /**Returns  the direction  <br> License requirements : None */
            public: bool Direction
            (
            );
            /**Sets  the direction  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDirection
            (
                bool direction /** direction */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
