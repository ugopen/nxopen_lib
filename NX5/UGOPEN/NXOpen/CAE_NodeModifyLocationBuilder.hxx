#ifndef NXOpen_CAE_NODEMODIFYLOCATIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_NODEMODIFYLOCATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_NodeModifyLocationBuilder.ja
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
#include <NXOpen/CAE_NodeModifyLocationBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class NodeModifyLocationBuilder;
    }
    class Builder;
    namespace CAE
    {
        class SelectFENodeList;
    }
    class CoordinateSystem;
    class Expression;
    namespace CAE
    {
        class _NodeModifyLocationBuilderBuilder;
        /**
            Represents a @link CAE::NodeModifyLocationBuilder CAE::NodeModifyLocationBuilder@endlink 
             <br> To create a new instance of this class, use @link CAE::NodeElementManager::CreateNodeModifyLocationBuilder CAE::NodeElementManager::CreateNodeModifyLocationBuilder@endlink  <br> */
        class NXOPENCPPEXPORT NodeModifyLocationBuilder : public Builder
        {
            private: friend class  _NodeModifyLocationBuilderBuilder;
            protected: NodeModifyLocationBuilder();
            /**Returns  the node  <br> License requirements : None */
            public: NXOpen::CAE::SelectFENodeList * Node
            (
            );
            /**Returns  the csys  <br> License requirements : None */
            public: NXOpen::CoordinateSystem * Csys
            (
            );
            /**Sets  the csys  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetCsys
            (
                NXOpen::CoordinateSystem * csys /** csys */ 
            );
            /**Returns  the x option  <br> License requirements : None */
            public: bool XOption
            (
            );
            /**Sets  the x option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetXOption
            (
                bool xOption /** xoption */ 
            );
            /**Returns  the x  <br> License requirements : None */
            public: NXOpen::Expression * X
            (
            );
            /**Returns  the y option  <br> License requirements : None */
            public: bool YOption
            (
            );
            /**Sets  the y option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetYOption
            (
                bool yOption /** yoption */ 
            );
            /**Returns  the y  <br> License requirements : None */
            public: NXOpen::Expression * Y
            (
            );
            /**Returns  the z option  <br> License requirements : None */
            public: bool ZOption
            (
            );
            /**Sets  the z option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetZOption
            (
                bool zOption /** zoption */ 
            );
            /**Returns  the z  <br> License requirements : None */
            public: NXOpen::Expression * Z
            (
            );
            /**Returns  the theta  <br> License requirements : None */
            public: NXOpen::Expression * Theta
            (
            );
            /**Returns  the phi  <br> License requirements : None */
            public: NXOpen::Expression * Phi
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
