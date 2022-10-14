#ifndef NXOpen_ANNOTATIONS_COMPANYPROPRIETARYINFORMATION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_COMPANYPROPRIETARYINFORMATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_CompanyProprietaryInformation.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Annotations_PmiAttribute.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class CompanyProprietaryInformation;
    }
    namespace Annotations
    {
        class PmiAttribute;
    }
    namespace Annotations
    {
        class _CompanyProprietaryInformationBuilder;
        /** Represents a Company Proprietary Information */
        class NXOPENCPPEXPORT CompanyProprietaryInformation : public Annotations::PmiAttribute
        {
            private: friend class  _CompanyProprietaryInformationBuilder;
            protected: CompanyProprietaryInformation();
        };
    }
}
#undef EXPORTLIBRARY
#endif