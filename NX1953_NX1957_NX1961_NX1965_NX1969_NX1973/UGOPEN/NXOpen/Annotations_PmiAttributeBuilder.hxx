#ifndef NXOpen_ANNOTATIONS_PMIATTRIBUTEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIATTRIBUTEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiAttributeBuilder.ja
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
#include <NXOpen/Annotations_AssociatedObjectsBuilder.hxx>
#include <NXOpen/Annotations_LeaderBuilder.hxx>
#include <NXOpen/Annotations_OriginBuilder.hxx>
#include <NXOpen/Annotations_StyleBuilder.hxx>
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
        class PmiAttributeBuilder;
    }
    namespace Annotations
    {
        class AssociatedObjectsBuilder;
    }
    namespace Annotations
    {
        class LeaderBuilder;
    }
    namespace Annotations
    {
        class OriginBuilder;
    }
    namespace Annotations
    {
        class Pmi;
    }
    namespace Annotations
    {
        class StyleBuilder;
    }
    class Builder;
    class NXObject;
    namespace Annotations
    {
        class _PmiAttributeBuilderBuilder;
        class PmiAttributeBuilderImpl;
        /** Represents a @link NXOpen::Annotations::PmiAttribute NXOpen::Annotations::PmiAttribute@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Annotations::PmiAttributeCollection::CreatePmiAttributeBuilder  NXOpen::Annotations::PmiAttributeCollection::CreatePmiAttributeBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiAttributeBuilder : public NXOpen::Builder
        {
            private: PmiAttributeBuilderImpl * m_pmiattributebuilder_impl;
            private: friend class  _PmiAttributeBuilderBuilder;
            protected: PmiAttributeBuilder();
            public: ~PmiAttributeBuilder();
            /**Returns  the @link NXOpen::Annotations::OriginBuilder NXOpen::Annotations::OriginBuilder@endlink  for the annotation 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::OriginBuilder * Origin
            (
            );
            /**Returns  the @link NXOpen::Annotations::LeaderBuilder NXOpen::Annotations::LeaderBuilder@endlink  for the annotation 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LeaderBuilder * Leader
            (
            );
            /**Returns  the @link NXOpen::Annotations::AssociatedObjectsBuilder NXOpen::Annotations::AssociatedObjectsBuilder@endlink  for the annotation 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::AssociatedObjectsBuilder * AssociatedObjects
            (
            );
            /**Returns  the @link NXOpen::Annotations::StyleBuilder NXOpen::Annotations::StyleBuilder@endlink  for the annotation 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::StyleBuilder * Style
            (
            );
            /**Returns  the business modifier 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * BusinessModifier
            (
            );
            /**Sets  the business modifier 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBusinessModifier
            (
                NXOpen::NXObject * businessModifier /** businessmodifier */ 
            );
            /**Returns  the knowledge fusion class name file, the default class is UG provided pmi KF class 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXString KnowledgeFusionClassName
            (
            );
            /**Sets  the knowledge fusion class name file, the default class is UG provided pmi KF class 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetKnowledgeFusionClassName
            (
                const NXString & knowledgeFusionClassName /** knowledgefusionclassname */ 
            );
            /**Sets  the knowledge fusion class name file, the default class is UG provided pmi KF class 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            void SetKnowledgeFusionClassName
            (
                const char * knowledgeFusionClassName /** knowledgefusionclassname */ 
            );
            /**  Returns the attribute values
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::NXObject *> GetAttributeValues
            (
            );
            /** Sets the attribute values
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAttributeValues
            (
                const std::vector<NXOpen::NXObject *> & attributeValues /** attribute values */
            );
            /**Returns  the @link NXOpen::Annotations::Pmi NXOpen::Annotations::Pmi@endlink  for this annotation 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::Pmi * Attribute
            (
            );
            /**Sets  the @link NXOpen::Annotations::Pmi NXOpen::Annotations::Pmi@endlink  for this annotation 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAttribute
            (
                NXOpen::Annotations::Pmi * attribute /** attribute */ 
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
