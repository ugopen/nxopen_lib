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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
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
            class GridSpacingBuilderImpl;
            /** Represents the grid spacing for certain types of section specifications for
                        the @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder@endlink .
                    
             <br>  Created in NX6.0.0.  <br>  
            */
            class NXOPENCPP_GEOMETRICANALYSISEXPORT  GridSpacingBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
            {
                private: GridSpacingBuilderImpl * m_gridspacingbuilder_impl;
                private: friend class  _GridSpacingBuilderBuilder;
                protected: GridSpacingBuilder();
                public: ~GridSpacingBuilder();
                /**Returns  the number of sections in direction 1 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: int SectionNumber1
                (
                );
                /**Sets  the number of sections in direction 1 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetSectionNumber1
                (
                    int sectionNumber1 /** sectionnumber1 */ 
                );
                /**Returns  the number of sections in direction 2 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: int SectionNumber2
                (
                );
                /**Sets  the number of sections in direction 2 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetSectionNumber2
                (
                    int sectionNumber2 /** sectionnumber2 */ 
                );
                /**Returns  the interval of sections in direction 1 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: double Interval1
                (
                );
                /**Sets  the interval of sections in direction 1 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetInterval1
                (
                    double interval1 /** interval1 */ 
                );
                /**Returns  the interval of sections in direction 2 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: double Interval2
                (
                );
                /**Sets  the interval of sections in direction 2 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetInterval2
                (
                    double interval2 /** interval2 */ 
                );
                /**Returns  the flag to lock the section interval in direction 1 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: bool LockInterval1
                (
                );
                /**Sets  the flag to lock the section interval in direction 1 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetLockInterval1
                (
                    bool lockInterval1 /** lockinterval1 */ 
                );
                /**Returns  the flag to lock the section interval in direction 2 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: bool LockInterval2
                (
                );
                /**Sets  the flag to lock the section interval in direction 2 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetLockInterval2
                (
                    bool lockInterval2 /** lockinterval2 */ 
                );
                /**Returns  the flag to bound the section to grid in direction 1 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: bool BoundSections1
                (
                );
                /**Sets  the flag to bound the section to grid in direction 1 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetBoundSections1
                (
                    bool boundSections1 /** boundsections1 */ 
                );
                /**Returns  the flag to bound the section to grid in direction 2 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: bool BoundSections2
                (
                );
                /**Sets  the flag to bound the section to grid in direction 2 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
                public: void SetBoundSections2
                (
                    bool boundSections2 /** boundsections2 */ 
                );
                /** Validate whether the inputs to the component are sufficient for 
                            commit to be called.  If the component is not in a state to commit
                            then an exception is thrown.  For example, if the component requires
                            you to set some property, this method will throw an exception if
                            you haven't set it.  This method throws a not yet implemented
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
