#ifndef NXOpen_IMPLICIT_CONEBUILDER_HXX_INCLUDED
#define NXOpen_IMPLICIT_CONEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Implicit_ConeBuilder.ja
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
        class ConeBuilder;
    }
    class CartesianCoordinateSystem;
    class Expression;
    namespace Implicit
    {
        class OperationBuilder;
    }
    namespace Implicit
    {
        class _ConeBuilderBuilder;
        class ConeBuilderImpl;
        /** 
            Represents a Implicit.ConeBuilder.
            It will create a cone inside the Implicit task environment.
             <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateConeBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateConeBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        Associative </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        BaseDiameter.Value </term> <description> 
         
        50 (millimeters part), 2 (inches part) </description> </item> 

        <item><term> 
         
        Height.Value </term> <description> 
         
        25 (millimeters part), 1 (inches part) </description> </item> 

        <item><term> 
         
        TopDiameter.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        </list> 

         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_IMPLICITEXPORT  ConeBuilder : public NXOpen::Implicit::OperationBuilder
        {
            private: ConeBuilderImpl * m_conebuilder_impl;
            private: friend class  _ConeBuilderBuilder;
            protected: ConeBuilder();
            public: ~ConeBuilder();
            /**Returns  the origin Point 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CartesianCoordinateSystem * CenterAndOrientation
            (
            );
            /**Sets  the origin Point 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_implicit (" NX Implicit Modeling") */
            public: void SetCenterAndOrientation
            (
                NXOpen::CartesianCoordinateSystem * csys /** csys */ 
            );
            /**Returns  the cone base diameter 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * BaseDiameter
            (
            );
            /**Returns  the cone top diameter 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * TopDiameter
            (
            );
            /**Returns  the height 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Height
            (
            );
            /**Returns  the option to keep the cone associative with the specified Center And Orientation.
                        this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the option to keep the cone associative with the specified Center And Orientation.
                        this does not apply to selection methods Dynamic, Inferred, Absolute CSYS, and CSYS of Current View.
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_implicit (" NX Implicit Modeling") */
            public: void SetAssociative
            (
                bool associativeCenter /** associativecenter */ 
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
