#ifndef NXOpen_IPLANE_HXX_INCLUDED
#define NXOpen_IPLANE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     IPlane.ja
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
#include <NXOpen/PlaneTypes.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class IPlane;
    class Expression;
    class INXObject;
    class NXObject;
    /** Represents an @link Plane Plane@endlink  class. 
     */
    class NXOPENCPPEXPORT IPlane : public virtual INXObject
    {
        /** a plane type  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetMethod
        (
            NXOpen::PlaneTypes::MethodType type /** */
        ) = 0;
        /**Returns  a plane type  <br> License requirements : None */
        public: virtual NXOpen::PlaneTypes::MethodType Method
        (
        ) = 0;
        /**Returns  the origin of the plane  <br> License requirements : None */
        public: virtual NXOpen::Point3d Origin
        (
        ) = 0;
        /**Sets  the origin of the plane  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetOrigin
        (
            const NXOpen::Point3d & origin /** */
        ) = 0;
        /**Returns  the normal of the plane  <br> License requirements : None */
        public: virtual NXOpen::Vector3d Normal
        (
        ) = 0;
        /**Sets  the normal of the plane  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetNormal
        (
            const NXOpen::Vector3d & normal /** */
        ) = 0;
        /** a plane value valid for the following types:  JA_PLANE_type_offset, JA_PLANE_type_on_curve <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetExpression
        (
            const NXString & value_expression /** offset value   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        ) = 0;
        /**Returns   value  <br> License requirements : None */
        public: virtual NXOpen::Expression * Expression
        (
        ) = 0;
        /** flip the direction of the plane  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetFlip
        (
            bool flip /** flip direction  */
        ) = 0;
        /**Returns  get the flip flag  <br> License requirements : None */
        public: virtual bool Flip
        (
        ) = 0;
        public: virtual void SetPercent
        (
            bool percent /** arclength or percent value */
        ) = 0;
        /**Returns  the arclenth or the percent value  <br> License requirements : None */
        public: virtual bool Percent
        (
        ) = 0;
        /** sets  geometry  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetGeometry
        (
            const std::vector<NXOpen::NXObject *> & geom /** */
        ) = 0;
        /** Gets  geometry  @return   <br> License requirements : None */
        public: virtual std::vector<NXOpen::NXObject *> GetGeometry
        (
        ) = 0;
        /** Evaluate the plane  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void Evaluate
        (
        ) = 0;
        /** sets  alternate  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetAlternate
        (
            NXOpen::PlaneTypes::AlternateType type /** */
        ) = 0;
        /** Gets  geometry  @return     <br> License requirements : None */
        public: virtual NXOpen::PlaneTypes::AlternateType GetAlternate
        (
        ) = 0;
        /** Gets  geometry  @return     <br> License requirements : None */
        public: virtual int GetNumberOfAlternate
        (
        ) = 0;
        /** sets  reverse_section  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetReverseSection
        (
            bool reverse_section /** */
        ) = 0;
        /** Gets  reverse_section  @return     <br> License requirements : None */
        public: virtual bool GetReverseSection
        (
        ) = 0;
        /** sets  reverse_side  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetReverseSide
        (
            bool reverse_side /** */
        ) = 0;
        /** Gets  reverse_side  @return     <br> License requirements : None */
        public: virtual bool GetReverseSide
        (
        ) = 0;
    };
}
#undef EXPORTLIBRARY
#endif
