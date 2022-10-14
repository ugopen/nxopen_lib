#ifndef NXOpen_CAE_INTERPOLATIONEADBUILDER_HXX_INCLUDED
#define NXOpen_CAE_INTERPOLATIONEADBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_InterpolationEADBuilder.ja
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
#include <NXOpen/CAE_InterpolationEADBuilder.hxx>
#include <NXOpen/CAE_SelectElementsBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class InterpolationEADBuilder;
    }
    class Builder;
    namespace CAE
    {
        class SelectElementsBuilder;
    }
    namespace CAE
    {
        class _InterpolationEADBuilderBuilder;
        class InterpolationEADBuilderImpl;
        /** This class provides Interpolation Associated Data Support  <br> To create a new instance of this class, use @link NXOpen::CAE::NodeElementManager::CreateInterpolationEadBuilder  NXOpen::CAE::NodeElementManager::CreateInterpolationEadBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  InterpolationEADBuilder : public NXOpen::Builder
        {
            private: InterpolationEADBuilderImpl * m_interpolationeadbuilder_impl;
            private: friend class  _InterpolationEADBuilderBuilder;
            protected: InterpolationEADBuilder();
            public: ~InterpolationEADBuilder();
            /**Returns  the select element operator selects elements 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::SelectElementsBuilder * Elements
            (
            );
            /** The set_dof1_weights operator selects elements 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetDof1Weights
            (
                const std::vector<double> & dofWeights /** dofweights */ 
            );
            /** The get dof1_weights operator gets dof 1 weight values  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<double> GetDof1Weights
            (
            );
            /** The set_dof2_weights operator selects elements 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetDof2Weights
            (
                const std::vector<double> & dofWeights /** dofweights */ 
            );
            /** The get dof2_weights operator gets dof 2 weight values  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<double> GetDof2Weights
            (
            );
            /** The set_dof3_weights operator selects elements 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetDof3Weights
            (
                const std::vector<double> & dofWeights /** dofweights */ 
            );
            /** The get dof3_weights operator gets dof 3 weight values  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<double> GetDof3Weights
            (
            );
            /** The set_dof4_weights operator selects elements 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetDof4Weights
            (
                const std::vector<double> & dofWeights /** dofweights */ 
            );
            /** The get dof4_weights operator gets dof 4 weight values  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<double> GetDof4Weights
            (
            );
            /** The set_dof5_weights operator selects elements 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetDof5Weights
            (
                const std::vector<double> & dofWeights /** dofweights */ 
            );
            /** The get dof5_weights operator gets dof 5 weight values  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<double> GetDof5Weights
            (
            );
            /** The set_dof6_weights operator selects elements 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetDof6Weights
            (
                const std::vector<double> & dofWeights /** dofweights */ 
            );
            /** The get dof6_weights operator gets dof 6 weight values  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<double> GetDof6Weights
            (
            );
            /** The set_um_data operator sets the array of 12 um_data values 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetUmData
            (
                const std::vector<int> & umData /** umdata */ 
            );
            /** The get_um_data operator gets the array of 12 um_data values  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<int> GetUmData
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