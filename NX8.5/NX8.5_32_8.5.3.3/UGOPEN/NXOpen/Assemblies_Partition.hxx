#ifndef NXOpen_ASSEMBLIES_PARTITION_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_PARTITION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_Partition.ja
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
        class Partition;
    }
    class NXObject;
    namespace Assemblies
    {
        class _PartitionBuilder;
        class PartitionImpl;
        /**
                A partition is a Teamcenter object in a Collaborative Design.  A partition can
                contain design elements and other partitions.
             <br> Instances of this object can be accessed through @link Assemblies::PartitionScheme Assemblies::PartitionScheme@endlink .  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_ASSEMBLIESEXPORT  Partition : public NXObject
        {
            private: PartitionImpl * m_partition_impl;
            private: friend class  _PartitionBuilder;
            protected: Partition();
            public: ~Partition();
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
