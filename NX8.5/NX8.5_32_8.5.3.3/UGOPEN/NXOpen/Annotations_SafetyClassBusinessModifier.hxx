#ifndef NXOpen_ANNOTATIONS_SAFETYCLASSBUSINESSMODIFIER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_SAFETYCLASSBUSINESSMODIFIER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_SafetyClassBusinessModifier.ja
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
#include <NXOpen/Annotations_ListBusinessModifier.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class SafetyClassBusinessModifier;
    }
    namespace Annotations
    {
        class ListBusinessModifier;
    }
    namespace Annotations
    {
        class _SafetyClassBusinessModifierBuilder;
        class SafetyClassBusinessModifierImpl;
        /** Represents buiness modifier that applies safety classification such as Critical, Major 
                to a PMI. please see ug_safety_class_busmod.dfa for attribute details.  <br> To create or edit an instance of this class, use @link Annotations::SafetyClassBusinessModifierBuilder  Annotations::SafetyClassBusinessModifierBuilder @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  SafetyClassBusinessModifier : public Annotations::ListBusinessModifier
        {
            private: SafetyClassBusinessModifierImpl * m_safetyclassbusinessmodifier_impl;
            private: friend class  _SafetyClassBusinessModifierBuilder;
            protected: SafetyClassBusinessModifier();
            public: ~SafetyClassBusinessModifier();
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