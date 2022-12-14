#ifndef NXOpen_MECHATRONICS_VIRTUALAXIS_HXX_INCLUDED
#define NXOpen_MECHATRONICS_VIRTUALAXIS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_VirtualAxis.ja
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
        class VirtualAxis;
    }
    class DisplayableObject;
    namespace Mechatronics
    {
        class _VirtualAxisBuilder;
        class VirtualAxisImpl;
        /** Represents the Virtual Axis. A virtual Axis defines the object that has kinematics attributes 
                without geometry.  <br> To create or edit an instance of this class, use @link NXOpen::Mechatronics::VirtualAxisBuilder  NXOpen::Mechatronics::VirtualAxisBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  VirtualAxis : public NXOpen::DisplayableObject
        {
            private: VirtualAxisImpl * m_virtualaxis_impl;
            private: friend class  _VirtualAxisBuilder;
            protected: VirtualAxis();
            public: ~VirtualAxis();
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
