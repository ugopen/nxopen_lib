#ifndef NXOpen_FEATURES_PROMOTIONBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_PROMOTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_PromotionBuilder.ja
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
#include <NXOpen/Features_PromotionBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
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
        class PromotionBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class SelectBodyList;
    namespace Features
    {
        class _PromotionBuilderBuilder;
        class PromotionBuilderImpl;
        /**
            Represents a @link NXOpen::Features::Promotion NXOpen::Features::Promotion@endlink  builder. Input to this class can be PSM facet objects.
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreatePromotionBuilder  NXOpen::Features::FeatureCollection::CreatePromotionBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Associative </td> <td> 
         
        True </td> </tr> 

        <tr><td> 
         
        ConvertToLinkedBody </td> <td> 
         
        False </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  PromotionBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: PromotionBuilderImpl * m_promotionbuilder_impl;
            private: friend class  _PromotionBuilderBuilder;
            protected: PromotionBuilder();
            public: ~PromotionBuilder();
            /**Returns  the body to be promoted  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBodyList * Body
            (
            );
            /**Returns  the face direction for a sheet body 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool FaceDirection
            (
            );
            /**Sets  the face direction for a sheet body 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFaceDirection
            (
                bool faceDirection /** facedirection */ 
            );
            /**Returns  the flag denoting the associative state of the Promotion feature 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the flag denoting the associative state of the Promotion feature 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /**Returns  the flag denoting whether the Promotion feature will convert to linked body 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool ConvertToLinkedBody
            (
            );
            /**Sets  the flag denoting whether the Promotion feature will convert to linked body 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetConvertToLinkedBody
            (
                bool convertToLinkedBody /** converttolinkedbody */ 
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
