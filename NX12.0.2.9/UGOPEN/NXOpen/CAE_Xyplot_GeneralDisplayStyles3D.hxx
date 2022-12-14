#ifndef NXOpen_CAE_XYPLOT_GENERALDISPLAYSTYLES3D_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_GENERALDISPLAYSTYLES3D_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_GeneralDisplayStyles3D.ja
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
#include <NXOpen/CAE_XyplotDataTypes.hxx>
#include <NXOpen/CAE_Xyplot_GeneralDisplayStyles.hxx>
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
            class GeneralDisplayStyles3D;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class GeneralDisplayStyles;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _GeneralDisplayStyles3DBuilder;
            class GeneralDisplayStyles3DImpl;
            /** Manages the general display styles for 3D plot.  <br> Not support KF.  <br> 
             <br>  Created in NX10.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  GeneralDisplayStyles3D : public NXOpen::CAE::Xyplot::GeneralDisplayStyles
            {
                private: GeneralDisplayStyles3DImpl * m_generaldisplaystyles3d_impl;
                private: friend class  _GeneralDisplayStyles3DBuilder;
                protected: GeneralDisplayStyles3D();
                public: ~GeneralDisplayStyles3D();
                /**Returns  the complex option 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::ComplexOption3D ComplexOption
                (
                );
                /**Sets  the complex option 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetComplexOption
                (
                    NXOpen::CAE::Xyplot::ComplexOption3D complexOption /** Complex option */
                );
            };
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
