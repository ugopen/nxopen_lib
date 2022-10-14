#ifndef NXOpen_CAM_WEDMUSERDEFINEDBUILDER_HXX_INCLUDED
#define NXOpen_CAM_WEDMUSERDEFINEDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_WedmUserDefinedBuilder.ja
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
#include <NXOpen/CAM_UserDefinedOprBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class WedmUserDefinedBuilder;
    }
    namespace CAM
    {
        class UserDefinedOprBuilder;
    }
    namespace CAM
    {
        class _WedmUserDefinedBuilderBuilder;
        /** Represents a WedmUserDefined Builder  <br> To create a new instance of this class, use @link CAM::OperationCollection::CreateWedmUserDefinedBuilder CAM::OperationCollection::CreateWedmUserDefinedBuilder@endlink  <br> */
        class NXOPENCPPEXPORT WedmUserDefinedBuilder : public CAM::UserDefinedOprBuilder
        {
            private: friend class  _WedmUserDefinedBuilderBuilder;
            protected: WedmUserDefinedBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif