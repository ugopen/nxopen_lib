#ifndef NXOpen_CAE_SUPPRESSHOLEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_SUPPRESSHOLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SuppressHoleBuilder.ja
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
#include <NXOpen/CAE_SuppressHoleBuilder.hxx>
#include <NXOpen/Expression.hxx>
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
        class SuppressHoleBuilder;
    }
    class Builder;
    class Expression;
    class SelectTaggedObjectList;
    namespace CAE
    {
        class _SuppressHoleBuilderBuilder;
        class SuppressHoleBuilderImpl;
        /**
            Builder for creating Hole Suppression Hole
             <br> To create a new instance of this class, use @link CAE::AbstractionManager::CreateSuppressHoleBuilder  CAE::AbstractionManager::CreateSuppressHoleBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Choice </td> <td> 
         
        Automatic </td> </tr> 

        <tr><td> 
         
        HoleDiameter.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        PointCreate </td> <td> 
         
        None </td> </tr> 

        </table>  

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SuppressHoleBuilder : public Builder
        {
            /** the enum  for method */
            public: enum OptionChoice
            {
                OptionChoiceAutomatic/** automatic */ ,
                OptionChoiceManual/** manual */ 
            };

            /** the enum  for point creation */
            public: enum OptionPointCreate
            {
                OptionPointCreateNone/** none */ ,
                OptionPointCreatePoint/** point */ ,
                OptionPointCreateMeshPoint/** mesh point */ 
            };

            private: SuppressHoleBuilderImpl * m_suppressholebuilder_impl;
            private: friend class  _SuppressHoleBuilderBuilder;
            protected: SuppressHoleBuilder();
            public: ~SuppressHoleBuilder();
            /**Returns  the type  Automatic or Manual 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SuppressHoleBuilder::OptionChoice Choice
            (
            );
            /**Sets  the type  Automatic or Manual 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetChoice
            (
                NXOpen::CAE::SuppressHoleBuilder::OptionChoice type /** type */ 
            );
            /**Returns  the bodyselect 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::SelectTaggedObjectList * BodySelect
            (
            );
            /**Returns  the edgeselect 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::SelectTaggedObjectList * EdgeSelect
            (
            );
            /**Returns  the holedia 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * HoleDiameter
            (
            );
            /**Returns  the pointcreate 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SuppressHoleBuilder::OptionPointCreate PointCreate
            (
            );
            /**Sets  the pointcreate 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPointCreate
            (
                NXOpen::CAE::SuppressHoleBuilder::OptionPointCreate pointCreate /** pointcreate */ 
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