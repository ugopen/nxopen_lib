#ifndef NXOpen_GEOMETRICANALYSIS_EXAMINEGEOMETRY_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_EXAMINEGEOMETRY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_ExamineGeometry.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/GeometricAnalysis_ExamineGeometry.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricAnalysis
    {
        class ExamineGeometry;
    }
    class Builder;
    class NXObject;
    class SelectObjectList;
    namespace GeometricAnalysis
    {
        class _ExamineGeometryBuilder;
        /** Represents the Examine Geometry class
              <br> To create a new instance of this class, use @link GeometricAnalysis::AnalysisManager::CreateExamineGeometryObject GeometricAnalysis::AnalysisManager::CreateExamineGeometryObject@endlink  <br> */
        class NXOPENCPPEXPORT ExamineGeometry : public Builder
        {
            /** Types of checks */
            public: enum Check
            {
                CheckObjectTiny/** ObjectTiny */,
                CheckObjectMisaligned/** ObjectMisaligned */,
                CheckBodyDataStructures/** BodyDataStructures */,
                CheckBodyConsistency/** BodyConsistency */,
                CheckBodyFaceIntersections/** BodyFaceIntersections */,
                CheckBodySheetBoundaries/** BodySheetBoundaries */,
                CheckFaceSmoothness/** FaceSmoothness */,
                CheckFaceSelfIntersection/** FaceSelfIntersection */,
                CheckFaceSpikesCuts/** FaceSpikesCuts */,
                CheckEdgeSmoothness/** EdgeSmoothness */,
                CheckEdgeTolerances/** EdgeTolerances */,
                CheckNumChecks/** Number of Checks */
            };

            private: friend class  _ExamineGeometryBuilder;
            protected: ExamineGeometry();
            /**Returns  the Objects to examine  <br> License requirements : None */
            public: NXOpen::SelectObjectList * ObjectsToExamine
            (
            );
            /** Set all types of checks to examine  <br> License requirements : None */
            public: void SetAllChecks
            (
            );
            /** Clear or unset all types of checks  <br> License requirements : None */
            public: void ClearAllChecks
            (
            );
            /** Set a specified type of check for examine geometry  <br> License requirements : None */
            public: void SetCheck
            (
                NXOpen::GeometricAnalysis::ExamineGeometry::Check check /** Type of Check */
            );
            /** Clear or unset a specified type of check  <br> License requirements : None */
            public: void ClearCheck
            (
                NXOpen::GeometricAnalysis::ExamineGeometry::Check check /** Type of Check */
            );
            /**Sets  the Check Criteria Distance  <br> License requirements : None */
            public: void SetCheckCriteriaDistance
            (
                double distance /** distance */ 
            );
            /**Returns  the Check Criteria Distance  <br> License requirements : None */
            public: double CheckCriteriaDistance
            (
            );
            /**Sets  the Check Criteria Angle  <br> License requirements : None */
            public: void SetCheckCriteriaAngle
            (
                double angle /** angle */ 
            );
            /**Returns  the Check Criteria Angle  <br> License requirements : None */
            public: double CheckCriteriaAngle
            (
            );
            /** Examines the geometry.  Before calling this method, use 
                        @link GeometricAnalysis::ExamineGeometry::SetCheck GeometricAnalysis::ExamineGeometry::SetCheck@endlink  and @link GeometricAnalysis::ExamineGeometry::ClearCheck GeometricAnalysis::ExamineGeometry::ClearCheck@endlink  
                        to specify which checks to perform and use @link GeometricAnalysis::ExamineGeometry::ObjectsToExamine GeometricAnalysis::ExamineGeometry::ObjectsToExamine@endlink  
                        to specify which objects to examine.  After calling this method, 
                        use @link GeometricAnalysis::ExamineGeometry::GetResults GeometricAnalysis::ExamineGeometry::GetResults@endlink  and 
                        @link GeometricAnalysis::ExamineGeometry::GetFailedObjects GeometricAnalysis::ExamineGeometry::GetFailedObjects@endlink  to get the results.  <br> License requirements : None */
            public: void Examine
            (
            );
            /** Returns an array containing the number of objects that failed each check.
                          You should call @link Examine Examine@endlink  before calling this 
                          method.    The array contains an entry for each check in the
                          @link Check Check@endlink  enumeration.  The nth item in the array corresponds to
                          the nth check in the @link Check Check@endlink  enumeration.  For example, the 
                          first item in the array is the number of objects that failed the 
                          @link GeometricAnalysis::ExamineGeometry::CheckObjectTiny GeometricAnalysis::ExamineGeometry::CheckObjectTiny@endlink  check.  
                          The corresponding entry in the array will be as follows:
                           <br>  <br> 
                          <ul>
                          <li> <b>-1</b>    errors</li>
                          <li> <b>0</b>    Check not performed as check is not selected</li>
                          <li> <b>-2</b>    a type of @link Check Check@endlink  is selected, no objects relevant to that type 
                                of @link Check Check@endlink  are selected. For example, no bodies are selected yet the 
                                @link GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures@endlink  check is
                                set or selected. </li>
                          <li> <b>-3</b>    @link Check Check@endlink  not performed as other relevant @link Check Check@endlink  failed. This occurs when 
                                @link GeometricAnalysis::ExamineGeometry::CheckBodyConsistency GeometricAnalysis::ExamineGeometry::CheckBodyConsistency@endlink 
                                and/or @link GeometricAnalysis::ExamineGeometry::CheckBodyFaceIntersections GeometricAnalysis::ExamineGeometry::CheckBodyFaceIntersections@endlink  check is set along with 
                                @link GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures@endlink  check.
                                If @link GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures@endlink  check
                                failed, @link GeometricAnalysis::ExamineGeometry::CheckBodyConsistency GeometricAnalysis::ExamineGeometry::CheckBodyConsistency@endlink 
                                and/or
                                @link GeometricAnalysis::ExamineGeometry::CheckBodyFaceIntersections GeometricAnalysis::ExamineGeometry::CheckBodyFaceIntersections@endlink  will
                                not be performed. </li> 
                        </ul>  @return  Results of Examine Geometry  <br> License requirements : None */
            public: std::vector<int> GetResults
            (
            );
            /** Returns the objects that failed a given type of check.  You should 
                    call @link Examine Examine@endlink  before calling this method.    @return  Objects that
                     failed above check during Examine Geometry  <br> License requirements : None */
            public: std::vector<NXOpen::NXObject *> GetFailedObjects
            (
                NXOpen::GeometricAnalysis::ExamineGeometry::Check check /** Type of Check */
            );
            /** Highlights results of a specified type of check. If the
                     highlighting fails for some of the entities, it returns True, otherwise
                     False.  Highlighting can fail when the entities are corrupt or missing
                     the information needed to display properly. Remaining entities are highlighted 
                     when highlighting fails for some entities.  @return  Return status of the method.
                                                               If return values equals
                                                               false, display was successful. 
                                                               if return value is true,
                                                               display of some objects
                                                               failed.  <br> License requirements : None */
            public: bool HighlightResult
            (
                NXOpen::GeometricAnalysis::ExamineGeometry::Check check /** Type of Check */
            );
            /** Unhighlight results of a specified type of check <br> License requirements : None */
            public: void UnhighlightResult
            (
                NXOpen::GeometricAnalysis::ExamineGeometry::Check check /** Type of Check */
            );
            /** Unhighlight all results  <br> License requirements : None */
            public: void UnhighlightAllResults
            (
            );
            /** Displays the results in the information window  <br> License requirements : None */
            public: void DisplayResultsAsInfo
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
