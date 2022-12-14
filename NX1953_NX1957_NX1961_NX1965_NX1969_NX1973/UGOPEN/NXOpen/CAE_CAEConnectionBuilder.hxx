#ifndef NXOpen_CAE_CAECONNECTIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_CAECONNECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CAEConnectionBuilder.ja
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
#include <NXOpen/CAE_ElementTypeBuilder.hxx>
#include <NXOpen/CAE_SelectElementsBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class CAEConnectionBuilder;
    }
    class Builder;
    namespace CAE
    {
        class CaeGroup;
    }
    namespace CAE
    {
        class ElementTypeBuilder;
    }
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        class SelectElementsBuilder;
    }
    namespace CAE
    {
        class SelectFENodeList;
    }
    class SelectTaggedObjectList;
    namespace CAE
    {
        class _CAEConnectionBuilderBuilder;
        class CAEConnectionBuilderImpl;
        /**
            Represents a @link NXOpen::CAE::CAEConnectionBuilder NXOpen::CAE::CAEConnectionBuilder@endlink  which can be used to create 
            1D connections. The commit call on the builder returns connection recipe.
             <br> 
            There are following two connections which don't create connection recipe and the builder
            returns NULL pointer in these cases:
            <ol>
            <li> Node to Node  </li>
            <li> Element Edge to Element Face  </li>
            </ol>
            Any call to methods like @link Builder::GetCommittedObjects Builder::GetCommittedObjects@endlink  or @link Builder::GetObject Builder::GetObject@endlink  
            returns NULL for the above mentioned two connection types.
             <br> 
            <br> To create a new instance of this class, use @link NXOpen::CAE::CAEConnectionCollection::CreateConnectionBuilder  NXOpen::CAE::CAEConnectionCollection::CreateConnectionBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CAEConnectionBuilder : public NXOpen::Builder
        {
            /** the type of connection to be created */
            public: enum ConnectionTypeEnum
            {
                ConnectionTypeEnumNodeToNode/** between nodes   */,
                ConnectionTypeEnumElemedgeToElemface/** between element edges and faces */,
                ConnectionTypeEnumPointToPoint/** between points */,
                ConnectionTypeEnumPointToEdge/** between points and edges */,
                ConnectionTypeEnumPointToFace/** between points and faces */,
                ConnectionTypeEnumEdgeToEdge/** between edges */,
                ConnectionTypeEnumEdgeToFace/** between edges and faces */,
                ConnectionTypeEnumFaceToFace/** between faces and faces */,
                ConnectionTypeEnumMesh1dToFace/** between 1d Mesh and polygon faces */
            };

            /** the method of connection to be created */
            public: enum MethodTypeEnum
            {
                MethodTypeEnumProximity/** Based on proximity */,
                MethodTypeEnumOrderOfSelection/** In order of selection   */,
                MethodTypeEnumMeanVector/** Based on Mean Vector */,
                MethodTypeEnumSortXcoord/** Based on sorted X coordinates*/,
                MethodTypeEnumSortYcoord/** Based on sorted Y coordinates*/,
                MethodTypeEnumSortZcoord/** Based on sorted Z coordinates*/,
                MethodTypeEnumSpiderConnection/** Create spider element core nodes and adjacent leg nodes */
            };

            /** the method of edge to edge connection to be created */
            public: enum EdgeToEdgeConnectionMethodTypeEnum
            {
                EdgeToEdgeConnectionMethodTypeEnumNodeToNode/** Create elements between nodes on source and target edges.*/,
                EdgeToEdgeConnectionMethodTypeEnumRbe2Rbe3ToElementEdge/** Create RBE2 between source node and projected node, and RBE3 between projected node and target edge nodes.*/,
                EdgeToEdgeConnectionMethodTypeEnumRbe2Rbe3ToElementFace/** Create RBE2 bewteen source node and projected node, and RBE3 between projected node and target face nodes.*/
            };

            /** the method of point to edge connection to be created */
            public: enum PointToEdgeConnectionMethodTypeEnum
            {
                PointToEdgeConnectionMethodTypeEnumPointToEdge/** Create connection between point on source and target edges.*/,
                PointToEdgeConnectionMethodTypeEnumArcToCenter/** Create connection between arc or circular edge and its center.*/
            };

            /** the method of spider connection to be created */
            public: enum SpiderConnectionMethodTypeEnum
            {
                SpiderConnectionMethodTypeEnumSearchRadius/** Create connection between source nodes and target nodes within search radius.*/,
                SpiderConnectionMethodTypeEnumAverageNode/** Create connection between nodes and their center node.*/
            };

            private: CAEConnectionBuilderImpl * m_caeconnectionbuilder_impl;
            private: friend class  _CAEConnectionBuilderBuilder;
            protected: CAEConnectionBuilder();
            public: ~CAEConnectionBuilder();
            /**Returns  the connection type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::CAEConnectionBuilder::ConnectionTypeEnum Type
            (
            );
            /**Sets  the connection type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetType
            (
                NXOpen::CAE::CAEConnectionBuilder::ConnectionTypeEnum connectionType /** connectiontype */ 
            );
            /**Returns  the method type for point-point or node-node connections 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::CAEConnectionBuilder::MethodTypeEnum MethodType
            (
            );
            /**Sets  the method type for point-point or node-node connections 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMethodType
            (
                NXOpen::CAE::CAEConnectionBuilder::MethodTypeEnum methodType /** methodtype */ 
            );
            /**Returns  the selected source object(s) 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectTaggedObjectList * SourceSelection
            (
            );
            /**Returns  the source Node(s) 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectFENodeList * SourceNodes
            (
            );
            /**Returns  the selected target object(s) 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectTaggedObjectList * TargetSelection
            (
            );
            /**Returns  the target Node(s) 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectFENodeList * TargetNodes
            (
            );
            /**Returns  the selected element edge(s) 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectElementsBuilder * ElementEdge
            (
            );
            /**Returns  the selected element face(s) 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectElementsBuilder * ElementFace
            (
            );
            /**Returns  the element type to be created
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ElementTypeBuilder * ElementType
            (
            );
            /**Returns  the element type to be created
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ElementTypeBuilder * ElementTypeRbe3
            (
            );
            /** The mesh density setting 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void MeshDensity
            (
            );
            /**Returns  the mid node option 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool MidNode
            (
            );
            /**Sets  the mid node option 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMidNode
            (
                bool midNode /** midnode */ 
            );
            /**Returns  the labeling of elements 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: int Label
            (
            );
            /**Sets  the labeling of elements 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetLabel
            (
                int label /** label */ 
            );
            /**Returns  the option to tune edge tolerance. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : None */
            public: double EdgeTolerance
            (
            );
            /**Sets  the option to tune edge tolerance. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : None */
            public: void SetEdgeTolerance
            (
                double edgeTolerance /** edgetolerance */ 
            );
            /**Returns  the method type for edge-to-edge connection 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::CAEConnectionBuilder::EdgeToEdgeConnectionMethodTypeEnum EdgeToEdgeConnectionMethodType
            (
            );
            /**Sets  the method type for edge-to-edge connection 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetEdgeToEdgeConnectionMethodType
            (
                NXOpen::CAE::CAEConnectionBuilder::EdgeToEdgeConnectionMethodTypeEnum edgeToEdgeConnectionMethodType /** edgetoedgeconnectionmethodtype */ 
            );
            /**Returns  the state defining whether the source of this connection is defined with a group 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: bool SourceGroupReferenceState
            (
            );
            /**Returns  the state defining whether the target of this connection is defined with a group 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: bool TargetGroupReferenceState
            (
            );
            /**Returns  the source group referenced by this connection 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::CaeGroup * SourceGroup
            (
            );
            /**Sets  the source group referenced by this connection 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetSourceGroup
            (
                NXOpen::CAE::CaeGroup * groupToRef /** grouptoref */ 
            );
            /**Returns  the target group referenced by this connection 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::CaeGroup * TargetGroup
            (
            );
            /**Sets  the target group referenced by this connection 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetTargetGroup
            (
                NXOpen::CAE::CaeGroup * groupToRef /** grouptoref */ 
            );
            /**Returns  the method type for point-to-edge connection 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::CAEConnectionBuilder::PointToEdgeConnectionMethodTypeEnum PointToEdgeConnectionMethodType
            (
            );
            /**Sets  the method type for point-to-edge connection 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPointToEdgeConnectionMethodType
            (
                NXOpen::CAE::CAEConnectionBuilder::PointToEdgeConnectionMethodTypeEnum pointToEdgeConnectionMethodType /** pointtoedgeconnectionmethodtype */ 
            );
            /**Returns  the filter type for source group selection 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int SourceGroupFilterType
            (
            );
            /**Sets  the filter type for source group selection 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetSourceGroupFilterType
            (
                int sourceGroupFiltertype /** sourcegroupfiltertype */ 
            );
            /**Returns  the filter type for target group selection 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int TargetGroupFilterType
            (
            );
            /**Sets  the filter type for target group selection 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetTargetGroupFilterType
            (
                int targetGroupFiltertype /** targetgroupfiltertype */ 
            );
            /**Returns  the check is edgbe projectable on face or not before commit at UI level 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int Isedgeprojectableonface
            (
            );
            /**Sets  the  proximity between node and face in the case of 1d mesh to face connection
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNodeFaceProximity
            (
                double nodeFaceProximity /** nodefaceproximity */ 
            );
            /**Returns  the  proximity between node and face in the case of 1d mesh to face connection
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: double NodeFaceProximity
            (
            );
            /**Returns  the check is to check if mesh to face connection possible before commit at UI level 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: int Ismeshtofaceconnectionpossible
            (
            );
            /**Returns  the mesh associated to this connection 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::Mesh * Mesh
            (
            );
            /**Returns  the spider mesh associated to Elem edge to elem face or edge to face or edge to edge connections or can be NULL in other cases 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::Mesh * SpiderMesh
            (
            );
            /**Sets  the search distance to create spider connections in node to node connections within search distance
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSearchDistance
            (
                double searchDistance /** searchdistance */ 
            );
            /**Returns  the search distance to create spider connections in node to node connections within search distance
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: double SearchDistance
            (
            );
            /**Returns  the method type for point-to-edge connection 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::CAEConnectionBuilder::SpiderConnectionMethodTypeEnum SpiderConnectionMethodType
            (
            );
            /**Sets  the method type for point-to-edge connection 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetSpiderConnectionMethodType
            (
                NXOpen::CAE::CAEConnectionBuilder::SpiderConnectionMethodTypeEnum spiderConnectionMethodType /** spiderconnectionmethodtype */ 
            );
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
