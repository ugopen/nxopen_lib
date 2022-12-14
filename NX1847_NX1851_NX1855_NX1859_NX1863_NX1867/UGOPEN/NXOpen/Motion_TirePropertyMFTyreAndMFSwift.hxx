#ifndef NXOpen_MOTION_TIREPROPERTYMFTYREANDMFSWIFT_HXX_INCLUDED
#define NXOpen_MOTION_TIREPROPERTYMFTYREANDMFSWIFT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_TirePropertyMFTyreAndMFSwift.ja
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
#include <NXOpen/Motion_TireProperty.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class TirePropertyMFTyreAndMFSwift;
    }
    namespace Motion
    {
        class TireProperty;
    }
    namespace Motion
    {
        class _TirePropertyMFTyreAndMFSwiftBuilder;
        class TirePropertyMFTyreAndMFSwiftImpl;
        /**  @brief MF-Tyre and MF-Swift Tire Property element 

         
                
                    This is an object that contains parameters needed for the MF-Tyre and MF-Swift model
                
             <br> To create or edit an instance of this class, use @link NXOpen::Motion::TirePropertyMFTyreAndMFSwiftBuilder  NXOpen::Motion::TirePropertyMFTyreAndMFSwiftBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  TirePropertyMFTyreAndMFSwift : public NXOpen::Motion::TireProperty
        {
            private: TirePropertyMFTyreAndMFSwiftImpl * m_tirepropertymftyreandmfswift_impl;
            private: friend class  _TirePropertyMFTyreAndMFSwiftBuilder;
            protected: TirePropertyMFTyreAndMFSwift();
            public: ~TirePropertyMFTyreAndMFSwift();
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
