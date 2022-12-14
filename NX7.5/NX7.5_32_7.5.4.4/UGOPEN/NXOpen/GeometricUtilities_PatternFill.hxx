#ifndef NXOpen_GEOMETRICUTILITIES_PATTERNFILL_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_PATTERNFILL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_PatternFill.ja
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
#include <NXOpen/GeometricUtilities_PatternFill.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class PatternFill;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class Section;
    namespace GeometricUtilities
    {
        class _PatternFillBuilder;
        class PatternFillImpl;
        /** the pattern fill definition.  Allows to speicify a section boundary with an offset margin. */
        class NXOPENCPPEXPORT  PatternFill : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /** This defines Fill Types */
            public: enum PatternFillOptions
            {
                PatternFillOptionsNone/** no section is defined */,
                PatternFillOptionsFillbyFace/** section is face-based, and for fill area. */,
                PatternFillOptionsFillbyBoundary/** section is for fill area.  */,
                PatternFillOptionsExcludeAreaOnly/** section is for exclude area only */
            };

            private: PatternFillImpl * m_patternfill_impl;
            private: friend class  _PatternFillBuilder;
            protected: PatternFill();
            public: ~PatternFill();
            /**Returns  the fill options  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::PatternFill::PatternFillOptions FillOptions
            (
            );
            /**Sets  the fill options  <br> License requirements : None */
            public: void SetFillOptions
            (
                NXOpen::GeometricUtilities::PatternFill::PatternFillOptions fillOptions /** filloptions */ 
            );
            /**Returns  the fill boundary  <br> License requirements : None */
            public: NXOpen::Section * FillBoundary
            (
            );
            /**Returns  the face boundary  <br> License requirements : None */
            public: NXOpen::Section * FaceBoundary
            (
            );
            /**Returns  the fill margin  <br> License requirements : None */
            public: NXOpen::Expression * FillMargin
            (
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : None */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
