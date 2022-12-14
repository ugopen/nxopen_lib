#ifndef NXOpen_ANNOTATIONS_EDITLEADERBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_EDITLEADERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_EditLeaderBuilder.ja
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
#include <NXOpen/Annotations_LeaderBuilder.hxx>
#include <NXOpen/Annotations_OriginBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class EditLeaderBuilder;
    }
    namespace Annotations
    {
        class LeaderBuilder;
    }
    namespace Annotations
    {
        class OriginBuilder;
    }
    class Builder;
    namespace Annotations
    {
        class _EditLeaderBuilderBuilder;
        class EditLeaderBuilderImpl;
        /** Represents a builder that provides an interface to adding and editing leaders
                to table entities  <br> To create a new instance of this class, use @link NXOpen::Annotations::AnnotationManager::CreateEditLeaderBuilder  NXOpen::Annotations::AnnotationManager::CreateEditLeaderBuilder @endlink  <br> 
         <br>  Created in NX6.0.1.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  EditLeaderBuilder : public NXOpen::Builder
        {
            private: EditLeaderBuilderImpl * m_editleaderbuilder_impl;
            private: friend class  _EditLeaderBuilderBuilder;
            protected: EditLeaderBuilder();
            public: ~EditLeaderBuilder();
            /**Returns  the @link NXOpen::Annotations::OriginBuilder NXOpen::Annotations::OriginBuilder@endlink  for the annotation 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::OriginBuilder * Origin
            (
            );
            /**Returns  the @link NXOpen::Annotations::LeaderBuilder NXOpen::Annotations::LeaderBuilder@endlink  for the annotation 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LeaderBuilder * Leader
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
