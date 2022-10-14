#ifndef NXOpen_CURVE_HXX_INCLUDED
#define NXOpen_CURVE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Curve.ja
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
#include <NXOpen/IBaseCurve.hxx>
#include <NXOpen/ICurve.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/IProfile.hxx>
#include <NXOpen/SmartObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class Curve;
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class IBaseCurve;
    class ICurve;
    class INXObject;
    class IProfile;
    class SmartObject;
    class _CurveBuilder;
    class CurveImpl;
    /** Represents a curve.  <br> This is an abstract class, and cannot be instantiated <br> */
    class NXOPENCPPEXPORT  Curve : public SmartObject, public virtual ICurve, public virtual IProfile
    {
        private: CurveImpl * m_curve_impl;
        private: friend class  _CurveBuilder;
        protected: Curve();
        public: ~Curve();
        /** Returns the length of the object  @return   <br> License requirements : None */
        public: virtual double GetLength
        (
        );
    };
}
#undef EXPORTLIBRARY
#endif