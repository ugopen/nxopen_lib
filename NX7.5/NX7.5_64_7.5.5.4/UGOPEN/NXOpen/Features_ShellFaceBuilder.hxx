#ifndef NXOpen_FEATURES_SHELLFACEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHELLFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShellFaceBuilder.ja
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
#include <NXOpen/Features_ShellFaceBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ShellFaceBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    namespace Features
    {
        class _ShellFaceBuilderBuilder;
        class ShellFaceBuilderImpl;
        /** Represents a @link Features::ShellFace Features::ShellFace@endlink  builder  <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateShellFaceBuilder Features::FeatureCollection::CreateShellFaceBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Thickness.Value </td> <td> 
         
        5.0 (millimeters part), 0.5 (inches part) </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  ShellFaceBuilder : public Features::FeatureBuilder
        {
            private: ShellFaceBuilderImpl * m_shellfacebuilder_impl;
            private: friend class  _ShellFaceBuilderBuilder;
            protected: ShellFaceBuilder();
            public: ~ShellFaceBuilder();
            /**Returns  the faces to be shelled  <br> License requirements : None */
            public: NXOpen::ScCollector * FacesToShell
            (
            );
            /**Returns  the faces to be pierced  <br> License requirements : None */
            public: NXOpen::ScCollector * FacesToPierce
            (
            );
            /**Returns  the thickness  <br> License requirements : None */
            public: NXOpen::Expression * Thickness
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif