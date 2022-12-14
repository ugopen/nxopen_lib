#ifndef NXOpen_CAE_AEROSTRUCTURES_AUTHOR_INPUTINTEGER_HXX_INCLUDED
#define NXOpen_CAE_AEROSTRUCTURES_AUTHOR_INPUTINTEGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AeroStructures_Author_InputInteger.ja
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
#include <NXOpen/CAE_AeroStructures_Author_InputParameter.hxx>
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
            namespace Author
            {
                class InputInteger;
            }
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            namespace Author
            {
                class InputParameter;
            }
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            namespace Author
            {
                class _InputIntegerBuilder;
                class InputIntegerImpl;
                /**  @brief  Represents an integer input parameter  

                   <br> No support for KF  <br> 
                 <br>  Created in NX12.0.0.  <br>  
                */
                class NXOPENCPP_CAEEXPORT  InputInteger : public NXOpen::CAE::AeroStructures::Author::InputParameter
                {
                    private: InputIntegerImpl * m_inputinteger_impl;
                    private: friend class  _InputIntegerBuilder;
                    protected: InputInteger();
                    public: ~InputInteger();
                    /**Returns  the value. 
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : None */
                    public: int Value
                    (
                    );
                };
            }
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
