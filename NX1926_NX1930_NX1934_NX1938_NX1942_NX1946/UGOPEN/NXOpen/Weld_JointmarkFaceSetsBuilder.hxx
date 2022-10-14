#ifndef NXOpen_WELD_JOINTMARKFACESETSBUILDER_HXX_INCLUDED
#define NXOpen_WELD_JOINTMARKFACESETSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_JointmarkFaceSetsBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class JointmarkFaceSetsBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class ScCollector;
    namespace Weld
    {
        class _JointmarkFaceSetsBuilderBuilder;
        class JointmarkFaceSetsBuilderImpl;
        /** Used to create or edit a set of faces for Jointmark  <br> To create a new instance of this class, use @link NXOpen::Weld::JointmarkBuilder::NewFaceSets  NXOpen::Weld::JointmarkBuilder::NewFaceSets @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  JointmarkFaceSetsBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: JointmarkFaceSetsBuilderImpl * m_jointmarkfacesetsbuilder_impl;
            private: friend class  _JointmarkFaceSetsBuilderBuilder;
            protected: JointmarkFaceSetsBuilder();
            public: ~JointmarkFaceSetsBuilder();
            /**Returns  the selected face collector 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::ScCollector * FaceSelect
            (
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
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