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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/GeometricAnalysis_SectionAnalysis_InteractiveBuilder.hxx>
#include <NXOpen/GeometricUtilities_InteractiveSectionBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_geometricanalysis_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

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
            class InteractiveBuilderImpl;
            /** Represents the Interactive specification for a @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder@endlink .
             <br>  Created in NX7.0.0.  <br>  
            */
            class NXOPENCPP_GEOMETRICANALYSISEXPORT  InteractiveBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
            {
                private: InteractiveBuilderImpl * m_interactivebuilder_impl;
                private: friend class  _InteractiveBuilderBuilder;
                protected: InteractiveBuilder();
                public: ~InteractiveBuilder();
                /**Returns  the interactive section lines 
                 <br>  Created in NX7.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::GeometricUtilities::InteractiveSectionBuilder * InteractiveSection
                (
                );
                /**Returns  a value indicating whether extending the interactive section lines to infinite 
                 <br>  Created in NX7.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IsCutInfiniteEnabled
                (
                );
                /**Sets  a value indicating whether extending the interactive section lines to infinite 
                 <br>  Created in NX7.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetCutInfiniteEnabled
                (
                    bool enabled /** enabled */ 
                );
                /** Validate whether the inputs to the component are sufficient for 
                            commit to be called.  If the component is not in a state to commit
                            then an exception is thrown.  For example, if the component requires
                            you to set some property, this method will throw an exception if
                            you haven't set it.  This method throws a not-yet-implemented
                            NXException for some components.
                         @return  Was self validation successful 
                 <br>  Created in NX3.0.1.  <br>  
                 <br> License requirements : None */
                public: virtual bool Validate
                (
                );
            };
        }
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
