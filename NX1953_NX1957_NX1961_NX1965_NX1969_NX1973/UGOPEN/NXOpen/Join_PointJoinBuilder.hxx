#ifndef NXOpen_JOIN_POINTJOINBUILDER_HXX_INCLUDED
#define NXOpen_JOIN_POINTJOINBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Join_PointJoinBuilder.ja
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
#include <NXOpen/Join_PointJoinHardware.hxx>
#include <NXOpen/Join_JoinBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libjoinopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Join
    {
        class PointJoinBuilder;
    }
    class Expression;
    namespace Join
    {
        class JoinBuilder;
    }
    namespace Join
    {
        class PointJoinHardware;
    }
    class Point;
    class ScCollector;
    class SelectPointList;
    class TaggedObject;
    namespace Join
    {
        class _PointJoinBuilderBuilder;
        class PointJoinBuilderImpl;
        /**
            Represents a @link NXOpen::Join::PointJoin NXOpen::Join::PointJoin@endlink  builder.
             <br> To create a new instance of this class, use @link NXOpen::Join::JoinManager::CreatePointJoinBuilder  NXOpen::Join::JoinManager::CreatePointJoinBuilder @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class JOINOPENCPPEXPORT  PointJoinBuilder : public NXOpen::Join::JoinBuilder
        {
            /** the stackup alignment type */
            public: enum StackupAlignmentTypes
            {
                StackupAlignmentTypesNormalClosestFace/** normal closest face */ ,
                StackupAlignmentTypesNormalSelectedFace/** normal selected face */ ,
                StackupAlignmentTypesAlongVector/** along vector */ 
            };

            /** the visualization geometry type */
            public: enum VisualizationGeometryType
            {
                VisualizationGeometryTypeSphere/** sphere */ ,
                VisualizationGeometryTypeCylinder/** cylinder */ ,
                VisualizationGeometryTypeCone/** cone */ ,
                VisualizationGeometryTypePrism/** prism */ 
            };

            /** the hole type */
            public: enum HoleTypes
            {
                HoleTypesSimple/** simple */ ,
                HoleTypesCounterbored/** counterbored */ ,
                HoleTypesCountersunk/** countersunk */ 
            };

            private: PointJoinBuilderImpl * m_pointjoinbuilder_impl;
            private: friend class  _PointJoinBuilderBuilder;
            protected: PointJoinBuilder();
            public: ~PointJoinBuilder();
            /**Returns  the selected points 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::SelectPointList * PointSelPoints
            (
            );
            /**Returns  the indication of whether to update a point join's location to match its linked point. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: bool SynchronizeLocation
            (
            );
            /**Sets  the indication of whether to update a point join's location to match its linked point. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetSynchronizeLocation
            (
                bool synchronizeLocation /** synchronizelocation */ 
            );
            /** Computes overlap regions 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: int FindOverlapRegions
            (
            );
            /** Sets selected overlap region index 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetSelectedOverlapRegionIndex
            (
                int selectedOverlapRegionIndex /** selectedoverlapregionindex */ 
            );
            /** Gets selected overlap region index 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: int GetSelectedOverlapRegionIndex
            (
            );
            /**Returns  the stackup alignment type value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Join::PointJoinBuilder::StackupAlignmentTypes StackupAlignmentType
            (
            );
            /**Sets  the stackup alignment type value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetStackupAlignmentType
            (
                NXOpen::Join::PointJoinBuilder::StackupAlignmentTypes stackupAlignmentType /** stackupalignmenttype */ 
            );
            /**Returns  the stackup alignment 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::TaggedObject * StackupAlignment
            (
            );
            /**Sets  the stackup alignment 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetStackupAlignment
            (
                NXOpen::TaggedObject * stackupAlignment /** stackupalignment */ 
            );
            /**Returns  the selected normal surface 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::ScCollector * StackupNormalSurface
            (
            );
            /**Returns  the stackup on surface tolerance 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Expression * StackupOnSurfaceTolerance
            (
            );
            /**Returns  the gap tolerance 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Expression * StackupGapTolerance
            (
            );
            /**Returns  the gap limit 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Expression * StackupGapLimit
            (
            );
            /**Returns  the overlap tolerance 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Expression * StackupOverlapTolerance
            (
            );
            /**Returns  the reverse stackup direction flag 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: bool StackupReverseDirection
            (
            );
            /**Sets  the reverse stackup direction flag 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetStackupReverseDirection
            (
                bool toReverse /** toreverse */ 
            );
            /**Returns  the visualization diameter 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Expression * VisualizationDiameter
            (
            );
            /**Returns  the visualization color value 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: int VisualizationColor
            (
            );
            /**Sets  the visualization color value 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetVisualizationColor
            (
                int visualizationColor /** visualizationcolor */ 
            );
            /**Returns  the visualization geometry type value 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Join::PointJoinBuilder::VisualizationGeometryType VisualizationGeometry
            (
            );
            /**Sets  the visualization geometry type value 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetVisualizationGeometry
            (
                NXOpen::Join::PointJoinBuilder::VisualizationGeometryType visualizationGeometry /** visualizationgeometry */ 
            );
            /**Returns  the point marker 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: int VisualizationPointMarker
            (
            );
            /**Sets  the point marker 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetVisualizationPointMarker
            (
                int visualizationPointMarker /** visualizationpointmarker */ 
            );
            /**Returns  the hole type value 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Join::PointJoinBuilder::HoleTypes HoleType
            (
            );
            /**Sets  the hole type value 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetHoleType
            (
                NXOpen::Join::PointJoinBuilder::HoleTypes holeType /** holetype */ 
            );
            /**Returns  the hole diameter 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Expression * HoleDiameter
            (
            );
            /**Returns  the Countersink diameter 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Expression * HoleCounterSinkDiameter
            (
            );
            /**Returns  the Counterbore diameter 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Expression * HoleCounterBoreDiameter
            (
            );
            /**Returns  the Countersink angle 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Expression * HoleCounterSinkAngle
            (
            );
            /**Returns  the Counterbore depth 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Expression * HoleCounterBoreDepth
            (
            );
            /**Returns  the hole creation status. If true, holes should be created in connected bodies. If false, holes should be removed (or not created) from connected bodies 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: bool HoleCreate
            (
            );
            /**Sets  the hole creation status. If true, holes should be created in connected bodies. If false, holes should be removed (or not created) from connected bodies 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetHoleCreate
            (
                bool status /** status */ 
            );
            /** Set hardware pin information from name. 
                    If reuse library is the hardware data source, pinName is the descriptive name of the part
                    and pinPath is the path of the part in the reuse library.
                    If an XML database is used, pinName is the look up name and pinPath may be null. 
                    
             <br>  @deprecated Deprecated in NX1926.0.0.  This functionality is no longer supported. <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NX_DEPRECATED("Deprecated in NX1926.0.0.  This functionality is no longer supported.") void SetHardwarePin
            (
                const NXString & pinName /** pinname */ ,
                const NXString & pinPath /** pinpath */ 
            );
            /** Set hardware pin information from name. 
                    If reuse library is the hardware data source, pinName is the descriptive name of the part
                    and pinPath is the path of the part in the reuse library.
                    If an XML database is used, pinName is the look up name and pinPath may be null. 
                    
             <br>  @deprecated Deprecated in NX1926.0.0.  This functionality is no longer supported. <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            void SetHardwarePin
            (
                const char * pinName /** pinname */ ,
                const char * pinPath /** pinpath */ 
            );
            /** Set hardware for head side parts.
                    If reuse library is the hardware data source, headNames are the descriptive names of the parts
                    and headPaths are the paths of the parts in the reuse library.
                    If an XML database is used, headNames are the look up names and headPaths may be empty strings. 
             <br>  @deprecated Deprecated in NX1926.0.0.  This functionality is no longer supported. <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NX_DEPRECATED("Deprecated in NX1926.0.0.  This functionality is no longer supported.") void SetHeadSideParts
            (
                std::vector<NXString> & headNames /** List of names */,
                std::vector<NXString> & headPaths /** List of paths */
            );
            /** Set hardware for tail side parts. 
                    If reuse library is the hardware data source, tailNames are the descriptive names of the parts
                    and tailPaths are the paths of the parts in the reuse library.
                    If an XML database is used, tailNames are the look up names and tailPaths may be empty strings. 
             <br>  @deprecated Deprecated in NX1926.0.0.  This functionality is no longer supported. <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NX_DEPRECATED("Deprecated in NX1926.0.0.  This functionality is no longer supported.") void SetTailSideParts
            (
                std::vector<NXString> & tailNames /** List of names */,
                std::vector<NXString> & tailPaths /** List of paths */
            );
            /** Gets the hardware pin. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Join::PointJoinHardware * GetHardwarePin
            (
            );
            /** Clears the hardware pin. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void ClearHardwarePin
            (
            );
            /** Creates a new hardware pin. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void CreateHardwarePin
            (
            );
            /** Gets number of headside hardware parts 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: int GetNumberOfHeadSideParts
            (
            );
            /** Sets the number of headside hardware parts.
                    Existing head side hardware objects are deleted and new head side hardware objects are created.
                    The number of newly created head side hardware objects equals numberOfHeadsideParts.
                    
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetNumberOfHeadSideParts
            (
                int numberOfHeadsideParts /** numberofheadsideparts */ 
            );
            /** Gets the headside hardware part by index 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Join::PointJoinHardware * GetNthHeadSidePart
            (
                int headsidePartIndex /** headsidepartindex */ 
            );
            /** Gets number of tailside hardware parts 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: int GetNumberOfTailSideParts
            (
            );
            /** Sets the number of tailside hardware parts.
                    Existing tail side hardware objects are deleted and new tail side hardware objects are created.
                    The number of newly created tail side hardware objects equals numberOfTailsideParts.
                    
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetNumberOfTailSideParts
            (
                int numberOfTailsideParts /** numberoftailsideparts */ 
            );
            /** Gets the tailside hardware part by index 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: NXOpen::Join::PointJoinHardware * GetNthTailSidePart
            (
                int tailsidePartIndex /** tailsidepartindex */ 
            );
            /** Gets the points created by the Reference Sheet Points builder. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void GetReferenceSheetPoints
            (
                std::vector<NXOpen::Point *> & points /**The array of points created by Reference Sheet Builder. */
            );
            /**Returns  the load hardware flag. If true, hardware should be loaded into assembly. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: bool HardwareLoad
            (
            );
            /**Sets  the load hardware flag. If true, hardware should be loaded into assembly. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetHardwareLoad
            (
                bool status /** status */ 
            );
            /** Loads hardware parts into assembly. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: bool LoadHardware
            (
            );
            /** Unloads hardware parts from assembly. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: bool UnloadHardware
            (
            );
            /** This method adds a point that the stackup direction should be reversed for.  @return  Indicates if the stackup direction should be reversed for this point. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: bool GetStackupDirectionForPoint
            (
                NXOpen::Point * point /** A point was selected to reverse the stackup direction. */
            );
            /** This method gets the stackup direction for a specific point. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_join (" NX Join") */
            public: void SetStackupDirectionForPoint
            (
                NXOpen::Point * point /** A point was selected to reverse the stackup direction. */,
                bool reverseStackupDirection /** Indicates if the stackup direction should be reversed for this point. */
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
