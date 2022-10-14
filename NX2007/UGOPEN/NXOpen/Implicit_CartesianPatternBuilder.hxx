#ifndef NXOpen_IMPLICIT_CARTESIANPATTERNBUILDER_HXX_INCLUDED
#define NXOpen_IMPLICIT_CARTESIANPATTERNBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Implicit_CartesianPatternBuilder.ja
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
#include <NXOpen/Implicit_OperationBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
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
        class CartesianPatternBuilder;
    }
    class CoordinateSystem;
    class Expression;
    namespace Implicit
    {
        class OperationBuilder;
    }
    class ScCollector;
    namespace Implicit
    {
        class _CartesianPatternBuilderBuilder;
        class CartesianPatternBuilderImpl;
        /**
            Represents a Implicit.CartesianPatternBuilder.
            The unit cell body will be scaled to the specified unit cell size and patterned in X, Y and Z orientation until it fills the boundary body (or it voids).
             <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateCartesianPatternBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateCartesianPatternBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        BlendFactor </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        BoundaryConditionOption </term> <description> 
         
        SolidVolume </description> </item> 

        <item><term> 
         
        EdgeLength.Value </term> <description> 
         
        10 (millimeters part), 0.4 (inches part) </description> </item> 

        <item><term> 
         
        SizeX.Value </term> <description> 
         
        10 (millimeters part), 0.4 (inches part) </description> </item> 

        <item><term> 
         
        SizeY.Value </term> <description> 
         
        10 (millimeters part), 0.4 (inches part) </description> </item> 

        <item><term> 
         
        SizeZ.Value </term> <description> 
         
        10 (millimeters part), 0.4 (inches part) </description> </item> 

        <item><term> 
         
        UniformCubeFlag </term> <description> 
         
        true </description> </item> 

        </list> 

         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_IMPLICITEXPORT  CartesianPatternBuilder : public NXOpen::Implicit::OperationBuilder
        {
            /** Boundary Condition options*/
            public: enum BoundaryConditionOptionType
            {
                BoundaryConditionOptionTypeSolidVolume/** Solid region */,
                BoundaryConditionOptionTypeVoidVolume/** Void region */,
                BoundaryConditionOptionTypeVoidVolumeAndUnite/** void volume and unite */ 
            };

            private: CartesianPatternBuilderImpl * m_cartesianpatternbuilder_impl;
            private: friend class  _CartesianPatternBuilderBuilder;
            protected: CartesianPatternBuilder();
            public: ~CartesianPatternBuilder();
            /**Returns  the input body.
                    As boundary body a solid body that is either an implicit body (within feature/TE)
                    or a parametric body from outside the TE can be provided.
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * BoundaryBody
            (
            );
            /**Returns  the Boundary Condition Option
                    Solid volume fill, void volume fill or void volume fill with unite to outer body
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Implicit::CartesianPatternBuilder::BoundaryConditionOptionType BoundaryConditionOption
            (
            );
            /**Sets  the Boundary Condition Option
                    Solid volume fill, void volume fill or void volume fill with unite to outer body
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_implicit (" NX Implicit Modeling") */
            public: void SetBoundaryConditionOption
            (
                NXOpen::Implicit::CartesianPatternBuilder::BoundaryConditionOptionType boundaryConditionOption /** boundaryconditionoption */ 
            );
            /**Returns  the blend factor.
                    factor to adjust the blend of intersections between tool and target body. 
                    No Blend(0) - to - large Blends(100)
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: int BlendFactor
            (
            );
            /**Sets  the blend factor.
                    factor to adjust the blend of intersections between tool and target body. 
                    No Blend(0) - to - large Blends(100)
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_implicit (" NX Implicit Modeling") */
            public: void SetBlendFactor
            (
                int blendFactor /** blendfactor */ 
            );
            /**Returns  the unit cell body.
                    The unit cell body will be scaled to the specified unit cell size.
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * UnitCellBody
            (
            );
            /**Returns  the uniform cube toggle.
                    A uniform cube with one edge length in all three
                    directions can be defined or specify the length for each axis separately.
                    ture for uniform cube false otherwise.
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool UniformCubeFlag
            (
            );
            /**Sets  the uniform cube toggle.
                    A uniform cube with one edge length in all three
                    directions can be defined or specify the length for each axis separately.
                    ture for uniform cube false otherwise.
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_implicit (" NX Implicit Modeling") */
            public: void SetUniformCubeFlag
            (
                bool uniformCubeFlag /** uniformcubeflag */ 
            );
            /**Returns  the edge length.
                    Edge length in X, Y and Z direction if it is a uniform cube.
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * EdgeLength
            (
            );
            /**Returns  the size x.
                    Edge length in X if it is a non-uniform cube.
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SizeX
            (
            );
            /**Returns  the size y.
                    Edge length in Y if it is a non-uniform cube.
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SizeY
            (
            );
            /**Returns  the size z.
                    Edge length in Z if it is a non-uniform cube.
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SizeZ
            (
            );
            /**Returns  the location and orientation of the seed cell.
                    The orientation can be inferred from objects inside or outside the TE.
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CoordinateSystem * LocationAndOrientation
            (
            );
            /**Sets  the location and orientation of the seed cell.
                    The orientation can be inferred from objects inside or outside the TE.
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_implicit (" NX Implicit Modeling") */
            public: void SetLocationAndOrientation
            (
                NXOpen::CoordinateSystem * locationAndOrientation /** locationandorientation */ 
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