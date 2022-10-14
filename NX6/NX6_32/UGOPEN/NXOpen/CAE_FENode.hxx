#ifndef NXOpen_CAE_FENODE_HXX_INCLUDED
#define NXOpen_CAE_FENODE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FENode.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class FENode;
    }
    namespace CAE
    {
        class _FENodeBuilder;
        /** Represents a Finite Element. */
        class NXOPENCPPEXPORT FENode : public TaggedObject
        {
            private: friend class  _FENodeBuilder;
            protected: FENode();
        };
    }
}
#undef EXPORTLIBRARY
#endif