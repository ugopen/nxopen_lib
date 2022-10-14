#ifndef NXOpen_CAE_XYPLOT_IDISPLAYSTYLE_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_IDISPLAYSTYLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_IDisplayStyle.ja
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
            class IDisplayStyle;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            /** Represents the interface for  plot display style classes
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  IDisplayStyle
            {
                virtual void EnsureVtableExists() {}
                public: virtual ~IDisplayStyle() {}
                /** Commits any edits that have been applied to the display style.
                                Triggers the corresponding plot to update graph. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: virtual void CommitChange
                (
                ) = 0;
                /**Returns  the owner style 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::Xyplot::IDisplayStyle * Owner
                (
                ) = 0;
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