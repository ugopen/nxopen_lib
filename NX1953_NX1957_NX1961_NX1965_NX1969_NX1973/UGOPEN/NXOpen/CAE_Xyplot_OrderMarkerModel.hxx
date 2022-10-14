#ifndef NXOpen_CAE_XYPLOT_ORDERMARKERMODEL_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_ORDERMARKERMODEL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_OrderMarkerModel.ja
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
#include <NXOpen/CAE_Xyplot_BasicModel.hxx>
#include <NXOpen/CAE_Xyplot_IDeletableModel.hxx>
#include <NXOpen/CAE_Xyplot_ITextModel.hxx>
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
            class OrderMarkerModel;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class BasicModel;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class IDeletableModel;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class ITextModel;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _OrderMarkerModelBuilder;
            class OrderMarkerModelImpl;
            /** Represents an marker which display order value on a @link CAE::Xyplot::PlotTypePlotCampbell CAE::Xyplot::PlotTypePlotCampbell@endlink  plot .  <br> Not support KF.  <br> 
             <br>  Created in NX1926.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  OrderMarkerModel : public NXOpen::CAE::Xyplot::BasicModel, public virtual NXOpen::CAE::Xyplot::IDeletableModel, public virtual NXOpen::CAE::Xyplot::ITextModel
            {
                private: OrderMarkerModelImpl * m_ordermarkermodel_impl;
                private: friend class  _OrderMarkerModelBuilder;
                protected: OrderMarkerModel();
                public: ~OrderMarkerModel();
                /** Returns the order value. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: double GetOrderValue
                (
                );
                /** Deletes the model 
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual void Delete
                (
                );
                /** Results text values 
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual void GetTexts
                (
                    std::vector<NXString> & textValues /** textvalues */ 
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