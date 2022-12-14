#ifndef NXOpen_DRAWINGS_VIEW2DORIENTBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_VIEW2DORIENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_View2dOrientBuilder.ja
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
#include <NXOpen/Drawings_View2dOrientBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class View2dOrientBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Drawings
    {
        class _View2dOrientBuilderBuilder;
        class View2dOrientBuilderImpl;
        /** Represents the View 2D Orientation (Drawings.View2dOrientBuilder)
            */
        class NXOPENCPPEXPORT  View2dOrientBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /** The view orientation type */
            public: enum Type
            {
                TypeNone/** not oriented */,
                TypeTop/** top view */,
                TypeFront/** front view */,
                TypeRight/** right view */,
                TypeBack/** back view */,
                TypeBottom/** bottom view */,
                TypeLeft/** left view */,
                TypeIso/** isometric view */,
                TypeTri/** trimetric view */,
                TypeCustom/** custom method used */
            };

            /** The custom orientation method */
            public: enum CustomMethod
            {
                CustomMethodAngles/** axis rotations */,
                CustomMethodVector/** cartesian vector*/
            };

            private: View2dOrientBuilderImpl * m_view2dorientbuilder_impl;
            private: friend class  _View2dOrientBuilderBuilder;
            protected: View2dOrientBuilder();
            public: ~View2dOrientBuilder();
            /**Returns  the orientation type  <br> License requirements : None */
            public: NXOpen::Drawings::View2dOrientBuilder::Type OrientationType
            (
            );
            /**Sets  the orientation type  <br> License requirements : drafting ("DRAFTING") */
            public: void SetOrientationType
            (
                NXOpen::Drawings::View2dOrientBuilder::Type type /** sets the orientation type. */
            );
            /**Returns  the custom orientation method  <br> License requirements : None */
            public: NXOpen::Drawings::View2dOrientBuilder::CustomMethod CustomOrientationMethod
            (
            );
            /**Sets  the custom orientation method  <br> License requirements : drafting ("DRAFTING") */
            public: void SetCustomOrientationMethod
            (
                NXOpen::Drawings::View2dOrientBuilder::CustomMethod methd /** sets the custom orientation method. */
            );
            /**Returns  the orientation angle around the X axis  <br> License requirements : None */
            public: double CustomXAngle
            (
            );
            /**Sets  the orientation angle around the X axis  <br> License requirements : drafting ("DRAFTING") */
            public: void SetCustomXAngle
            (
                double angle /** sets the angle around X axis */
            );
            /**Returns  the orientation angle around the Y axis  <br> License requirements : None */
            public: double CustomYAngle
            (
            );
            /**Sets  the orientation angle around the Y axis  <br> License requirements : drafting ("DRAFTING") */
            public: void SetCustomYAngle
            (
                double angle /** sets the angle around Y axis */
            );
            /**Returns  the orientation angle around the Z axis  <br> License requirements : None */
            public: double CustomZAngle
            (
            );
            /**Sets  the orientation angle around the Z axis  <br> License requirements : drafting ("DRAFTING") */
            public: void SetCustomZAngle
            (
                double angle /** sets the angle around Z axis */
            );
            /** Returns the X component of the custom view-normal vector  @return  returns the X component of view normal in global CS  <br> License requirements : None */
            public: double GetCustomNormalX
            (
            );
            /**Sets the X component of the custom view-normal vector   <br> License requirements : drafting ("DRAFTING") */
            public: void SetCustomNormalX
            (
                double component /** sets the the X component of view normal in global CS */
            );
            /** Returns the Y component of the custom view-normal vector  @return  returns the Y component of view normal in global CS  <br> License requirements : None */
            public: double GetCustomNormalY
            (
            );
            /** Sets the Y component of the custom view-normal vector  <br> License requirements : drafting ("DRAFTING") */
            public: void SetCustomNormalY
            (
                double component /** sets the the Y component of view normal in global CS */
            );
            /** Returns the Z component of the custom view-normal vector  @return  returns the Z component of view normal in global CS  <br> License requirements : None */
            public: double GetCustomNormalZ
            (
            );
            /** Sets the Z component of the custom view-normal vector  <br> License requirements : drafting ("DRAFTING") */
            public: void SetCustomNormalZ
            (
                double component /** sets the the Z component of view normal in global CS */
            );
            /** Returns the option to infer the direction view X vector in 3D space  @return  returns the inferred option  <br> License requirements : None */
            public: bool GetInferredPrimary
            (
            );
            /** Sets the option to infer the direction view X vector in 3D space  <br> License requirements : drafting ("DRAFTING") */
            public: void SetInferredPrimary
            (
                bool inferred /** sets the inferred option */
            );
            /** Returns the X component of the custom view-primary vector  @return  returns the X component of view primary vector in global CS  <br> License requirements : None */
            public: double GetCustomPrimaryX
            (
            );
            /** Sets the X component of the custom view-primary vector  <br> License requirements : drafting ("DRAFTING") */
            public: void SetCustomPrimaryX
            (
                double component /** sets the the X component of view primary vector in global CS */
            );
            /** Returns the Y component of the custom view-primary vector  @return  returns the Y component of view primary vector in global CS  <br> License requirements : None */
            public: double GetCustomPrimaryY
            (
            );
            /** Sets the Y component of the custom view-primary vector  <br> License requirements : drafting ("DRAFTING") */
            public: void SetCustomPrimaryY
            (
                double component /** sets the the Y component of view primary vector in global CS */
            );
            /**Returns the Z component of the custom view-primary vector  @return  returns the Z component of view primary vector in global CS  <br> License requirements : None */
            public: double GetCustomPrimaryZ
            (
            );
            /**Sets the Z component of the custom view-primary vector  <br> License requirements : drafting ("DRAFTING") */
            public: void SetCustomPrimaryZ
            (
                double component /** sets the the Z component of view primary vector in global CS */
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : None */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
