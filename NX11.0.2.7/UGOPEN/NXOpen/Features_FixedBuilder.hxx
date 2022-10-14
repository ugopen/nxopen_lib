#ifndef NXOpen_FEATURES_FIXEDBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_FIXEDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_FixedBuilder.ja
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
#include <NXOpen/Features_FaceRecognitionBuilder.hxx>
#include <NXOpen/Features_FixedBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
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
        class FixedBuilder;
    }
    namespace Features
    {
        class FaceRecognitionBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class _FixedBuilderBuilder;
        class FixedBuilderImpl;
        /**
            Represents a builder for a fixed feature.
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateFixedBuilder  NXOpen::Features::FeatureCollection::CreateFixedBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        FaceToFix.CoaxialEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToFix.CoplanarAxesEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToFix.CoplanarEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToFix.EqualDiameterEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToFix.OffsetEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToFix.ParallelEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToFix.PerpendicularEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToFix.SymmetricEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToFix.TangentEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToFix.ThicknessChainEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToFix.UseFaceBrowse </td> <td> 
         
        1 </td> </tr> 

        </table>  

         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  FixedBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: FixedBuilderImpl * m_fixedbuilder_impl;
            private: friend class  _FixedBuilderBuilder;
            protected: FixedBuilder();
            public: ~FixedBuilder();
            /**Returns   the face recognition builder holding the faces to be fixed. 
                         Please refer @link NXOpen::Features::FaceRecognitionBuilder NXOpen::Features::FaceRecognitionBuilder@endlink  for details. 
                    
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::FaceRecognitionBuilder * FaceToFix
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