#ifndef NXOpen_MEASUREANGLE_HXX_INCLUDED
#define NXOpen_MEASUREANGLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MeasureAngle.ja
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
#include <NXOpen/MeasureManager.hxx>
#include <NXOpen/SingleMeasure.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class MeasureAngle;
    class Measure;
    class Scalar;
    class SingleMeasure;
    class MeasureAngleImpl;
    /** Represents a single valued Angle measurement */
    class NXOPENCPPEXPORT  MeasureAngle : public SingleMeasure
    {
        private: MeasureAngleImpl * m_measureangle_impl;
        public: explicit MeasureAngle(void *ptr);
        /** Creates and returns a measurement feature  @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: NXOpen::Measure * CreateFeature
        (
        );
        /** Creates and returns an embedded measurement expression. 
          Deprecated: Use CreateEmbeddedObject instead  @return  
         @deprecated Deprecated in NX5.0.1 <br> 
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public:  NX_DEPRECATED("Deprecated in NX5.0.1") NXString CreateEmbedded
        (
        );
        /** Creates an embedded measurement.  
              The name of the measurement can be used in an expression formula.  @return  the measurement  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: NXOpen::Scalar * CreateEmbeddedObject
        (
            NXString* name /** the name of the measurement */
        );
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif