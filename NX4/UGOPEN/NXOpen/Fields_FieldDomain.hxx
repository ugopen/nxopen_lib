#ifndef NXOpen_FIELDS_FIELDDOMAIN_HXX_INCLUDED
#define NXOpen_FIELDS_FIELDDOMAIN_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Fields_FieldDomain.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Fields
    {
        class FieldDomain;
    }
    class NXObject;
    namespace Fields
    {
        class _FieldDomainBuilder;
        /**  @brief  Represents the Field Domains  

          */
        class NXOPENCPPEXPORT FieldDomain : public NXObject
        {
            private: friend class  _FieldDomainBuilder;
            protected: FieldDomain();
        };
    }
}
#undef EXPORTLIBRARY
#endif