#ifndef NXOpen_GEOMETRICANALYSIS_SECTIONANALYSIS_GRIDSPACINGBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_SECTIONANALYSIS_GRIDSPACINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_SectionAnalysis_GridSpacingBuilder.ja
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
#include <NXOpen/GeometricAnalysis_SectionAnalysis_GridSpacingBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class GridSpacingBuilder;
        }
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricAnalysis
    {
        namespace SectionAnalysis
        {
            class _GridSpacingBuilderBuilder;
            /** Represents the grid spacing for certain types of section specifications for
                        the @link GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder@endlink . 
                    */
            class NXOPENCPPEXPORT GridSpacingBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
            {
                private: friend class  _GridSpacingBuilderBuilder;
                protected: GridSpacingBuilder();
                /**Returns  the number of sections in direction 1  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: int SectionNumber1
                (
                );
                /**Sets  the number of sections in direction 1  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetSectionNumber1
                (
                    int sectionNumber1 /** sectionnumber1 */ 
                );
                /**Returns  the number of sections in direction 2  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: int SectionNumber2
                (
                );
                /**Sets  the number of sections in direction 2  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetSectionNumber2
                (
                    int sectionNumber2 /** sectionnumber2 */ 
                );
                /**Returns  the interval of sections in direction 1  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: double Interval1
                (
                );
                /**Sets  the interval of sections in direction 1  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetInterval1
                (
                    double interval1 /** interval1 */ 
                );
                /**Returns  the interval of sections in direction 2  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: double Interval2
                (
                );
                /**Sets  the interval of sections in direction 2  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetInterval2
                (
                    double interval2 /** interval2 */ 
                );
                /**Returns  the flag to lock the section interval in direction 1  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: bool LockInterval1
                (
                );
                /**Sets  the flag to lock the section interval in direction 1  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetLockInterval1
                (
                    bool lockInterval1 /** lockinterval1 */ 
                );
                /**Returns  the flag to lock the section interval in direction 2  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: bool LockInterval2
                (
                );
                /**Sets  the flag to lock the section interval in direction 2  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetLockInterval2
                (
                    bool lockInterval2 /** lockinterval2 */ 
                );
                /**Returns  the flag to bound the section to grid in direction 1  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: bool BoundSections1
                (
                );
                /**Sets  the flag to bound the section to grid in direction 1  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetBoundSections1
                (
                    bool boundSections1 /** boundsections1 */ 
                );
                /**Returns  the flag to bound the section to grid in direction 2  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: bool BoundSections2
                (
                );
                /**Sets  the flag to bound the section to grid in direction 2  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetBoundSections2
                (
                    bool boundSections2 /** boundsections2 */ 
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