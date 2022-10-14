#ifndef NXOpen_MFG_AM_SERIALNUMBER_HXX_INCLUDED
#define NXOpen_MFG_AM_SERIALNUMBER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mfg_AM_SerialNumber.ja
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
#include <NXOpen/Mfg_AM_PartRegion.hxx>
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
            class SerialNumber;
        }
    }
    namespace Mfg
    {
        namespace AM
        {
            class PartRegion;
        }
    }
    namespace Mfg
    {
        namespace AM
        {
            class _SerialNumberBuilder;
            class SerialNumberImpl;
            /** Interface for Model Build Tray objects  <br> To obtain an instance of this class use JAX_MFG_AM_PART_GetSerialNumbers  <br> 
             <br>  Created in NX1872.0.0.  <br>  
            */
            class MFGAMOPENCPPEXPORT  SerialNumber : public NXOpen::Mfg::AM::PartRegion
            {
                private: SerialNumberImpl * m_serialnumber_impl;
                private: friend class  _SerialNumberBuilder;
                protected: SerialNumber();
                public: ~SerialNumber();
                /** Get Serial Number Text 
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString GetText
                (
                );
                /** Set Serial Number Text 
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : am_pb_cam_advanced ("Advanced NX Powder Bed Additive Manufacturing Application") */
                public: void SetText
                (
                    const NXString & printMarkText /** printmarktext */ 
                );
                /** Set Serial Number Text 
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : am_pb_cam_advanced ("Advanced NX Powder Bed Additive Manufacturing Application") */
                void SetText
                (
                    const char * printMarkText /** printmarktext */ 
                );
                /** Get Usable Label of Serial Number 
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : am_pb_cam_advanced ("Advanced NX Powder Bed Additive Manufacturing Application") */
                public: NXString GetUsageLabel
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