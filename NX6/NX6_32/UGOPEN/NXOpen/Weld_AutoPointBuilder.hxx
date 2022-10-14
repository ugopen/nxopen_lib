#ifndef NXOpen_WELD_AUTOPOINTBUILDER_HXX_INCLUDED
#define NXOpen_WELD_AUTOPOINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_AutoPointBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/WeldAssistant.hxx>
#include <NXOpen/Weld_AutoPointBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Weld
    {
        class AutoPointBuilder;
    }
    namespace Assemblies
    {
        class SelectComponentList;
    }
    class Builder;
    class NXObject;
    namespace Weld
    {
        class _AutoPointBuilderBuilder;
        /** Represents a @link Weld::AutoPointBuilder Weld::AutoPointBuilder@endlink  builder  <br> To create a new instance of this class, use @link Weld::WeldManager::CreateAutoPointBuilder Weld::WeldManager::CreateAutoPointBuilder@endlink  <br> 
        Default values:
        DistanceFromEnds: 15.0 (millimeters part), 0.5 (inches part)
        FaceGapDistance: 1.5 (millimeters part), 0.05 (inches part)
        MaximumCenterlineWidth: 100 (millimeters part), 4 (inches part)
        MaximumSpacingBetweenPoints: 50 (millimeters part), 2.0 (inches part)
        MimimumNumberPointsOnOverlap: 3
        MinimumSpacingBetweenPoints: 25 (millimeters part), 1.0 (inches part)
        OffsetDistanceFromEdge: 6.25 (millimeters part), 0.25 (inches part)
        */
        class NXOPENCPPEXPORT AutoPointBuilder : public Builder
        {
            /** indicates whether an interference is near existing weld points */
            public: enum InterferenceStatus
            {
                InterferenceStatusNoWeldsNearBodies/** Indicates no existing weld points are in this interference area */,
                InterferenceStatusWeldsNearBodies/** Indicates weld points exist in this interference area */
            };

            private: friend class  _AutoPointBuilderBuilder;
            protected: AutoPointBuilder();
            /**Returns  the components that should be welded together. This can be one components, or many.  <br> License requirements : None */
            public: NXOpen::Assemblies::SelectComponentList * ComponentsToJoin
            (
            );
            /**Returns  the components to treat as unit. No interferences will be found within this component.  <br> License requirements : None */
            public: NXOpen::Assemblies::SelectComponentList * ComponentsTreatAsUnit
            (
            );
            /** Finds all the interference areas between the selected components. This
                        must be executed or no weld points will be created. The number of regions is 
                        used as an index to get the interference status. The first index is 0.  @return   <br> License requirements : ugweld ("UG WELD") */
            public: int FindNumberOfInterferenceRegions
            (
            );
            /** Creates a feature set containing weld points for a given interference.  @return   <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::NXObject * CreateFeatureSet
            (
                int interferenceIndex /**  Index to the desired interference */
            );
            /** The status indicating if the interference has existing weld points touching it. The
                        index for this function is described in the find number of interference regions method.  @return   <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::AutoPointBuilder::InterferenceStatus GetInterferenceStatus
            (
                int interferenceIndex /**  Index to the desired interference */
            );
            /**Returns  the face gap distance. This will be used to find interferences between bodies.  <br> License requirements : None */
            public: double FaceGapDistance
            (
            );
            /**Sets  the face gap distance. This will be used to find interferences between bodies.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetFaceGapDistance
            (
                double faceGapDistance /** facegapdistance */ 
            );
            /**Returns  the mimimum number points to create on an overlap sheet  <br> License requirements : None */
            public: int MimimumNumberPointsOnOverlap
            (
            );
            /**Sets  the mimimum number points to create on an overlap sheet  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMimimumNumberPointsOnOverlap
            (
                int mimimumNumberPointsOnOverlap /** mimimumnumberpointsonoverlap */ 
            );
            /**Returns  the minimum spacing between points  <br> License requirements : None */
            public: double MinimumSpacingBetweenPoints
            (
            );
            /**Sets  the minimum spacing between points  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMinimumSpacingBetweenPoints
            (
                double minimumSpacingBetweenPoints /** minimumspacingbetweenpoints */ 
            );
            /**Returns  the maximum spacing between points  <br> License requirements : None */
            public: double MaximumSpacingBetweenPoints
            (
            );
            /**Sets  the maximum spacing between points  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMaximumSpacingBetweenPoints
            (
                double maximumSpacingBetweenPoints /** maximumspacingbetweenpoints */ 
            );
            /**Returns  the offset distance from edge  <br> License requirements : None */
            public: double OffsetDistanceFromEdge
            (
            );
            /**Sets  the offset distance from edge  <br> License requirements : ugweld ("UG WELD") */
            public: void SetOffsetDistanceFromEdge
            (
                double offsetDistanceFromEdge /** offsetdistancefromedge */ 
            );
            /**Returns  the maximum centerline width. Points will be created using the centerline method
                        if the smallest width is less than this value. If greater, points will be
                        created using the offset from edge method.  <br> License requirements : None */
            public: double MaximumCenterlineWidth
            (
            );
            /**Sets  the maximum centerline width. Points will be created using the centerline method
                        if the smallest width is less than this value. If greater, points will be
                        created using the offset from edge method.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMaximumCenterlineWidth
            (
                double maximumCenterlineWidth /** maximumcenterlinewidth */ 
            );
            /**Returns  the distance from the ends to start creating weld points at  <br> License requirements : None */
            public: double DistanceFromEnds
            (
            );
            /**Sets  the distance from the ends to start creating weld points at  <br> License requirements : ugweld ("UG WELD") */
            public: void SetDistanceFromEnds
            (
                double distanceFromEnds /** distancefromends */ 
            );
            /**Returns  the weld point type to create  <br> License requirements : None */
            public: NXOpen::Weld::WeldFeatureSetType WeldType
            (
            );
            /**Sets  the weld point type to create  <br> License requirements : ugweld ("UG WELD") */
            public: void SetWeldType
            (
                NXOpen::Weld::WeldFeatureSetType weldPointType /** weldpointtype */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif