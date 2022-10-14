#ifndef NXOpen_MFG_MLP_PRODUCT_HXX_INCLUDED
#define NXOpen_MFG_MLP_PRODUCT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mfg_Mlp_Product.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/libmfgmlpopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mfg
    {
        namespace Mlp
        {
            class Product;
        }
    }
    class DisplayableObject;
    namespace Mfg
    {
        namespace Mlp
        {
            class Blank;
        }
    }
    namespace Mfg
    {
        namespace Mlp
        {
            class Part;
        }
    }
    namespace Mfg
    {
        namespace Mlp
        {
            class Workpiece;
        }
    }
    namespace Mfg
    {
        namespace Mlp
        {
            class _ProductBuilder;
            class ProductImpl;
            /** Represents a Machining Line Planner product  <br> To obtain an instance of this class use GetProducts of ProcessPlan.  <br> 
             <br>  Created in NX11.0.1.  <br>  
            */
            class MFGMLPOPENCPPEXPORT  Product : public NXOpen::DisplayableObject
            {
                private: ProductImpl * m_product_impl;
                private: friend class  _ProductBuilder;
                protected: Product();
                public: ~Product();
                /** Get the Part Model  @return  
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Mfg::Mlp::Part * GetPartModel
                (
                );
                /** Get the Blank Model  @return  
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Mfg::Mlp::Blank * GetBlankModel
                (
                );
                /** Get the Workpieces  @return  
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::Mfg::Mlp::Workpiece *> GetWorkpieces
                (
                );
                /** Get the workpiece of this product in the not allocated setup  @return  
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Mfg::Mlp::Workpiece * GetNotAllocatedWorkpiece
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