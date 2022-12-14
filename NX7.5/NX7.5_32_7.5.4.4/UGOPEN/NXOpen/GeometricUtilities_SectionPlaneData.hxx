#ifndef NXOpen_GEOMETRICUTILITIES_SECTIONPLANEDATA_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_SECTIONPLANEDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_SectionPlaneData.ja
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
#include <NXOpen/GeometricUtilities_SectionPlaneData.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class SectionPlaneData;
    }
    class Direction;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class Point;
    namespace GeometricUtilities
    {
        class _SectionPlaneDataBuilder;
        class SectionPlaneDataImpl;
        /** Represents a Section Plane Data class
                This class acts like a container to hold the data needed to create a plane. It provides the ability to define two points on a plane */
        class NXOPENCPPEXPORT  SectionPlaneData : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: SectionPlaneDataImpl * m_sectionplanedata_impl;
            private: friend class  _SectionPlaneDataBuilder;
            protected: SectionPlaneData();
            public: ~SectionPlaneData();
            /**Sets the origin of the plane  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetPlaneOrigin
            (
                NXOpen::Point * point /** point */ 
            );
            /**Returns the origin of the plane  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::Point * PlaneOrigin
            (
            );
            /**Sets the normal of the plane  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetPlaneNormal
            (
                NXOpen::Direction * point /** point */ 
            );
            /**Returns the normal of the plane  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::Direction * PlaneNormal
            (
            );
            /**Sets the first point of the plane  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetPlanePoint1
            (
                NXOpen::Point * point /** point */ 
            );
            /**Sets the second point of the plane  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetPlanePoint2
            (
                NXOpen::Point * point /** point */ 
            );
            /**Returns the first point of the plane  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::Point * PlanePoint1
            (
            );
            /**Returns the second point of the plane  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::Point * PlanePoint2
            (
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
