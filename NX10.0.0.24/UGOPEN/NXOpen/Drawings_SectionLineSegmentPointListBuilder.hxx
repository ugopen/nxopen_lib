#ifndef NXOpen_DRAWINGS_SECTIONLINESEGMENTPOINTLISTBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_SECTIONLINESEGMENTPOINTLISTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_SectionLineSegmentPointListBuilder.ja
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
#include <NXOpen/Drawings_SectionLineSegmentPointBuilder.hxx>
#include <NXOpen/Drawings_SectionLineSegmentPointListBuilder.hxx>
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
        class SectionLineSegmentPointListBuilder;
    }
    namespace Drawings
    {
        class SectionLineSegmentPointBuilder;
    }
    class Point;
    namespace Drawings
    {
        class _SectionLineSegmentPointListBuilderBuilder;
        class SectionLineSegmentPointListBuilderImpl;
        /** Represents SectionLineSegmentPointListBuilder class.
                This class maintains a list of @link NXOpen::Drawings::SectionLineSegmentPointBuilder NXOpen::Drawings::SectionLineSegmentPointBuilder@endlink  objects
                and manages them.
            
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  SectionLineSegmentPointListBuilder : public NXOpen::TaggedObject
        {
            private: SectionLineSegmentPointListBuilderImpl * m_sectionlinesegmentpointlistbuilder_impl;
            private: friend class  _SectionLineSegmentPointListBuilderBuilder;
            protected: SectionLineSegmentPointListBuilder();
            public: ~SectionLineSegmentPointListBuilder();
            /** Creates a new @link NXOpen::Drawings::SectionLineSegmentPointBuilder NXOpen::Drawings::SectionLineSegmentPointBuilder@endlink  object  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SectionLineSegmentPointBuilder * CreateSectionLineSegmentPointBuilder
            (
            );
            /** Creates a new @link NXOpen::Drawings::SectionLineSegmentPointBuilder NXOpen::Drawings::SectionLineSegmentPointBuilder@endlink  object  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SectionLineSegmentPointBuilder * AddCutSegment
            (
                NXOpen::Point * location /** location */ 
            );
            /** Creates a new @link NXOpen::Drawings::SectionLineSegmentPointBuilder NXOpen::Drawings::SectionLineSegmentPointBuilder@endlink 
                         In case of point to point section line ,new segment is added at location prior to reference cut segment specified.
                         If reference cut segment is not specified , new segment is added prior to last arrow segment. @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SectionLineSegmentPointBuilder * AddCutSegment
            (
                NXOpen::Point * location /** location */ ,
                NXOpen::Drawings::SectionLineSegmentPointBuilder * referencedCutSegment /**reference SectionLineSegmentPointBuilder */
            );
            /** Appends @link NXOpen::Drawings::SectionLineSegmentPointBuilder NXOpen::Drawings::SectionLineSegmentPointBuilder@endlink  object to the end of the list 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void Append
            (
                NXOpen::Drawings::SectionLineSegmentPointBuilder * pointData /** pointdata */ 
            );
            /** Inserts @link NXOpen::Drawings::SectionLineSegmentPointBuilder NXOpen::Drawings::SectionLineSegmentPointBuilder@endlink  object in the list
                        before a given position 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void Insert
            (
                int insertBeforeIndex /** insert before index */ ,
                NXOpen::Drawings::SectionLineSegmentPointBuilder * point /** point */ 
            );
            /** Deletes a given @link NXOpen::Drawings::SectionLineSegmentPointBuilder NXOpen::Drawings::SectionLineSegmentPointBuilder@endlink  object from the list 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void Delete
            (
                NXOpen::Drawings::SectionLineSegmentPointBuilder * point /** point */ 
            );
            /** Deletes @link NXOpen::Drawings::SectionLineSegmentPointBuilder NXOpen::Drawings::SectionLineSegmentPointBuilder@endlink  object of a certain index from the list 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void Delete
            (
                int index /** index */ 
            );
            /** Deletes all @link NXOpen::Drawings::SectionLineSegmentPointBuilder NXOpen::Drawings::SectionLineSegmentPointBuilder@endlink  objects from the list 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void Clear
            (
            );
            /**Returns  the number of @link NXOpen::Drawings::SectionLineSegmentPointBuilder NXOpen::Drawings::SectionLineSegmentPointBuilder@endlink  objects in the list 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: int Length
            (
            );
            /** Queries all the @link NXOpen::Drawings::SectionLineSegmentPointBuilder NXOpen::Drawings::SectionLineSegmentPointBuilder@endlink  objects  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: std::vector<NXOpen::Drawings::SectionLineSegmentPointBuilder *> GetContents
            (
            );
            /** Sets array of @link NXOpen::Drawings::SectionLineSegmentPointBuilder NXOpen::Drawings::SectionLineSegmentPointBuilder@endlink  objects in the list. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetContents
            (
                const std::vector<NXOpen::Drawings::SectionLineSegmentPointBuilder *> & points /** points */ 
            );
            /** Returns @link NXOpen::Drawings::SectionLineSegmentPointBuilder NXOpen::Drawings::SectionLineSegmentPointBuilder@endlink  object at the input index. 
                        May be NULL if not found.  @return  object found at input index 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Drawings::SectionLineSegmentPointBuilder * FindItem
            (
                int index /** index of object to return */
            );
            /** Finds index of @link NXOpen::Drawings::SectionLineSegmentPointBuilder NXOpen::Drawings::SectionLineSegmentPointBuilder@endlink  object in the list  @return  Equals -1 if not found 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: int GetIndex
            (
                NXOpen::Drawings::SectionLineSegmentPointBuilder * point /** point */ 
            );
            /** Moves a given @link NXOpen::Drawings::SectionLineSegmentPointBuilder NXOpen::Drawings::SectionLineSegmentPointBuilder@endlink  object from the list 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void MoveSegment
            (
                NXOpen::Drawings::SectionLineSegmentPointBuilder * point /** point */ ,
                NXOpen::Point * pointspecified /** pointspecified */ 
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
