#ifndef NXOpen_ANNOTATIONS_DRAFTINGFEATURECONTROLFRAMEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DRAFTINGFEATURECONTROLFRAMEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DraftingFeatureControlFrameBuilder.ja
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
#include <NXOpen/Annotations_FeatureControlFrameBuilder.hxx>
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
        class DraftingFeatureControlFrameBuilder;
    }
    namespace Annotations
    {
        class FeatureControlFrameBuilder;
    }
    namespace Annotations
    {
        class _DraftingFeatureControlFrameBuilderBuilder;
        class DraftingFeatureControlFrameBuilderImpl;
        /**
            Represents a @link Annotations::DraftingFeatureControlFrameBuilder Annotations::DraftingFeatureControlFrameBuilder@endlink 
             <br> To create a new instance of this class, use @link Annotations::AnnotationManager::CreateDraftingFeatureControlFrameBuilder  Annotations::AnnotationManager::CreateDraftingFeatureControlFrameBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Characteristic </td> <td> 
         
        Straightness </td> </tr> 

        <tr><td> 
         
        FrameStyle </td> <td> 
         
        SingleFrame </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  DraftingFeatureControlFrameBuilder : public Annotations::FeatureControlFrameBuilder
        {
            private: DraftingFeatureControlFrameBuilderImpl * m_draftingfeaturecontrolframebuilder_impl;
            private: friend class  _DraftingFeatureControlFrameBuilderBuilder;
            protected: DraftingFeatureControlFrameBuilder();
            public: ~DraftingFeatureControlFrameBuilder();
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