#ifndef NXOpen_CAE_CAEWELDCONNECTIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_CAEWELDCONNECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CAEWeldConnectionBuilder.ja
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
#include <NXOpen/CAE_CAEWeldConnectionBuilder.hxx>
#include <NXOpen/CAE_ElementTypeBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class CAEWeldConnectionBuilder;
    }
    class Builder;
    namespace CAE
    {
        class CAEWeldConnection;
    }
    namespace CAE
    {
        class ElementTypeBuilder;
    }
    class Expression;
    class SelectTaggedObjectList;
    namespace CAE
    {
        class _CAEWeldConnectionBuilderBuilder;
        /**
            Builder for creating 1D Weld Connection
             <br> To create a new instance of this class, use @link CAE::CAEConnectionCollection::CreateWeldConnectionBuilder CAE::CAEConnectionCollection::CreateWeldConnectionBuilder@endlink  <br> */
        class NXOPENCPPEXPORT CAEWeldConnectionBuilder : public Builder
        {
            /** point_to_point_3d_weld = It's a point to point in-direct weldconnection,3D elements are created during weld connection */
            public: enum WeldTypeEnum
            {
                WeldTypeEnumPointToPointDirect/** point to point direct */ ,
                WeldTypeEnumPointToPointIndirect/** point to point indirect */ ,
                WeldTypeEnumPointToPoint3dWeld/** point to point3d weld */ 
            };

            /** enum_number = Number of elements on the hard object*/
            public: enum MeshDensityTypeEnum
            {
                MeshDensityTypeEnumSize/** size */ ,
                MeshDensityTypeEnumNumber/** number */ 
            };

            private: friend class  _CAEWeldConnectionBuilderBuilder;
            protected: CAEWeldConnectionBuilder();
            /**Returns  the weld connection type  <br> License requirements : None */
            public: NXOpen::CAE::CAEWeldConnectionBuilder::WeldTypeEnum WeldType
            (
            );
            /**Sets  the weld connection type  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetWeldType
            (
                NXOpen::CAE::CAEWeldConnectionBuilder::WeldTypeEnum weldType /** weldtype */ 
            );
            /**Returns  the hard obj selection  <br> License requirements : None */
            public: NXOpen::SelectTaggedObjectList * HardObjSelection
            (
            );
            /**Returns  the top face selection(s)  <br> License requirements : None */
            public: NXOpen::SelectTaggedObjectList * TopFaceSelection
            (
            );
            /**Returns  the bottom face selection(s)  <br> License requirements : None */
            public: NXOpen::SelectTaggedObjectList * BottomFaceSelection
            (
            );
            /**Returns  the mesh density type  <br> License requirements : None */
            public: NXOpen::CAE::CAEWeldConnectionBuilder::MeshDensityTypeEnum MeshDensityType
            (
            );
            /**Sets  the mesh density type  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMeshDensityType
            (
                NXOpen::CAE::CAEWeldConnectionBuilder::MeshDensityTypeEnum meshDensityType /** meshdensitytype */ 
            );
            /**Returns  the mesh density value  <br> License requirements : None */
            public: NXOpen::Expression * MeshDensityValue
            (
            );
            /**Returns  the merge node tol  <br> License requirements : None */
            public: NXOpen::Expression * MergeNodeTol
            (
            );
            /**Returns  the element type to be created <br> License requirements : None */
            public: NXOpen::CAE::ElementTypeBuilder * ElementType
            (
            );
            public: NXOpen::CAE::CAEWeldConnection * CommitWeldconnection
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
