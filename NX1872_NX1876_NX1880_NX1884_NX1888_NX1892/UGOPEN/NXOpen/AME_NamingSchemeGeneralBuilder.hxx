#ifndef NXOpen_AME_NAMINGSCHEMEGENERALBUILDER_HXX_INCLUDED
#define NXOpen_AME_NAMINGSCHEMEGENERALBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_NamingSchemeGeneralBuilder.ja
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
#include <NXOpen/Builder.hxx>
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
        class NamingSchemeGeneralBuilder;
    }
    class Builder;
    namespace AME
    {
        class _NamingSchemeGeneralBuilderBuilder;
        class NamingSchemeGeneralBuilderImpl;
        /**
                JA class for Naming Scheme General Builder
             <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateNamingSchemeGeneralBuilder  NXOpen::AME::AMEManager::CreateNamingSchemeGeneralBuilder @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  NamingSchemeGeneralBuilder : public NXOpen::Builder
        {
            /** represents delimiter type */
            public: enum DelimiterType
            {
                DelimiterTypeDot/** A dot (.) is used as the delimiter */,
                DelimiterTypeAspectPrefix/** Aspect Prefix is used as the delimiter */,
                DelimiterTypeNoDelimiter/** No delimiter will be used */
            };

            private: NamingSchemeGeneralBuilderImpl * m_namingschemegeneralbuilder_impl;
            private: friend class  _NamingSchemeGeneralBuilderBuilder;
            protected: NamingSchemeGeneralBuilder();
            public: ~NamingSchemeGeneralBuilder();
            /**Returns  the aspect prefix of function aspect 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString Function
            (
            );
            /**Sets  the aspect prefix of function aspect 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetFunction
            (
                const NXString & functionPrefix /** functionprefix */ 
            );
            /**Sets  the aspect prefix of function aspect 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetFunction
            (
                const char * functionPrefix /** functionprefix */ 
            );
            /**Returns  the aspect prefix of location aspect 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString Location
            (
            );
            /**Sets  the aspect prefix of location aspect 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetLocation
            (
                const NXString & location /** location */ 
            );
            /**Sets  the aspect prefix of location aspect 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetLocation
            (
                const char * location /** location */ 
            );
            /**Returns  the aspect prefix of product aspect 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString Product
            (
            );
            /**Sets  the aspect prefix of product aspect 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetProduct
            (
                const NXString & product /** product */ 
            );
            /**Sets  the aspect prefix of product aspect 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetProduct
            (
                const char * product /** product */ 
            );
            /**Returns  the @link NXOpen::AME::NamingSchemeGeneralBuilder::DelimiterType NXOpen::AME::NamingSchemeGeneralBuilder::DelimiterType@endlink  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::NamingSchemeGeneralBuilder::DelimiterType Delimiter
            (
            );
            /**Sets  the @link NXOpen::AME::NamingSchemeGeneralBuilder::DelimiterType NXOpen::AME::NamingSchemeGeneralBuilder::DelimiterType@endlink  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetDelimiter
            (
                NXOpen::AME::NamingSchemeGeneralBuilder::DelimiterType delimiter /** delimiter */ 
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
