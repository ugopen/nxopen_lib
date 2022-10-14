#ifndef NXOpen_GEOMETRICANALYSIS_SECTIONANALYSIS_INTERACTIVEBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_SECTIONANALYSIS_INTERACTIVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_SectionAnalysis_InteractiveBuilder.ja
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
#include <NXOpen/GeometricAnalysis_SectionAnalysis_InteractiveBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/GeometricUtilities_InteractiveSectionBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class InteractiveBuilder;
        }
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class InteractiveSectionBuilder;
    }
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class _InteractiveBuilderBuilder;
            /** Represents the Interactive specification for a @link GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder@endlink .*/
            class NXOPENCPPEXPORT InteractiveBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
            {
                private: friend class  _InteractiveBuilderBuilder;
                protected: InteractiveBuilder();
                /**Returns  the interactive section lines  <br> License requirements : None */
                public: NXOpen::GeometricUtilities::InteractiveSectionBuilder * InteractiveSection
                (
                );
                /**Returns  a value indicating whether extending the interactive section lines to infinite  <br> License requirements : None */
                public: bool IsCutInfiniteEnabled
                (
                );
                /**Sets  a value indicating whether extending the interactive section lines to infinite  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetCutInfiniteEnabled
                (
                    bool enabled /** enabled */ 
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