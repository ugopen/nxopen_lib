#ifndef NXOpen_ASSEMBLIES_PARTITIONSCHEME_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_PARTITIONSCHEME_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_PartitionScheme.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_assemblies_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Assemblies
    {
        class PartitionScheme;
    }
    namespace Assemblies
    {
        class Partition;
    }
    class CollaborativeDesign;
    class NXObject;
    namespace Assemblies
    {
        class _PartitionSchemeBuilder;
        class PartitionSchemeImpl;
        /**
                A partition scheme is a Teamcenter object in a Collaborative Design.  A partition scheme 
                contains partitions.
             <br> Instances of this object can be accessed through @link CollaborativeDesign CollaborativeDesign@endlink .  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_ASSEMBLIESEXPORT  PartitionScheme : public NXOpen::NXObject
        {
            private: PartitionSchemeImpl * m_partitionscheme_impl;
            private: friend class  _PartitionSchemeBuilder;
            protected: PartitionScheme();
            public: ~PartitionScheme();
            /**
                        Get the root partitions of partition scheme. 
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void GetRootPartitions
            (
                std::vector<NXOpen::Assemblies::Partition *> & rootPartitions /** rootpartitions */ 
            );
            /**Returns 
                        the owning collaborative design.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CollaborativeDesign * CollaborativeDesign
            (
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