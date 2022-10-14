#ifndef NXOpen_GEOMETRICANALYSIS_ANALYSISMANAGER_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_ANALYSISMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_AnalysisManager.ja
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
#include <NXOpen/GeometricAnalysis_DeviationChecking.hxx>
#include <NXOpen/GeometricAnalysis_SolidDensity.hxx>
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
        class AnalysisManager;
    }
    class BasePart;
    namespace GeometricAnalysis
    {
        class AnalysisObjectCollection;
    }
    namespace GeometricAnalysis
    {
        class DeviationChecking;
    }
    namespace GeometricAnalysis
    {
        class ExamineGeometry;
    }
    namespace GeometricAnalysis
    {
        class GeometricProperties;
    }
    namespace GeometricAnalysis
    {
        class SimpleInterference;
    }
    namespace GeometricAnalysis
    {
        class SolidDensity;
    }
    namespace GeometricAnalysis
    {
        class AnalysisManagerImpl;
        /** Represents the collection of analysis commands  <br> To obtain an instance of this class, refer to @link BasePart  BasePart @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICANALYSISEXPORT  AnalysisManager
        {
            private: AnalysisManagerImpl * m_analysismanager_impl;
            private: NXOpen::BasePart* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit AnalysisManager(NXOpen::BasePart *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~AnalysisManager();
            /** Creates an examine geometry object  @return  Examine
                                                                                                Geometry object 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricAnalysis::ExamineGeometry * CreateExamineGeometryObject
            (
            );
            /** Creates a simple interference object  @return 
                                                                                         Simple Interference object 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricAnalysis::SimpleInterference * CreateSimpleInterferenceObject
            (
            );
            /** Creates a geometric properties object  @return 
                                                                                        Geometric
                                                                                        Properties object 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricAnalysis::GeometricProperties * CreateGeometricPropertiesObject
            (
            );
            /** Creates a solid density object  @return  SolidDensity object
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricAnalysis::SolidDensity * CreateSolidDensityObject
            (
            );
            /** Creates a deviation checking object  @return  DeviationChecking object
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricAnalysis::DeviationChecking * CreateDeviationCheckingObject
            (
            );


            /** Returns the AnalysisObjectCollection instance belonging to this part 
             <br>  Created in NX3.0.0.  <br>  
            */
            public: NXOpen::GeometricAnalysis::AnalysisObjectCollection *AnalysisObjects();
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