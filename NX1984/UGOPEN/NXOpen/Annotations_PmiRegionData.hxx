#ifndef NXOpen_ANNOTATIONS_PMIREGIONDATA_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIREGIONDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiRegionData.ja
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
        class PmiRegionData;
    }
    namespace Annotations
    {
        class PmiSemanticData;
    }
    namespace Annotations
    {
        class PmiRegionDataImpl;
        /** Represents PMI Region data. 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiRegionData : public NXOpen::Annotations::PmiSemanticData
        {
            /** Specifies the PMI Region type */
            public: enum RegionTypes
            {
                RegionTypesUnspecified/** unspecified */ ,
                RegionTypesAnnularType/** annular type */ ,
                RegionTypesCircularType/** circular type */ ,
                RegionTypesCylindricalType/** cylindrical type */ ,
                RegionTypesRectangularType/** rectangular type */ ,
                RegionTypesArbitraryType/** arbitrary type */ 
            };

            private: PmiRegionDataImpl * m_pmiregiondata_impl;
            /// \cond NX_NO_DOC 
            public: explicit PmiRegionData(void *ptr);
            /// \endcond 
            /**Returns  the region type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::PmiRegionData::RegionTypes RegionType
            (
            );
            /**Returns  the region diameter as it applies to circular and annular types 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: double Diameter
            (
            );
            /**Returns  the region inner diameter as it applies to annular types 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: double InnerDiameter
            (
            );
            /**Returns  the region width as it applies to rectangular types 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: double Width
            (
            );
            /**Returns  the region height as it applies to rectangular types 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: double Height
            (
            );
            /**Returns  the region point for end of a cylindrical type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Point3d Point1
            (
            );
            /**Returns  the region point for other side of a cylindrical type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Point3d Point2
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