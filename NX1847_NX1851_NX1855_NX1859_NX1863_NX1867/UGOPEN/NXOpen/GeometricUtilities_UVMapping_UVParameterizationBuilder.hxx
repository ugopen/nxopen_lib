#ifndef NXOpen_GEOMETRICUTILITIES_UVMAPPING_UVPARAMETERIZATIONBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_UVMAPPING_UVPARAMETERIZATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_UVMapping_UVParameterizationBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/SelectObject.hxx>
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
            class UVParameterizationBuilder;
        }
    }
    class Builder;
    class ScCollector;
    class Section;
    class SelectEdge;
    namespace GeometricUtilities
    {
        namespace UVMapping
        {
            class _UVParameterizationBuilderBuilder;
            class UVParameterizationBuilderImpl;
            /** Represents a UVParameterization builder  <br> To create a new instance of this class, use @link NXOpen::GeometricUtilities::UVMapping::UVMappingCollection::CreateUVParameterizationBuilder  NXOpen::GeometricUtilities::UVMapping::UVMappingCollection::CreateUVParameterizationBuilder @endlink  <br> 
             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_GEOMETRICUTILITIESEXPORT  UVParameterizationBuilder : public NXOpen::Builder
            {
                /** the perserving type */
                public: enum ParameterizationTypes
                {
                    ParameterizationTypesShapePreserving/** shape preserving */ ,
                    ParameterizationTypesLengthPreserving/** length preserving */ 
                };

                private: UVParameterizationBuilderImpl * m_uvparameterizationbuilder_impl;
                private: friend class  _UVParameterizationBuilderBuilder;
                protected: UVParameterizationBuilder();
                public: ~UVParameterizationBuilder();
                /**Returns  the preserving type 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::GeometricUtilities::UVMapping::UVParameterizationBuilder::ParameterizationTypes Type
                (
                );
                /**Sets  the preserving type 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetType
                (
                    NXOpen::GeometricUtilities::UVMapping::UVParameterizationBuilder::ParameterizationTypes type /** type */ 
                );
                /**Returns  the faces 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * Faces
                (
                );
                /**Returns  the rip edges 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Section * RipEdges
                (
                );
                /**Returns  the seed edge 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectEdge * OuterBoundarySeedEdge
                (
                );
                /**Returns  the number of grid lines 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: int NumberOfGridLines
                (
                );
                /**Sets  the number of grid lines 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetNumberOfGridLines
                (
                    int numGridLines /** numgridlines */ 
                );
                /** Evaluates parameterization 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void Evaluate
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
