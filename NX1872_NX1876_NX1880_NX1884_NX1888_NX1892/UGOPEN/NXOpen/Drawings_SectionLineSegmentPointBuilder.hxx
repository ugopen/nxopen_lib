#ifndef NXOpen_DRAWINGS_SECTIONLINESEGMENTPOINTBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_SECTIONLINESEGMENTPOINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_SectionLineSegmentPointBuilder.ja
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
#include <NXOpen/libnxopencpp_drawings_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drawings
    {
        class SectionLineSegmentPointBuilder;
    }
    class Point;
    namespace Drawings
    {
        class _SectionLineSegmentPointBuilderBuilder;
        class SectionLineSegmentPointBuilderImpl;
        /** Represents Section Line Segment Point Builder   <br> To create a new instance of this class, use @link NXOpen::Drawings::SectionLineSegmentPointListBuilder::CreateSectionLineSegmentPointBuilder  NXOpen::Drawings::SectionLineSegmentPointListBuilder::CreateSectionLineSegmentPointBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  SectionLineSegmentPointBuilder : public NXOpen::TaggedObject
        {
            /** Section Segment Types*/
            public: enum SegmentTypes
            {
                SegmentTypesArrow/** arrow */  = 1,
                SegmentTypesCut/** cut */ ,
                SegmentTypesBend/** bend */ 
            };

            private: SectionLineSegmentPointBuilderImpl * m_sectionlinesegmentpointbuilder_impl;
            private: friend class  _SectionLineSegmentPointBuilderBuilder;
            protected: SectionLineSegmentPointBuilder();
            public: ~SectionLineSegmentPointBuilder();
            /**Returns  the section line segment @link NXOpen::Point NXOpen::Point@endlink  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Point * Point
            (
            );
            /**Sets  the section line segment @link NXOpen::Point NXOpen::Point@endlink  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetPoint
            (
                NXOpen::Point * point /** point */ 
            );
            /**Returns  the segment type
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Drawings::SectionLineSegmentPointBuilder::SegmentTypes SegmentType
            (
            );
            /**Sets  the segment type
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetSegmentType
            (
                NXOpen::Drawings::SectionLineSegmentPointBuilder::SegmentTypes type /** type */ 
            );
        };
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