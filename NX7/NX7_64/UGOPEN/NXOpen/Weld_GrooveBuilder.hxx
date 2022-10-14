#ifndef NXOpen_WELD_GROOVEBUILDER_HXX_INCLUDED
#define NXOpen_WELD_GROOVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_GrooveBuilder.ja
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
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Weld
    {
        class GrooveBuilder;
    }
    class Expression;
    class Face;
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    class Section;
    namespace Weld
    {
        class _GrooveBuilderBuilder;
        /** Represents a Groove Weld feature  <br> To create a new instance of this class, use @link Weld::WeldManager::CreateWeldGrooveBuilder Weld::WeldManager::CreateWeldGrooveBuilder@endlink  <br> */
        class NXOPENCPPEXPORT GrooveBuilder : public Features::FeatureBuilder
        {
            private: friend class  _GrooveBuilderBuilder;
            protected: GrooveBuilder();
            /**Returns  the output type.  <br> License requirements : None */
            public: NXOpen::Weld::OutputType OutputType
            (
            );
            /**Sets  the output type.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetOutputType
            (
                NXOpen::Weld::OutputType outputType /** output type */ 
            );
            /**Returns  the first set of faces  <br> License requirements : None */
            public: NXOpen::ScCollector * FirstFaceset
            (
            );
            /**Sets  the first set of faces  <br> License requirements : ugweld ("UG WELD") */
            public: void SetFirstFaceset
            (
                NXOpen::ScCollector * faceCollector /** face collector */ 
            );
            /**Returns  the first set top edges to extend  <br> License requirements : None */
            public: NXOpen::Section * FirstFacesetTopEdges
            (
            );
            /**Sets  the first set top edges to extend  <br> License requirements : ugweld ("UG WELD") */
            public: void SetFirstFacesetTopEdges
            (
                NXOpen::Section * section /** section */ 
            );
            /**Returns  the first set bottom edges to extend  <br> License requirements : None */
            public: NXOpen::Section * FirstFacesetBottomEdges
            (
            );
            /**Sets  the first set bottom edges to extend  <br> License requirements : ugweld ("UG WELD") */
            public: void SetFirstFacesetBottomEdges
            (
                NXOpen::Section * section /** section */ 
            );
            /**Returns  the first set help point. If multiple solutions exist, the desired solution 
                    used will be the one closest to this point  <br> License requirements : None */
            public: NXOpen::Point3d FirstFacesetHelpPoint
            (
            );
            /**Sets  the first set help point. If multiple solutions exist, the desired solution 
                    used will be the one closest to this point  <br> License requirements : ugweld ("UG WELD") */
            public: void SetFirstFacesetHelpPoint
            (
                const NXOpen::Point3d & helpPoint /** help point */ 
            );
            /**Returns  the side of the faceset to build the groove feature. The feature will
                    be built opposite the face closest to the help point 
                     <br> License requirements : None */
            public: bool IsFirstFacesetNormalReversed
            (
            );
            /**Sets  the side of the faceset to build the groove feature. The feature will
                    be built opposite the face closest to the help point 
                     <br> License requirements : ugweld ("UG WELD") */
            public: void SetFirstFacesetNormalReversed
            (
                bool reversed /** reversed */ 
            );
            /**Returns  the second set of faces  <br> License requirements : None */
            public: NXOpen::ScCollector * SecondFaceset
            (
            );
            /**Sets  the second set of faces  <br> License requirements : ugweld ("UG WELD") */
            public: void SetSecondFaceset
            (
                NXOpen::ScCollector * faceCollector /** face collector */ 
            );
            /**Returns  the second set top edges to extend  <br> License requirements : None */
            public: NXOpen::Section * SecondFacesetTopEdges
            (
            );
            /**Sets  the second set top edges to extend  <br> License requirements : ugweld ("UG WELD") */
            public: void SetSecondFacesetTopEdges
            (
                NXOpen::Section * edgeCollector /** edge collector */ 
            );
            /**Returns  the second set bottom edges to extend  <br> License requirements : None */
            public: NXOpen::Section * SecondFacesetBottomEdges
            (
            );
            /**Sets  the second set bottom edges to extend  <br> License requirements : ugweld ("UG WELD") */
            public: void SetSecondFacesetBottomEdges
            (
                NXOpen::Section * edgeCollector /** edge collector */ 
            );
            /**Returns  the second set help point. If multiple solutions exist, the desired solution 
                    used will be the one closest to this point  <br> License requirements : None */
            public: NXOpen::Point3d SecondFacesetHelpPoint
            (
            );
            /**Sets  the second set help point. If multiple solutions exist, the desired solution 
                    used will be the one closest to this point  <br> License requirements : ugweld ("UG WELD") */
            public: void SetSecondFacesetHelpPoint
            (
                const NXOpen::Point3d & helpPoint /** help point */ 
            );
            /**Returns  the side of the faceset to build the groove feature. The feature will
                    be built opposite the face closest to the help point 
                     <br> License requirements : None */
            public: bool IsSecondFacesetNormalReversed
            (
            );
            /**Sets  the side of the faceset to build the groove feature. The feature will
                    be built opposite the face closest to the help point 
                     <br> License requirements : ugweld ("UG WELD") */
            public: void SetSecondFacesetNormalReversed
            (
                bool reversed /** reversed */ 
            );
            /** Sets the adjacent faces of the target solid. These faces are used to
                    trim the groove weld solid with.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetFirstFacesetStartAdjacentFaces
            (
                const std::vector<NXOpen::Face *> & objects /** objects */ 
            );
            /** Gets the adjacent faces of the target solid. These faces are used to
                    trim the groove weld solid with.  @return  the adjacent face reference objects  <br> License requirements : None */
            public: std::vector<NXOpen::Face *> GetFirstFacesetStartAdjacentFaces
            (
            );
            /** Sets the adjacent faces of the target solid. These faces are used to
                    trim the groove weld solid with.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetFirstFacesetEndAdjacentFaces
            (
                const std::vector<NXOpen::Face *> & objects /** objects */ 
            );
            /** Gets the adjacent faces of the target solid. These faces are used to
                    trim the groove weld solid with.  @return  the adjacent face reference objects  <br> License requirements : None */
            public: std::vector<NXOpen::Face *> GetFirstFacesetEndAdjacentFaces
            (
            );
            /** Sets the adjacent faces of the target solid. These faces are used to
                    trim the groove weld solid with.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetSecondFacesetStartAdjacentFaces
            (
                const std::vector<NXOpen::Face *> & objects /** objects */ 
            );
            /** Gets the adjacent faces of the target solid. These faces are used to
                    trim the groove weld solid with.  @return  the adjacent face reference objects  <br> License requirements : None */
            public: std::vector<NXOpen::Face *> GetSecondFacesetStartAdjacentFaces
            (
            );
            /** Sets the adjacent faces of the target solid. These faces are used to
                    trim the groove weld solid with.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetSecondFacesetEndAdjacentFaces
            (
                const std::vector<NXOpen::Face *> & objects /** objects */ 
            );
            /** Gets the adjacent faces of the target solid. These faces are used to
                    trim the groove weld solid with.  @return  the adjacent face reference objects  <br> License requirements : None */
            public: std::vector<NXOpen::Face *> GetSecondFacesetEndAdjacentFaces
            (
            );
            /**Returns  the contour contour shape. This is the shape on the top of the groove weld  <br> License requirements : None */
            public: NXOpen::Weld::WeldContourShape ContourShape
            (
            );
            /**Sets  the contour contour shape. This is the shape on the top of the groove weld  <br> License requirements : ugweld ("UG WELD") */
            public: void SetContourShape
            (
                NXOpen::Weld::WeldContourShape contourShape /** contour shape */ 
            );
            /**Returns  the shape of the groove weld to create  <br> License requirements : None */
            public: NXOpen::Weld::WeldGrooveShape GrooveShape
            (
            );
            /**Sets  the shape of the groove weld to create  <br> License requirements : ugweld ("UG WELD") */
            public: void SetGrooveShape
            (
                NXOpen::Weld::WeldGrooveShape grooveShape /** groove shape */ 
            );
            /** Gets the contour height needed to describe groove weld shape  @return  expression  <br> License requirements : None */
            public: NXOpen::Expression * GetContourHeight
            (
            );
            /** Sets the contour height needed to describe groove weld  <br> License requirements : ugweld ("UG WELD") */
            public: void SetContourHeight
            (
                const NXString & contourHeight /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the root opening height needed to describe groove weld  @return  expression  <br> License requirements : None */
            public: NXOpen::Expression * GetRootOpening
            (
            );
            /** Sets the root opening height needed to describe groove weld  <br> License requirements : ugweld ("UG WELD") */
            public: void SetRootOpening
            (
                const NXString & rootOpening /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the root penetration needed to describe groove weld  @return  expression  <br> License requirements : None */
            public: NXOpen::Expression * GetRootPenetration
            (
            );
            /** Sets the root penetration needed to describe groove weld  <br> License requirements : ugweld ("UG WELD") */
            public: void SetRootPenetration
            (
                const NXString & rootPenetration /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the groove angle needed to describe groove weld  @return  expression  <br> License requirements : None */
            public: NXOpen::Expression * GetGrooveAngle
            (
            );
            /** Sets the groove angle needed to describe groove weld  <br> License requirements : ugweld ("UG WELD") */
            public: void SetGrooveAngle
            (
                const NXString & grooveAngle /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the groove radius needed to describe groove weld  @return  expression  <br> License requirements : None */
            public: NXOpen::Expression * GetGrooveRadius
            (
            );
            /** Sets the groove radius needed to describe groove weld  <br> License requirements : ugweld ("UG WELD") */
            public: void SetGrooveRadius
            (
                const NXString & grooveAngle /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the penetration depth needed to describe groove weld  @return  expression  <br> License requirements : None */
            public: NXOpen::Expression * GetPenetrationDepth
            (
            );
            /** Sets the penetration depth needed to describe groove weld  <br> License requirements : ugweld ("UG WELD") */
            public: void SetPenetrationDepth
            (
                const NXString & penetrationDepth /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the second penetration depth needed to describe groove weld. This is only needed if face heights are different.  @return  expression  <br> License requirements : None */
            public: NXOpen::Expression * GetSecondPenetrationDepth
            (
            );
            /** Sets the penetration depth needed to describe groove weld  <br> License requirements : ugweld ("UG WELD") */
            public: void SetSecondPenetrationDepth
            (
                const NXString & secondPenetrationDepth /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the groove creation type  <br> License requirements : None */
            public: NXOpen::Weld::WeldGrooveType GrooveType
            (
            );
            /**Sets  the groove creation type  <br> License requirements : ugweld ("UG WELD") */
            public: void SetGrooveType
            (
                NXOpen::Weld::WeldGrooveType grooveType /** groove type */ 
            );
            /**Returns  the process type  <br> License requirements : None */
            public: NXOpen::Weld::WeldRootUpdate RootUpdate
            (
            );
            /**Sets  the process type  <br> License requirements : ugweld ("UG WELD") */
            public: void SetRootUpdate
            (
                NXOpen::Weld::WeldRootUpdate rootUpdate /** root update */ 
            );
            /**Returns  the field weld status. If true then this is a field weld,
                    if false it is not.  <br> License requirements : None */
            public: bool IsFieldWeld
            (
            );
            /**Sets  the field weld status. If true then this is a field weld,
                    if false it is not.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetFieldWeld
            (
                bool fieldWeld /** field weld */ 
            );
            /**Returns  the the extension method for the top edges  <br> License requirements : None */
            public: NXOpen::Weld::WeldGrooveExtension TopExtension
            (
            );
            /**Sets  the the extension method for the top edges  <br> License requirements : ugweld ("UG WELD") */
            public: void SetTopExtension
            (
                NXOpen::Weld::WeldGrooveExtension extensionType /** extension type */ 
            );
            /**Returns  the extension method for the bottom edges  <br> License requirements : None */
            public: NXOpen::Weld::WeldGrooveExtension BottomExtension
            (
            );
            /**Sets  the extension method for the bottom edges  <br> License requirements : ugweld ("UG WELD") */
            public: void SetBottomExtension
            (
                NXOpen::Weld::WeldGrooveExtension extensionType /** extension type */ 
            );
            /**Returns  the number of connected parts. Either one for two.  <br> License requirements : None */
            public: int NumberRequiredFaceSets
            (
            );
            /**Sets  the number of connected parts. Either one for two.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetNumberRequiredFaceSets
            (
                int numberRequiredFaceSets /** number required face sets */ 
            );
            /**Returns  the distance from the start of the faces to build the groove weld  <br> License requirements : None */
            public: NXOpen::Expression * DistanceFromStart
            (
            );
            /** Set the distance from the start of the faces to build the groove weld  <br> License requirements : ugweld ("UG WELD") */
            public: void SetDistanceFromStart
            (
                const NXString & startDistance /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the distance from the end of the faces to build the groove weld  <br> License requirements : None */
            public: NXOpen::Expression * DistanceFromEnd
            (
            );
            /** Sets the distance from the end of the faces to build the groove weld  <br> License requirements : ugweld ("UG WELD") */
            public: void SetDistanceFromEnd
            (
                const NXString & endDistance /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the taper angle at the start. A positive number will taper towards
                    the inside of the weld.  <br> License requirements : None */
            public: NXOpen::Expression * TaperAtStart
            (
            );
            /** Sets the taper angle at the start. A positive number will taper towards
                    the inside of the weld.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetTaperAtStart
            (
                const NXString & startTaper /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the taper angle at the end. A positive number will taper towards
                    the inside of the weld.  <br> License requirements : None */
            public: NXOpen::Expression * TaperAtEnd
            (
            );
            /** Sets the taper angle at the end. A positive number will taper towards
                    the inside of the weld.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetTaperAtEnd
            (
                const NXString & endTaper /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the method  <br> License requirements : None */
            public: NXOpen::Weld::WeldArcMethod Method
            (
            );
            /**Sets  the method  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMethod
            (
                NXOpen::Weld::WeldArcMethod method /** method */ 
            );
            /**Returns  the is spacing option. This is used when creating skip welds to 
                    compute the spacing between them.  <br> License requirements : None */
            public: bool IsSpacing
            (
            );
            /**Sets  the is spacing option. This is used when creating skip welds to 
                    compute the spacing between them.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetSpacing
            (
                bool isSpacing /** is spacing */ 
            );
            /**Returns  the is number of segments option. This is used when creating skip welds to
                   compute the spacing between them.  <br> License requirements : None */
            public: bool IsNumberOfSegments
            (
            );
            /**Sets  the is number of segments option. This is used when creating skip welds to
                   compute the spacing between them.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetNumberOfSegments
            (
                bool isNumberOfSegments /** is number of segments */ 
            );
            /**Returns  the is segment length option. This is used when creating skip welds to
                   compute the spacing between them.  <br> License requirements : None */
            public: bool IsSegmentLength
            (
            );
            /**Sets  the is segment length option. This is used when creating skip welds to
                   compute the spacing between them.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetSegmentLength
            (
                bool isSegmentLength /** is segment length */ 
            );
            /**Returns  the desired spacing between skip welds.  <br> License requirements : None */
            public: NXOpen::Expression * SpacingDistance
            (
            );
            /** Sets the desired spacing between skip welds.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetSpacingDistance
            (
                const NXString & spacingDistance /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the number of weld welds for a skip weld.   <br> License requirements : None */
            public: NXOpen::Expression * NumberOfSegments
            (
            );
            /** Sets the desired number of segments for the groove weld.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetNumberOfSegments
            (
                const NXString & numSegments /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the segment length for a skip weld.   <br> License requirements : None */
            public: NXOpen::Expression * SegmentLength
            (
            );
            /** Sets the desired segment lengh for the skip weld.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetSegmentLength
            (
                const NXString & segmentLength /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the sequence number for the groove feature. Each groove feature contains a solid.
                    If multiple groove wels are to be created, you must specify the sequence of the groove weld you want.
                    For example if you are expecting 3 welds to be created. You must create 3 groove weld features.
                    The features will have sequence numbers 0,1 and 2.   <br> License requirements : None */
            public: int SequenceNumber
            (
            );
            /**Sets  the sequence number for the groove feature. Each groove feature contains a solid.
                    If multiple groove wels are to be created, you must specify the sequence of the groove weld you want.
                    For example if you are expecting 3 welds to be created. You must create 3 groove weld features.
                    The features will have sequence numbers 0,1 and 2.   <br> License requirements : ugweld ("UG WELD") */
            public: void SetSequenceNumber
            (
                int sequenceNumber /** sequence number */ 
            );
            /**Returns  the output geometry type  <br> License requirements : None */
            public: NXOpen::Weld::WeldFeatureOutput OutputGeometryType
            (
            );
            /**Sets  the output geometry type  <br> License requirements : ugweld ("UG WELD") */
            public: void SetOutputGeometryType
            (
                NXOpen::Weld::WeldFeatureOutput outputGeometryType /** output geometry type */ 
            );
            /**Returns  the apply edge preportion indicator.  <br> License requirements : None */
            public: NXOpen::Weld::WeldPrepareEdges PrepareEdges
            (
            );
            /**Sets  the apply edge preportion indicator.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetPrepareEdges
            (
                NXOpen::Weld::WeldPrepareEdges prepareEdges /** prepare edges */ 
            );
            /**Returns  the taper method to use if tapering is specified.  <br> License requirements : None */
            public: NXOpen::Weld::WeldTaperMethod TaperMethod
            (
            );
            /**Sets  the taper method to use if tapering is specified.  <br> License requirements : ugweld ("UG WELD") */
            public: void SetTaperMethod
            (
                NXOpen::Weld::WeldTaperMethod taperMethod /** taper method */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif