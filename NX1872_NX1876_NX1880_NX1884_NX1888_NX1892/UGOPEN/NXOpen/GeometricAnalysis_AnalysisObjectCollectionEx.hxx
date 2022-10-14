#ifndef NXOpen_GEOMETRICANALYSIS_ANALYSISOBJECTCOLLECTIONEX_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_ANALYSISOBJECTCOLLECTIONEX_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_AnalysisObjectCollectionEx.ja
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
        class AnalysisObjectCollectionEx;
    }
    namespace GeometricAnalysis
    {
        class AnalysisObjectCollection;
    }
    class DisplayableObject;
    namespace GeometricAnalysis
    {
        class DistanceAnalysisBuilder;
    }
    namespace GeometricAnalysis
    {
        class RadiusAnalysisBuilder;
    }
    namespace GeometricAnalysis
    {
        class ReflectionAnalysisBuilder;
    }
    namespace GeometricAnalysis
    {
        class SlopeAnalysisBuilder;
    }
    namespace GeometricAnalysis
    {
        class AnalysisObjectCollectionExImpl;
        /** Collection of analysis objects  <br> To obtain an instance of this class, refer to @link NXOpen::GeometricAnalysis::AnalysisObjectCollection  NXOpen::GeometricAnalysis::AnalysisObjectCollection @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICANALYSISEXPORT  AnalysisObjectCollectionEx
        {
            private: AnalysisObjectCollectionExImpl * m_analysisobjectcollectionex_impl;
            private: NXOpen::GeometricAnalysis::AnalysisObjectCollection* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit AnalysisObjectCollectionEx(NXOpen::GeometricAnalysis::AnalysisObjectCollection *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~AnalysisObjectCollectionEx();
            /** Creates a radius analysis builder.  @return  radius analysis builder 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : gateway ("UG GATEWAY") */
            public: NXOpen::GeometricAnalysis::RadiusAnalysisBuilder * CreateRadiusAnalysisBuilder
            (
                NXOpen::DisplayableObject * radiusAO /** RadiusAO */
            );
            /** Creates a slope analysis builder.  @return  slope analysis builder 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : gateway ("UG GATEWAY") */
            public: NXOpen::GeometricAnalysis::SlopeAnalysisBuilder * CreateSlopeAnalysisBuilder
            (
                NXOpen::DisplayableObject * slopeAO /** SlopeAO */
            );
            /** Creates a distance analysis builder.  @return  distance analysis builder 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : gateway ("UG GATEWAY") */
            public: NXOpen::GeometricAnalysis::DistanceAnalysisBuilder * CreateDistanceAnalysisBuilder
            (
                NXOpen::DisplayableObject * distanceAO /** DistanceAO */
            );
            /** Creates a reflection analysis builder.  @return  reflection analysis builder 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : gateway ("UG GATEWAY") */
            public: NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder * CreateReflectionAnalysisBuilder
            (
                NXOpen::DisplayableObject * reflectionAO /** ReflectionAO */
            );
        }; //lint !e1712 default constructor not defined for class  

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