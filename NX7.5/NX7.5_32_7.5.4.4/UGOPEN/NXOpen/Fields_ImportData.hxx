#ifndef NXOpen_FIELDS_IMPORTDATA_HXX_INCLUDED
#define NXOpen_FIELDS_IMPORTDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Fields_ImportData.ja
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
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Fields
    {
        class ImportData;
    }
    namespace Fields
    {
        class Field;
    }
    namespace Fields
    {
        class ImportDataImpl;
        /**  @brief  Represents data transfer objectst for field import  

           <br> To create a new instance of this class, use @link Fields::FieldManager::CreateImportData Fields::FieldManager::CreateImportData@endlink  <br> */
        class NXOPENCPPEXPORT  ImportData : public TransientObject
        {
            private: ImportDataImpl * m_importdata_impl;
            public: explicit ImportData(void *ptr);
            /** Set file name  <br> License requirements : None */
            public: void SetFileName
            (
                const NXString & fileName /** file name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Get file name  @return  file name  <br> License requirements : None */
            public: NXString GetFileName
            (
            );
            /** Return the fields that have been imported  <br> License requirements : None */
            public: void GetFields
            (
                std::vector<NXOpen::Fields::Field *> & fields /** the fields that have been imported */
            );
            /** Destroys the object  <br> License requirements : None */
            public: virtual ~ImportData();
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
