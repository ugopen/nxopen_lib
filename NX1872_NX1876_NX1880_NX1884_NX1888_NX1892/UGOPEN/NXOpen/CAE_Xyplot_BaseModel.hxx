#ifndef NXOpen_CAE_XYPLOT_BASEMODEL_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_BASEMODEL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_BaseModel.ja
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
#include <NXOpen/CAE_Xyplot_IDisplayableModel.hxx>
#include <NXOpen/NXObject.hxx>
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
            class BaseModel;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class BaseDisplayStyleSetting;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class IDisplayableModel;
        }
    }
    class NXObject;
    namespace CAE
    {
        namespace Xyplot
        {
            class _BaseModelBuilder;
            class BaseModelImpl;
            /** Represents an abstract component object on a XY graphing.  <br> not support KF.  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  BaseModel : public NXOpen::NXObject, public virtual NXOpen::CAE::Xyplot::IDisplayableModel
            {
                private: BaseModelImpl * m_basemodel_impl;
                private: friend class  _BaseModelBuilder;
                protected: BaseModel();
                public: ~BaseModel();
                /**Returns  the style setting associated to the model 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::BaseDisplayStyleSetting * StyleSetting
                (
                );
                /** Updates model display 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual void UpdateDisplay
                (
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