#ifndef NXOpen_DRAWINGS_POINTANDANGLESECTIONLINEBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_POINTANDANGLESECTIONLINEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_PointAndAngleSectionLineBuilder.ja
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
#include <NXOpen/Drawings_PointAndAngleSectionLineBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
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
        class PointAndAngleSectionLineBuilder;
    }
    namespace Drawings
    {
        class SectionLineSegmentBuilderList;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class Point;
    namespace Drawings
    {
        class _PointAndAngleSectionLineBuilderBuilder;
        class PointAndAngleSectionLineBuilderImpl;
        /** Represents a @link Drawings::PointAndAngleSectionLineBuilder Drawings::PointAndAngleSectionLineBuilder@endlink .
                This class is used to create or edit a
                @link Drawings::PointAndAngleSectionLine Drawings::PointAndAngleSectionLine@endlink . 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  PointAndAngleSectionLineBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: PointAndAngleSectionLineBuilderImpl * m_pointandanglesectionlinebuilder_impl;
            private: friend class  _PointAndAngleSectionLineBuilderBuilder;
            protected: PointAndAngleSectionLineBuilder();
            public: ~PointAndAngleSectionLineBuilder();
            /**Returns  the list of cut segments.

                        The list will contain @link Drawings::SectionLineSegmentBuilder Drawings::SectionLineSegmentBuilder@endlink 
                        segments of type @link Drawings::SectionLineSegmentBuilder::TypesAngle Drawings::SectionLineSegmentBuilder::TypesAngle@endlink  only.

                        Note that the segments are added in the order that they appear in this list. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SectionLineSegmentBuilderList * Leg1
            (
            );
            /**Returns  the end location 1 which determines the position of the
                        first arrow segment in the section line. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * EndLocation1
            (
            );
            /**Sets  the end location 1 which determines the position of the
                        first arrow segment in the section line. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetEndLocation1
            (
                NXOpen::Point * endLocation1 /** endlocation1 */ 
            );
            /**Returns  the end location 2 which determines the position of the
                        second arrow segment in the section line 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * EndLocation2
            (
            );
            /**Sets  the end location 2 which determines the position of the
                        second arrow segment in the section line 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetEndLocation2
            (
                NXOpen::Point * endLocation2 /** endlocation2 */ 
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