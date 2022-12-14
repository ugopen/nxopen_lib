#ifndef NXOpen_CAE_MESHPOINTMULTIPLEONCURVEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MESHPOINTMULTIPLEONCURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_MeshPointMultipleOnCurveBuilder.ja
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
#include <NXOpen/CAE_MeshPointMultipleOnCurveBuilder.hxx>
#include <NXOpen/Expression.hxx>
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
        class MeshPointMultipleOnCurveBuilder;
    }
    class Builder;
    class Expression;
    class SelectIBaseCurveList;
    namespace CAE
    {
        class _MeshPointMultipleOnCurveBuilderBuilder;
        class MeshPointMultipleOnCurveBuilderImpl;
        /**
            Represents a @link NXOpen::CAE::MeshPointMultipleOnCurveBuilder NXOpen::CAE::MeshPointMultipleOnCurveBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::CAE::MeshPointCollection::CreateMeshpointMultipleOnCurveBuilder  NXOpen::CAE::MeshPointCollection::CreateMeshpointMultipleOnCurveBuilder @endlink  <br> 
         <br>  Created in NX5.0.2.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  MeshPointMultipleOnCurveBuilder : public NXOpen::Builder
        {
            /** the placement type types */
            public: enum PlacementType
            {
                PlacementTypeByNumber/**by number */,
                PlacementTypeByDistance/**by distance */
            };

            private: MeshPointMultipleOnCurveBuilderImpl * m_meshpointmultipleoncurvebuilder_impl;
            private: friend class  _MeshPointMultipleOnCurveBuilderBuilder;
            protected: MeshPointMultipleOnCurveBuilder();
            public: ~MeshPointMultipleOnCurveBuilder();
            /**Returns  the node 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectIBaseCurveList * Edge
            (
            );
            /**Returns  the distance 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Distance
            (
            );
            /**Returns  the number of meshpoints 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int NumMeshpoints
            (
            );
            /**Sets  the number of meshpoints 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetNumMeshpoints
            (
                int numMeshpoints /** nummeshpoints */ 
            );
            /**Returns  the placement option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::MeshPointMultipleOnCurveBuilder::PlacementType PlacementOption
            (
            );
            /**Sets  the placement option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPlacementOption
            (
                NXOpen::CAE::MeshPointMultipleOnCurveBuilder::PlacementType placementOption /** placementoption */ 
            );
            /**Returns  the create option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool CreateOption
            (
            );
            /**Sets  the create option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetCreateOption
            (
                bool createOption /** createoption */ 
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
