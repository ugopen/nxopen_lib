#ifndef NXOpen_GEOMETRICANALYSIS_SECTIONANALYSIS_RADIALBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_SECTIONANALYSIS_RADIALBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_SectionAnalysis_RadialBuilder.ja
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
#include <NXOpen/GeometricAnalysis_SectionAnalysis_RadialBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class RadialBuilder;
        }
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class Point;
    class SelectPoint;
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class _RadialBuilderBuilder;
            /** Represents the Radial specification for a @link GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder@endlink .*/
            class NXOPENCPPEXPORT RadialBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
            {
                /** The type of the rotation axis*/
                public: enum RotationAxisType
                {
                    RotationAxisTypeXc/** XC axis */,
                    RotationAxisTypeYc/** YC axis */,
                    RotationAxisTypeZc/** ZC axis */,
                    RotationAxisTypeView/** View direction */,
                    RotationAxisTypeArbitraryVector/** A user specified vector */
                };

                private: friend class  _RadialBuilderBuilder;
                protected: RadialBuilder();
                /**Returns  a value indicating the type of the rotation axis <br> License requirements : None */
                public: NXOpen::GeometricAnalysis::SectionAnalysis::RadialBuilder::RotationAxisType RotationAxis
                (
                );
                /**Sets  a value indicating the type of the rotation axis <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetRotationAxis
                (
                    NXOpen::GeometricAnalysis::SectionAnalysis::RadialBuilder::RotationAxisType rotationAxis /** rotationaxis */ 
                );
                /**Returns  the user specified rotation vector  <br> License requirements : None */
                public: NXOpen::Vector3d RotationVector
                (
                );
                /**Sets  the user specified rotation vector  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetRotationVector
                (
                    const NXOpen::Vector3d & rotationVector /** rotationvector */ 
                );
                /**Returns  the rotation point  <br> License requirements : None */
                public: NXOpen::Point * SpecifiedRotationPoint
                (
                );
                /**Sets  the rotation point  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetSpecifiedRotationPoint
                (
                    NXOpen::Point * specifiedRotationPoint /** specifiedrotationpoint */ 
                );
                /**Returns  the start position  <br> License requirements : None */
                public: NXOpen::SelectPoint * StartPosition
                (
                );
                /**Returns  a value indicating how many sections should created  <br> License requirements : None */
                public: int Number
                (
                );
                /**Sets  a value indicating how many sections should created  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetNumber
                (
                    int number /** number */ 
                );
                /**Returns  a value indicating whether the spacing is applied  <br> License requirements : None */
                public: bool IsSpacingEnabled
                (
                );
                /**Sets  a value indicating whether the spacing is applied  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetSpacingEnabled
                (
                    bool isSpacingEnabled /** isspacingenabled */ 
                );
                /**Returns  a value indicating the space between sections  <br> License requirements : None */
                public: double Spacing
                (
                );
                /**Sets  a value indicating the space between sections  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetSpacing
                (
                    double spacing /** spacing */ 
                );
                /**Returns  a value indicating the distance from the start position  <br> License requirements : None */
                public: double Offset
                (
                );
                /**Sets  a value indicating the distance from the start position  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetOffset
                (
                    double offset /** offset */ 
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
}
#undef EXPORTLIBRARY
#endif