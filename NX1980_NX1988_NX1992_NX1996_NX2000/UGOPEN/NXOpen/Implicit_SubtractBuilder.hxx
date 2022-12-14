#ifndef NXOpen_IMPLICIT_SUBTRACTBUILDER_HXX_INCLUDED
#define NXOpen_IMPLICIT_SUBTRACTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Implicit_SubtractBuilder.ja
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
#include <NXOpen/Implicit_BooleanBuilder.hxx>
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
        class SubtractBuilder;
    }
    namespace Implicit
    {
        class BooleanBuilder;
    }
    namespace Implicit
    {
        class _SubtractBuilderBuilder;
        class SubtractBuilderImpl;
        /**
            Represents an Implicit.SubtractBuilder.
            It will create a subtract operation on the selected bodies.
             <br> To create a new instance of this class, use @link NXOpen::Implicit::ImplicitOperationCollection::CreateSubtractBuilder  NXOpen::Implicit::ImplicitOperationCollection::CreateSubtractBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        BlendFactor </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        CreateBlends (deprecated) </term> <description> 
         
        0 </description> </item> 

        </list> 

         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_IMPLICITEXPORT  SubtractBuilder : public NXOpen::Implicit::BooleanBuilder
        {
            private: SubtractBuilderImpl * m_subtractbuilder_impl;
            private: friend class  _SubtractBuilderBuilder;
            protected: SubtractBuilder();
            public: ~SubtractBuilder();
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
