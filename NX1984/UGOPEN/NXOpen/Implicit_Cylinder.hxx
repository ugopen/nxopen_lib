#ifndef NXOpen_IMPLICIT_CYLINDER_HXX_INCLUDED
#define NXOpen_IMPLICIT_CYLINDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Implicit_Cylinder.ja
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
#include <NXOpen/Implicit_ImplicitOperation.hxx>
#include <NXOpen/libnxopencpp_implicit_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Implicit
    {
        class Cylinder;
    }
    namespace Implicit
    {
        class ImplicitOperation;
    }
    namespace Implicit
    {
        class _CylinderBuilder;
        class CylinderImpl;
        /** Represents a Cylinder Implicit Operation.  <br> To create or edit an instance of this class, use @link NXOpen::Implicit::CylinderBuilder  NXOpen::Implicit::CylinderBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_IMPLICITEXPORT  Cylinder : public NXOpen::Implicit::ImplicitOperation
        {
            private: CylinderImpl * m_cylinder_impl;
            private: friend class  _CylinderBuilder;
            protected: Cylinder();
            public: ~Cylinder();
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