#ifndef NXOpen_ANNOTATIONS_FEATURECONTROLFRAMEINDICATORBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_FEATURECONTROLFRAMEINDICATORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_FeatureControlFrameIndicatorBuilder.ja
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
        class FeatureControlFrameIndicatorBuilder;
    }
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
        class _FeatureControlFrameIndicatorBuilderBuilder;
        class FeatureControlFrameIndicatorBuilderImpl;
        /**
            Represents a FcfIndicatorBuilder
             <br> To create a new instance of this class, use @link NXOpen::Annotations::AnnotationManager::CreateFeatureControlFrameIndicatorBuilder  NXOpen::Annotations::AnnotationManager::CreateFeatureControlFrameIndicatorBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  FeatureControlFrameIndicatorBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** Specifies the type of FCF indicator */
            public: enum FcfIndicatorType
            {
                FcfIndicatorTypeIntersectionPlane/** intersection plane */ ,
                FcfIndicatorTypeOrientationPlane/** orientation plane */ ,
                FcfIndicatorTypeCollectionPlane/** collection plane */ ,
                FcfIndicatorTypeDirectionFeature/** direction feature */ 
            };

            /** Specifies the characteristic of the FCF indicator */
            public: enum FcfIndicatorCharacteristic
            {
                FcfIndicatorCharacteristicParallel/** parallel */ ,
                FcfIndicatorCharacteristicPerpendicular/** perpendicular */ ,
                FcfIndicatorCharacteristicAngular/** angular */ ,
                FcfIndicatorCharacteristicIncluding/** including */ 
            };

            /** Specifies the direction of the FCF indicator */
            public: enum FcfIndicatorDirection
            {
                FcfIndicatorDirectionAfter/** after */ ,
                FcfIndicatorDirectionBefore/** before */ 
            };

            private: FeatureControlFrameIndicatorBuilderImpl * m_featurecontrolframeindicatorbuilder_impl;
            private: friend class  _FeatureControlFrameIndicatorBuilderBuilder;
            protected: FeatureControlFrameIndicatorBuilder();
            public: ~FeatureControlFrameIndicatorBuilder();
            /**Returns  the indicator type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::FeatureControlFrameIndicatorBuilder::FcfIndicatorType IndicatorType
            (
            );
            /**Sets  the indicator type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetIndicatorType
            (
                NXOpen::Annotations::FeatureControlFrameIndicatorBuilder::FcfIndicatorType indicatorType /** indicatortype */ 
            );
            /**Returns  the charactersitic 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::FeatureControlFrameIndicatorBuilder::FcfIndicatorCharacteristic Symbol
            (
            );
            /**Sets  the charactersitic 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetSymbol
            (
                NXOpen::Annotations::FeatureControlFrameIndicatorBuilder::FcfIndicatorCharacteristic symbol /** symbol */ 
            );
            /**Returns  the label 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DatumReferenceBuilder * Label
            (
            );
            /**Returns  the direction 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::FeatureControlFrameIndicatorBuilder::FcfIndicatorDirection Direction
            (
            );
            /**Sets  the direction 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetDirection
            (
                NXOpen::Annotations::FeatureControlFrameIndicatorBuilder::FcfIndicatorDirection direction /** direction */ 
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