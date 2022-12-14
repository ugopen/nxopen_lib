#ifndef NXOpen_FEATURES_POINTSETFACEPERCENTAGEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_POINTSETFACEPERCENTAGEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_PointSetFacePercentageBuilder.ja
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
#include <NXOpen/Features_PointSetFacePercentageBuilder.hxx>
#include <NXOpen/NXObject.hxx>
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
        class PointSetFacePercentageBuilder;
    }
    class Expression;
    class NXObject;
    namespace Features
    {
        class _PointSetFacePercentageBuilderBuilder;
        class PointSetFacePercentageBuilderImpl;
        /**
            Represents a @link NXOpen::Features::PointSetFacePercentageBuilder NXOpen::Features::PointSetFacePercentageBuilder@endlink . This builder is used to
            interrogate the face percentage items in the list.
             <br> To create a new instance of this class, use @link NXOpen::Features::PointSetBuilder::CreateFacePercentageListItem  NXOpen::Features::PointSetBuilder::CreateFacePercentageListItem @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  PointSetFacePercentageBuilder : public NXOpen::NXObject
        {
            private: PointSetFacePercentageBuilderImpl * m_pointsetfacepercentagebuilder_impl;
            private: friend class  _PointSetFacePercentageBuilderBuilder;
            protected: PointSetFacePercentageBuilder();
            public: ~PointSetFacePercentageBuilder();
            /**Returns  the u percentage expression. The u value on the face to create a point. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * UPercentage
            (
            );
            /**Returns  the v percentage expression. The v value on the face to create a point. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * VPercentage
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
