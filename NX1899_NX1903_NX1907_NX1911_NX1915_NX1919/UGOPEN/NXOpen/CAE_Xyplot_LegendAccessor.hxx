#ifndef NXOpen_CAE_XYPLOT_LEGENDACCESSOR_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_LEGENDACCESSOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_LegendAccessor.ja
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
        namespace Xyplot
        {
            class LegendAccessor;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class LegendAccessorImpl;
            /**  @brief  Represents a data accessor to retrieve data of a legend.  

              
             <br>  Created in NX1899.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  LegendAccessor : public NXOpen::TransientObject
            {
                private: LegendAccessorImpl * m_legendaccessor_impl;
                /// \cond NX_NO_DOC 
                public: explicit LegendAccessor(void *ptr);
                /// \endcond 
                /**Returns  the free text. 
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString FreeText
                (
                );
                /** Destroys the object. 
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual ~LegendAccessor();
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
