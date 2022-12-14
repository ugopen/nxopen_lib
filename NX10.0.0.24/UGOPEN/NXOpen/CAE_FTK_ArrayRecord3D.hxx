#ifndef NXOpen_CAE_FTK_ARRAYRECORD3D_HXX_INCLUDED
#define NXOpen_CAE_FTK_ARRAYRECORD3D_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FTK_ArrayRecord3D.ja
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
#include <NXOpen/CAE_FTK_ArrayRecord3D.hxx>
#include <NXOpen/CAE_FTK_BaseUnit.hxx>
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
            class ArrayRecord3D;
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
            class BaseUnit;
        }
    }
    namespace CAE
    {
        namespace FTK
        {
            class _ArrayRecord3DBuilder;
            class ArrayRecord3DImpl;
            /** Manages the 3d array record  <br> Not support KF.  <br> 
             <br>  Created in NX7.5.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ArrayRecord3D : public NXOpen::CAE::FTK::ArrayRecord2D
            {
                private: ArrayRecord3DImpl * m_arrayrecord3d_impl;
                private: friend class  _ArrayRecord3DBuilder;
                protected: ArrayRecord3D();
                public: ~ArrayRecord3D();
                /** Sets Z-Coordinate unit 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetZCoordinateUnit
                (
                    NXOpen::CAE::FTK::BaseUnit * zCoordinateUnit /** Z-Coordinate unit */
                );
                /** Gets Z-Coordinate unit  @return  Z-Coordinate unit 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: NXOpen::CAE::FTK::BaseUnit * GetZCoordinateUnit
                (
                );
                /** Sets Z-Coordinate points 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetZCoordinatePoints
                (
                    const std::vector<double> & zCoordinatePoints /** Z-Coordinate data */
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
