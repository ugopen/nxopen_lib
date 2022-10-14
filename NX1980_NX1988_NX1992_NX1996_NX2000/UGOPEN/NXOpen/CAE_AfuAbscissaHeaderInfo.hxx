#ifndef NXOpen_CAE_AFUABSCISSAHEADERINFO_HXX_INCLUDED
#define NXOpen_CAE_AFUABSCISSAHEADERINFO_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AfuAbscissaHeaderInfo.ja
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
        class AfuAbscissaHeaderInfo;
    }
    namespace CAE
    {
        class AfuAbscissaHeaderInfoImpl;
        /**  @brief  Represents the data to define abscissa header information for an afu record  

          
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  AfuAbscissaHeaderInfo : public NXOpen::TransientObject
        {
            private: AfuAbscissaHeaderInfoImpl * m_afuabscissaheaderinfo_impl;
            /// \cond NX_NO_DOC 
            public: explicit AfuAbscissaHeaderInfo(void *ptr);
            /// \endcond 
            /** The object destructor 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~AfuAbscissaHeaderInfo();
            /**Sets  the value of spacing 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSpacing
            (
                int spacing /** the value of spacing */
            );
            /**Returns  the value of spacing 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: int Spacing
            (
            );
            /**Sets  the customized axis label 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAxisLabel
            (
                const NXString & axisLabel /** the customized axis label . 
                                                                                            Up to 80 characters are allowed and the redundant
                                                                                            characters will be ignored.
                                                                                           */
            );
            /**Sets  the customized axis label 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            void SetAxisLabel
            (
                const char * axisLabel /** the customized axis label . 
                                                                                            Up to 80 characters are allowed and the redundant
                                                                                            characters will be ignored.
                                                                                           */
            );
            /**Returns  the customized axis label 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXString AxisLabel
            (
            );
            /**Sets  the customized unit label 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetUnitLabel
            (
                const NXString & unitLabel /** the customized unit label. 
                                                                                            Up to 80 characters are allowed and the redundant
                                                                                            characters will be ignored.
                                                                                           */
            );
            /**Sets  the customized unit label 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            void SetUnitLabel
            (
                const char * unitLabel /** the customized unit label. 
                                                                                            Up to 80 characters are allowed and the redundant
                                                                                            characters will be ignored.
                                                                                           */
            );
            /**Returns  the customized unit label 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXString UnitLabel
            (
            );
            /**Sets  the abscissa offset for real part 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRealOffset
            (
                double realOffset /** the abscissa offset for real part*/
            );
            /**Returns  the abscissa offset for real part 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double RealOffset
            (
            );
            /**Sets  the abscissa scale for real part 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRealScale
            (
                double realScale /** the abscissa scale for real part*/
            );
            /**Returns  the abscissa scale for real part 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double RealScale
            (
            );
        }; //lint !e1712 default constructor not defined for class  

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