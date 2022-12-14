#ifndef NXOpen_ANNOTATIONS_PMIDATUMTARGETDATA_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIDATUMTARGETDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiDatumTargetData.ja
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
#include <NXOpen/Annotations_PmiSemanticData.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class PmiDatumTargetData;
    }
    namespace Annotations
    {
        class PmiSemanticData;
    }
    namespace Annotations
    {
        class PmiDatumTargetDataImpl;
        /** Represents PMI datum target semantic data object 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiDatumTargetData : public NXOpen::Annotations::PmiSemanticData
        {
            /** the datum target types */
            public: enum Types
            {
                TypesNone/** default target type */,
                TypesPoint/** point datum target type */,
                TypesLine/** line datum target type */,
                TypesRectangular/** rectangular datum target type */,
                TypesCircular/** circular datum target type */,
                TypesCylindrical/** cylindrical datum target type */,
                TypesSpherical/** spherical datum target type */,
                TypesArbitrary/** arbitrary datum target type */
            };

            private: PmiDatumTargetDataImpl * m_pmidatumtargetdata_impl;
            /// \cond NX_NO_DOC 
            public: explicit PmiDatumTargetData(void *ptr);
            /// \endcond 
            /**Returns  the datum label 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString Label
            (
            );
            /**Returns  the datum target index 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: int Index
            (
            );
            /**Returns  the datum target type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::PmiDatumTargetData::Types Type
            (
            );
            /**Returns  a flag indicating whether the datum target is movable 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool IsMovable
            (
            );
            /**Returns  the movable modifier angle 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: double MovableModifierAngle
            (
            );
            /**Returns  the length for the rectangular datum target 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: double Length
            (
            );
            /**Returns  the width for the rectangular datum target 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: double Width
            (
            );
            /**Returns  the diameter for the circular or spherical datum target 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: double Diameter
            (
            );
            /**Returns  the inner diameter for the circular datum target 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: double InnerDiameter
            (
            );
            /**Returns  the first point for all target types 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Point3d FirstPoint
            (
            );
            /**Returns  the second point for the line or cylindrical datum target 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Point3d SecondPoint
            (
            );
            /**Returns  the area size for the arbitrary datum target 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString AreaSize
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
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
