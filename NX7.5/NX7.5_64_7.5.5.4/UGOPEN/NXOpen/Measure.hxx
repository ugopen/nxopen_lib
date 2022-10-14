#ifndef NXOpen_MEASURE_HXX_INCLUDED
#define NXOpen_MEASURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Measure.ja
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
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class Measure;
    namespace Features
    {
        class Feature;
    }
    class _MeasureBuilder;
    class MeasureImpl;
    /** Represents a measurement feature  <br> To create an instance of this use 
                        @link MeasureBodies MeasureBodies@endlink ,
                        @link MeasureDistance MeasureDistance@endlink ,
                        @link MeasureAngle MeasureAngle@endlink ,
                        @link MeasureFaces MeasureFaces@endlink , and
                        @link MeasureLength MeasureLength@endlink   <br> */
    class NXOPENCPPEXPORT  Measure : public Features::Feature
    {
        private: MeasureImpl * m_measure_impl;
        private: friend class  _MeasureBuilder;
        protected: Measure();
        public: ~Measure();
    };
}
#undef EXPORTLIBRARY
#endif