#ifndef NXOpen_CAM_CAVITYMILLINGBUILDER_HXX_INCLUDED
#define NXOpen_CAM_CAVITYMILLINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CavityMillingBuilder.ja
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
#include <NXOpen/CAM_PlanarOperationBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class CavityMillingBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class InheritableToolDepBuilder;
    }
    namespace CAM
    {
        class PlanarOperationBuilder;
    }
    namespace CAM
    {
        class _CavityMillingBuilderBuilder;
        /** Represents a CavityMilling Builder  <br> To create a new instance of this class, use @link CAM::OperationCollection::CreateCavityMillingBuilder CAM::OperationCollection::CreateCavityMillingBuilder@endlink  <br> */
        class NXOPENCPPEXPORT CavityMillingBuilder : public CAM::PlanarOperationBuilder
        {
            private: friend class  _CavityMillingBuilderBuilder;
            protected: CavityMillingBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
