#ifndef NXOpen_CAE_FTK_ARRAYRECORD2DEVEN_HXX_INCLUDED
#define NXOpen_CAE_FTK_ARRAYRECORD2DEVEN_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FTK_ArrayRecord2DEven.ja
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
#include <NXOpen/CAE_FTK_ArrayRecord2DEven.hxx>
#include <NXOpen/CAE_FTK_ArrayRecord2D.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        namespace FTK
        {
            class ArrayRecord2DEven;
        }
    }
    namespace CAE
    {
        namespace FTK
        {
            class ArrayRecord2D;
        }
    }
    namespace CAE
    {
        namespace FTK
        {
            class _ArrayRecord2DEvenBuilder;
            class ArrayRecord2DEvenImpl;
            /** Manages the 2d array record with even abscissa data  <br> Not support KF.  <br> 
             <br>  Created in NX7.5.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ArrayRecord2DEven : public NXOpen::CAE::FTK::ArrayRecord2D
            {
                private: ArrayRecord2DEvenImpl * m_arrayrecord2deven_impl;
                private: friend class  _ArrayRecord2DEvenBuilder;
                protected: ArrayRecord2DEven();
                public: ~ArrayRecord2DEven();
                /** Sets even real data 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetEvenRealData
                (
                    double xMinimum /** Minimum abscissa data value */,
                    double xIncrement /** Abscissa increment */,
                    const std::vector<double> & yCoordinatePoints /** Y-Coordinate data */
                );
                /** Gets even real data  @return  Y-Coordinate data 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: std::vector<double> GetEvenRealData
                (
                    double* xMinimum /** Minimum abscissa data value */,
                    double* xIncrement /** Abscissa increment */
                );
                /** Sets even complex data 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetEvenComplexData
                (
                    double xMinimum /** Minimum abscissa data value */,
                    double xIncrement /** Abscissa increment */,
                    const std::vector<double> & yCoordinateReal /** Real part of Y-Coordinate data */,
                    const std::vector<double> & yCoordinateImag /** Imaginary part of Y-Coordinate data */
                );
                /** Gets even complex data  @return  Real part of Y-Coordinate data 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: std::vector<double> GetEvenComplexData
                (
                    double* xMinimum /** Minimum abscissa data value */,
                    double* xIncrement /** Abscissa increment */,
                    std::vector<double> & yCoordinateImag /** Imaginary part of Y-Coordinate data */
                );
            };
        }
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
