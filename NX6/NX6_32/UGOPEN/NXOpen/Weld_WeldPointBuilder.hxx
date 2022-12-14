#ifndef NXOpen_WELD_WELDPOINTBUILDER_HXX_INCLUDED
#define NXOpen_WELD_WELDPOINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_WeldPointBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/WeldAssistant.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Weld
    {
        class WeldPointBuilder;
    }
    class CoordinateSystem;
    class Direction;
    class DisplayableObject;
    class Expression;
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class Plane;
    class Point;
    class ScCollector;
    class Section;
    namespace Weld
    {
        class _WeldPointBuilderBuilder;
        /** Represents a Spot Weld feature  <br> To create a new instance of this class, use @link Weld::WeldManager::CreateWeldPointBuilder Weld::WeldManager::CreateWeldPointBuilder@endlink  <br> */
        class NXOPENCPPEXPORT WeldPointBuilder : public Features::FeatureBuilder
        {
            private: friend class  _WeldPointBuilderBuilder;
            protected: WeldPointBuilder();
            /**Returns  the output type.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::OutputType OutputType
            (
            );
            /**Sets  the output type.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetOutputType
            (
                NXOpen::Weld::OutputType outputType /** output type */ 
            );
            /**Returns   the method for creating weld points.  Weld points can be created using guide
                     entities or @link Point Point@endlink  objects.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldPointMethod Method
            (
            );
            /**Sets   the method for creating weld points.  Weld points can be created using guide
                     entities or @link Point Point@endlink  objects.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMethod
            (
                NXOpen::Weld::WeldPointMethod method /** method */ 
            );
            /**Returns  the spacing method to control to use to create multiple weld points.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldPointSpacingMethod SpacingMethod
            (
            );
            /**Sets  the spacing method to control to use to create multiple weld points.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetSpacingMethod
            (
                NXOpen::Weld::WeldPointSpacingMethod spacingMethod /** spacing method */ 
            );
            /**Returns   the type of sheet to create to place weld points on.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldPointReferenceSheetType ReferenceSheetType
            (
            );
            /**Sets   the type of sheet to create to place weld points on.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetReferenceSheetType
            (
                NXOpen::Weld::WeldPointReferenceSheetType referenceSheetType /** reference sheet type */ 
            );
            /**Returns  the processing method to use for generating weld points along reference section(s)  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldPointLocation LocationMethod
            (
            );
            /**Sets  the processing method to use for generating weld points along reference section(s)  <br> License requirements : ugweld ("UG WELD") */
            public: void SetLocationMethod
            (
                NXOpen::Weld::WeldPointLocation locationMethod /** location method */ 
            );
            /**Returns  the offset curve extend method.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldPointExtendMethod ExtendMethod
            (
            );
            /**  <br> License requirements : ugweld ("UG WELD") */
            public: void SetExtendMethod
            (
                NXOpen::Weld::WeldPointExtendMethod extendMethod /** extend method */ 
            );
            /**Returns  the direction flag. This is for use only with the
                    JA_WELD_point_method_multiple option.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldPointDirection Direction
            (
            );
            /**Sets  the direction flag. This is for use only with the
                    JA_WELD_point_method_multiple option.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetDirection
            (
                NXOpen::Weld::WeldPointDirection direction /** direction */ 
            );
            /**Returns  the sequence number for the weld point feature. Each Weld point feature contains a single point.
                    If multiple Weld points are to be created, you must specify the sequence of the point you want.
                    For example if you are expecting 3 points to be created. You must create 3 weld point features.
                    The features will have sequence numbers 0,1 and 2.   <br> License requirements : ugweld ("UG WELD") */
            public: int SequenceNumber
            (
            );
            /**Sets  the sequence number for the weld point feature. Each Weld point feature contains a single point.
                    If multiple Weld points are to be created, you must specify the sequence of the point you want.
                    For example if you are expecting 3 points to be created. You must create 3 weld point features.
                    The features will have sequence numbers 0,1 and 2.   <br> License requirements : ugweld ("UG WELD") */
            public: void SetSequenceNumber
            (
                int sequenceNumber /** sequence number */ 
            );
            /**  Gets the object for the point geometry in the weld point feature.  @return   <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Point * GetFinalPoint
            (
            );
            /**Returns   the @link Point Point@endlink  object that is referenced. The is 
                     used for @link Weld::WeldPointMethodSingle Weld::WeldPointMethodSingle@endlink 
                     and @link Weld::WeldPointMethodMirror Weld::WeldPointMethodMirror@endlink   <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Point * ReferencePoint
            (
            );
            /**Sets   the @link Point Point@endlink  object that is referenced. The is 
                     used for @link Weld::WeldPointMethodSingle Weld::WeldPointMethodSingle@endlink 
                     and @link Weld::WeldPointMethodMirror Weld::WeldPointMethodMirror@endlink   <br> License requirements : ugweld ("UG WELD") */
            public: void SetReferencePoint
            (
                NXOpen::Point * referencePoint /** reference point */ 
            );
            /**Returns   the guide curve(s) or guide edge(s) used for generating weld points  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Section * GuideCollector1
            (
            );
            /**Sets   the guide curve(s) or guide edge(s) used for generating weld points  <br> License requirements : ugweld ("UG WELD") */
            public: void SetGuideCollector1
            (
                NXOpen::Section * guideCollector1 /** guide collector1 */ 
            );
            /**Returns  the second guide curve(s) or guide edge used when location equals place along centerline  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Section * GuideCollector2
            (
            );
            /**Sets  the second guide curve(s) or guide edge used when location equals place along centerline  <br> License requirements : ugweld ("UG WELD") */
            public: void SetGuideCollector2
            (
                NXOpen::Section * guideCollector2 /** guide collector2 */ 
            );
            /**Returns   the guide face(s) used for projecting weld points when location equals along guide curve  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::ScCollector * AlongGuideCollector
            (
            );
            /**Sets   the guide face(s) used for projecting weld points when location equals along guide curve  <br> License requirements : ugweld ("UG WELD") */
            public: void SetAlongGuideCollector
            (
                NXOpen::ScCollector * alongGuideCollector /** along guide collector */ 
            );
            /**Returns  the coordinate system for the weld point  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::CoordinateSystem * CoordinateSystem
            (
            );
            /**Sets  the coordinate system for the weld point  <br> License requirements : ugweld ("UG WELD") */
            public: void SetCoordinateSystem
            (
                NXOpen::CoordinateSystem * coordinateSystem /** coordinate system */ 
            );
            /**Returns  the plane that a point is to be mirrored about.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Plane * MirrorPlane
            (
            );
            /**Sets  the plane that a point is to be mirrored about.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMirrorPlane
            (
                NXOpen::Plane * plane /** plane */ 
            );
            /**Returns  the coordinate system that a point is to be translated about.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::CoordinateSystem * TranslateCsys
            (
            );
            /**Sets  the coordinate system that a point is to be translated about.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetTranslateCsys
            (
                NXOpen::CoordinateSystem * coordinateSystem /** coordinate system */ 
            );
            /**Returns  the offset distance from edges in guide_collector1 to place weld points   <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Expression * OffsetDistance
            (
            );
            /** Sets the offset distance from edges in guide_collector1 to place weld points   <br> License requirements : ugweld ("UG WELD") */
            public: void SetOffsetDistance
            (
                const NXString & offsetDistance /** expression string   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the distance from the start of the reference section(s) that should not have weld points.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Expression * DistanceFromStart
            (
            );
            /** Sets the distance from the start of the reference section(s) that should not have weld points.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetDistanceFromStart
            (
                const NXString & startDistance /** expression string   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the distance from the end of the reference section(s) that should not have weld points.   <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Expression * DistanceFromEnd
            (
            );
            /** Sets the distance from the end of the reference section(s) that should not have weld points.   <br> License requirements : ugweld ("UG WELD") */
            public: void SetDistanceFromEnd
            (
                const NXString & endDistance /** expression string   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the desired spacing distance between weld points.   <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Expression * SpacingDistance
            (
            );
            /** Sets the desired spacing distance between weld points.   <br> License requirements : ugweld ("UG WELD") */
            public: void SetSpacingDistance
            (
                const NXString & spacingDistance /** expression string   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the number of weld points.   <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Expression * NumberOfPoints
            (
            );
            /** Sets the number of weld points.   <br> License requirements : ugweld ("UG WELD") */
            public: void SetNumberOfPoints
            (
                const NXString & numPoints /** expression string   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the translate distance for weld points in x axis direction.   <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Expression * TranslateXDistance
            (
            );
            /** Sets the translate distance for weld points in x axis direction.   <br> License requirements : ugweld ("UG WELD") */
            public: void SetTranslateXDistance
            (
                const NXString & translateDistance /** expression string   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the translate distance for weld points in y axis direction.   <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Expression * TranslateYDistance
            (
            );
            /** Sets the translate distance for weld points in y axis direction.   <br> License requirements : ugweld ("UG WELD") */
            public: void SetTranslateYDistance
            (
                const NXString & translateDistance /** expression string   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the translate distance for weld points in z axis direction.   <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Expression * TranslateZDistance
            (
            );
            /** Sets the translate distance for weld points in z axis direction.   <br> License requirements : ugweld ("UG WELD") */
            public: void SetTranslateZDistance
            (
                const NXString & translateDistance /** expression string   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the distance tolerance for the weld point  <br> License requirements : ugweld ("UG WELD") */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance for the weld point  <br> License requirements : ugweld ("UG WELD") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distance tolerance */ 
            );
            /**Returns  the distance percentage from the start of the curve where the
                    weld point should be. 0.0 is the start of the curve
                    100.0 is the end of the curve.  <br> License requirements : ugweld ("UG WELD") */
            public: double AlongGuideDistance
            (
            );
            /**Sets  the distance percentage from the start of the curve where the
                    weld point should be. 0.0 is the start of the curve
                    100.0 is the end of the curve.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetAlongGuideDistance
            (
                double alongGuideDistance /** along guide distance */ 
            );
            /**Returns  the radius to create the sphere, cylinder, or cone with  <br> License requirements : ugweld ("UG WELD") */
            public: double CustomRadius
            (
            );
            /**Sets  the radius to create the sphere, cylinder, or cone with  <br> License requirements : ugweld ("UG WELD") */
            public: void SetCustomRadius
            (
                double customRadius /** custom radius */ 
            );
            /**Returns  the distance the custom cylinder should be created above the
                    weld point  <br> License requirements : ugweld ("UG WELD") */
            public: double CustomCylinderAbove
            (
            );
            /**Sets  the distance the custom cylinder should be created above the
                    weld point  <br> License requirements : ugweld ("UG WELD") */
            public: void SetCustomCylinderAbove
            (
                double cylinderAboveHeight /** cylinder above height */ 
            );
            /**Returns  the total length of the cylinder to be created.  <br> License requirements : ugweld ("UG WELD") */
            public: double CustomTotalCylinderLength
            (
            );
            /**Sets  the total length of the cylinder to be created.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetCustomTotalCylinderLength
            (
                double totalCylinderLength /** total cylinder length */ 
            );
            /**Returns  the default width of the object for measurement to be created.  <br> License requirements : ugweld ("UG WELD") */
            public: double MeasurementDefaultWidth
            (
            );
            /**Sets  the default width of the object for measurement to be created.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMeasurementDefaultWidth
            (
                double totalCylinderLength /** total cylinder length */ 
            );
            /**Returns  the default height of the object for measurement to be created.  <br> License requirements : ugweld ("UG WELD") */
            public: double MeasurementDefaultHeight
            (
            );
            /**Sets  the default height of the object for measurement to be created.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMeasurementDefaultHeight
            (
                double totalCylinderLength /** total cylinder length */ 
            );
            /**Returns  the hole_size of the object for measurement to be created.  <br> License requirements : ugweld ("UG WELD") */
            public: double MeasurementHoleSize
            (
            );
            /**Sets  the hole_size of the object for measurement to be created.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMeasurementHoleSize
            (
                double holeSize /** hole size */ 
            );
            /**Returns  the slot width of the object for measurement to be created.  <br> License requirements : ugweld ("UG WELD") */
            public: double MeasurementSlotWidth
            (
            );
            /**Sets  the slot width of the object for measurement to be created.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMeasurementSlotWidth
            (
                double slotWidth /** slot width */ 
            );
            /**Returns  the slot height of the object for measurement to be created.  <br> License requirements : ugweld ("UG WELD") */
            public: double MeasurementSlotLength
            (
            );
            /**Sets  the slot height of the object for measurement to be created.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMeasurementSlotLength
            (
                double slotLength /** slot length */ 
            );
            /**Returns  the stud size of the object for measurement to be created.  <br> License requirements : ugweld ("UG WELD") */
            public: double MeasurementStudSize
            (
            );
            /**Sets  the stud size of the object for measurement to be created.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMeasurementStudSize
            (
                double studSize /** stud size */ 
            );
            /** Computes the numbers of weld points that will be created if the
                    creating multiple weld points using a spacing distance.  @return  the number of weld points that will be created  <br> License requirements : ugweld ("UG WELD") */
            public: int GetNumberPointsFromSpacingDistance
            (
            );
            /** Sets a group of reference objects that represent the sheet metal for a part. Allowable
                    objects are linked features, linked curves, faces or curves.  All objects must
                    be in the work part. No occurrences are allowed.   <br> License requirements : ugweld ("UG WELD") */
            public: void SetFaceset
            (
                int facesetIndex /** Which faceset to get the faces for. 0 is the first */,
                const std::vector<NXOpen::DisplayableObject *> & objects /** the face set reference objects */,
                const std::vector<NXOpen::Features::Feature *> & frecs /** the face set wave linked frecs */
            );
            /** Gets a group of reference objects that represent the sheet metal for a part.  <br> License requirements : ugweld ("UG WELD") */
            public: void GetFaceset
            (
                int facesetIndex /** Which faceset to get the faces for. 0 is the first */,
                std::vector<NXOpen::DisplayableObject *> & objects /** the face set reference objects */,
                std::vector<NXOpen::Features::Feature *> & frecs /** the face set wave linked frecs */
            );
            /**Returns  the output solid type.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldCustom SolidType
            (
            );
            /**Sets  the output solid type.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetSolidType
            (
                NXOpen::Weld::WeldCustom solidType /** solid type */ 
            );
            /**Returns  the weld type.  <br> License requirements : ugweld ("UG WELD") */
            public: int WeldType
            (
            );
            /**Sets  the weld type.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetWeldType
            (
                int weldType /** weld type */ 
            );
            /**Returns  the project method type.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldProjectionMethod ProjectionMethod
            (
            );
            /**Sets  the project method type.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetProjectionMethod
            (
                NXOpen::Weld::WeldProjectionMethod projMethod /** proj method */ 
            );
            /**Sets   <br> License requirements : ugweld ("UG WELD") */
            public: void SetConnOnePart
            (
                int isConnOnePart /** is conn one part */ 
            );
            /**Returns   <br> License requirements : ugweld ("UG WELD") */
            public: int ConnOnePart
            (
            );
            /**Sets   <br> License requirements : ugweld ("UG WELD") */
            public: void SetProjectDirection
            (
                NXOpen::Direction * direction /** Project direction */
            );
            /**Returns   <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Direction * ProjectDirection
            (
            );
            /**Returns   <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Plane * SectionPlaneEntity
            (
            );
            /**Sets   <br> License requirements : ugweld ("UG WELD") */
            public: void SetSectionPlaneEntity
            (
                NXOpen::Plane * plane /** plane */ 
            );
            /**Returns  the project method type.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldSpacingCalcMethod SpacingCalcMethod
            (
            );
            /**Sets  the project method type.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetSpacingCalcMethod
            (
                NXOpen::Weld::WeldSpacingCalcMethod spacingCalcMethod /** spacing calc method */ 
            );
            /**Returns  the datum major direction type.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldDatumControlDirection DatumMajorDirection
            (
            );
            /**Sets  the datum major direction type.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetDatumMajorDirection
            (
                NXOpen::Weld::WeldDatumControlDirection datumMajorDir /** datum major dir */ 
            );
            /**Returns  the datum reference direction type.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldDatumControlDirection DatumFirstReferenceDirection
            (
            );
            /**Sets  the datum reference direction type.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetDatumFirstReferenceDirection
            (
                NXOpen::Weld::WeldDatumControlDirection datumRefDir /** datum ref dir */ 
            );
            /**Returns  the datum reference direction type.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldDatumControlDirection DatumSecondReferenceDirection
            (
            );
            /**Sets  the datum reference direction type.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetDatumSecondReferenceDirection
            (
                NXOpen::Weld::WeldDatumControlDirection datumRefDir /** datum ref dir */ 
            );
            /**Sets  the measurement size method.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMeasurementSizeMethod
            (
                NXOpen::Weld::WeldMeasurementSizeMethod sizeMethod /** size method */ 
            );
            /**Returns  the measurement size method.  <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldMeasurementSizeMethod MeasurementSizeMethod
            (
            );
            /** Removes all the face sets associated with the feature.  <br> License requirements : ugweld ("UG WELD") */
            public: void ClearFacesets
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
