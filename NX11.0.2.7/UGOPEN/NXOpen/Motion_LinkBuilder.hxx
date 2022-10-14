#ifndef NXOpen_MOTION_LINKBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_LINKBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_LinkBuilder.ja
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
#include <NXOpen/Motion_LinkBuilder.hxx>
#include <NXOpen/Motion_LinkInitialVelocity.hxx>
#include <NXOpen/Motion_LinkMassProperty.hxx>
#include <NXOpen/Motion_MotionBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class LinkBuilder;
    }
    namespace Motion
    {
        class LinkInitialVelocity;
    }
    namespace Motion
    {
        class LinkMassProperty;
    }
    namespace Motion
    {
        class MotionBuilder;
    }
    class SelectNXObjectList;
    namespace Motion
    {
        class _LinkBuilderBuilder;
        class LinkBuilderImpl;
        /**
            Represents a @link NXOpen::Motion::LinkBuilder NXOpen::Motion::LinkBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::Motion::LinkCollection::CreateLinkBuilder  NXOpen::Motion::LinkCollection::CreateLinkBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  LinkBuilder : public NXOpen::Motion::MotionBuilder
        {
            private: LinkBuilderImpl * m_linkbuilder_impl;
            private: friend class  _LinkBuilderBuilder;
            protected: LinkBuilder();
            public: ~LinkBuilder();
            /**Returns  the geometries 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * Geometries
            (
            );
            /**Returns  the mass property 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::LinkMassProperty * MassProperty
            (
            );
            /**Returns  the initial velocity 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::LinkInitialVelocity * InitialVelocity
            (
            );
            /**Returns  the link fixed to the ground 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool Fixed
            (
            );
            /**Sets  the link fixed to the ground 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFixed
            (
                bool fixed /** fixed */ 
            );
            /**Returns  the name 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
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