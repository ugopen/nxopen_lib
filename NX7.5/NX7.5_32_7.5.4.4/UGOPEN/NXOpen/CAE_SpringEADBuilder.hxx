#ifndef NXOpen_CAE_SPRINGEADBUILDER_HXX_INCLUDED
#define NXOpen_CAE_SPRINGEADBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SpringEADBuilder.ja
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
#include <NXOpen/CAE_SelectElementsBuilder.hxx>
#include <NXOpen/CAE_SpringEADBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class SpringEADBuilder;
    }
    class Builder;
    namespace CAE
    {
        class SelectElementsBuilder;
    }
    class Expression;
    namespace CAE
    {
        class _SpringEADBuilderBuilder;
        class SpringEADBuilderImpl;
        /** This class provides Spring Associated Data Support  <br> To create a new instance of this class, use @link CAE::NodeElementManager::CreateSpringEadBuilder CAE::NodeElementManager::CreateSpringEadBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        RotationalStiffness.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        StiffnessState </td> <td> 
         
        Apply </td> </tr> 

        <tr><td> 
         
        TranslationalStiffness.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  SpringEADBuilder : public Builder
        {
            /** indicates to apply or clear the stiffness property upon commit */
            public: enum State
            {
                StateApply/** apply the property */,
                StateClear/** clear the property */
            };

            private: SpringEADBuilderImpl * m_springeadbuilder_impl;
            private: friend class  _SpringEADBuilderBuilder;
            protected: SpringEADBuilder();
            public: ~SpringEADBuilder();
            /**Returns  the select element operator selects elements  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::SelectElementsBuilder * Elements
            (
            );
            /**Returns  the expression stiffness operator gets spring translational stiffness value  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::Expression * TranslationalStiffness
            (
            );
            /**Returns  the expression rotational stiffness operator gets spring rotational stiffness value  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::Expression * RotationalStiffness
            (
            );
            /**Returns  the stiffness state drives the action upon commit  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::SpringEADBuilder::State StiffnessState
            (
            );
            /**Sets  the stiffness state drives the action upon commit  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetStiffnessState
            (
                NXOpen::CAE::SpringEADBuilder::State stiffnessState /** stiffnessstate */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
