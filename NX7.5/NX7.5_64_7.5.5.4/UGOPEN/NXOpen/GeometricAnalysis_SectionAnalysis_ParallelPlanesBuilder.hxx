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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
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
            class ParallelPlanesBuilderImpl;
            /** Represents the parallel planes section specifications for a @link GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder@endlink .
                        Only used when type is @link GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesParallel GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesParallel@endlink .
                    
             @deprecated Deprecated in NX7.0.0 <br> 
            */
            class NXOPENCPPEXPORT  NX_DEPRECATED("Deprecated in NX7.0.0")  ParallelPlanesBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
            {
                /** Represents the parallel planes methods */
                public: enum Methods
                {
                    MethodsXYZ/** XYZ Planes */,
                    MethodsParallel/** Parallel Planes */
                };

                private: ParallelPlanesBuilderImpl * m_parallelplanesbuilder_impl;
                private: friend class  _ParallelPlanesBuilderBuilder;
                protected: ParallelPlanesBuilder();
                public: ~ParallelPlanesBuilder();
                /**Returns  the method 
                 @deprecated Deprecated in NX7.0.0 <br> 
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public:  NX_DEPRECATED("Deprecated in NX7.0.0") NXOpen::GeometricAnalysis::SectionAnalysis::ParallelPlanesBuilder::Methods Method
                (
                );
                /**Sets  the method 
                 @deprecated Deprecated in NX7.0.0 <br> 
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public:  NX_DEPRECATED("Deprecated in NX7.0.0") void SetMethod
                (
                    NXOpen::GeometricAnalysis::SectionAnalysis::ParallelPlanesBuilder::Methods method /** method */ 
                );
                /**Returns  the flag to enable parallel sections in x-direction 
                 @deprecated Deprecated in NX7.0.0 <br> 
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public:  NX_DEPRECATED("Deprecated in NX7.0.0") bool IsXDirectionEnabled
                (
                );
                /**Sets  the flag to enable parallel sections in x-direction 
                 @deprecated Deprecated in NX7.0.0 <br> 
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public:  NX_DEPRECATED("Deprecated in NX7.0.0") void SetXDirectionEnabled
                (
                    bool enableDirection /** enabledirection */ 
                );
                /**Returns  the flag to enable parallel sections in y-direction 
                 @deprecated Deprecated in NX7.0.0 <br> 
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public:  NX_DEPRECATED("Deprecated in NX7.0.0") bool IsYDirectionEnabled
                (
                );
                /**Sets  the flag to enable parallel sections in y-direction 
                 @deprecated Deprecated in NX7.0.0 <br> 
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public:  NX_DEPRECATED("Deprecated in NX7.0.0") void SetYDirectionEnabled
                (
                    bool enableDirection /** enabledirection */ 
                );
                /**Returns  the flag to enable parallel sections in z-direction 
                 @deprecated Deprecated in NX7.0.0 <br> 
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public:  NX_DEPRECATED("Deprecated in NX7.0.0") bool IsZDirectionEnabled
                (
                );
                /**Sets  the flag to enable parallel sections in z-direction 
                 @deprecated Deprecated in NX7.0.0 <br> 
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public:  NX_DEPRECATED("Deprecated in NX7.0.0") void SetZDirectionEnabled
                (
                    bool enableDirection /** enabledirection */ 
                );
                /**Returns  the spacing specification for the parallel planes 
                 @deprecated Deprecated in NX7.0.0 <br> 
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public:  NX_DEPRECATED("Deprecated in NX7.0.0") NXOpen::GeometricAnalysis::SectionAnalysis::ParallelSpacingBuilder * Spacing
                (
                );
                /**Returns  the anchor of the parallel planes 
                 @deprecated Deprecated in NX7.0.0 <br> 
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public:  NX_DEPRECATED("Deprecated in NX7.0.0") NXOpen::GeometricUtilities::AnchorLocatorBuilder * Anchor
                (
                );
                /** Returns true if the inputs to the component are sufficient for 
                            commit to be called.  For example, if the component requires
                            you to set some property, this method will return false if
                            you haven't set it.  This method throws a not-yet-implemented
                            NXException for some components.
                         @return  Was self validation successful  <br> License requirements : None */
                public: virtual bool Validate
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif