#ifndef NXOpen_CAE_XYPLOT_DIAGRAMDISPLAYSTYLES2D_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_DIAGRAMDISPLAYSTYLES2D_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_DiagramDisplayStyles2D.ja
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
#include <NXOpen/CAE_Xyplot_GraphOptionsStyle2D.hxx>
#include <NXOpen/CAE_Xyplot_DiagramDisplayStyles.hxx>
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
            class DiagramDisplayStyles2D;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class DiagramDisplayStyles;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class GraphOptionsStyle2D;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _DiagramDisplayStyles2DBuilder;
            class DiagramDisplayStyles2DImpl;
            /** Manages the display styles for 2D diagram.  <br> Not support KF.  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  DiagramDisplayStyles2D : public NXOpen::CAE::Xyplot::DiagramDisplayStyles
            {
                private: DiagramDisplayStyles2DImpl * m_diagramdisplaystyles2d_impl;
                private: friend class  _DiagramDisplayStyles2DBuilder;
                protected: DiagramDisplayStyles2D();
                public: ~DiagramDisplayStyles2D();
                /** Gets the nth graph options display style. The style index must be greater than or equal to 0 and
                                less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::GraphOptionsStyle2D * GetGraphOptionsStyle
                (
                    int styleIndex /** styleindex */ 
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
