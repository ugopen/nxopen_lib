#ifndef NXOpen_ROUTING_ADOPTIONBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_ADOPTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_AdoptionBuilder.ja
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
#include <NXOpen/Assemblies_Partition.hxx>
#include <NXOpen/CollaborativeDesign.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_routing_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Routing
    {
        class AdoptionBuilder;
    }
    namespace Assemblies
    {
        class Partition;
    }
    class Builder;
    class CollaborativeDesign;
    namespace Routing
    {
        class _AdoptionBuilderBuilder;
        class AdoptionBuilderImpl;

        /// \cond NX_NO_DOC 
        /**
                Represents a @link NXOpen::Routing::AdoptionBuilder NXOpen::Routing::AdoptionBuilder@endlink 
            
                This builder takes assembly / subassembly and converts it to next gen structure.
             <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateAdoptionBuilder  NXOpen::Routing::RouteManager::CreateAdoptionBuilder @endlink  <br> 
         <br>  Created in NX12.0.2.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  AdoptionBuilder : public NXOpen::Builder
        {
            private: AdoptionBuilderImpl * m_adoptionbuilder_impl;
            private: friend class  _AdoptionBuilderBuilder;
            protected: AdoptionBuilder();
            public: ~AdoptionBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the selected collaborative design 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced") */
            public: NXOpen::CollaborativeDesign * CollaborativeDesign
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the selected collaborative design 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced") */
            public: void SetCollaborativeDesign
            (
                NXOpen::CollaborativeDesign * collaborativeDesign /** collaborativedesign */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the partition list of selected collaborative design 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced") */
            public: NXOpen::Assemblies::Partition * SelectedPartition
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the partition list of selected collaborative design 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced") */
            public: void SetSelectedPartition
            (
                NXOpen::Assemblies::Partition * partition /** partition */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Checks the adoption validity of part containing this builder object. 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced") */
            public: int IsValidPartToAdopt
            (
            );

            /// \endcond 
        };

        /// \endcond 
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