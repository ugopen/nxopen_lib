#ifndef NXOpen_DRAWINGS_VIEWSTYLEPERSPECTIVEBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_VIEWSTYLEPERSPECTIVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ViewStylePerspectiveBuilder.ja
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
#include <NXOpen/Drawings_ViewStylePerspectiveBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class ViewStylePerspectiveBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Drawings
    {
        class _ViewStylePerspectiveBuilderBuilder;
        /** Represents the PERSPECTIVE tab on the View Style Dialog (Drawings.ViewStylePerspectiveBuilder)
            */
        class NXOPENCPPEXPORT ViewStylePerspectiveBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: friend class  _ViewStylePerspectiveBuilderBuilder;
            protected: ViewStylePerspectiveBuilder();
            /**Returns  the front clip toggle on the PERSPECTIVE tab of the View Style Dialog  <br> License requirements : None */
            public: bool FrontClip
            (
            );
            /**Sets  the front clip toggle on the PERSPECTIVE tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetFrontClip
            (
                bool frontClipToggle /** Sets a new front clip toggle value on the perspective sub-builder */
            );
            /**Returns  the front clip distance data on the PERSPECTIVE tab of the View Style Dialog  <br> License requirements : None */
            public: double FrontClipDistance
            (
            );
            /**Sets  the front clip distance data on the PERSPECTIVE tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetFrontClipDistance
            (
                double frontClipDistanceData /** Sets a new front clip distance  on the perspective sub-builder */
            );
            /**Returns  the back clip toggle on the PERSPECTIVE tab of the View Style Dialog  <br> License requirements : None */
            public: bool BackClip
            (
            );
            /**Sets  the back clip toggle on the PERSPECTIVE tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetBackClip
            (
                bool backClipToggle /** Sets a new back clip toggle value on the perspective sub-builder */
            );
            /**Returns  the back clip distance data on the PERSPECTIVE tab of the View Style Dialog  <br> License requirements : None */
            public: double BackClipDistance
            (
            );
            /**Sets  the back clip distance data on the PERSPECTIVE tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetBackClipDistance
            (
                double backClipDistanceData /** Sets a new back clip distance on the perspective sub-builder */
            );
            /**Returns  the perspective toggle on the PERSPECTIVE tab of the View Style Dialog  <br> License requirements : None */
            public: bool Perspective
            (
            );
            /**Sets  the perspective toggle on the PERSPECTIVE tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetPerspective
            (
                bool perspectiveToggle /** Sets a new perspective toggle value on the perspective sub-builder */
            );
            /**Returns  the perspective distance data on the PERSPECTIVE tab of the View Style Dialog  <br> License requirements : None */
            public: double PerspectiveDistance
            (
            );
            /**Sets  the perspective distance data on the PERSPECTIVE tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetPerspectiveDistance
            (
                double perspectiveDistanceData /** Sets a new perspective distance on the perspective sub-builder */
            );
            /**Returns  the perspective view origin on the PERSPECTIVE tab of the View Style Dialog  <br> License requirements : None */
            public: NXOpen::Point3d ViewOrigin
            (
            );
            /**Sets  the perspective view origin on the PERSPECTIVE tab of the View Style Dialog  <br> License requirements : drafting ("DRAFTING") */
            public: void SetViewOrigin
            (
                const NXOpen::Point3d & viewOrigin /** Sets a new view origin on the perspective sub-builder */
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
#undef EXPORTLIBRARY
#endif