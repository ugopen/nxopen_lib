#ifndef NXOpen_CAM_FEATURERECOGNITIONBUILDER_HXX_INCLUDED
#define NXOpen_CAM_FEATURERECOGNITIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_FeatureRecognitionBuilder.ja
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
#include <NXOpen/CAM_FeatureRecognitionBuilder.hxx>
#include <NXOpen/CAM_ManualFeatureBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class FeatureRecognitionBuilder;
    }
    class Builder;
    namespace CAM
    {
        class CAMFeature;
    }
    namespace CAM
    {
        class ManualFeatureBuilder;
    }
    namespace CAM
    {
        class ManualFeatureBuilderList;
    }
    class Direction;
    class DisplayableObject;
    class Face;
    class ScCollector;
    class SelectBodyList;
    class TaggedObject;
    namespace CAM
    {
        class _FeatureRecognitionBuilderBuilder;
        class FeatureRecognitionBuilderImpl;
        /** Represents a FeatureRecognition Builder  <br> To create a new instance of this class, use @link CAM::CAMSetup::CreateFeatureRecognitionBuilder CAM::CAMSetup::CreateFeatureRecognitionBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  FeatureRecognitionBuilder : public Builder
        {
            /** the type of feature search */
            public: enum RecognitionEnum
            {
                RecognitionEnumIdentify/** Feature Identification from modeling features */,
                RecognitionEnumParametric/** Parametric Feature Recognition */,
                RecognitionEnumLegacy/** Legacy Hole Feature Recognition */,
                RecognitionEnumGeneric/** Legacy Face and Pocket Feature Recognition */,
                RecognitionEnumManual/** Manual Feature Recognition */
            };

            /** the method of body selection 
             @deprecated Deprecated in NX7.5.0 <br> 
            */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") enum FindBodyEnum
            {
                FindBodyEnumWorkpiece/** Search for features in bodies from workpiece */,
                FindBodyEnumAllBodies/** Search for features in all bodies */,
                FindBodyEnumSpecified/** Search for features in user-selected bodies */
            };

            /** the geometry search type */
            public: enum GeometrySearch
            {
                GeometrySearchWorkpiece/** Search for features in workpiece */,
                GeometrySearchAllGeometry/** Search for features in all geometry */,
                GeometrySearchSelected/** Search for features in user-selected geometry */
            };

            private: FeatureRecognitionBuilderImpl * m_featurerecognitionbuilder_impl;
            private: friend class  _FeatureRecognitionBuilderBuilder;
            protected: FeatureRecognitionBuilder();
            public: ~FeatureRecognitionBuilder();
            /**Returns  the type of feature search  <br> License requirements : None */
            public: NXOpen::CAM::FeatureRecognitionBuilder::RecognitionEnum RecognitionType
            (
            );
            /**Sets  the type of feature search  <br> License requirements : None */
            public: void SetRecognitionType
            (
                NXOpen::CAM::FeatureRecognitionBuilder::RecognitionEnum recognitionType /** recognition type */ 
            );
            /**Returns  the bodies to search 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::SelectBodyList * SelBodiesToSearch
            (
            );
            /** Returns the geometry search  @return   <br> License requirements : None */
            public: std::vector<NXOpen::DisplayableObject *> GetSearchGeometry
            (
            );
            /** Sets the geometry to search  <br> License requirements : None */
            public: void SetSearchGeometry
            (
                const std::vector<NXOpen::DisplayableObject *> & objects /** objects */ 
            );
            /**Returns  the method of body selection 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::CAM::FeatureRecognitionBuilder::FindBodyEnum CmbFindBodyFrom
            (
            );
            /**Returns  the method of geometry search  <br> License requirements : None */
            public: NXOpen::CAM::FeatureRecognitionBuilder::GeometrySearch GeometrySearchType
            (
            );
            /**Sets  the method of body selection 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") void SetCmbFindBodyFrom
            (
                NXOpen::CAM::FeatureRecognitionBuilder::FindBodyEnum cmbFindBodyType /** cmbfindbodytype */ 
            );
            /**Sets  the method of geometry search  <br> License requirements : None */
            public: void SetGeometrySearchType
            (
                NXOpen::CAM::FeatureRecognitionBuilder::GeometrySearch geometrySearch /** geometry search */ 
            );
            /**Returns  the machining access direction vector  <br> License requirements : None */
            public: NXOpen::Direction * VecDirection
            (
            );
            /**Sets  the machining access direction vector  <br> License requirements : None */
            public: void SetVecDirection
            (
                NXOpen::Direction * vecDirection /** vecdirection */ 
            );
            /**Returns  the limited set of faces to search in  <br> License requirements : None */
            public: NXOpen::ScCollector * LimitFaces
            (
            );
            /**Returns  the floor faces  <br> License requirements : None */
            public: NXOpen::ScCollector * FloorFaces
            (
            );
            /**Returns  the flag indicating whether the feature name will be used as feature type  <br> License requirements : None */
            public: bool UseFeatureNameAsType
            (
            );
            /**Sets  the flag indicating whether the feature name will be used as feature type  <br> License requirements : None */
            public: void SetUseFeatureNameAsType
            (
                bool useFeatureNameAsType /** use feature name as type */ 
            );
            /**Returns  the flag indicating whether features will get a color assigned if their faces have a unique color that is different from the body color  <br> License requirements : None */
            public: bool AssignColor
            (
            );
            /**Sets  the flag indicating whether features will get a color assigned if their faces have a unique color that is different from the body color  <br> License requirements : None */
            public: void SetAssignColor
            (
                bool assignColor /** assign color */ 
            );
            /**Returns  the flag indicating whether features will get attributes added of enclosed modeling features  <br> License requirements : None */
            public: bool AddCadFeatureAttributes
            (
            );
            /**Sets  the flag indicating whether features will get attributes added of enclosed modeling features  <br> License requirements : None */
            public: void SetAddCadFeatureAttributes
            (
                bool addCadAttributes /** add cad attributes */ 
            );
            /**Returns  the flag indicating whether features will be mapped to other features if possible  <br> License requirements : None */
            public: bool MapFeatures
            (
            );
            /**Sets  the flag indicating whether features will be mapped to other features if possible  <br> License requirements : None */
            public: void SetMapFeatures
            (
                bool mapFeatures /** map features */ 
            );
            /** Finds manufacturing features  @return  The found features <br> License requirements : None */
            public: std::vector<NXOpen::CAM::CAMFeature *> FindFeatures
            (
            );
            /** Finds manufacturing features 
                     <br> This method is deprecated. Use @link CAM::FeatureRecognitionBuilder::FindFeatures CAM::FeatureRecognitionBuilder::FindFeatures@endlink  instead.
                     <br>   @return  The found features
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") std::vector<NXOpen::TaggedObject *> Recognize
            (
            );
            /**Returns  the flag indicating if mapping is enabled. Only when a valid mapping module is loaded 
                        the feature mapper is enabled <br> License requirements : None */
            public: bool FeatureMapperEnabled
            (
            );
            /** Returns the found features  @return   <br> License requirements : None */
            public: std::vector<NXOpen::CAM::CAMFeature *> GetFoundFeatures
            (
            );
            /** Returns the found features         
                     <br> This method is deprecated. Use @link CAM::FeatureRecognitionBuilder::GetFoundFeatures CAM::FeatureRecognitionBuilder::GetFoundFeatures@endlink  instead.
                     <br>   @return  
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") std::vector<NXOpen::TaggedObject *> GetRecognizedFeatures
            (
            );
            /** Sets the feature types used by the recognizer  <br> License requirements : None */
            public: void SetFeatureTypes
            (
                std::vector<NXString> & featureTypes /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the registered feature types  <br> License requirements : None */
            public: void GetRegisteredFeatureTypes
            (
                std::vector<NXString> & featureTypes /** feature types */ 
            );
            /** Creates a new manual feature builder  @return  feature builder  <br> License requirements : None */
            public: NXOpen::CAM::ManualFeatureBuilder * CreateManualFeatureBuilder
            (
            );
            /**Returns  the manual feature builder list <br> License requirements : None */
            public: NXOpen::CAM::ManualFeatureBuilderList * LstManualFeatures
            (
            );
            /** Creates a feature based on name, floor and wall faces  @return   <br> License requirements : None */
            public: NXOpen::CAM::CAMFeature * MakeFeature
            (
                const NXString & featureName /** name of new feature   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const std::vector<NXOpen::Face *> & faces /** floor faces of new feature */,
                const std::vector<NXOpen::Face *> & wallFaces /** wall faces of new feature */,
                bool deleteFeatures /** Deletes previous found features */
            );
            /** Creates a feature based on name, floor and wall faces                 
                     <br> This method is deprecated. Use @link CAM::FeatureRecognitionBuilder::MakeFeature CAM::FeatureRecognitionBuilder::MakeFeature@endlink  instead.
                     <br>   @return  
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::TaggedObject * CreateFeature
            (
                const NXString & featureName /** name of new feature   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const std::vector<NXOpen::Face *> & faces /** floor faces of new feature */,
                const std::vector<NXOpen::Face *> & wallFaces /** wall faces of new feature */,
                bool deleteFeatures /** Deletes previous found features */
            );
            /** Deletes a manufacturing feature that was created through this builder instance  <br> License requirements : None */
            public: void DeleteFeature
            (
                NXOpen::CAM::CAMFeature * feature /** feature */ 
            );
            /** Deletes manufacturing feature that was created through this builder instance      
                     <br> This method is deprecated. Use the overloaded version of this method
                    that takes @link CAM::CAMFeature CAM::CAMFeature@endlink  instead.
                     <br>  
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") void DeleteFeature
            (
                NXOpen::TaggedObject * feature /** feature */ 
            );
            /**Returns  the flag indicating whether found features are checked agains existing features. If this
                        flag is set then features are recognized even if they match existing features.   <br> License requirements : None */
            public: bool IgnoreExistingFeatures
            (
            );
            /**Sets  the flag indicating whether found features are checked agains existing features. If this
                        flag is set then features are recognized even if they match existing features.   <br> License requirements : None */
            public: void SetIgnoreExistingFeatures
            (
                bool ignoreExistingFeatures /** ignore existing features */ 
            );
            /** Gets the modeling feature types from the bodies currently set in this builder <br> License requirements : None */
            public: void GetModelingFeatureTypes
            (
                std::vector<NXString> & featureTypes /** feature types */ 
            );
            /**Returns  the flag indicating whether to ignore warnings while finding features.   <br> License requirements : None */
            public: bool IgnoreWarnings
            (
            );
            /**Sets  the flag indicating whether to ignore warnings while finding features.   <br> License requirements : None */
            public: void SetIgnoreWarnings
            (
                bool ignoreWarnings /** ignore warnings */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
