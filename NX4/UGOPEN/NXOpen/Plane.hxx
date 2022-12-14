#ifndef NXOpen_PLANE_HXX_INCLUDED
#define NXOpen_PLANE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Plane.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/IOrientation.hxx>
#include <NXOpen/IPlane.hxx>
#include <NXOpen/ISurface.hxx>
#include <NXOpen/PlaneTypes.hxx>
#include <NXOpen/SmartObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class Plane;
    class BasePart;
    class Expression;
    class INXObject;
    class IOrientation;
    class IPlane;
    class ISurface;
    class NXObject;
    class SmartObject;
    class _PlaneBuilder;
    /** Represents an @link Plane Plane@endlink  class. 
      <br> No Creator because of a problem with arrays in APIWRAP <br> */
    class NXOPENCPPEXPORT Plane : public SmartObject, public virtual IPlane, public virtual ISurface, public virtual IOrientation
    {
        private: friend class  _PlaneBuilder;
        protected: Plane();
        /** a plane type  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetMethod
        (
            NXOpen::PlaneTypes::MethodType type /** */
        );
        /**Returns  a plane type  <br> License requirements : None */
        public: virtual NXOpen::PlaneTypes::MethodType Method
        (
        );
        /**Returns  the origin of the plane  <br> License requirements : None */
        public: virtual NXOpen::Point3d Origin
        (
        );
        /**Sets  the origin of the plane  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetOrigin
        (
            const NXOpen::Point3d & origin /** */
        );
        /**Returns  the normal of the plane  <br> License requirements : None */
        public: virtual NXOpen::Vector3d Normal
        (
        );
        /**Sets  the normal of the plane  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetNormal
        (
            const NXOpen::Vector3d & normal /** */
        );
        /** a plane value valid for the following types:  JA_PLANE_type_offset, JA_PLANE_type_on_curve <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetExpression
        (
            const NXString & value_expression /** offset value   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /**Returns   value  <br> License requirements : None */
        public: virtual NXOpen::Expression * Expression
        (
        );
        /** flip the direction of the plane  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetFlip
        (
            bool flip /** flip direction  */
        );
        /**Returns  get the flip flag  <br> License requirements : None */
        public: virtual bool Flip
        (
        );
        public: virtual void SetPercent
        (
            bool percent /** arclength or percent value */
        );
        /**Returns  the arclenth or the percent value  <br> License requirements : None */
        public: virtual bool Percent
        (
        );
        /** sets  geometry  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetGeometry
        (
            const std::vector<NXOpen::NXObject *> & geom /** */
        );
        /** Gets  geometry  @return   <br> License requirements : None */
        public: virtual std::vector<NXOpen::NXObject *> GetGeometry
        (
        );
        /** Evaluate the plane  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void Evaluate
        (
        );
        /** sets  alternate  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetAlternate
        (
            NXOpen::PlaneTypes::AlternateType type /** */
        );
        /** Gets  geometry  @return     <br> License requirements : None */
        public: virtual NXOpen::PlaneTypes::AlternateType GetAlternate
        (
        );
        /** Gets  geometry  @return     <br> License requirements : None */
        public: virtual int GetNumberOfAlternate
        (
        );
        /** sets  reverse_section  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetReverseSection
        (
            bool reverse_section /** */
        );
        /** Gets  reverse_section  @return     <br> License requirements : None */
        public: virtual bool GetReverseSection
        (
        );
        /** sets  reverse_side  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetReverseSide
        (
            bool reverse_side /** */
        );
        /** Gets  reverse_side  @return     <br> License requirements : None */
        public: virtual bool GetReverseSide
        (
        );
    };
}
#undef EXPORTLIBRARY
#endif
