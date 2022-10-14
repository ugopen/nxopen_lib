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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/GeometricAnalysis_SolidDensity.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /** Represents the collection of analysis commands  <br> To obtain an instance of this class, refer to @link BasePart BasePart@endlink  <br> */
        class NXOPENCPPEXPORT AnalysisManager
        {
            private: NXOpen::BasePart* m_owner;
            public: explicit AnalysisManager(NXOpen::BasePart *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Creates an examine geometry object  @return  Examine
                                                                                                Geometry object  <br> License requirements : None */
            public: NXOpen::GeometricAnalysis::ExamineGeometry * CreateExamineGeometryObject
            (
            );
            /** Creates a simple interference object  @return 
                                                                                         Simple Interference object  <br> License requirements : None */
            public: NXOpen::GeometricAnalysis::SimpleInterference * CreateSimpleInterferenceObject
            (
            );
            /** Creates a geometric properties object  @return 
                                                                                        Geometric
                                                                                        Properties object  <br> License requirements : None */
            public: NXOpen::GeometricAnalysis::GeometricProperties * CreateGeometricPropertiesObject
            (
            );
            /** Creates a solid density object  @return  SolidDensity object <br> License requirements : None */
            public: NXOpen::GeometricAnalysis::SolidDensity * CreateSolidDensityObject
            (
            );


            private: NXOpen::GeometricAnalysis::AnalysisObjectCollection *analysisObjects;
            /** Returns the AnalysisObjectCollection instance belonging to this part */
            public: NXOpen::GeometricAnalysis::AnalysisObjectCollection *AnalysisObjects()
            {
                return analysisObjects;
            }
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif