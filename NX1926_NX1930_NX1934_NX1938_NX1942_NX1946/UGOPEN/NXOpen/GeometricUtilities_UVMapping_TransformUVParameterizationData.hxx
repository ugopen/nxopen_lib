#ifndef NXOpen_GEOMETRICUTILITIES_UVMAPPING_TRANSFORMUVPARAMETERIZATIONDATA_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_UVMAPPING_TRANSFORMUVPARAMETERIZATIONDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_UVMapping_TransformUVParameterizationData.ja
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
#include <NXOpen/GeometricUtilities_UVMapping_UVMeshManipulatorData.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        namespace UVMapping
        {
            class TransformUVParameterizationData;
        }
    }
    class Builder;
    namespace GeometricUtilities
    {
        namespace UVMapping
        {
            class UVMeshManipulatorData;
        }
    }
    namespace GeometricUtilities
    {
        namespace UVMapping
        {
            class _TransformUVParameterizationDataBuilder;
            class TransformUVParameterizationDataImpl;
            /** Transform UV parameterization by transforming patches in UV spaces.  <br> To create a new instance of this class, use @link NXOpen::GeometricUtilities::UVMapping::UVMappingCollection::CreateTransformUVParameterizationData  NXOpen::GeometricUtilities::UVMapping::UVMappingCollection::CreateTransformUVParameterizationData @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            CanRelocateToolToSelection </term> <description> 
             
            true </description> </item> 

            <item><term> 
             
            CanReorientToolToSelection </term> <description> 
             
            true </description> </item> 

            </list> 

             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_GEOMETRICUTILITIESEXPORT  TransformUVParameterizationData : public NXOpen::Builder
            {
                private: TransformUVParameterizationDataImpl * m_transformuvparameterizationdata_impl;
                private: friend class  _TransformUVParameterizationDataBuilder;
                protected: TransformUVParameterizationData();
                public: ~TransformUVParameterizationData();
                /**Returns  the UV mesh manipulation Tool. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::GeometricUtilities::UVMapping::UVMeshManipulatorData * UVMeshManipulator
                (
                );
                /**Returns  the flag indicating if only the transformation tool can be moved without affecting UV patches. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: bool CanMoveToolOnly
                (
                );
                /**Sets  the flag indicating if only the transformation tool can be moved without affecting UV patches. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetCanMoveToolOnly
                (
                    bool canMoveToolOnly /** canmovetoolonly */ 
                );
                /**Returns  the flat indicating if transformation tool can be relocated based on selected entities. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: bool CanRelocateToolToSelection
                (
                );
                /**Sets  the flat indicating if transformation tool can be relocated based on selected entities. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetCanRelocateToolToSelection
                (
                    bool canRelocateToolToSelection /** canrelocatetooltoselection */ 
                );
                /**Returns  the flat indicating if transformation tool can be reoriented based on selected entities. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: bool CanReorientToolToSelection
                (
                );
                /**Sets  the flat indicating if transformation tool can be reoriented based on selected entities. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetCanReorientToolToSelection
                (
                    bool canReorientToolToSelection /** canreorienttooltoselection */ 
                );
                /**Returns  the flag indicating if UV patches can be scaled uniformly. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: bool CanScaleUniformly
                (
                );
                /**Sets  the flag indicating if UV patches can be scaled uniformly. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetCanScaleUniformly
                (
                    bool canScaleUniformly /** canscaleuniformly */ 
                );
                /** Updates the parameterization by applying the transformation. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void Update
                (
                );
            };
        }
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
