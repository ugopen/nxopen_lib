#ifndef NXOpen_GEOMETRICANALYSIS_SECTIONANALYSISOBJECT_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_SECTIONANALYSISOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_SectionAnalysisObject.ja
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
#include <NXOpen/GeometricAnalysis_AnalysisObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricAnalysis
    {
        class SectionAnalysisObject;
    }
    namespace GeometricAnalysis
    {
        class AnalysisObject;
    }
    namespace GeometricAnalysis
    {
        class _SectionAnalysisObjectBuilder;
        class SectionAnalysisObjectImpl;
        /** Represents a Section Analysis object. Section Analysis
            generates planar, circular, or isoparametric sections across faces and faceted bodies 
            to help evaluating sectional curvature flow of faces and surface quality and 
            characteristics in general. Section Analysis object update dynamically on geometry 
            changes of the sectioned faces and faceted bodies. */
        class NXOPENCPPEXPORT  SectionAnalysisObject : public GeometricAnalysis::AnalysisObject
        {
            private: SectionAnalysisObjectImpl * m_sectionanalysisobject_impl;
            private: friend class  _SectionAnalysisObjectBuilder;
            protected: SectionAnalysisObject();
            public: ~SectionAnalysisObject();
        };
    }
}
#undef EXPORTLIBRARY
#endif