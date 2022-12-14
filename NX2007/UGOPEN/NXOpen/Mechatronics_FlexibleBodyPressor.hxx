#ifndef NXOpen_MECHATRONICS_FLEXIBLEBODYPRESSOR_HXX_INCLUDED
#define NXOpen_MECHATRONICS_FLEXIBLEBODYPRESSOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_FlexibleBodyPressor.ja
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
        class FlexibleBodyPressor;
    }
    class DisplayableObject;
    namespace Mechatronics
    {
        class _FlexibleBodyPressorBuilder;
        class FlexibleBodyPressorImpl;
        /** Represents the Flexible Body Pressor class.  A Flexible Body Pressor defines 
            a pressor object to simulate pressing behavior on a flexible body.  <br> To create or edit an instance of this class, use @link NXOpen::Mechatronics::FlexibleBodyPressorBuilder  NXOpen::Mechatronics::FlexibleBodyPressorBuilder @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  FlexibleBodyPressor : public NXOpen::DisplayableObject
        {
            private: FlexibleBodyPressorImpl * m_flexiblebodypressor_impl;
            private: friend class  _FlexibleBodyPressorBuilder;
            protected: FlexibleBodyPressor();
            public: ~FlexibleBodyPressor();
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
