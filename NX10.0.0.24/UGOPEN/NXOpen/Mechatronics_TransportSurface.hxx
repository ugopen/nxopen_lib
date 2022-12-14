#ifndef NXOpen_MECHATRONICS_TRANSPORTSURFACE_HXX_INCLUDED
#define NXOpen_MECHATRONICS_TRANSPORTSURFACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_TransportSurface.ja
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
#include <NXOpen/Mechatronics_PhysicsJoint.hxx>
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
        class TransportSurface;
    }
    namespace Mechatronics
    {
        class PhysicsJoint;
    }
    namespace Mechatronics
    {
        class _TransportSurfaceBuilder;
        class TransportSurfaceImpl;
        /** Represents the Transport Surface class. Transport Surface causes a face on a geometric object to 
            behave like it is moving even if the object it is attached to is not.  <br> To create or edit an instance of this class, use @link NXOpen::Mechatronics::TransportSurfaceBuilder  NXOpen::Mechatronics::TransportSurfaceBuilder @endlink  <br> 
         <br>  Created in NX7.5.1.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  TransportSurface : public NXOpen::Mechatronics::PhysicsJoint
        {
            private: TransportSurfaceImpl * m_transportsurface_impl;
            private: friend class  _TransportSurfaceBuilder;
            protected: TransportSurface();
            public: ~TransportSurface();
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
