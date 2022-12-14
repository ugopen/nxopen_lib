#ifndef NXOpen_CAE_NODESREPOSITIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_NODESREPOSITIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_NodesRepositionBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAE_NodesRepositionBuilder.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class NodesRepositionBuilder;
    }
    class Builder;
    namespace CAE
    {
        class FENode;
    }
    namespace CAE
    {
        class _NodesRepositionBuilderBuilder;
        /**
            Represents a @link CAE::NodesRepositionBuilder CAE::NodesRepositionBuilder@endlink 
             <br> To create a new instance of this class, use @link CAE::NodeElementManager::CreateNodesRepositionBuilder CAE::NodeElementManager::CreateNodesRepositionBuilder@endlink  <br> */
        class NXOPENCPPEXPORT NodesRepositionBuilder : public Builder
        {
            private: friend class  _NodesRepositionBuilderBuilder;
            protected: NodesRepositionBuilder();
            /** Set the new absolute postion for the input node. New position will only 
                      take affect when Commit is done.  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetNodePosition
            (
                NXOpen::CAE::FENode * fenode /** @link CAE::FENode CAE::FENode@endlink  input node   */,
                const NXOpen::Point3d & position /** new absolute position of node */
            );
            /** Set the new absolute postions for an array of input nodes. New position will only 
                      take affect when Commit is done.  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetNodePositions
            (
                const std::vector<NXOpen::CAE::FENode *> & fenodes /** FENodes */,
                const std::vector<NXOpen::Point3d> & positions /** FENodes positions */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
