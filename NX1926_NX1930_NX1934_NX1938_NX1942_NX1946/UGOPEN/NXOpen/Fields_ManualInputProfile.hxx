#ifndef NXOpen_FIELDS_MANUALINPUTPROFILE_HXX_INCLUDED
#define NXOpen_FIELDS_MANUALINPUTPROFILE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Fields_ManualInputProfile.ja
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
#include <NXOpen/Fields_FieldTable.hxx>
#include <NXOpen/libnxopencpp_fields_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Fields
    {
        class ManualInputProfile;
    }
    namespace Fields
    {
        class FieldTable;
    }
    namespace Fields
    {
        class _ManualInputProfileBuilder;
        class ManualInputProfileImpl;
        /**  @brief  Represents the Manual Input Profile class. 

           <br> To obtain an instance of this class use @link NXOpen::Fields::FieldManager NXOpen::Fields::FieldManager@endlink  .  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_FIELDSEXPORT  ManualInputProfile : public NXOpen::Fields::FieldTable
        {
            private: ManualInputProfileImpl * m_manualinputprofile_impl;
            private: friend class  _ManualInputProfileBuilder;
            protected: ManualInputProfile();
            public: ~ManualInputProfile();
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
