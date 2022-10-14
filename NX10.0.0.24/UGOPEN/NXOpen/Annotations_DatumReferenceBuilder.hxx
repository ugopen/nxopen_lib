#ifndef NXOpen_ANNOTATIONS_DATUMREFERENCEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DATUMREFERENCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DatumReferenceBuilder.ja
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
#include <NXOpen/Annotations_DatumReferenceBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class DatumReferenceBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Annotations
    {
        class _DatumReferenceBuilderBuilder;
        class DatumReferenceBuilderImpl;
        /**
            Represents a @link NXOpen::Annotations::DatumReferenceBuilder NXOpen::Annotations::DatumReferenceBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::Annotations::AnnotationManager::CreateEmptyDatumReferenceBuilder  NXOpen::Annotations::AnnotationManager::CreateEmptyDatumReferenceBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  DatumReferenceBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** Specifies the material modifier condition for the datum reference */
            public: enum DatumReferenceMaterialCondition
            {
                DatumReferenceMaterialConditionNone/** none */,
                DatumReferenceMaterialConditionLeastMaterialCondition/** least material condition */,
                DatumReferenceMaterialConditionMaximumMaterialCondition/** maximum material condition */,
                DatumReferenceMaterialConditionRegardlessOfFeatureSize/** regardless of size */
            };

            private: DatumReferenceBuilderImpl * m_datumreferencebuilder_impl;
            private: friend class  _DatumReferenceBuilderBuilder;
            protected: DatumReferenceBuilder();
            public: ~DatumReferenceBuilder();
            /**Returns  the datum reference datum letter 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Letter
            (
            );
            /**Sets  the datum reference datum letter 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetLetter
            (
                const NXString & datumReferenceDatum /** datumreferencedatum */ 
            );
            /**Sets  the datum reference datum letter 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            void SetLetter
            (
                const char * datumReferenceDatum /** datumreferencedatum */ 
            );
            /**Returns  the datum reference material condition 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DatumReferenceBuilder::DatumReferenceMaterialCondition MaterialCondition
            (
            );
            /**Sets  the datum reference material condition 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetMaterialCondition
            (
                NXOpen::Annotations::DatumReferenceBuilder::DatumReferenceMaterialCondition materialCondition /** materialcondition */ 
            );
            /**Returns  the datum reference free state 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool FreeState
            (
            );
            /**Sets  the datum reference free state 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetFreeState
            (
                bool datumReferenceFreeState /** datumreferencefreestate */ 
            );
            /**Returns  the datum reference projected 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool Projected
            (
            );
            /**Sets  the datum reference projected 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetProjected
            (
                bool datumReferenceProjected /** datumreferenceprojected */ 
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