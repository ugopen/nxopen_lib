#ifndef NXOpen_IMPLICIT_IMPLICITMODELINGPREFERENCESBUILDER_HXX_INCLUDED
#define NXOpen_IMPLICIT_IMPLICITMODELINGPREFERENCESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Implicit_ImplicitModelingPreferencesBuilder.ja
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
        class ImplicitModelingPreferencesBuilder;
    }
    class Builder;
    class Expression;
    namespace Implicit
    {
        class _ImplicitModelingPreferencesBuilderBuilder;
        class ImplicitModelingPreferencesBuilderImpl;
        /** Represents an implicit feature. Output of this feature is convergent body.  <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateImplicitModelingPreferencesBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateImplicitModelingPreferencesBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        ChordalTolerance </term> <description> 
         
        0.1 (millimeters part), 0.005 (inches part) </description> </item> 

        <item><term> 
         
        MaxFacetSize.Value </term> <description> 
         
        10 (millimeters part), 0.5 (inches part) </description> </item> 

        <item><term> 
         
        RemeshFlag </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        VoxelSize.Value </term> <description> 
         
        1 (millimeters part), 0.05 (inches part) </description> </item> 

        </list> 

         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_IMPLICITEXPORT  ImplicitModelingPreferencesBuilder : public NXOpen::Builder
        {
            private: ImplicitModelingPreferencesBuilderImpl * m_implicitmodelingpreferencesbuilder_impl;
            private: friend class  _ImplicitModelingPreferencesBuilderBuilder;
            protected: ImplicitModelingPreferencesBuilder();
            public: ~ImplicitModelingPreferencesBuilder();
            /**Returns  the voxel size for implicit feature. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * VoxelSize
            (
            );
            /**Returns  the flag to remesh the implict body. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemeshFlag
            (
            );
            /**Sets  the flag to remesh the implict body. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_implicit (" NX Implicit Modeling") */
            public: void SetRemeshFlag
            (
                bool remeshFlag /** remeshflag */ 
            );
            /**Returns  the maximum facet size in areas of low face curvature. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MaxFacetSize
            (
            );
            /**Returns  the maximum chordal deviation between the original mesh and the output mesh. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double ChordalTolerance
            (
            );
            /**Sets  the maximum chordal deviation between the original mesh and the output mesh. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_implicit (" NX Implicit Modeling") */
            public: void SetChordalTolerance
            (
                double chordalTolerance /** chordaltolerance */ 
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
