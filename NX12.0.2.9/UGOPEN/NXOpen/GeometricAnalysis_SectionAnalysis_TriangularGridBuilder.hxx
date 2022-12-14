#ifndef NXOpen_GEOMETRICANALYSIS_SECTIONANALYSIS_TRIANGULARGRIDBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_SECTIONANALYSIS_TRIANGULARGRIDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_SectionAnalysis_TriangularGridBuilder.ja
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
#include <NXOpen/GeometricAnalysis_SectionAnalysis_GridSpacingBuilder.hxx>
#include <NXOpen/GeometricAnalysis_SectionAnalysis_SectionPlaneBuilder.hxx>
#include <NXOpen/GeometricUtilities_TriangularFrameBuilder.hxx>
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
            class TriangularGridBuilder;
        }
    }
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class GridSpacingBuilder;
        }
    }
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class SectionPlaneBuilder;
        }
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class TriangularFrameBuilder;
    }
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class _TriangularGridBuilderBuilder;
            class TriangularGridBuilderImpl;
            /** Represents the triangular grid section specifications for a SectionAnalysisBuilder.
                        Only used when type is @link GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesTriangular GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesTriangular@endlink .
                    
             <br>  Created in NX6.0.0.  <br>  
            */
            class NXOPENCPP_GEOMETRICANALYSISEXPORT  TriangularGridBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
            {
                private: TriangularGridBuilderImpl * m_triangulargridbuilder_impl;
                private: friend class  _TriangularGridBuilderBuilder;
                protected: TriangularGridBuilder();
                public: ~TriangularGridBuilder();
                /**Returns  the spacing specification for the triangular grid 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: NXOpen::GeometricAnalysis::SectionAnalysis::GridSpacingBuilder * Spacing
                (
                );
                /**Returns  the triangular frame 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: NXOpen::GeometricUtilities::TriangularFrameBuilder * TriangularFrame
                (
                );
                /**Returns  the user specified section plane 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::GeometricAnalysis::SectionAnalysis::SectionPlaneBuilder * SpecifiedPlane
                (
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
