#ifndef NXOpen_MECHATRONICS_LASERSCANNER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_LASERSCANNER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_LaserScanner.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class LaserScanner;
    }
    class DisplayableObject;
    namespace Mechatronics
    {
        class _LaserScannerBuilder;
        class LaserScannerImpl;
        /**  @brief  Represents the Laser Scanner. A Laser Scanner is able to detect the shortest distance between the sensor and collision body
            of objects that intersect with its volume.  

           <br> To create or edit an instance of this class, use @link NXOpen::Mechatronics::LaserScannerBuilder  NXOpen::Mechatronics::LaserScannerBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  LaserScanner : public NXOpen::DisplayableObject
        {
            private: LaserScannerImpl * m_laserscanner_impl;
            private: friend class  _LaserScannerBuilder;
            protected: LaserScanner();
            public: ~LaserScanner();
        };
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
