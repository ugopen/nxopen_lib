#ifndef NXOpen_MPA_PREFERENCESARROWCONNECTIONBUILDER_HXX_INCLUDED
#define NXOpen_MPA_PREFERENCESARROWCONNECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MPA_PreferencesArrowConnectionBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libmpaopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace MPA
    {
        class PreferencesArrowConnectionBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace MPA
    {
        class _PreferencesArrowConnectionBuilderBuilder;
        class PreferencesArrowConnectionBuilderImpl;
        /** Represents a PreferencesArrowConnectionBuilder which controls size, style of arrows in physical Diagram 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class MPAOPENCPPEXPORT  PreferencesArrowConnectionBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** Enum that represents ..the Arrow Style of Connection on sheet */
            public: enum Styles
            {
                StylesClosed/** closed*/,
                StylesCloseddouble/** closed Double  */,
                StylesCloseddoublesolid/** closed double solid  */,
                StylesClosedsolid/** closed solid  */,
                StylesFilled/**  filled  */,
                StylesFilleddouble/**  filled double  */,
                StylesOpen/**  open  */,
                StylesOpendouble/** open double  */
            };

            private: PreferencesArrowConnectionBuilderImpl * m_preferencesarrowconnectionbuilder_impl;
            private: friend class  _PreferencesArrowConnectionBuilderBuilder;
            protected: PreferencesArrowConnectionBuilder();
            public: ~PreferencesArrowConnectionBuilder();
            /**Returns  the value of arrow size for connection of MPA diagram  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double ArrowSize
            (
            );
            /**Sets  the value of arrow size for connection of MPA diagram  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_sdpd_pam_a (" NX Physical Architecture Diagram Author") */
            public: void SetArrowSize
            (
                double size /** size */ 
            );
            /**Returns  the arrow style for connection of MPA diagram 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: int ArrowStyle
            (
            );
            /**Sets  the arrow style for connection of MPA diagram 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_sdpd_pam_a (" NX Physical Architecture Diagram Author") */
            public: void SetArrowStyle
            (
                int style /** style */ 
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not yet implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
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