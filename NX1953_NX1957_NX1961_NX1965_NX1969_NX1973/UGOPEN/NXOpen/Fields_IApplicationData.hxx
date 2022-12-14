#ifndef NXOpen_FIELDS_IAPPLICATIONDATA_HXX_INCLUDED
#define NXOpen_FIELDS_IAPPLICATIONDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Fields_IApplicationData.ja
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
#include <NXOpen/Fields_IApplication.hxx>
#include <NXOpen/INXObject.hxx>
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
        class IApplicationData;
    }
    namespace Fields
    {
        class Field;
    }
    namespace Fields
    {
        class IApplication;
    }
    class INXObject;
    namespace Fields
    {
        /**  @brief Interface for all application specific data to be registered on fields. Only one 
            application specific data object per IApplication can be added to a field. 

         
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_FIELDSEXPORT  IApplicationData : public virtual NXOpen::INXObject
        {
            public: virtual ~IApplicationData() {}
            /** Returns the application associated with this application data object. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXOpen::Fields::IApplication * GetApplication
            (
            ) = 0;
            /** Delete the Application Data object 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: virtual void DeleteApplicationData
            (
            ) = 0;
            /** Copy the Application Data object to the specified field 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: virtual void CopyToField
            (
                NXOpen::Fields::Field * field /** field to copy to */
            ) = 0;
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
