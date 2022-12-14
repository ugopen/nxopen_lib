#ifndef NXOpen_AME_AMEENGINEERINGOBJECTLABEL_HXX_INCLUDED
#define NXOpen_AME_AMEENGINEERINGOBJECTLABEL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_AMEEngineeringObjectLabel.ja
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
#include <NXOpen/libameopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        class AMEEngineeringObjectLabel;
    }
    namespace Annotations
    {
        class PmiNote;
    }
    class NXObject;
    namespace AME
    {
        class _AMEEngineeringObjectLabelBuilder;
        class AMEEngineeringObjectLabelImpl;
        /** Represents Engineering Object Label Object  <br> This object does not need a creator.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  AMEEngineeringObjectLabel : public NXOpen::NXObject
        {
            private: AMEEngineeringObjectLabelImpl * m_ameengineeringobjectlabel_impl;
            private: friend class  _AMEEngineeringObjectLabelBuilder;
            protected: AMEEngineeringObjectLabel();
            public: ~AMEEngineeringObjectLabel();
            /**Returns  the PMI note object stored by AME Engineering object label 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::Annotations::PmiNote * PmiFromLabel
            (
            );
        };
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
