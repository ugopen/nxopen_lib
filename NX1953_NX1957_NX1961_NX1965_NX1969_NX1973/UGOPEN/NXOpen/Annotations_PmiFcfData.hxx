#ifndef NXOpen_ANNOTATIONS_PMIFCFDATA_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIFCFDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiFcfData.ja
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
#include <NXOpen/Annotations_FeatureControlFrameDataBuilder.hxx>
#include <NXOpen/Annotations_FeatureControlFrameIndicatorBuilder.hxx>
#include <NXOpen/Annotations_PmiFcfDatumData.hxx>
#include <NXOpen/Annotations_PmiSemanticData.hxx>
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
        class PmiFcfData;
    }
    namespace Annotations
    {
        class PmiFcfDatumData;
    }
    namespace Annotations
    {
        class PmiSemanticData;
    }
    namespace Annotations
    {
        class PmiFcfDataImpl;
        /** Represents PMI Feature Control Frame data. 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiFcfData : public NXOpen::Annotations::PmiSemanticData
        {
            /** Specifies unit basis types */
            public: enum PmiFcfDataUnitBasisType
            {
                PmiFcfDataUnitBasisTypeNone/** None */,
                PmiFcfDataUnitBasisTypeLength/** length type */,
                PmiFcfDataUnitBasisTypeArea/** area type */,
                PmiFcfDataUnitBasisTypeCircularArea/** circular area type */,
                PmiFcfDataUnitBasisTypeSphericalArea/** spherical area type */,
                PmiFcfDataUnitBasisTypeSquare/** square type */
            };

            private: PmiFcfDataImpl * m_pmifcfdata_impl;
            /// \cond NX_NO_DOC 
            public: explicit PmiFcfData(void *ptr);
            /// \endcond 
            /**Returns  the fcf characteristic 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::FeatureControlFrameBuilder::FcfCharacteristic Characteristic
            (
            );
            /** Returns the above feature control frame appended text. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void GetAboveAppendedText
            (
                std::vector<NXString> & textLines /** List of above appended text lines */
            );
            /** Returns the below feature control frame appended text. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void GetBelowAppendedText
            (
                std::vector<NXString> & textLines /** List of below appended text lines */
            );
            /** Returns the before feature control frame appended text. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void GetBeforeAppendedText
            (
                std::vector<NXString> & textLines /** List of before appended text lines */
            );
            /** Returns the after feature control frame appended text. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void GetAfterAppendedText
            (
                std::vector<NXString> & textLines /** List of after appended text lines */
            );
            /**Returns  the number of fcf frames 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: int FrameCount
            (
            );
            /** Returns the fcf frame tolerance zone shape 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::FeatureControlFrameDataBuilder::ToleranceZoneShape GetZoneShape
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the fcf frame tolerance value shape 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString GetToleranceValue
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the fcf frame tolerance zone modifier 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::FeatureControlFrameDataBuilder::ToleranceMaterialModifier GetToleranceZoneModifier
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame has a reciprocity requirement 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetReciprocityRequirement
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame has a free state modifier 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetFreeState
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame has a statistical modifier 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetStatistical
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame has a tangential modifier 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetTangential
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame defines a common zone 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetCommonZone
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame has a projected zone 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetProjectedZone
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the fcf frame projected zone value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString GetProjectedZoneValue
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame has an unequally disposed zone 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetUnequallyDisposedZone
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame unequally disposed zone uses the uz symbol 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetUz
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the fcf frame unequally disposed zone value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString GetUnequallyDisposedZoneValue
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame has a dynamic profile 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetDynamicProfile
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame is a derived feature 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetDerivedFeature
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame is a least squares feature 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetLeastSquaresFeature
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame is a minmax feature 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetMinmaxFeature
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame is a circumscribed feature 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetCircumscribedFeature
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame is an inscribed feature 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetInscribedFeature
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame has a maximum tolerance 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetMaxTolerance
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the fcf frame max tolerance value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString GetMaxToleranceValue
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns if the fcf frame tolerance is applied on a unit basis 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool GetUnitBasis
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the type of unit basis applied to a fcf frame 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::PmiFcfData::PmiFcfDataUnitBasisType GetUnitBasisType
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the zone shape of a unit basis applied to a fcf frame 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::FeatureControlFrameDataBuilder::AreaSymbolType GetUnitBasisZoneShape
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the fcf frame unit basis value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString GetUnitBasisValue
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the fcf frame unit basis x range 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString GetUnitBasisXRange
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the fcf frame unit basis y range 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString GetUnitBasisYRange
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the fcf frame primary datum references 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void GetPrimaryDatumReference
            (
                int frameNumber /** framenumber */ ,
                std::vector<NXOpen::Annotations::PmiFcfDatumData *> & datums /** PMI fcf datum semantic data */
            );
            /** Returns the fcf frame primary datum extended text 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString GetPrimaryDatumExtendedText
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the fcf frame secondary datum references 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void GetSecondaryDatumReference
            (
                int frameNumber /** framenumber */ ,
                std::vector<NXOpen::Annotations::PmiFcfDatumData *> & datums /** PMI fcf datum semantic data */
            );
            /** Returns the fcf frame secondary datum extended text 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString GetSecondaryDatumExtendedText
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the fcf frame tertiary datum references 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void GetTertiaryDatumReference
            (
                int frameNumber /** framenumber */ ,
                std::vector<NXOpen::Annotations::PmiFcfDatumData *> & datums /** PMI fcf datum semantic data */
            );
            /** Returns the fcf frame tertiary datum extended text 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString GetTertiaryDatumExtendedText
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the number of before indicators for a fcf frame 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: int GetBeforeIndicatorCount
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the number of after indicators for a fcf frame 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: int GetAfterIndicatorCount
            (
                int frameNumber /** framenumber */ 
            );
            /** Returns the fcf frame before indicator type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::FeatureControlFrameIndicatorBuilder::FcfIndicatorType GetBeforeIndicatorType
            (
                int frameNumber /** framenumber */ ,
                int indicatorNumber /** indicatornumber */ 
            );
            /** Returns the fcf frame after indicator type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::FeatureControlFrameIndicatorBuilder::FcfIndicatorType GetAfterIndicatorType
            (
                int frameNumber /** framenumber */ ,
                int indicatorNumber /** indicatornumber */ 
            );
            /** Returns the fcf frame before indicator characteristic 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::FeatureControlFrameIndicatorBuilder::FcfIndicatorCharacteristic GetBeforeIndicatorCharacteristic
            (
                int frameNumber /** framenumber */ ,
                int indicatorNumber /** indicatornumber */ 
            );
            /** Returns the fcf frame after indicator characteristic 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::FeatureControlFrameIndicatorBuilder::FcfIndicatorCharacteristic GetAfterIndicatorCharacteristic
            (
                int frameNumber /** framenumber */ ,
                int indicatorNumber /** indicatornumber */ 
            );
            /** Returns the fcf frame before indicator datum reference 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::PmiFcfDatumData * GetBeforeIndicatorDatumReference
            (
                int frameNumber /** framenumber */ ,
                int indicatorNumber /** indicatornumber */ 
            );
            /** Returns the fcf frame after indicator datum reference 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::PmiFcfDatumData * GetAfterIndicatorDatumReference
            (
                int frameNumber /** framenumber */ ,
                int indicatorNumber /** indicatornumber */ 
            );
        }; //lint !e1712 default constructor not defined for class  

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
