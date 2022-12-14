#ifndef NXOpen_SIM_KINEMATICJUNCTION_HXX_INCLUDED
#define NXOpen_SIM_KINEMATICJUNCTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SIM_KinematicJunction.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_sim_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace SIM
    {
        class KinematicJunction;
    }
    class NXObject;
    namespace SIM
    {
        class _KinematicJunctionBuilder;
        class KinematicJunctionImpl;
        /**  @brief  Represents the KinematicJunction class object  

            <br> Use the @link SIM::KinematicConfigurator SIM::KinematicConfigurator@endlink  class to create a SimKimJunction object.  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_SIMEXPORT  KinematicJunction : public NXObject
        {
            private: KinematicJunctionImpl * m_kinematicjunction_impl;
            private: friend class  _KinematicJunctionBuilder;
            protected: KinematicJunction();
            public: ~KinematicJunction();
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
