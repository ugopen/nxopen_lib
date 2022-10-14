#ifndef NXOpen_ANNOTATIONS_GOVERNMENTSECURITYINFORMATIONBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_GOVERNMENTSECURITYINFORMATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_GovernmentSecurityInformationBuilder.ja
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
#include <NXOpen/Annotations_GovernmentSecurityInformationBuilder.hxx>
#include <NXOpen/Annotations_PmiAttributeBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class GovernmentSecurityInformationBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeBuilder;
    }
    namespace Annotations
    {
        class _GovernmentSecurityInformationBuilderBuilder;
        class GovernmentSecurityInformationBuilderImpl;
        /** Represents a @link Annotations::GovernmentSecurityInformation Annotations::GovernmentSecurityInformation@endlink  builder  <br> To create a new instance of this class, use @link Annotations::PmiAttributeCollection::CreateGovernmentSecurityInformationBuilder Annotations::PmiAttributeCollection::CreateGovernmentSecurityInformationBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  GovernmentSecurityInformationBuilder : public Annotations::PmiAttributeBuilder
        {
            private: GovernmentSecurityInformationBuilderImpl * m_governmentsecurityinformationbuilder_impl;
            private: friend class  _GovernmentSecurityInformationBuilderBuilder;
            protected: GovernmentSecurityInformationBuilder();
            public: ~GovernmentSecurityInformationBuilder();
            /**Returns  the str title  <br> License requirements : None */
            public: NXString Title
            (
            );
            /**Sets  the str title  <br> License requirements : None */
            public: void SetTitle
            (
                const NXString & title /** title */ 
            );
            /**Returns  the identifier  <br> License requirements : None */
            public: NXString Identifier
            (
            );
            /**Sets  the identifier  <br> License requirements : None */
            public: void SetIdentifier
            (
                const NXString & identifier /** identifier */ 
            );
            /** Returns the str text  @return   <br> License requirements : None */
            public: std::vector<NXString> GetStringText
            (
            );
            /** Sets the str text  <br> License requirements : None */
            public: void SetStringText
            (
                const std::vector<NXString> & stringText /** stringtext */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif