#ifndef NXOpen_ANNOTATIONS_PMIFEATURECONTROLFRAMEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIFEATURECONTROLFRAMEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiFeatureControlFrameBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Annotations_AssociatedObjectsBuilder.hxx>
#include <NXOpen/Annotations_PmiFeatureControlFrameBuilder.hxx>
#include <NXOpen/Annotations_FeatureControlFrameBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiFeatureControlFrameBuilder;
    }
    namespace Annotations
    {
        class AssociatedObjectsBuilder;
    }
    namespace Annotations
    {
        class FeatureControlFrameBuilder;
    }
    namespace Annotations
    {
        class _PmiFeatureControlFrameBuilderBuilder;
        /**
            Represents a @link Annotations::PmiFeatureControlFrameBuilder Annotations::PmiFeatureControlFrameBuilder@endlink 
             <br> To create a new instance of this class, use @link Annotations::AnnotationManager::CreatePmiFeatureControlFrameBuilder Annotations::AnnotationManager::CreatePmiFeatureControlFrameBuilder@endlink  <br> */
        class NXOPENCPPEXPORT PmiFeatureControlFrameBuilder : public Annotations::FeatureControlFrameBuilder
        {
            private: friend class  _PmiFeatureControlFrameBuilderBuilder;
            protected: PmiFeatureControlFrameBuilder();
            /**Returns  the associated objects builder for the annotation  <br> License requirements : None */
            public: NXOpen::Annotations::AssociatedObjectsBuilder * AssociatedObjects
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif