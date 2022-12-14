#ifndef NXOpen_ANNOTATIONS_PMILOCATORDESIGNATORDATA_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMILOCATORDESIGNATORDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiLocatorDesignatorData.ja
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
        class PmiLocatorDesignatorData;
    }
    namespace Annotations
    {
        class PmiSemanticData;
    }
    namespace Annotations
    {
        class PmiLocatorDesignatorDataImpl;
        /** Represents PMI Locator data. 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiLocatorDesignatorData : public NXOpen::Annotations::PmiSemanticData
        {
            private: PmiLocatorDesignatorDataImpl * m_pmilocatordesignatordata_impl;
            /// \cond NX_NO_DOC 
            public: explicit PmiLocatorDesignatorData(void *ptr);
            /// \endcond 
            /**Returns  the locator designator title 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString Title
            (
            );
            /**Returns  the locator designator change level type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString ChangeLevelType
            (
            );
            /**Returns  the locator designator hotspot 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString Hotspot
            (
            );
            /**Returns  the locator designator note 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString Note
            (
            );
            /**Returns  the locator designator part name 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString PartName
            (
            );
            /**Returns  the locator designator functional subscript 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString FunctionalSubscript
            (
            );
            /**Returns  the locator designator letter 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString Letter
            (
            );
            /**Returns  the locator designator subtype 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString Subtype
            (
            );
            /**Returns  the locator designator decimal precision 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: int DecimalPrecision
            (
            );
            /**Returns  the locator designator coordinate plane 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString CoordinatePlane
            (
            );
            /**Returns  the locator designator punch direction 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Vector3d PunchDirection
            (
            );
            /**Returns  the locator designator pin direction 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Vector3d PinDirection
            (
            );
            /**Returns  the locator designator normal direction 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Vector3d NormalDirection
            (
            );
            /**Returns  the locator designator symbol name 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString SymbolName
            (
            );
            /**Returns  the locator designator symbol group 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString Group
            (
            );
            /**Returns  the locator designator symbol attribute type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXString AttributeType
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
