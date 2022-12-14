#ifndef NXOpen_ANNOTATIONS_ARCCOMPONENT_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_ARCCOMPONENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_ArcComponent.ja
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
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class ArcComponent;
    }
    namespace Annotations
    {
    }
    namespace Annotations
    {
        class ArcComponentImpl;
        /** Represents a single arc in an annotation and can be queried
                for information about that arc.  This information
                includes the arc type, the start angle, the end angle, 
                the radius, and the center point in absolute coordinates. */
        class NXOPENCPPEXPORT  ArcComponent : public TransientObject
        {
            /** the arc type*/
            public: enum ArcType
            {
                ArcTypeExtension/** extension arc */,
                ArcTypeDimension/** dimension arc */,
                ArcTypeAllAround/** all around */,
                ArcTypeAnnotation/** annotation arc */,
                ArcTypeInspection/** inspection arc */
            };

            private: ArcComponentImpl * m_arccomponent_impl;
            public: explicit ArcComponent(void *ptr);
            /** Free resources associated with the arc component. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage
                    collector.   <br> License requirements : None */
            public: virtual ~ArcComponent();
            /**Returns  the arc type. <br> License requirements : None */
            public: NXOpen::Annotations::ArcComponent::ArcType Type
            (
            );
            /**Returns  the arc center point in absolute coordinates.
                    If the annotation is on a drawing, the center point is returned 
                    in drawing space. If the annotation is on the model,
                    the center point is returned in model space.  <br> License requirements : None */
            public: NXOpen::Point3d CenterPoint
            (
            );
            /**Returns  the arc start angle in radians. <br> License requirements : None */
            public: double StartAngle
            (
            );
            /**Returns  the arc end angle in radians. <br> License requirements : None */
            public: double EndAngle
            (
            );
            /**Returns  the arc radius.  <br> License requirements : None */
            public: double Radius
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
