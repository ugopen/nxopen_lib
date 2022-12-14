#ifndef NXOpen_MOTION_CONFIGURATIONFLOATPARAMETER_HXX_INCLUDED
#define NXOpen_MOTION_CONFIGURATIONFLOATPARAMETER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_ConfigurationFloatParameter.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Motion_ConfigurationFloatParameter.hxx>
#include <NXOpen/Motion_ConfigurationParameter.hxx>
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
        class ConfigurationFloatParameter;
    }
    class Expression;
    namespace Motion
    {
        class ConfigurationParameter;
    }
    namespace Motion
    {
        class _ConfigurationFloatParameterBuilder;
        class ConfigurationFloatParameterImpl;
        /** Represents a @link Motion::ConfigurationFloatParameter Motion::ConfigurationFloatParameter@endlink . This class
                contains the port association for the output of a mechatronics element  <br> No KF support  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  ConfigurationFloatParameter : public NXOpen::Motion::ConfigurationParameter
        {
            private: ConfigurationFloatParameterImpl * m_configurationfloatparameter_impl;
            private: friend class  _ConfigurationFloatParameterBuilder;
            protected: ConfigurationFloatParameter();
            public: ~ConfigurationFloatParameter();
            /**Returns  the initial value 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * InitialValue
            (
            );
            /**Returns  the actual value 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Expression * ActualValue
            (
            );
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
