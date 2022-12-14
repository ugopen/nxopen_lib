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
#include <NXOpen/Callback.hxx>
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
    namespace Assemblies
    {
        class Component;
    }
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
        /** Creates an @link Plane Plane@endlink  using a datum plane feature.  @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: NXOpen::Plane * CopySoPlane
        (
        );
        /** Sets a plane type  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetMethod
        (
            NXOpen::PlaneTypes::MethodType type /** type */ 
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
            const NXOpen::Point3d & origin /** origin */ 
        );
        /**Returns  the normal of the plane  <br> License requirements : None */
        public: virtual NXOpen::Vector3d Normal
        (
        );
        /**Sets  the normal of the plane  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetNormal
        (
            const NXOpen::Vector3d & normal /** normal */ 
        );
        /** Sets the plane expression.  
             Only valid for the following types:  @link PlaneTypes::MethodTypeFrenet PlaneTypes::MethodTypeFrenet@endlink  or
              @link PlaneTypes::MethodTypeDistance PlaneTypes::MethodTypeDistance@endlink . <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetExpression
        (
            const NXString & value_expression /** offset value   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /**Returns  the plane expression.    <br> License requirements : None */
        public: virtual NXOpen::Expression * Expression
        (
        );
        /** Flip the direction of the plane  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetFlip
        (
            bool flip /** flip direction  */
        );
        /**Returns  the flip direction of the plane  <br> License requirements : None */
        public: virtual bool Flip
        (
        );
        /** Sets the arclenth or the percent value  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetPercent
        (
            bool percent /** arclength or percent value */
        );
        /**Returns  the arclenth or the percent value  <br> License requirements : None */
        public: virtual bool Percent
        (
        );
        /** Sets the geometry  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetGeometry
        (
            const std::vector<NXOpen::NXObject *> & geom /** geom */ 
        );
        /** Returns the geometry  @return   <br> License requirements : None */
        public: virtual std::vector<NXOpen::NXObject *> GetGeometry
        (
        );
        /** Evaluates the plane  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void Evaluate
        (
        );
        /** Sets the alternate type  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetAlternate
        (
            NXOpen::PlaneTypes::AlternateType type /** type */ 
        );
        /** Returns the alternate type  @return     <br> License requirements : None */
        public: virtual NXOpen::PlaneTypes::AlternateType GetAlternate
        (
        );
        /** Returns the number of alternate solutions  @return     <br> License requirements : None */
        public: virtual int GetNumberOfAlternate
        (
        );
        /** Sets the reverse_section  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetReverseSection
        (
            bool reverse_section /** reverse section */ 
        );
        /** Returns the reverse section  @return     <br> License requirements : None */
        public: virtual bool GetReverseSection
        (
        );
        /** Sets the reverse side  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: virtual void SetReverseSide
        (
            bool reverse_side /** reverse side */ 
        );
        /** Returns the reverse side  @return     <br> License requirements : None */
        public: virtual bool GetReverseSide
        (
        );
    };
}
#undef EXPORTLIBRARY
#endif
