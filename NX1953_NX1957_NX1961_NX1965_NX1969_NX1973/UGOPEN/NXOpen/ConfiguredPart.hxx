#ifndef NXOpen_CONFIGUREDPART_HXX_INCLUDED
#define NXOpen_CONFIGUREDPART_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ConfiguredPart.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class ConfiguredPart;
    class NXObject;
    class _ConfiguredPartBuilder;
    class ConfiguredPartImpl;

    /// \cond NX_NO_DOC 
    /** Contains configuration-specific information about a @link NXOpen::BasePart NXOpen::BasePart@endlink .
        This is used to differentiate between different aspects of a @link NXOpen::BasePart NXOpen::BasePart@endlink 
        which has been loaded multiple times using different configurations as controlled by the load
        options in managed mode. In native NX, there is only ever a single configuration of a part
        loaded at any one time because no native load options control configuration.
     <br> Use the @link NXOpen::PartCollection NXOpen::PartCollection@endlink  class to find @link NXOpen::ConfiguredPart NXOpen::ConfiguredPart@endlink  objects.  <br> 
     <br>  Created in NX1953.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  ConfiguredPart : public NXOpen::NXObject
    {
        private: ConfiguredPartImpl * m_configuredpart_impl;
        private: friend class  _ConfiguredPartBuilder;
        protected: ConfiguredPart();
        public: ~ConfiguredPart();
    };

    /// \endcond 
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
