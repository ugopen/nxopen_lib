#ifndef NXOpen_REGIONPOINT_HXX_INCLUDED
#define NXOpen_REGIONPOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     RegionPoint.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class RegionPoint;
    class Body;
    class NXObject;
    class Point;
    class _RegionPointBuilder;
    class RegionPointImpl;
    /** Represents a point and body context on a region point.
     <br> To create a new instance of this class, use @link Part::CreateEmptyRegionPoint Part::CreateEmptyRegionPoint@endlink  <br> */
    class NXOPENCPPEXPORT  RegionPoint : public NXObject
    {
        private: RegionPointImpl * m_regionpoint_impl;
        private: friend class  _RegionPointBuilder;
        protected: RegionPoint();
        public: ~RegionPoint();
        /**Returns  the Point  <br> License requirements : None */
        public: NXOpen::Point * Point
        (
        );
        /**Sets  the Point  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetPoint
        (
            NXOpen::Point * point /** point to add */
        );
        /**Returns  the Body  <br> License requirements : None */
        public: NXOpen::Body * Body
        (
        );
        /**Sets  the Body  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetBody
        (
            NXOpen::Body * body /** body to add corrosponding point */
        );
    };
}
#undef EXPORTLIBRARY
#endif