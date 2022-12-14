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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/WeldAssistant.hxx>
#include <NXOpen/Weld_PointMarkBuilder.hxx>
#include <NXOpen/ugmath.hxx>
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
        class AutoPointBuilder;
    }
    namespace Assemblies
    {
        class SelectComponentList;
    }
    class Builder;
    namespace Features
    {
        class SelectFeatureList;
    }
    class NXObject;
    namespace Weld
    {
        class _AutoPointBuilderBuilder;
        class AutoPointBuilderImpl;
        /** Represents a @link NXOpen::Weld::AutoPointBuilder NXOpen::Weld::AutoPointBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Weld::WeldManager::CreateAutoPointBuilder  NXOpen::Weld::WeldManager::CreateAutoPointBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        DistanceFromEnds </td> <td> 
         
        15.0 (millimeters part), 0.5 (inches part) </td> </tr> 

        <tr><td> 
         
        FaceGapDistance </td> <td> 
         
        1.5 (millimeters part), 0.05 (inches part) </td> </tr> 

        <tr><td> 
         
        MaximumBendRadius </td> <td> 
         
        16 (millimeters part), 0.75 (inches part) </td> </tr> 

        <tr><td> 
         
        MaximumCenterlineWidth </td> <td> 
         
        100 (millimeters part), 4 (inches part) </td> </tr> 

        <tr><td> 
         
        MaximumSingleThickness </td> <td> 
         
        2 (millimeters part), 0.08 (inches part) </td> </tr> 

        <tr><td> 
         
        MaximumSpacingBetweenPoints </td> <td> 
         
        50 (millimeters part), 2.0 (inches part) </td> </tr> 

        <tr><td> 
         
        MimimumNumberPointsOnOverlap </td> <td> 
         
        3 </td> </tr> 

        <tr><td> 
         
        MinimumFlangeWidth </td> <td> 
         
        6.0 (millimeters part), 0.25 (inches part) </td> </tr> 

        <tr><td> 
         
        MinimumSpacingBetweenPoints </td> <td> 
         
        25 (millimeters part), 1.0 (inches part) </td> </tr> 

        <tr><td> 
         
        OffsetDistanceFromEdge </td> <td> 
         
        6.25 (millimeters part), 0.25 (inches part) </td> </tr> 

        <tr><td> 
         
        ReuseMatchTolerance </td> <td> 
         
        1.0 (millimeters part), 0.04 (inches part) </td> </tr> 

        <tr><td> 
         
        UniformSpacingTolerance </td> <td> 
         
        4 (millimeters part), 0.16 (inches part) </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  AutoPointBuilder : public NXOpen::Builder
        {
            /** Settings to indicate whether new features should be created, or if features will be reused. */
            public: enum Types
            {
                TypesNew/** new points are being created */,
                TypesMove/** move existing points         */
            };

            /** Setting to indicate the default weld csys Z direction. */
            public: enum ZDirection
            {
                ZDirectionFaceNormal/** along face normal  */,
                ZDirectionOpposite/** opposite face normal */
            };

            /** The type of orientation method for defining the default coordinate system. */
            public: enum OrientationMethodTypes
            {
                OrientationMethodTypesSurfaceNormal/** Surface Normals. */,
                OrientationMethodTypesCoordinateSystem/** Use fixed csys instead of surface normals. */
            };

            /** Settings to indicate whether an interference is near an existing weld point. */
            public: enum InterferenceDetails
            {
                InterferenceDetailsNoWeldsNearBodies/** Indicates no existing weld points are in this interference area */,
                InterferenceDetailsSame/** Indicates weld points exist and part name are the same. */,
                InterferenceDetailsReplaced/** Indicates weld points exist and part names have changed. */,
                InterferenceDetailsAdded/** Indicates weld points exist and parts were added. */,
                InterferenceDetailsDeleted/** Indicates weld points exist and parts were removed. */
            };

            private: AutoPointBuilderImpl * m_autopointbuilder_impl;
            private: friend class  _AutoPointBuilderBuilder;
            protected: AutoPointBuilder();
            public: ~AutoPointBuilder();
            /**Returns  the type of creation. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::AutoPointBuilder::Types Type
            (
            );
            /**Sets  the type of creation. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetType
            (
                NXOpen::Weld::AutoPointBuilder::Types type /** type */ 
            );
            /**Returns  the components that should be welded together. This can be one components, or many. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::SelectComponentList * ComponentsToJoin
            (
            );
            /**Returns  the components to treat as unit. No interferences will be found within this component. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::SelectComponentList * ComponentsTreatAsUnit
            (
            );
            /**Returns  the feature to reuse intead of creating new.  These features will be updated instead of creating new. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SelectFeatureList * ReuseFeatures
            (
            );
            /** Finds all the interference areas between the selected components. This
                        must be executed or no weld points will be created. The number of regions is 
                        used as an index to get the interference status. The first index is 0. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: int FindNumberOfInterferenceRegions
            (
            );
            /** Creates a feature set containing weld points for a given interference. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::NXObject * CreateFeatureSet
            (
                int interferenceIndex /**  Index to the desired interference */
            );
            /** The status indicating if the interference has existing weld points touching it. The
                        index for this function is described in the find number of interference regions method. 
             <br>  Created in NX7.5.4.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::AutoPointBuilder::InterferenceDetails GetInterferenceDetails
            (
                int interferenceIndex /**  Index to the desired interference */
            );
            /**Returns  the face gap distance. This will be used to find interferences between bodies. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double FaceGapDistance
            (
            );
            /**Sets  the face gap distance. This will be used to find interferences between bodies. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetFaceGapDistance
            (
                double faceGapDistance /** facegapdistance */ 
            );
            /**Returns  the mimimum number points to create on an overlap sheet 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: int MimimumNumberPointsOnOverlap
            (
            );
            /**Sets  the mimimum number points to create on an overlap sheet 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetMimimumNumberPointsOnOverlap
            (
                int mimimumNumberPointsOnOverlap /** mimimumnumberpointsonoverlap */ 
            );
            /**Returns  the minimum spacing between points 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double MinimumSpacingBetweenPoints
            (
            );
            /**Sets  the minimum spacing between points 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetMinimumSpacingBetweenPoints
            (
                double minimumSpacingBetweenPoints /** minimumspacingbetweenpoints */ 
            );
            /**Returns  the maximum spacing between points 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double MaximumSpacingBetweenPoints
            (
            );
            /**Sets  the maximum spacing between points 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetMaximumSpacingBetweenPoints
            (
                double maximumSpacingBetweenPoints /** maximumspacingbetweenpoints */ 
            );
            /**Returns  the distance that maximum spacing can be exceeded to achieve uniform spacing 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: double UniformSpacingTolerance
            (
            );
            /**Sets  the distance that maximum spacing can be exceeded to achieve uniform spacing 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetUniformSpacingTolerance
            (
                double uniformSpacingTolerance /** uniformspacingtolerance */ 
            );
            /**Returns  the offset distance from edge 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double OffsetDistanceFromEdge
            (
            );
            /**Sets  the offset distance from edge 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetOffsetDistanceFromEdge
            (
                double offsetDistanceFromEdge /** offsetdistancefromedge */ 
            );
            /**Returns  the maximum centerline width. Points will be created using the centerline method
                        if the smallest width is less than this value. If greater, points will be
                        created using the offset from edge method. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double MaximumCenterlineWidth
            (
            );
            /**Sets  the maximum centerline width. Points will be created using the centerline method
                        if the smallest width is less than this value. If greater, points will be
                        created using the offset from edge method. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetMaximumCenterlineWidth
            (
                double maximumCenterlineWidth /** maximumcenterlinewidth */ 
            );
            /**Returns  the maximum single metal thinkness for all the selected components.
                        If the distance between top faces of two panels (or sheets) is greater
                        than single thickness plus face gap distance, a point will not be created
                        at that location. 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : None */
            public: double MaximumSingleThickness
            (
            );
            /**Sets  the maximum single metal thinkness for all the selected components.
                        If the distance between top faces of two panels (or sheets) is greater
                        than single thickness plus face gap distance, a point will not be created
                        at that location. 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetMaximumSingleThickness
            (
                double maximumSingleThickness /** maximumsinglethickness */ 
            );
            /**Returns  the bend radius of a flange.  Points will not be put on faces with a 
                        radius smaller than this value. 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : None */
            public: double MaximumBendRadius
            (
            );
            /**Sets  the bend radius of a flange.  Points will not be put on faces with a 
                        radius smaller than this value. 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetMaximumBendRadius
            (
                double maximumBendRadius /** maximumbendradius */ 
            );
            /**Returns  the minimum flange width. If opposite sides of a flange are smaller than
                        minimum flange width, it will be ignored. 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : None */
            public: double MinimumFlangeWidth
            (
            );
            /**Sets  the minimum flange width. If opposite sides of a flange are smaller than
                        minimum flange width, it will be ignored. 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetMinimumFlangeWidth
            (
                double minimumFlangeWidth /** minimumflangewidth */ 
            );
            /**Returns  the distance used to determine if the location of an existing weld feature is coincident with the 
                        newly calculated location. If the locations are coincident, then the existing weld feature location will be reused.
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: double ReuseMatchTolerance
            (
            );
            /**Sets  the distance used to determine if the location of an existing weld feature is coincident with the 
                        newly calculated location. If the locations are coincident, then the existing weld feature location will be reused.
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetReuseMatchTolerance
            (
                double reuseMatchTolerance /** reusematchtolerance */ 
            );
            /**Returns  the distance from the ends to start creating weld points at 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double DistanceFromEnds
            (
            );
            /**Sets  the distance from the ends to start creating weld points at 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetDistanceFromEnds
            (
                double distanceFromEnds /** distancefromends */ 
            );
            /**Returns  the weld point type to create 
             <br>  @deprecated Deprecated in NX10.0.0.  Use overloaded function with PointMark enum instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  Use overloaded function with PointMark enum instead.") NXOpen::Weld::WeldFeatureSetType WeldType
            (
            );
            /**Sets  the weld point type to create 
             <br>  @deprecated Deprecated in NX10.0.0.  Use overloaded function with PointMark enum instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  Use overloaded function with PointMark enum instead.") void SetWeldType
            (
                NXOpen::Weld::WeldFeatureSetType weldPointType /** weldpointtype */ 
            );
            /** Gets the weld type references in the customer defaults to create. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::PointMarkBuilder::WeldTypes GetWeldType
            (
            );
            /** Sets the weld type references in the customer defaults to create. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetWeldType
            (
                NXOpen::Weld::PointMarkBuilder::WeldTypes weldType /** weldtype */ 
            );
            /**Returns  the direction of the Z axis of the coordinate system for the feature. 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::AutoPointBuilder::ZDirection DefaultZDirection
            (
            );
            /**Sets  the direction of the Z axis of the coordinate system for the feature. 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetDefaultZDirection
            (
                NXOpen::Weld::AutoPointBuilder::ZDirection defaultZDirection /** defaultzdirection */ 
            );
            /**Returns  the orientation method for defining a csys 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::AutoPointBuilder::OrientationMethodTypes OrientationMethod
            (
            );
            /**Sets  the orientation method for defining a csys 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetOrientationMethod
            (
                NXOpen::Weld::AutoPointBuilder::OrientationMethodTypes orientationMethod /** orientationmethod */ 
            );
            /**Returns  the rotation matrix to use for defining the feature csys. 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Matrix3x3 ManipulatorMatrix
            (
            );
            /**Sets  the rotation matrix to use for defining the feature csys. 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetManipulatorMatrix
            (
                const NXOpen::Matrix3x3 & manipulatorMatrix /** manipulatormatrix */ 
            );
            /** Indicates whether the csys should be displayed on creation 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetDisplayCsys
            (
                bool showCsys /** showcsys */ 
            );
            /** Indicates whether the output point should show thru on creation 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetShowThruState
            (
                bool showThruState /** showthrustate */ 
            );
            /** Indicates the display mode. The created feature output can be shown as a solid or point. 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetShowSolids
            (
                bool showSolids /** showsolids */ 
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
