#ifndef NXOpen_GEOMETRICANALYSIS_SECTIONANALYSIS_PARALLELPLANESBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_SECTIONANALYSIS_PARALLELPLANESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_SectionAnalysis_ParallelPlanesBuilder.ja
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
#include <NXOpen/GeometricAnalysis_SectionAnalysis_ParallelPlanesBuilder.hxx>
#include <NXOpen/GeometricAnalysis_SectionAnalysis_ParallelSpacingBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/GeometricUtilities_AnchorLocatorBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class ParallelPlanesBuilder;
        }
    }
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class ParallelSpacingBuilder;
        }
    }
    namespace GeometricUtilities
    {
        class AnchorLocatorBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class _ParallelPlanesBuilderBuilder;
            /** Represents the parallel planes section specifications for a @link GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder@endlink .
                        Only used when type is @link SectionAnalysisBuilder::TypesParallel SectionAnalysisBuilder::TypesParallel@endlink .
                    
             @deprecated Deprecated in NX7.0 <br> 
            */
            class NXOPENCPPEXPORT ParallelPlanesBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
            {
                /** Represents the parallel planes methods */
                public: enum Methods
                {
                    MethodsXYZ/** XYZ Planes */,
                    MethodsParallel/** Parallel Planes */
                };

                private: friend class  _ParallelPlanesBuilderBuilder;
                protected: ParallelPlanesBuilder();
                /**Returns  the method  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: NXOpen::GeometricAnalysis::SectionAnalysis::ParallelPlanesBuilder::Methods Method
                (
                );
                /**Sets  the method  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetMethod
                (
                    NXOpen::GeometricAnalysis::SectionAnalysis::ParallelPlanesBuilder::Methods method /** method */ 
                );
                /**Returns  the flag to enable parallel sections in x-direction  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: bool IsXDirectionEnabled
                (
                );
                /**Sets  the flag to enable parallel sections in x-direction  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetXDirectionEnabled
                (
                    bool enableDirection /** enabledirection */ 
                );
                /**Returns  the flag to enable parallel sections in y-direction  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: bool IsYDirectionEnabled
                (
                );
                /**Sets  the flag to enable parallel sections in y-direction  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetYDirectionEnabled
                (
                    bool enableDirection /** enabledirection */ 
                );
                /**Returns  the flag to enable parallel sections in z-direction  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: bool IsZDirectionEnabled
                (
                );
                /**Sets  the flag to enable parallel sections in z-direction  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetZDirectionEnabled
                (
                    bool enableDirection /** enabledirection */ 
                );
                /**Returns  the spacing specification for the parallel planes  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: NXOpen::GeometricAnalysis::SectionAnalysis::ParallelSpacingBuilder * Spacing
                (
                );
                /**Returns  the anchor of the parallel planes  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: NXOpen::GeometricUtilities::AnchorLocatorBuilder * Anchor
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
}
#undef EXPORTLIBRARY
#endif