#ifndef NXOpen_DIE_DIEPLANEBUILDER_HXX_INCLUDED
#define NXOpen_DIE_DIEPLANEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_DiePlaneBuilder.ja
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
#include <NXOpen/Die_DiePlaneBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        class DiePlaneBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class Plane;
    class SelectNXObject;
    namespace Die
    {
        class _DiePlaneBuilderBuilder;
        /**
            Represents a @link Die::DiePlaneBuilder Die::DiePlaneBuilder@endlink . The Die Plane is
            a helper to the main Die Design feature to specify the plane, such as the
            base plane or end planes. If a coordinate system is specified, then the
            XY plane of the coordinate system will be used.
             <br> To create a new instance of this class, use @link Die::DieCollection::CreateDiePlane Die::DieCollection::CreateDiePlane@endlink  <br> */
        class NXOPENCPPEXPORT DiePlaneBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /** the options available for defining the plane */
            public: enum PlaneType
            {
                PlaneTypeSelection/** Select the plane to be used. */,
                PlaneTypePlane/** Define the plane to be used. */,
                PlaneTypeCoordinateSystem/** Define a coordinate system to specify the plane. */
            };

            private: friend class  _DiePlaneBuilderBuilder;
            protected: DiePlaneBuilder();
            /**Returns  the type of source that defined the plane  <br> License requirements : None */
            public: NXOpen::Die::DiePlaneBuilder::PlaneType SourceDataType
            (
            );
            /**Sets  the type of source that defined the plane  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetSourceDataType
            (
                NXOpen::Die::DiePlaneBuilder::PlaneType sourceDataType /** sourcedatatype */ 
            );
            /**Returns  the selected plane  <br> License requirements : None */
            public: NXOpen::SelectNXObject * SelectPlane
            (
            );
            /**Returns  the specified plane  <br> License requirements : None */
            public: NXOpen::Plane * SpecifyPlane
            (
            );
            /**Sets  the specified plane  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetSpecifyPlane
            (
                NXOpen::Plane * specifyPlane /** specifyplane */ 
            );
            /**Returns  the coordinate system origin  <br> License requirements : None */
            public: NXOpen::Point3d CoordinateSystemOrigin
            (
            );
            /**Sets  the coordinate system origin  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCoordinateSystemOrigin
            (
                const NXOpen::Point3d & coordinateSystemOrigin /** coordinatesystemorigin */ 
            );
            /**Returns  the coordinate system matrix  <br> License requirements : None */
            public: NXOpen::Matrix3x3 CoordinateSystemMatrix
            (
            );
            /**Sets  the coordinate system matrix  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCoordinateSystemMatrix
            (
                const NXOpen::Matrix3x3 & coordinateSystemMatrix /** coordinatesystemmatrix */ 
            );
            /**Returns  the indication if the source's direction should be reversed. True indicates the source's direction should be reversed  <br> License requirements : None */
            public: bool ReverseSourceDirection
            (
            );
            /**Sets  the indication if the source's direction should be reversed. True indicates the source's direction should be reversed  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetReverseSourceDirection
            (
                bool reverseSourceDirection /** reversesourcedirection */ 
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