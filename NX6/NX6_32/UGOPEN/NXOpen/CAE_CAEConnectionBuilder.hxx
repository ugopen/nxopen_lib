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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAE_CAEConnectionBuilder.hxx>
#include <NXOpen/CAE_ElementTypeBuilder.hxx>
#include <NXOpen/CAE_SelectElementsBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class CAEConnectionBuilder;
    }
    class Builder;
    namespace CAE
    {
        class CAEConnection;
    }
    namespace CAE
    {
        class ElementTypeBuilder;
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
        /**
            Builder for creating Connection Recipes
             <br> To create a new instance of this class, use @link CAE::CAEConnectionCollection::CreateConnectionBuilder CAE::CAEConnectionCollection::CreateConnectionBuilder@endlink  <br> */
        class NXOPENCPPEXPORT CAEConnectionBuilder : public Builder
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
                ConnectionTypeEnumEdgeToFace/** between edges and faces */
            };

            /** the method of connection to be created */
            public: enum MethodTypeEnum
            {
                MethodTypeEnumProximity/** Based on proximity */,
                MethodTypeEnumOrderOfSelection/** In order of selection   */
            };

            private: friend class  _CAEConnectionBuilderBuilder;
            protected: CAEConnectionBuilder();
            /**Returns  the connection type  <br> License requirements : None */
            public: NXOpen::CAE::CAEConnectionBuilder::ConnectionTypeEnum Type
            (
            );
            /**Sets  the connection type  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetType
            (
                NXOpen::CAE::CAEConnectionBuilder::ConnectionTypeEnum connectionType /** connectiontype */ 
            );
            /**Returns  the method type for point-point or node-node connections  <br> License requirements : None */
            public: NXOpen::CAE::CAEConnectionBuilder::MethodTypeEnum MethodType
            (
            );
            /**Sets  the method type for point-point or node-node connections  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMethodType
            (
                NXOpen::CAE::CAEConnectionBuilder::MethodTypeEnum methodType /** methodtype */ 
            );
            /**Returns  the selected source object(s)  <br> License requirements : None */
            public: NXOpen::SelectTaggedObjectList * SourceSelection
            (
            );
            /**Returns  the source Node(s)  <br> License requirements : None */
            public: NXOpen::CAE::SelectFENodeList * SourceNodes
            (
            );
            /**Returns  the selected target object(s)  <br> License requirements : None */
            public: NXOpen::SelectTaggedObjectList * TargetSelection
            (
            );
            /**Returns  the target Node(s)  <br> License requirements : None */
            public: NXOpen::CAE::SelectFENodeList * TargetNodes
            (
            );
            /**Returns  the selected element edge(s)  <br> License requirements : None */
            public: NXOpen::CAE::SelectElementsBuilder * ElementEdge
            (
            );
            /**Returns  the selected element face(s)  <br> License requirements : None */
            public: NXOpen::CAE::SelectElementsBuilder * ElementFace
            (
            );
            /**Returns  the element type to be created <br> License requirements : None */
            public: NXOpen::CAE::ElementTypeBuilder * ElementType
            (
            );
            /** The mesh density setting  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void MeshDensity
            (
            );
            /**Returns  the mid node option  <br> License requirements : None */
            public: bool MidNode
            (
            );
            /**Sets  the mid node option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMidNode
            (
                bool midNode /** midnode */ 
            );
            /**Returns  the labeling of elements  <br> License requirements : None */
            public: int Label
            (
            );
            /**Sets  the labeling of elements  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetLabel
            (
                int label /** label */ 
            );
            public: NXOpen::CAE::CAEConnection * CommitConnection
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif