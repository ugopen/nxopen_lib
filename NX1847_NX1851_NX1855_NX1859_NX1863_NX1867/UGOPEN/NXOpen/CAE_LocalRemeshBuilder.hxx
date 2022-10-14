#ifndef NXOpen_CAE_LOCALREMESHBUILDER_HXX_INCLUDED
#define NXOpen_CAE_LOCALREMESHBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LocalRemeshBuilder.ja
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
#include <NXOpen/CAE_SelectElementsBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class LocalRemeshBuilder;
    }
    class Builder;
    namespace CAE
    {
        class SelectElementsBuilder;
    }
    class Expression;
    class SelectTaggedObjectList;
    namespace CAE
    {
        class _LocalRemeshBuilderBuilder;
        class LocalRemeshBuilderImpl;
        /**
            Represents a @link NXOpen::CAE::LocalRemeshBuilder NXOpen::CAE::LocalRemeshBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::CAE::MeshManager::CreateLocalRemeshBuilder  NXOpen::CAE::MeshManager::CreateLocalRemeshBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        FactorValue.Value </td> <td> 
         
        0.5 </td> </tr> 

        <tr><td> 
         
        SizeOption </td> <td> 
         
        Factor </td> </tr> 

        <tr><td> 
         
        SizeValue.Value </td> <td> 
         
        1.0 </td> </tr> 

        <tr><td> 
         
        Transition </td> <td> 
         
        50 </td> </tr> 

        </table>  

         <br>  Created in NX7.5.2.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  LocalRemeshBuilder : public NXOpen::Builder
        {
            /** Size Option */
            public: enum Option
            {
                OptionFactor/** Factor */,
                OptionSize/** Absolute Size */
            };

            private: LocalRemeshBuilderImpl * m_localremeshbuilder_impl;
            private: friend class  _LocalRemeshBuilderBuilder;
            protected: LocalRemeshBuilder();
            public: ~LocalRemeshBuilder();
            /**Returns  the select elements 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectElementsBuilder * ElementList
            (
            );
            /**Returns  the size option 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::LocalRemeshBuilder::Option SizeOption
            (
            );
            /**Sets  the size option 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetSizeOption
            (
                NXOpen::CAE::LocalRemeshBuilder::Option sizeOption /** sizeoption */ 
            );
            /**Returns  the size value 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SizeValue
            (
            );
            /**Returns  the factor value 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * FactorValue
            (
            );
            /**Returns  the transition 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public: int Transition
            (
            );
            /**Sets  the transition 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetTransition
            (
                int transition /** transition */ 
            );
            /**Returns  the select element edges to lock 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectTaggedObjectList * SelectionElementEdges
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