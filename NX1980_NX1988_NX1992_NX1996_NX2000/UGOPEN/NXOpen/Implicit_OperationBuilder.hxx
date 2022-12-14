#ifndef NXOpen_IMPLICIT_OPERATIONBUILDER_HXX_INCLUDED
#define NXOpen_IMPLICIT_OPERATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Implicit_OperationBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_implicit_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Implicit
    {
        class OperationBuilder;
    }
    class Builder;
    class Expression;
    namespace Implicit
    {
        class _OperationBuilderBuilder;
        class OperationBuilderImpl;
        /**
            Represents a Implicit.OperationBuilder. This is an abstract class.
            This is the base class of all Implicit operations builder classes.
             <br> This is abstract class.  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_IMPLICITEXPORT  OperationBuilder : public NXOpen::Builder
        {
            private: OperationBuilderImpl * m_operationbuilder_impl;
            private: friend class  _OperationBuilderBuilder;
            protected: OperationBuilder();
            public: ~OperationBuilder();
            /**Returns  the flag to update default voxel size based on the size of first operation
                     <br> 
                    This API is now deprecated.
                    Please use @link NXOpen::Implicit::OperationBuilder::VoxelSizePercent NXOpen::Implicit::OperationBuilder::VoxelSizePercent@endlink  instead.
                     <br> 
                    
             <br>  @deprecated Deprecated in NX1980.0.0.  Please use @link NXOpen::Implicit::OperationBuilder::VoxelSizePercent NXOpen::Implicit::OperationBuilder::VoxelSizePercent@endlink  instead. <br>  

             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  Please use NXOpen::Implicit::OperationBuilder::VoxelSizePercent instead.") bool UpdateDefaultVoxelSizeBasedOnFirstOperation
            (
            );
            /**Sets  the flag to update default voxel size based on the size of first operation
                     <br> 
                    This API is now deprecated.
                    Please use @link NXOpen::Implicit::OperationBuilder::VoxelSizePercent NXOpen::Implicit::OperationBuilder::VoxelSizePercent@endlink  instead.
                     <br> 
                    
             <br>  @deprecated Deprecated in NX1980.0.0.  Please use @link NXOpen::Implicit::OperationBuilder::VoxelSizePercent NXOpen::Implicit::OperationBuilder::VoxelSizePercent@endlink  instead. <br>  

             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_implicit (" NX Implicit Modeling") */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  Please use NXOpen::Implicit::OperationBuilder::VoxelSizePercent instead.") void SetUpdateDefaultVoxelSizeBasedOnFirstOperation
            (
                bool updateVoxelSize /** updatevoxelsize */ 
            );
            /**Returns  the size of voxels in percentage of body size
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * VoxelSizePercent
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
