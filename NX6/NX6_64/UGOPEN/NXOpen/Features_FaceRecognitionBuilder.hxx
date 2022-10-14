#ifndef NXOpen_FEATURES_FACERECOGNITIONBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_FACERECOGNITIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_FaceRecognitionBuilder.ja
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
#include <NXOpen/Features_FaceRecognitionBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/GeometricUtilities_OrientXpressBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class FaceRecognitionBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class OrientXpressBuilder;
    }
    class NXObject;
    class ScCollector;
    namespace Features
    {
        class _FaceRecognitionBuilderBuilder;
        /** Represents a collection of faces and their relationships to other faces in the model */
        class NXOPENCPPEXPORT FaceRecognitionBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: friend class  _FaceRecognitionBuilderBuilder;
            protected: FaceRecognitionBuilder();
            /**Returns  the face collector  <br> License requirements : None */
            public: NXOpen::ScCollector * FaceCollector
            (
            );
            /**Returns  a value that indicates whether coplanar relation recognition is enabled  <br> License requirements : None */
            public: bool CoplanarEnabled
            (
            );
            /**Sets  a value that indicates whether coplanar relation recognition is enabled  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCoplanarEnabled
            (
                bool coplanarEnabled /** coplanarenabled */ 
            );
            /**Returns  a value that indicates whether coplanar axes relation recognition is enabled  <br> License requirements : None */
            public: bool CoplanarAxesEnabled
            (
            );
            /**Sets  a value that indicates whether coplanar axes relation recognition is enabled  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCoplanarAxesEnabled
            (
                bool coplanarEnabled /** coplanarenabled */ 
            );
            /**Returns  a value that indicates whether coaxial relation recognition is enabled  <br> License requirements : None */
            public: bool CoaxialEnabled
            (
            );
            /**Sets  a value that indicates whether coaxial relation recognition is enabled  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCoaxialEnabled
            (
                bool coaxialEnabled /** coaxialenabled */ 
            );
            /**Returns  a value that indicates whether tangent relation recognition is enabled  <br> License requirements : None */
            public: bool TangentEnabled
            (
            );
            /**Sets  a value that indicates whether tangent relation recognition is enabled  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTangentEnabled
            (
                bool tangentEnabled /** tangentenabled */ 
            );
            /**Returns  a value that indicates whether equal diameter recognition is enabled  <br> License requirements : None */
            public: bool EqualDiameterEnabled
            (
            );
            /**Sets  a value that indicates whether equal diameter recognition is enabled  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetEqualDiameterEnabled
            (
                bool equalDiameterEnabled /** equaldiameterenabled */ 
            );
            /**Returns  a value that indicates whether symmetric relation recognition is enabled  <br> License requirements : None */
            public: bool SymmetricEnabled
            (
            );
            /**Sets  a value that indicates whether symmetric relation recognition is enabled  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSymmetricEnabled
            (
                bool symmetricEnabled /** symmetricenabled */ 
            );
            /**Returns  a value that indicates whether parallel relation recognition is enabled  <br> License requirements : None */
            public: bool ParallelEnabled
            (
            );
            /**Sets  a value that indicates whether parallel relation recognition is enabled  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetParallelEnabled
            (
                bool parallelEnabled /** parallelenabled */ 
            );
            /**Returns  a value that indicates whether perpendicular relation recognition is enabled  <br> License requirements : None */
            public: bool PerpendicularEnabled
            (
            );
            /**Sets  a value that indicates whether perpendicular relation recognition is enabled  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPerpendicularEnabled
            (
                bool perpendicularEnabled /** perpendicularenabled */ 
            );
            /** Adds entities to collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SelectEntities
            (
                const std::vector<NXOpen::NXObject *> & entities /** entities */ 
            );
            /** Removes entities from collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void DeselectEntities
            (
                const std::vector<NXOpen::NXObject *> & entities /** entities */ 
            );
            /** Recognizes coplanar relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void RecognizeCoplanar
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /** Removes coplanar relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void UnrecognizeCoplanar
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /** Recognizes coplanar axes relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void RecognizeCoplanarAxes
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /** Removes coplanar axes relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void UnrecognizeCoplanarAxes
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /** Recognizes coaxial relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void RecognizeCoaxial
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /** Removes coaxial relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void UnrecognizeCoaxial
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /** Recognizes tangent relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void RecognizeTangent
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /** Removes tangent relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void UnrecognizeTangent
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /** Recognizes symmetric relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void RecognizeSymmetric
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /** Removes symmetric relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void UnrecognizeSymmetric
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /** Recognizes equal diameter relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void RecognizeEqualDiameter
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /** Removes equal diameter relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void UnrecognizeEqualDiameter
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /** Recognizes parallel relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void RecognizeParallel
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /** Removes parallel relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void UnrecognizeParallel
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /** Recognizes perpendicular relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void RecognizePerpendicular
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /** Removes perpendicular relations to last faces added to face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void UnrecognizePerpendicular
            (
                bool isNear /** true for near relations, false for far relations*/
            );
            /**Returns  a value that indicates whether relations are found when faces are added to the face collector  <br> License requirements : None */
            public: bool UseFaceBrowse
            (
            );
            /**Sets  a value that indicates whether relations are found when faces are added to the face collector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetUseFaceBrowse
            (
                bool useFaceBrowse /** usefacebrowse */ 
            );
            /**Returns  the reference coordinate system to use for symmetry and coplanar axis recognition  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OrientXpressBuilder * ReferenceCoordinateSystem
            (
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif