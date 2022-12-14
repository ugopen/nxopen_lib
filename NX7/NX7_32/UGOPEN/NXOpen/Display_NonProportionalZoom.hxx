#ifndef NXOpen_DISPLAY_NONPROPORTIONALZOOM_HXX_INCLUDED
#define NXOpen_DISPLAY_NONPROPORTIONALZOOM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_NonProportionalZoom.ja
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
#include <NXOpen/Display_NonProportionalZoom.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Display
    {
        class NonProportionalZoom;
    }
    class Builder;
    class View;
    namespace Display
    {
        class _NonProportionalZoomBuilder;
        /** Provides non-proportional zoom capability  <br> To create a new instance of this class, use @link ViewCollection::CreateNonProportionalZoom ViewCollection::CreateNonProportionalZoom@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AnchorCenter </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        Method </td> <td> 
         
        Dynamic </td> </tr> 

        <tr><td> 
         
        ZoomSensitivity </td> <td> 
         
        5 </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT NonProportionalZoom : public Builder
        {
            /** Sets the kind of mouse interaction that will define the non-proportional zoom. */
            public: enum MethodType
            {
                MethodTypeRectangle/** Uses a rectangular region to be zoomed. */,
                MethodTypeDynamic/** Defines a line to define aspect ratio of non-proportional zoom. */
            };

            private: friend class  _NonProportionalZoomBuilder;
            protected: NonProportionalZoom();
            /**Returns  the type of mouse interaction used to define the non-proportional zoom.  <br> License requirements : None */
            public: NXOpen::Display::NonProportionalZoom::MethodType Method
            (
            );
            /**Sets  the type of mouse interaction used to define the non-proportional zoom.  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: void SetMethod
            (
                NXOpen::Display::NonProportionalZoom::MethodType method /** method */ 
            );
            /**Returns  a value indicating if the display will be recentered on the initial line endpoint  <br> License requirements : None */
            public: bool AnchorCenter
            (
            );
            /**Sets  a value indicating if the display will be recentered on the initial line endpoint  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: void SetAnchorCenter
            (
                bool anchorCenter /** anchorcenter */ 
            );
            /**Returns  the sensitivity of the zoom relative to the length of the drawn line  <br> License requirements : None */
            public: int ZoomSensitivity
            (
            );
            /**Sets  the sensitivity of the zoom relative to the length of the drawn line  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: void SetZoomSensitivity
            (
                int sensitivity /** sensitivity */ 
            );
            /** Prepares NX to receive one or more gestures delimited by pairs of points
                    which define a non-proportional zoom.  This function records the display state
                    to which the view will return when non-proportional zoom is disabled. In a typical
                    scenario, call start.  Then call first point accompanied by one or more calls to
                    second point, followed by a call to finish, followed optionaly by further 
                    first point/second point/finish combinations of calls.  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: void Start
            (
                NXOpen::View * view /** the view to receive gestures */
            );
            /** Scales the specified view non-proportionally in the horizontal (X) and vertical (Y)
                    dimensions, based on a mouse gesture defined by two points in a view.  Based on
                    @link Display::NonProportionalZoom::MethodType Display::NonProportionalZoom::MethodType@endlink  setting, the gesture may be
                    interpreted as a bounding box or a line, but will determine the XY aspect ratio and the zoom.
                     <br>  In batch mode, the the aspect ratio, scale and center of the view are modified,
                    but no display occurs.  <br>   <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: void FirstPoint
            (
                const NXOpen::Point3d & point1 /** First point in a mouse gesture to define a non-proportional zoom */,
                NXOpen::View * view /** Apply pan (if any) and scale in this view only, if it still exists */
            );
            /** Scales the specified view non-proportionally in the horizontal (X) and vertical (Y)
                    dimensions, based on a mouse gesture defined by two points in a view.  Call this once
                    for every call to first point, to redefine a non-proportional zoom.
                     <br>  In batch mode, the the aspect ratio, scale and center of the view are modified,
                    but no display occurs.  <br>   <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: void SecondPoint
            (
                const NXOpen::Point3d & point2 /** Second point in a mouse gesture to define a non-proportional zoom */,
                NXOpen::View * view /** Apply pan (if any) and scale in this view only, if it still exists */
            );
            /** Signals the completion of a non-proportional zoom defined by one or more pairs
                        of points defined by a mouse gesture.  <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: void Finish
            (
                NXOpen::View * view /** the view to receive gestures */
            );
            /** Enables non-proportional zoom.
                     <br>  In batch mode, the the aspect ratio, scale and center of the view are modified,
                    but no display occurs.  <br>   <br> License requirements : studio_analyze ("STUDIO ANALYZE") */
            public: void Enable
            (
                bool enable /** True if using the previously defined non-proportional zoom */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
