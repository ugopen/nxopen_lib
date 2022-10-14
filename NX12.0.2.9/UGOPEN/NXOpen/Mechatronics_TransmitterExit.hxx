#ifndef NXOpen_MECHATRONICS_TRANSMITTEREXIT_HXX_INCLUDED
#define NXOpen_MECHATRONICS_TRANSMITTEREXIT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_TransmitterExit.ja
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
#include <NXOpen/Mechatronics_PhysicsConstraint.hxx>
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
        class TransmitterExit;
    }
    namespace Mechatronics
    {
        class PhysicsConstraint;
    }
    namespace Mechatronics
    {
        class _TransmitterExitBuilder;
        class TransmitterExitImpl;
        /**  @brief  Represents the Transmitter Exit. A Transmitter Exit is able to receive rigid bodies sending by an entry.  

           <br> To create or edit an instance of this class, use @link NXOpen::Mechatronics::TransmitterExitBuilder  NXOpen::Mechatronics::TransmitterExitBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  TransmitterExit : public NXOpen::Mechatronics::PhysicsConstraint
        {
            private: TransmitterExitImpl * m_transmitterexit_impl;
            private: friend class  _TransmitterExitBuilder;
            protected: TransmitterExit();
            public: ~TransmitterExit();
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