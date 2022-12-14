#ifndef NXOpen_POINT_HXX_INCLUDED
#define NXOpen_POINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Point.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/ILocation.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/IOrientation.hxx>
#include <NXOpen/SmartObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class Point;
    class BasePart;
    class ILocation;
    class INXObject;
    class IOrientation;
    class NXObject;
    class SmartObject;
    class _PointBuilder;
    /**
     Represents a smart @link Point Point@endlink . 
     <br> To create a new instance of this class, use @link PointCollection::CreatePoint PointCollection::CreatePoint@endlink  <br> */
    class NXOPENCPPEXPORT Point : public SmartObject, public virtual IOrientation, public virtual ILocation
    {
        private: friend class  _PointBuilder;
        protected: Point();
        /**Returns  the coordinates of the point  <br> License requirements : None */
        public: NXOpen::Point3d Coordinates
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link Coordinates() Coordinates@endlink instead.
        @deprecated
        */
        public: NXOpen::Point3d GetCoordinates
        (
        ) { return this->Coordinates(); }
        /** Sets the coordinates of the point  <br> License requirements : None */
        public: void SetCoordinates
        (
            const NXOpen::Point3d & coordinates /** */
        );
    };
}
#undef EXPORTLIBRARY
#endif
