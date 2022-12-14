#ifndef NXOpen_CAM_INSPECTIONMETHODBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONMETHODBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionMethodBuilder.ja
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
#include <NXOpen/CAM_InspectionMethodBuilder.hxx>
#include <NXOpen/CAM_MethodBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class InspectionMethodBuilder;
    }
    namespace CAM
    {
        class MethodBuilder;
    }
    class NXColor;
    namespace CAM
    {
        class _InspectionMethodBuilderBuilder;
        /** Represents the builder for a CMM Inspection method.  <br> To create a new instance of this class, use @link CAM::InspectionGroupCollection::CreateInspectionMethodBuilder CAM::InspectionGroupCollection::CreateInspectionMethodBuilder@endlink  <br> */
        class NXOPENCPPEXPORT InspectionMethodBuilder : public CAM::MethodBuilder
        {
            /** CMM Inspection modes. */
            public: enum InspectionModeEnum
            {
                InspectionModeEnumProgramDefault/** Program Default */,
                InspectionModeEnumProgram/** Program */,
                InspectionModeEnumManual/** Manual */,
                InspectionModeEnumAuto/** Auto */
            };

            /** CMM Inspection operation types. */
            public: enum OperationTypeEnum
            {
                OperationTypeEnumNone/** None */,
                OperationTypeEnumManualPoint/** Manual Point */,
                OperationTypeEnumUVGrid/** Rectangular UV Grid */,
                OperationTypeEnumPointHelix/** Point Helix */,
                OperationTypeEnumLineScan/** Line Scan */,
                OperationTypeEnumCircularScan/** Circular Scan */,
                OperationTypeEnumCurveScan/** Curve Scan */,
                OperationTypeEnumHelicalScan/** Helical Scan */
            };

            /** CMM Inspection transition modes. */
            public: enum TransitionEnum
            {
                TransitionEnumNone/** No Transition Point */,
                TransitionEnumManual/** Manual Transition Point */,
                TransitionEnumSafePlane/** Safe Plane Transition Point */
            };

            /** CMM Inspection method feature type. */
            public: enum MethodTypeEnum
            {
                MethodTypeEnumNone/** None */,
                MethodTypeEnumArc/** Arc */,
                MethodTypeEnumCircle/** Circle */,
                MethodTypeEnumPoint/** Point */,
                MethodTypeEnumSphere/** Sphere */,
                MethodTypeEnumSurface/** Surface */,
                MethodTypeEnumPattern/** Pattern */,
                MethodTypeEnumCurve/** Curve */,
                MethodTypeEnumCylinder/** Cylinder */,
                MethodTypeEnumCone/** Cone */,
                MethodTypeEnumPlane/** Plane */,
                MethodTypeEnumLine/** Line */,
                MethodTypeEnumCParln/** Bounded Slot Tab */,
                MethodTypeEnumSlotTab/** Slot Tab */,
                MethodTypeEnumSurfaceOfRevolution/** Surface of Revolution */,
                MethodTypeEnumTorus/** Torus */
            };

            private: friend class  _InspectionMethodBuilderBuilder;
            protected: InspectionMethodBuilder();
            /**Returns  the method feature type  <br> License requirements : None */
            public: NXOpen::CAM::InspectionMethodBuilder::MethodTypeEnum MethodType
            (
            );
            /**Sets  the method feature type  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetMethodType
            (
                NXOpen::CAM::InspectionMethodBuilder::MethodTypeEnum type /** type */ 
            );
            /**Returns  the number of path points  <br> License requirements : None */
            public: int PointCount
            (
            );
            /**Sets  the number of path points  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetPointCount
            (
                int pointCount /** pointcount */ 
            );
            /**Returns  the number of points in U direction  <br> License requirements : None */
            public: int UCount
            (
            );
            /**Sets  the number of points in U direction  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetUCount
            (
                int uCount /** ucount */ 
            );
            /**Returns  the number of points in V direction  <br> License requirements : None */
            public: int VCount
            (
            );
            /**Sets  the number of points in V direction  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetVCount
            (
                int vCount /** vcount */ 
            );
            /**Returns  the approach distance  <br> License requirements : None */
            public: double ApproachDistance
            (
            );
            /**Sets  the approach distance  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetApproachDistance
            (
                double distance /** distance */ 
            );
            /**Returns  the retract distance  <br> License requirements : None */
            public: double RetractDistance
            (
            );
            /**Sets  the retract distance  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetRetractDistance
            (
                double distance /** distance */ 
            );
            /**Returns  the default inspection mode  <br> License requirements : None */
            public: NXOpen::CAM::InspectionMethodBuilder::InspectionModeEnum InspectionMode
            (
            );
            /**Sets  the default inspection mode  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetInspectionMode
            (
                NXOpen::CAM::InspectionMethodBuilder::InspectionModeEnum inspectionMode /** inspectionmode */ 
            );
            /**Returns  the default inspection operation type  <br> License requirements : None */
            public: NXOpen::CAM::InspectionMethodBuilder::OperationTypeEnum DefaultOperationType
            (
            );
            /**Sets  the default inspection operation type  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetDefaultOperationType
            (
                NXOpen::CAM::InspectionMethodBuilder::OperationTypeEnum operationType /** operationtype */ 
            );
            /**Returns  the type of entry transition  <br> License requirements : None */
            public: NXOpen::CAM::InspectionMethodBuilder::TransitionEnum EntryTransition
            (
            );
            /**Sets  the type of entry transition  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetEntryTransition
            (
                NXOpen::CAM::InspectionMethodBuilder::TransitionEnum entryTransition /** entrytransition */ 
            );
            /**Returns  a flag to indicate if an entry point is required  <br> License requirements : None */
            public: bool EntryPoint
            (
            );
            /**Sets  a flag to indicate if an entry point is required  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetEntryPoint
            (
                bool entryPoint /** entrypoint */ 
            );
            /**Returns  a flag to indicate if collision avoidance is required at entry  <br> License requirements : None */
            public: bool EntryAvoidance
            (
            );
            /**Sets  a flag to indicate if collision avoidance is required at entry  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetEntryAvoidance
            (
                bool entryAvoidance /** entryavoidance */ 
            );
            /**Returns  the distance from the entry or exit point to safe plane  <br> License requirements : None */
            public: double EntryExitDistance
            (
            );
            /**Sets  the distance from the entry or exit point to safe plane  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetEntryExitDistance
            (
                double entryExitDistance /** entryexitdistance */ 
            );
            /**Returns  a flag to indicate if collision avoidance is required at exit  <br> License requirements : None */
            public: bool ExitAvoidance
            (
            );
            /**Sets  a flag to indicate if collision avoidance is required at exit  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetExitAvoidance
            (
                bool exitAvoidance /** exitavoidance */ 
            );
            /**Returns  a flag to indicate if an exit point is required  <br> License requirements : None */
            public: bool ExitPoint
            (
            );
            /**Sets  a flag to indicate if an exit point is required  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetExitPoint
            (
                bool exitPoint /** exitpoint */ 
            );
            /**Returns  the type of exit transition  <br> License requirements : None */
            public: NXOpen::CAM::InspectionMethodBuilder::TransitionEnum ExitTransition
            (
            );
            /**Sets  the type of exit transition  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetExitTransition
            (
                NXOpen::CAM::InspectionMethodBuilder::TransitionEnum exitTransition /** exittransition */ 
            );
            /**Returns  the default animation speed setting  <br> License requirements : None */
            public: int Speed
            (
            );
            /**Sets  the default animation speed setting  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetSpeed
            (
                int speed /** speed */ 
            );
            /**Returns  the color used for displaying transition elements  <br> License requirements : None */
            public: NXOpen::NXColor * ColorTransition
            (
            );
            /**Sets  the color used for displaying transition elements  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetColorTransition
            (
                NXOpen::NXColor * colorTransition /** colortransition */ 
            );
            /**Returns  the color used for displaying approach elements  <br> License requirements : None */
            public: NXOpen::NXColor * ColorApproach
            (
            );
            /**Sets  the color used for displaying approach elements  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetColorApproach
            (
                NXOpen::NXColor * colorApproach /** colorapproach */ 
            );
            /**Returns  the color used for displaying entry and exit elements  <br> License requirements : None */
            public: NXOpen::NXColor * ColorEntryExit
            (
            );
            /**Sets  the color used for displaying entry and exit elements  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetColorEntryExit
            (
                NXOpen::NXColor * colorEntryExit /** colorentryexit */ 
            );
            /**Returns  the color used for displaying measured points  <br> License requirements : None */
            public: NXOpen::NXColor * ColorMeasure
            (
            );
            /**Sets  the color used for displaying measured points  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetColorMeasure
            (
                NXOpen::NXColor * colorMeasure /** colormeasure */ 
            );
            /**Returns  the color used for displaying path lines  <br> License requirements : None */
            public: NXOpen::NXColor * ColorLine
            (
            );
            /**Sets  the color used for displaying path lines  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetColorLine
            (
                NXOpen::NXColor * colorLine /** colorline */ 
            );
            /**Returns  the color used for displaying a scan line  <br> License requirements : None */
            public: NXOpen::NXColor * ColorScanLine
            (
            );
            /**Sets  the color used for displaying a scan line  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetColorScanLine
            (
                NXOpen::NXColor * colorScanLine /** colorscanline */ 
            );
            /**Returns  the color used for displaying a scan arc  <br> License requirements : None */
            public: NXOpen::NXColor * ColorScanArc
            (
            );
            /**Sets  the color used for displaying a scan arc  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetColorScanArc
            (
                NXOpen::NXColor * colorScanArc /** colorscanarc */ 
            );
            /**Returns  the color used for displaying a scan helix  <br> License requirements : None */
            public: NXOpen::NXColor * ColorScanHelix
            (
            );
            /**Sets  the color used for displaying a scan helix  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetColorScanHelix
            (
                NXOpen::NXColor * colorScanHelix /** colorscanhelix */ 
            );
            /**Returns  a flag to indicate if manual point creation is allowed  <br> License requirements : None */
            public: bool ManualPoint
            (
            );
            /**Sets  a flag to indicate if manual point creation is allowed  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetManualPoint
            (
                bool manualPoint /** manualpoint */ 
            );
            /**Returns  a flag to indicate if rectangular UV grid is allowed  <br> License requirements : None */
            public: bool UVGrid
            (
            );
            /**Sets  a flag to indicate if rectangular UV grid is allowed  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetUVGrid
            (
                bool uvGrid /** uvgrid */ 
            );
            /**Returns  a flag to indicate if point helix is allowed  <br> License requirements : None */
            public: bool PointHelix
            (
            );
            /**Sets  a flag to indicate if point helix is allowed  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetPointHelix
            (
                bool pointHelix /** pointhelix */ 
            );
            /**Returns  a flag to indicate if scan line is allowed  <br> License requirements : None */
            public: bool LineScan
            (
            );
            /**Sets  a flag to indicate if scan line is allowed  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetLineScan
            (
                bool lineScan /** linescan */ 
            );
            /**Returns  a flag to indicate if scan arc is allowed  <br> License requirements : None */
            public: bool CircularScan
            (
            );
            /**Sets  a flag to indicate if scan arc is allowed  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetCircularScan
            (
                bool circularScan /** circularscan */ 
            );
            /**Returns  a flag to indicate if scan curve is allowed  <br> License requirements : None */
            public: bool CurveScan
            (
            );
            /**Sets  a flag to indicate if scan curve is allowed  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetCurveScan
            (
                bool curveScan /** curvescan */ 
            );
            /**Returns  a flag to indicate if helical scan is allowed  <br> License requirements : None */
            public: bool HelicalScan
            (
            );
            /**Sets  a flag to indicate if helical scan is allowed  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetHelicalScan
            (
                bool helicalScan /** helicalscan */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
