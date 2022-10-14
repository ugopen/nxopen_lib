#ifndef NXOpen_CAE_AEROSTRUCTURES_PARAMETERDESCRIPTOR_HXX_INCLUDED
#define NXOpen_CAE_AEROSTRUCTURES_PARAMETERDESCRIPTOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AeroStructures_ParameterDescriptor.ja
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
#include <NXOpen/TransientObject.hxx>
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
        namespace AeroStructures
        {
            class ParameterDescriptor;
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            class ParameterDescriptorImpl;
            /**  @brief  This is the Parameter Descriptor  

              
             <br>  Created in NX12.0.1.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ParameterDescriptor : public NXOpen::TransientObject
            {
                /** the Parameter Type */
                public: enum ParameterType
                {
                    ParameterTypeBoolean/** boolean */ ,
                    ParameterTypeInteger/** integer */ ,
                    ParameterTypeScalar/** scalar */ ,
                    ParameterTypeText/** text */ ,
                    ParameterTypeLoad/** load */ ,
                    ParameterTypeUnknown/** unknown */ 
                };

                /** the Dimensionality */
                public: enum DimensionalityType
                {
                    DimensionalityTypeNone/** none */ ,
                    DimensionalityTypeFailuremode/** failuremode */ ,
                    DimensionalityTypeLoadcase/** loadcase */ ,
                    DimensionalityTypeFmLc/** fm lc */ 
                };

                private: ParameterDescriptorImpl * m_parameterdescriptor_impl;
                /// \cond NX_NO_DOC 
                public: explicit ParameterDescriptor(void *ptr);
                /// \endcond 
                /** Dispose 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: virtual ~ParameterDescriptor();
                /**Returns  the id 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: NXString Id
                (
                );
                /**Returns  the UI name 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: NXString UiName
                (
                );
                /**Returns  the ParameterType 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: NXOpen::CAE::AeroStructures::ParameterDescriptor::ParameterType ParamType
                (
                );
                /**Returns  the Dimensionality 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: NXOpen::CAE::AeroStructures::ParameterDescriptor::DimensionalityType Dimensionality
                (
                );
            }; //lint !e1712 default constructor not defined for class  

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