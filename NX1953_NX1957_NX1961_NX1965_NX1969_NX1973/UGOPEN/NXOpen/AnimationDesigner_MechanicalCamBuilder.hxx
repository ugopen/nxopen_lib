#ifndef NXOpen_ANIMATIONDESIGNER_MECHANICALCAMBUILDER_HXX_INCLUDED
#define NXOpen_ANIMATIONDESIGNER_MECHANICALCAMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AnimationDesigner_MechanicalCamBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libanimationdesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AnimationDesigner
    {
        class MechanicalCamBuilder;
    }
    class Builder;
    class SelectNXObject;
    class SelectNXObjectList;
    namespace AnimationDesigner
    {
        class _MechanicalCamBuilderBuilder;
        class MechanicalCamBuilderImpl;
        /**
            Represents a @link NXOpen::AnimationDesigner::MechanicalCamBuilder NXOpen::AnimationDesigner::MechanicalCamBuilder@endlink .
             <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::MechanicalCamCollection::CreateMechanicalCamBuilder  NXOpen::AnimationDesigner::MechanicalCamCollection::CreateMechanicalCamBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class ANIMATIONDESIGNEROPENCPPEXPORT  MechanicalCamBuilder : public NXOpen::Builder
        {
            private: MechanicalCamBuilderImpl * m_mechanicalcambuilder_impl;
            private: friend class  _MechanicalCamBuilderBuilder;
            protected: MechanicalCamBuilder();
            public: ~MechanicalCamBuilder();
            /**Returns  the master axis joint. This can be a @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink  or @link NXOpen::AnimationDesigner::SliderJoint NXOpen::AnimationDesigner::SliderJoint@endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: NXOpen::SelectNXObject * MasterAxis
            (
            );
            /**Returns  the master faces. This can be a @link NXOpen::Face NXOpen::Face@endlink . 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: NXOpen::SelectNXObjectList * MasterFaces
            (
            );
            /**Returns  the follower axis joint. This can be a @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink  or @link NXOpen::AnimationDesigner::SliderJoint NXOpen::AnimationDesigner::SliderJoint@endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: NXOpen::SelectNXObject * FollowerAxis
            (
            );
            /**Returns  the follower faces. This can be a @link NXOpen::Face NXOpen::Face@endlink . 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: NXOpen::SelectNXObjectList * FollowerFaces
            (
            );
            /**Returns  the name. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: NXString Name
            (
            );
            /**Sets  the name. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            void SetName
            (
                const char * name /** name */ 
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