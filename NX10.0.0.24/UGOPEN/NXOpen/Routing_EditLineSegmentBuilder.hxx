#ifndef NXOpen_ROUTING_EDITLINESEGMENTBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_EDITLINESEGMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_EditLineSegmentBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Routing_EditLineSegmentBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_routing_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Routing
    {
        class EditLineSegmentBuilder;
    }
    class Builder;
    class Expression;
    namespace Routing
    {
        class LineSegment;
    }
    namespace Routing
    {
        class SelectLineSegment;
    }
    namespace Routing
    {
        class _EditLineSegmentBuilderBuilder;
        class EditLineSegmentBuilderImpl;
        /** 
                Builder for the "Edit Line Segment" operation.  Sets (and locks or unlocks)
                the length of @link NXOpen::Routing::LineSegment NXOpen::Routing::LineSegment@endlink  objects.  Also moves geometry
                attached to the line segment to ensure that the attached geometry has the correct
                shape after an edit. 
             <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateEditLineSegmentBuilder  NXOpen::Routing::RouteManager::CreateEditLineSegmentBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  EditLineSegmentBuilder : public NXOpen::Builder
        {
            private: EditLineSegmentBuilderImpl * m_editlinesegmentbuilder_impl;
            private: friend class  _EditLineSegmentBuilderBuilder;
            protected: EditLineSegmentBuilder();
            public: ~EditLineSegmentBuilder();
            /**Returns  the line selection.  Stores the line segment selected by the user. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::SelectLineSegment * LineSelection
            (
            );
            /**Returns  the length expression.  This data from this expression is copied to (or from)
                        the distance constraint applied to the ends of the line segment.  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * Length
            (
            );
            /**Returns  the reverse direction flag.  Flips the direction that the extends towards (or
                        shrinks along).  This flips the origin of the line as well as the direction. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool ReverseDirection
            (
            );
            /**Sets  the reverse direction flag.  Flips the direction that the extends towards (or
                        shrinks along).  This flips the origin of the line as well as the direction. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetReverseDirection
            (
                bool reverse /** reverse */ 
            );
            /**Returns  the lock length flag.  Forces the commit method to lock the length to the 
                        specified value if set to true.  Otherwise the length of the line segment 
                        is unconstrained after the commit method is invoked. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool LockLength
            (
            );
            /**Sets  the lock length flag.  Forces the commit method to lock the length to the 
                        specified value if set to true.  Otherwise the length of the line segment 
                        is unconstrained after the commit method is invoked. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetLockLength
            (
                bool lockLength /** locklength */ 
            );
            /** Determines the orientation information for the line selected by the user.  Returns
                        false if there is no line currently stored in the builder.   @return  True if there
                                                                                                is a line 
                                                                                                associated with
                                                                                                this builder. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool GetOrientation
            (
                NXOpen::Point3d* startPoint /** The start 
                                                                                                of the line. */,
                NXOpen::Vector3d* direction /** The direction 
                                                                                                of the line 
                                                                                                (unit vector).*/
            );
            /** Initializes (or resets) the builder based off of the input line segment.  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void InitializeFromLine
            (
                NXOpen::Routing::LineSegment * line /** Line object, may be NULL*/
            );
            /** Updates the line length based on the expression stored in this builder.  The line is
                        not fully updated only partially updated (i.e. solid bodies build on the line do not
                        update).    This method assumes the difference between the new length value and the
                        previous length value is very small (e.g. a drag operation). 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void DragLineLength
            (
            );
            /** Updates the line length based on the expression stored in this builder.  The line is
                        not fully updated only partially updated (i.e. solid bodies build on the line do not
                        update).   This method doesn't assume anything about the new value.  This method
                        updates the line incrementally from the original length to the new length
                        as this usually results in better looking geometry. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void ModifiedLineLength
            (
            );
            /** Stop the drag operation if it has begun. This will commit the drag and update the assembly.
                        This will not remove the segment from the builder and dragging can be restarted by calling
                        @link NXOpen::Routing::EditLineSegmentBuilder::RestartDrag NXOpen::Routing::EditLineSegmentBuilder::RestartDrag@endlink . 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void StopDrag
            (
            );
            /** Restart a line drag operation. This routine should only be called if 
                    @link NXOpen::Routing::EditLineSegmentBuilder::StopDrag NXOpen::Routing::EditLineSegmentBuilder::StopDrag@endlink . was previously
                    called to stop a line drag operation. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void RestartDrag
            (
            );
            /**Returns  the conversion flag.  Forces the commit method to convert line segment to eccentric line segment if set to true.  Otherwise 
                     convert it to vice versa 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool ConvertEccentricSegment
            (
            );
            /**Sets  the conversion flag.  Forces the commit method to convert line segment to eccentric line segment if set to true.  Otherwise 
                     convert it to vice versa 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetConvertEccentricSegment
            (
                bool convertEccentricSegment /** converteccentricsegment */ 
            );
            /** Determines the active RCP for the line selected by the user.
                        This is end RCP other than the start point of line segment.
                        This RCP could be dragged along the segment. @return  End point other
                                                                                              than the start point 
                                                                                              of line segment. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Point3d GetActiveRcpPositon
            (
            );
            /** Detaches the line segment, stored in builder, at its active end RCP.
                        By reversing the direction of line segment, user could make other end RCP as active 
                        RCP. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void DetachActiveRcp
            (
            );
            /** Adds the current line segment to the set of all line segments that have been edited
                        by the user. 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void AddLineToSetOfAllEditedSegments
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
