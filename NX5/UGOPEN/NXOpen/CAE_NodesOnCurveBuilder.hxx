#ifndef NXOpen_CAE_NODESONCURVEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_NODESONCURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_NodesOnCurveBuilder.ja
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
#include <NXOpen/CAE_NodesOnCurveBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class NodesOnCurveBuilder;
    }
    class Builder;
    namespace CAE
    {
        class SelectCAEEdge;
    }
    class CoordinateSystem;
    class Expression;
    namespace CAE
    {
        class _NodesOnCurveBuilderBuilder;
        /**
            Represents a @link CAE::NodesOnCurveBuilder CAE::NodesOnCurveBuilder@endlink 
             <br> To create a new instance of this class, use @link CAE::NodeElementManager::CreateNodesOnCurveBuilder CAE::NodeElementManager::CreateNodesOnCurveBuilder@endlink  <br> */
        class NXOPENCPPEXPORT NodesOnCurveBuilder : public Builder
        {
            /** the placement type types */
            public: enum PlacementType
            {
                PlacementTypeByNumber/**by number */,
                PlacementTypeByDistance/**by distance */
            };

            private: friend class  _NodesOnCurveBuilderBuilder;
            protected: NodesOnCurveBuilder();
            /**Returns  the edge  <br> License requirements : None */
            public: NXOpen::CAE::SelectCAEEdge * Edge
            (
            );
            /**Returns  the length  <br> License requirements : None */
            public: double Length
            (
            );
            /**Sets  the length  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetLength
            (
                double length /** length */ 
            );
            /**Returns  the placement option  <br> License requirements : None */
            public: NXOpen::CAE::NodesOnCurveBuilder::PlacementType PlacementOption
            (
            );
            /**Sets  the placement option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPlacementOption
            (
                NXOpen::CAE::NodesOnCurveBuilder::PlacementType placementOption /** placementoption */ 
            );
            /**Returns  the num nodes  <br> License requirements : None */
            public: int NumNodes
            (
            );
            /**Sets  the num nodes  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetNumNodes
            (
                int numNodes /** numnodes */ 
            );
            /**Returns  the distance  <br> License requirements : None */
            public: NXOpen::Expression * Distance
            (
            );
            /**Returns  the label  <br> License requirements : None */
            public: int Label
            (
            );
            /**Sets  the label  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetLabel
            (
                int label /** label */ 
            );
            /**Returns  the increment  <br> License requirements : None */
            public: int Increment
            (
            );
            /**Sets  the increment  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetIncrement
            (
                int increment /** increment */ 
            );
            /**Returns  the ref csys  <br> License requirements : None */
            public: NXOpen::CoordinateSystem * RefCsys
            (
            );
            /**Sets  the ref csys  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetRefCsys
            (
                NXOpen::CoordinateSystem * refCsys /** refcsys */ 
            );
            /**Returns  the disp csys  <br> License requirements : None */
            public: NXOpen::CoordinateSystem * DispCsys
            (
            );
            /**Sets  the disp csys  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetDispCsys
            (
                NXOpen::CoordinateSystem * dispCsys /** dispcsys */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
