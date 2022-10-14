#ifndef NXOpen_WELD_JOINTMARKBUILDER_HXX_INCLUDED
#define NXOpen_WELD_JOINTMARKBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_JointmarkBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Weld_CharacteristicsBuilder.hxx>
#include <NXOpen/Weld_ConnectedPart.hxx>
#include <NXOpen/Weld_JointmarkFaceSetsBuilder.hxx>
#include <NXOpen/Weld_JointmarkGuideBuilder.hxx>
#include <NXOpen/Weld_JointmarkPointsBuilder.hxx>
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
        class JointmarkBuilder;
    }
    class CoordinateSystem;
    class Curve;
    class Direction;
    class Edge;
    class Expression;
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class SelectFeatureList;
    }
    class NXObject;
    class Plane;
    class SelectPointList;
    class SelectTaggedObjectList;
    namespace Weld
    {
        class CharacteristicsBuilder;
    }
    namespace Weld
    {
        class ConnectedPart;
    }
    namespace Weld
    {
        class JointmarkFaceSetsBuilder;
    }
    namespace Weld
    {
        class JointmarkFaceSetsBuilderList;
    }
    namespace Weld
    {
        class JointmarkGuideBuilder;
    }
    namespace Weld
    {
        class JointmarkGuideBuilderList;
    }
    namespace Weld
    {
        class JointmarkPointsBuilder;
    }
    namespace Weld
    {
        class JointmarkPointsBuilderList;
    }
    namespace Weld
    {
        class _JointmarkBuilderBuilder;
        class JointmarkBuilderImpl;
        /** Represents a @link NXOpen::Weld::Jointmark NXOpen::Weld::Jointmark@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Weld::WeldManager::CreateJointmarkBuilder  NXOpen::Weld::WeldManager::CreateJointmarkBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        Associativity </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        ConnectPart (deprecated) </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        ConnectPartType </term> <description> 
         
        AllUniqueParts </description> </item> 

        <item><term> 
         
        ConstructionMethod </term> <description> 
         
        GuideCurve </description> </item> 

        <item><term> 
         
        CreateSingleFeatures </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        OrientationMethod </term> <description> 
         
        SurfaceNormal </description> </item> 

        <item><term> 
         
        ReferenceSheetType </term> <description> 
         
        Overlap </description> </item> 

        <item><term> 
         
        ReuseFeaturesMethod </term> <description> 
         
        SameConnectingParts </description> </item> 

        <item><term> 
         
        ShowWorkCsys </term> <description> 
         
        1 </description> </item> 

        </list> 

         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  JointmarkBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** The type of construction method for creating Jointmark */
            public: enum Method
            {
                MethodGuideCurve/** Guide Curve */,
                MethodMirror/** Mirror      */,
                MethodPoints/** Points      */,
                MethodTranslate/** Translate   */,
                MethodExistingPoints/** Existing Points. Only allowed for @link NXOpen::Weld::PointMark NXOpen::Weld::PointMark@endlink  class. */
            };

            /** The type of connect part */
            public: enum ConnectPartTypes
            {
                ConnectPartTypesAllUniqueParts/** All unique parts */,
                ConnectPartTypesOnlyOnePart/** Only one part    */,
                ConnectPartTypesIgnoreFiltering/** Ignore Filtering */
            };

            /** The type of sheets to create */
            public: enum ReferenceSheetTypes
            {
                ReferenceSheetTypesOverlap/** Overlap */,
                ReferenceSheetTypesTop/** Top     */
            };

            /** The type of sheets to create */
            public: enum ConnectedPanelTypes
            {
                ConnectedPanelTypesTwo/** two */ ,
                ConnectedPanelTypesThree/** three */ ,
                ConnectedPanelTypesFour/** four */ 
            };

            /** The method to indicate if all reuse features have the same connected parts */
            public: enum ReuseMethod
            {
                ReuseMethodSameConnectingParts/** same connecting parts */ ,
                ReuseMethodAnyConnectingParts/** any connecting parts */ 
            };

            /** The projection direction used to project points onto the reference sheet */
            public: enum ProjectionDirectionOptions
            {
                ProjectionDirectionOptionsNone/** none */ ,
                ProjectionDirectionOptionsAlongFaceNormal/** along face normal */ ,
                ProjectionDirectionOptionsPricipalAxis/** pricipal axis */ ,
                ProjectionDirectionOptionsX/** x */ ,
                ProjectionDirectionOptionsY/** y */ ,
                ProjectionDirectionOptionsZ/** z */ 
            };

            /** The type of orientation method for defining the default coordinate system. */
            public: enum OrientationMethodTypes
            {
                OrientationMethodTypesSurfaceNormal/** Surface Normals. */,
                OrientationMethodTypesCoordinateSystem/** Use fixed csys instead of surface normals. */
            };

            private: JointmarkBuilderImpl * m_jointmarkbuilder_impl;
            private: friend class  _JointmarkBuilderBuilder;
            protected: JointmarkBuilder();
            public: ~JointmarkBuilder();
            /**Returns  the construction method for creating Jointmark 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::JointmarkBuilder::Method ConstructionMethod
            (
            );
            /**Sets  the construction method for creating Jointmark 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetConstructionMethod
            (
                NXOpen::Weld::JointmarkBuilder::Method method /** method */ 
            );
            /**Returns  the method used to infer feature parameters if all connected parts are the same, or skip inferring due to connected parts being different. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::JointmarkBuilder::ReuseMethod ReuseFeaturesMethod
            (
            );
            /**Sets  the method used to infer feature parameters if all connected parts are the same, or skip inferring due to connected parts being different. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetReuseFeaturesMethod
            (
                NXOpen::Weld::JointmarkBuilder::ReuseMethod reuseMethod /** reusemethod */ 
            );
            /**Returns  the automatic update option also known as associativity. If true, the curve representing the Jointmark feature will change its location if the guide curve is updated
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: bool Associativity
            (
            );
            /**Sets  the automatic update option also known as associativity. If true, the curve representing the Jointmark feature will change its location if the guide curve is updated
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetAssociativity
            (
                bool associativity /** associativity */ 
            );
            /**Returns  the selected objects for mirror. These objects can be features or curves representing Jointmark 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::SelectTaggedObjectList * SelectMirrorObject
            (
            );
            /**Returns  the plane used for mirror
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Plane * Plane
            (
            );
            /**Sets  the plane used for mirror
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetPlane
            (
                NXOpen::Plane * plane /** plane */ 
            );
            /**Returns  the selected objects to translate. These objects can be features or curves representing Jointmark 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::SelectTaggedObjectList * SelectTranslateObject
            (
            );
            /**Returns  the coordinate system that defines the translate offset directions. If not specified the absolute csys will be used.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CoordinateSystem * TranslateCsys
            (
            );
            /**Sets  the coordinate system that defines the translate offset directions. If not specified the absolute csys will be used.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetTranslateCsys
            (
                NXOpen::CoordinateSystem * csys /** csys */ 
            );
            /**Returns  the expression containing the value of the x translation distance. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * TranslateX
            (
            );
            /**Returns  the expression containing the value of the y translation distance. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * TranslateY
            (
            );
            /**Returns  the expression containing the value of the z translation distance. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * TranslateZ
            (
            );
            /**Returns  the option of connecting only one part. If true, Jointmark feature is created on a single component.  
             <br>  @deprecated Deprecated in NX1872.0.0.  Use @link JA_JOINTMARK_BUILDER_get_ConnectPartType JA_JOINTMARK_BUILDER_get_ConnectPartType@endlink  instead. <br>  

             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NX_DEPRECATED("Deprecated in NX1872.0.0.  Use JA_JOINTMARK_BUILDER_get_ConnectPartType instead.") bool ConnectPart
            (
            );
            /**Sets  the option of connecting only one part. If true, Jointmark feature is created on a single component.  
             <br>  @deprecated Deprecated in NX1872.0.0.  Use @link JA_JOINTMARK_BUILDER_set_ConnectPartType JA_JOINTMARK_BUILDER_set_ConnectPartType@endlink  instead. <br>  

             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NX_DEPRECATED("Deprecated in NX1872.0.0.  Use JA_JOINTMARK_BUILDER_set_ConnectPartType instead.") void SetConnectPart
            (
                bool connectPart /** connectpart */ 
            );
            /**Returns  the option of connecting only one part. If true, Jointmark feature is created on a single component.  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::JointmarkBuilder::ConnectPartTypes ConnectPartType
            (
            );
            /**Sets  the option of connecting only one part. If true, Jointmark feature is created on a single component.  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetConnectPartType
            (
                NXOpen::Weld::JointmarkBuilder::ConnectPartTypes connectPart /** connectpart */ 
            );
            /**Returns  the type of reference sheet
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::JointmarkBuilder::ReferenceSheetTypes ReferenceSheetType
            (
            );
            /**Sets  the type of reference sheet
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetReferenceSheetType
            (
                NXOpen::Weld::JointmarkBuilder::ReferenceSheetTypes refSheet /** refsheet */ 
            );
            /**Returns  the list of face sets  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::JointmarkFaceSetsBuilderList * FaceSetsList
            (
            );
            /**Returns  the list of guide curves 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::JointmarkGuideBuilderList * GuideCurvesList
            (
            );
            /**Returns  the selected objects for Points 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::SelectPointList * SelectPointsObject
            (
            );
            /**Returns  the vector which points to Y axis 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Direction * Vector
            (
            );
            /**Sets  the vector which points to Y axis 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetVector
            (
                NXOpen::Direction * vector /** vector */ 
            );
            /** Updates all the items on the points list based on the construction method and related inputs. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void UpdateFeatures
            (
            );
            /** Updates the selected point by projecting it to the guide curve. 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void UpdatePoint
            (
            );
            /** Use the Weld Assistant Connected Face Finder command to rediscover faces based on the current feature point positions. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void RediscoverFaces
            (
            );
            /** Create a temporary overlap or top sheet and guide curve. Use with independent @link NXOpen::Weld::PointMarkPoint NXOpen::Weld::PointMarkPoint@endlink  features. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void CreateReferenceData
            (
            );
            /** Delete temporary overlap or top sheet feature. Use with independent @link NXOpen::Weld::PointMarkPoint NXOpen::Weld::PointMarkPoint@endlink  features. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void DeleteReferenceData
            (
            );
            /**Returns  the list of points
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::JointmarkPointsBuilderList * PointList
            (
            );
            /**Returns  the characteristics 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::CharacteristicsBuilder * Characteristics
            (
            );
            /** Indicates whether the csys should be displayed on creation 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetDisplayCsys
            (
                bool status /** status */ 
            );
            /** Indicates whether the output objects should show thru on creation 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetShowThruState
            (
                bool status /** status */ 
            );
            /**Returns  the distance tolerance 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distancetolerance */ 
            );
            /** Creates a @link NXOpen::Weld::JointmarkGuideBuilder NXOpen::Weld::JointmarkGuideBuilder@endlink  object. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::JointmarkGuideBuilder * NewGuide
            (
            );
            /** Creates a @link NXOpen::Weld::JointmarkFaceSetsBuilder NXOpen::Weld::JointmarkFaceSetsBuilder@endlink  object. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::JointmarkFaceSetsBuilder * NewFaceSets
            (
            );
            /** Creates a @link NXOpen::Weld::JointmarkPointsBuilder NXOpen::Weld::JointmarkPointsBuilder@endlink  object. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::JointmarkPointsBuilder * NewPoints
            (
            );
            /** Prepares a Reference Sheet for placing Jointmark features. If the sheet is suppressed, it will be unsuppressed. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Features::Feature * UpdateReferenceSheet
            (
                bool facesModified /** Indicates if Reference Sheet needs to be updated. */
            );
            /** Returns the Reference Sheet feature
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Features::Feature * GetReferenceSheet
            (
            );
            /** Edges of created sheet 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void GetSheetEdges
            (
                std::vector<NXOpen::Edge *> & edges /** edges */ 
            );
            /** Create curve From PMI symbol  @return  Curve from symbol 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Curve * CreateSymbolCurve
            (
                const NXString & path /** Symbol path */,
                const NXString & name /** Symbol id   */
            );
            /** Create curve From PMI symbol  @return  Curve from symbol 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            NXOpen::Curve * CreateSymbolCurve
            (
                const char * path /** Symbol path */,
                const char * name /** Symbol id   */
            );
            /** Creates a list of points on the overlap sheet. In addition, a curve selected by the user will be placed at these points. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void AppendPoints
            (
                bool mode /** Create or Edit */,
                NXOpen::Curve * curve /** Curve to place at these points*/
            );
            /**Returns  the projection direction option used to project @link NXOpen::Weld::JointmarkBuilder::SelectPointsObject NXOpen::Weld::JointmarkBuilder::SelectPointsObject@endlink  onto the @link NXOpen::Weld::JointmarkBuilder::GetReferenceSheet NXOpen::Weld::JointmarkBuilder::GetReferenceSheet@endlink . 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::JointmarkBuilder::ProjectionDirectionOptions ProjectionDirectionOption
            (
            );
            /**Sets  the projection direction option used to project @link NXOpen::Weld::JointmarkBuilder::SelectPointsObject NXOpen::Weld::JointmarkBuilder::SelectPointsObject@endlink  onto the @link NXOpen::Weld::JointmarkBuilder::GetReferenceSheet NXOpen::Weld::JointmarkBuilder::GetReferenceSheet@endlink . 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetProjectionDirectionOption
            (
                NXOpen::Weld::JointmarkBuilder::ProjectionDirectionOptions projectionOption /** projectionoption */ 
            );
            /**Returns  the number of connected panels at a point. This is used when the construction method is Existing Points 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::JointmarkBuilder::ConnectedPanelTypes ConnectedPanelType
            (
            );
            /**Sets  the number of connected panels at a point. This is used when the construction method is Existing Points 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetConnectedPanelType
            (
                NXOpen::Weld::JointmarkBuilder::ConnectedPanelTypes method /** method */ 
            );
            /** Maps the selected reuse features to the new preview point locations. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void MapFeaturesToPoints
            (
            );
            /** Initializes face sets, guide curve, and points builders from reuse features.  
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void FromReuseFeatures
            (
                bool* faceSetsUpdated /** Indicates if the face set list was updated. */,
                bool* guideCurvesUpdated /** Indicates if the guide curve list was updated. */,
                bool* pointSelectionUpdated /** Indicates if point selection object was updated. */
            );
            /**Returns  the selected reuse features 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Features::SelectFeatureList * ReuseFeatures
            (
            );
            /**Returns  the orientation method for defining a csys 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::JointmarkBuilder::OrientationMethodTypes OrientationMethod
            (
            );
            /**Sets  the orientation method for defining a csys 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetOrientationMethod
            (
                NXOpen::Weld::JointmarkBuilder::OrientationMethodTypes orientationMethod /** orientationmethod */ 
            );
            /**Returns  the option to control if the work coordinate system should be showing. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: bool ShowWorkCsys
            (
            );
            /**Sets  the option to control if the work coordinate system should be showing. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetShowWorkCsys
            (
                bool showWorkCsys /** showworkcsys */ 
            );
            /**Returns  the fixed csys that overrides the default Csys orientation. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::CoordinateSystem * FixedCsys
            (
            );
            /**Sets  the fixed csys that overrides the default Csys orientation. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetFixedCsys
            (
                NXOpen::CoordinateSystem * fixedCsys /** fixedcsys */ 
            );
            /**Returns  the control option to determine if individual features should be created. Only allowed for @link NXOpen::Weld::PointMark NXOpen::Weld::PointMark@endlink  class. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: bool CreateSingleFeatures
            (
            );
            /**Sets  the control option to determine if individual features should be created. Only allowed for @link NXOpen::Weld::PointMark NXOpen::Weld::PointMark@endlink  class. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetCreateSingleFeatures
            (
                bool createSingleFeatures /** true- Full associative features are created. false- single non associative features.*/
            );
            /**Returns  the option to indicate if an alert should be issued when the parent point moves.  Valid when using @link NXOpen::Weld::JointmarkBuilder::MethodExistingPoints NXOpen::Weld::JointmarkBuilder::MethodExistingPoints@endlink  and associativity is off. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: bool NotifyIfParentPointMoved
            (
            );
            /**Sets  the option to indicate if an alert should be issued when the parent point moves.  Valid when using @link NXOpen::Weld::JointmarkBuilder::MethodExistingPoints NXOpen::Weld::JointmarkBuilder::MethodExistingPoints@endlink  and associativity is off. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetNotifyIfParentPointMoved
            (
                bool notifyIfParentPointMoved /** true- provide notificaton when parent moves. false - do not provide notification. */
            );
            /** Gets the selected points, or point features, references. Does not apply to the guide curves method. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void GetSelectedReferences
            (
                std::vector<NXOpen::NXObject *> & references /**The array of references. These may be points or point features. */
            );
            /** Get all the messages created by @link NXOpen::Weld::JointmarkBuilder::CreateReferenceData NXOpen::Weld::JointmarkBuilder::CreateReferenceData@endlink . 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void GetCreateReferenceDataMessages
            (
                std::vector<NXString> & messages /** The array of messages generated during the process of discovering the reference data. */
            );
            /** Move the Reference Sheet to work layer, and unlink from grouping feature. 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void MoveReferenceSheet
            (
            );
            /**
                    Find the connected face information. 
                     <br> 
                    The data is stored in @link NXOpen::Weld::ConnectedPart NXOpen::Weld::ConnectedPart@endlink  containing the appropriate
                    connected part face occurrence information. 
                     <br>   @return  Connected face information. NULL if none are found. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::ConnectedPart * AskConnectedFaces
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