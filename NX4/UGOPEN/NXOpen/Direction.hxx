#ifndef NXOpen_DIRECTION_HXX_INCLUDED
#define NXOpen_DIRECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Direction.ja
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
#include <NXOpen/IReferenceAxis.hxx>
#include <NXOpen/SmartObject.hxx>
#include <NXOpen/type.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class Direction;
    class BasePart;
    class ILocation;
    class INXObject;
    class IReferenceAxis;
    class NXObject;
    class SmartObject;
    class _DirectionBuilder;
    /** Represents a direction.  <br> To create a new instance of this class, use @link DirectionCollection::CreateDirection DirectionCollection::CreateDirection@endlink  <br> */
    class NXOPENCPPEXPORT Direction : public SmartObject, public virtual IReferenceAxis, public virtual ILocation
    {
        /** Specifies the direction in relation to a curve. */
        public: enum OnCurveOption
        {
            OnCurveOptionTangent/** Use direction tangent to curve. */,
            OnCurveOptionNormal/** Use direction normal to curve. */,
            OnCurveOptionBinormal/** Use direction binormal to curve (B = T x N). */
        };

        private: friend class  _DirectionBuilder;
        protected: Direction();
        /** Reverses the sense of a direction.  If a direction was created using
                @link DirectionCollection::CreateDirection DirectionCollection::CreateDirection@endlink  for an extract
                type, then the sense cannot be reversed.  The method returns true
                if the direction is reversed and false otherwise.  @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: bool ReverseDirection
        (
        );
        /**Returns  the sense of the direction.  If a direction was created using
                @link DirectionCollection::CreateDirection DirectionCollection::CreateDirection@endlink  for an extract
                type, then the sense cannot be reversed.  In this case,
                the method returns @link NXOpen::SenseForward NXOpen::SenseForward@endlink . <br> License requirements : None */
        public: NXOpen::Sense Sense
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link Sense() Sense@endlink instead.
        @deprecated
        */
        public: NXOpen::Sense GetSense
        (
        ) { return this->Sense(); }
        /**Returns  the unit vector of the direction.  <br> License requirements : None */
        public: NXOpen::Vector3d Vector
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link Vector() Vector@endlink instead.
        @deprecated
        */
        public: NXOpen::Vector3d GetVector
        (
        ) { return this->Vector(); }
        /**Returns  the origin of the direction.  <br> License requirements : None */
        public: NXOpen::Point3d Origin
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link Origin() Origin@endlink instead.
        @deprecated
        */
        public: NXOpen::Point3d GetOrigin
        (
        ) { return this->Origin(); }
        /**Sets  the origin of the direction.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetOrigin
        (
            const NXOpen::Point3d & origin /** */
        );
        /**Sets  the unit vector of the direction.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetVector
        (
            const NXOpen::Vector3d & vector /** */
        );
    };
}
#undef EXPORTLIBRARY
#endif
