#ifndef NXOpen_FEATURES_SHEETMETAL_JOGGLESIDEOPTIONSBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_JOGGLESIDEOPTIONSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_JoggleSideOptionsBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class JoggleSideOptionsBuilder;
        }
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class _JoggleSideOptionsBuilderBuilder;
            class JoggleSideOptionsBuilderImpl;
            /** Represents a Sheetmetal Joggle side Options class. 
             <br>  Created in NX11.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  JoggleSideOptionsBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
            {
                private: JoggleSideOptionsBuilderImpl * m_jogglesideoptionsbuilder_impl;
                private: friend class  _JoggleSideOptionsBuilderBuilder;
                protected: JoggleSideOptionsBuilder();
                public: ~JoggleSideOptionsBuilder();
                /**Returns  the runout 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                public: NXOpen::Expression * Runout
                (
                );
                /**Returns  the clearance 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                public: NXOpen::Expression * Clearance
                (
                );
                /**Returns  the stationary radius 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                public: NXOpen::Expression * StationaryRadius
                (
                );
                /**Returns  the offset radius 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                public: NXOpen::Expression * OffsetRadius
                (
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