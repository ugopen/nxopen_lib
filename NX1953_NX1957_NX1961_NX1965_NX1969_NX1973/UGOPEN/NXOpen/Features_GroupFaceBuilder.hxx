#ifndef NXOpen_FEATURES_GROUPFACEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_GROUPFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_GroupFaceBuilder.ja
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
        class GroupFaceBuilder;
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
        class _GroupFaceBuilderBuilder;
        class GroupFaceBuilderImpl;
        /**
            Represents a builder for a group face feature.
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateGroupFaceBuilder  NXOpen::Features::FeatureCollection::CreateGroupFaceBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        FaceToGroup.CoaxialEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToGroup.CoplanarAxesEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToGroup.CoplanarEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToGroup.EqualDiameterEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToGroup.OffsetEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToGroup.ParallelEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToGroup.PerpendicularEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToGroup.SameOrbitEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToGroup.SymmetricEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToGroup.TangentEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToGroup.ThicknessChainEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToGroup.UseFaceBrowse </term> <description> 
         
        1 </description> </item> 

        </list> 

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  GroupFaceBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: GroupFaceBuilderImpl * m_groupfacebuilder_impl;
            private: friend class  _GroupFaceBuilderBuilder;
            protected: GroupFaceBuilder();
            public: ~GroupFaceBuilder();
            /**Returns   the face recognition builder holding the faces to group. 
                         Please refer @link Features::FaceRecognitionBuilder Features::FaceRecognitionBuilder@endlink  for details. 
                    
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::FaceRecognitionBuilder * FaceToGroup
            (
            );
            /**Sets  the rigid flag
                    
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRigid
            (
                bool rigid /** rigid */ 
            );
            /**Returns  the rigid flag
                    
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: bool Rigid
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
