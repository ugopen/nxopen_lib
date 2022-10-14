#ifndef NXOpen_MFG_AM_ATTRIBUTECLIPBOARD_HXX_INCLUDED
#define NXOpen_MFG_AM_ATTRIBUTECLIPBOARD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mfg_AM_AttributeClipboard.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libmfgamopencpp_exports.hxx>

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
        namespace AM
        {
            class AttributeClipboard;
        }
    }
    class NXObject;
    class TaggedObject;
    namespace Mfg
    {
        namespace AM
        {
            class _AttributeClipboardBuilder;
            class AttributeClipboardImpl;
            /**  attribute clipboard  <br> To obtain an instance of this class use @link NXOpen::Mfg::AM::ApplicationManager NXOpen::Mfg::AM::ApplicationManager@endlink .  <br> 
             <br>  Created in NX12.0.1.  <br>  
            */
            class MFGAMOPENCPPEXPORT  AttributeClipboard : public NXOpen::NXObject
            {
                private: AttributeClipboardImpl * m_attributeclipboard_impl;
                private: friend class  _AttributeClipboardBuilder;
                protected: AttributeClipboard();
                public: ~AttributeClipboard();
                /** Copy attributes 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: void CopyAttributes
                (
                    NXOpen::TaggedObject * target /** target */ 
                );
                /** Paste attributes 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: void PasteAttributes
                (
                    NXOpen::TaggedObject * target /** target */ 
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