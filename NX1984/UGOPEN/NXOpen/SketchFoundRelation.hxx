#ifndef NXOpen_SKETCHFOUNDRELATION_HXX_INCLUDED
#define NXOpen_SKETCHFOUNDRELATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchFoundRelation.ja
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
#include <NXOpen/SketchRelation.hxx>
#include <NXOpen/Sketch.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class SketchFoundRelation;
    class NXObject;
    class SketchRelation;
    class _SketchFoundRelationBuilder;
    class SketchFoundRelationImpl;
    /** Represents a relation in a sketch.
     <br> To create an instance of this class refer to @link NXOpen::Sketch NXOpen::Sketch@endlink   <br> 
     <br>  Created in NX1926.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchFoundRelation : public NXOpen::SketchRelation
    {
        private: SketchFoundRelationImpl * m_sketchfoundrelation_impl;
        private: friend class  _SketchFoundRelationBuilder;
        protected: SketchFoundRelation();
        public: ~SketchFoundRelation();
        /**Returns  the type of the relation
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Sketch::ConstraintType Type
        (
        );
        /** The method returns the geometry associated with the relation  @return  the geometry associated with the relation
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: std::vector<NXOpen::Sketch::ConstraintGeometry> GetGeometry
        (
        );
        /** The method returns the help data of the relation 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void GetHelpData
        (
            NXOpen::Point3d* helpPoint1 /** The first help point. */,
            NXOpen::Point3d* helpPoint2 /** The second help point. */,
            double* helpParameter1 /** The first help parameter. */,
            double* helpParameter2 /** The second help parameter. */
        );
        /**Returns  a flag indicating whether the relation is an ignored relation 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: bool IsIgnored
        (
        );
        /** Sets the given relation to be ignored. To remove the ignore state, simply delete it. 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void MakeIgnored
        (
        );
    };
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif