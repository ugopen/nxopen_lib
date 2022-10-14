#ifndef NXOpen_ANNOTATIONS_BUSINESSMODIFIER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_BUSINESSMODIFIER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_BusinessModifier.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class BusinessModifier;
    }
    class NXObject;
    namespace Annotations
    {
        class _BusinessModifierBuilder;
        class BusinessModifierImpl;
        /** Represents a business modifier object. A business modifier can be applied to a PMI to embed
                additional business/process information. The business modifier objects are knowledge fusion 
                driven meaning that they are created from the attributes defined in a .dfa file. */
        class NXOPENCPPEXPORT  BusinessModifier : public NXObject
        {
            private: BusinessModifierImpl * m_businessmodifier_impl;
            private: friend class  _BusinessModifierBuilder;
            protected: BusinessModifier();
            public: ~BusinessModifier();
            /**Returns  the title  <br> License requirements : None */
            public: NXString Title
            (
            );
            /**Sets  the title  <br> License requirements : geometric_tol ("GDT") */
            public: void SetTitle
            (
                const NXString & title /** New title */
            );
            /**Returns  the value  <br> License requirements : None */
            public: NXString TextValue
            (
            );
            /**Sets  the value  <br> License requirements : geometric_tol ("GDT") */
            public: void SetTextValue
            (
                const NXString & textValue /** New value in the text format */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif