#ifndef NXOpen_SKETCHEXPRESSIONMODIFIERBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHEXPRESSIONMODIFIERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchExpressionModifierBuilder.ja
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
#include <NXOpen/SketchExpressionModifierBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class SketchExpressionModifierBuilder;
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class Sketch;
    class _SketchExpressionModifierBuilderBuilder;
    class SketchExpressionModifierBuilderImpl;
    /** Represents a Sketch Expression Modifier Builder. */
    class NXOPENCPPEXPORT  SketchExpressionModifierBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
    {
        /** End cut */
        public: enum EndCuts
        {
            EndCutsEndCut1/** end cut1 */ ,
            EndCutsEndCut2/** end cut2 */ 
        };

        private: SketchExpressionModifierBuilderImpl * m_sketchexpressionmodifierbuilder_impl;
        private: friend class  _SketchExpressionModifierBuilderBuilder;
        protected: SketchExpressionModifierBuilder();
        public: ~SketchExpressionModifierBuilder();
        /**Returns  the sketches  <br> License requirements : None */
        public: NXOpen::SketchExpressionModifierBuilder::EndCuts Sketches
        (
        );
        /**Sets  the sketches  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetSketches
        (
            NXOpen::SketchExpressionModifierBuilder::EndCuts sketches /** sketches */ 
        );
        /**Returns  the exp1  <br> License requirements : None */
        public: NXOpen::Expression * Exp1
        (
        );
        /**Returns  the exp2  <br> License requirements : None */
        public: NXOpen::Expression * Exp2
        (
        );
        /**Returns  the exp3  <br> License requirements : None */
        public: NXOpen::Expression * Exp3
        (
        );
        /**Returns  the exp4  <br> License requirements : None */
        public: NXOpen::Expression * Exp4
        (
        );
        /**Returns  the exp5  <br> License requirements : None */
        public: NXOpen::Expression * Exp5
        (
        );
        /**Returns  the exp6  <br> License requirements : None */
        public: NXOpen::Expression * Exp6
        (
        );
        /**Returns  the exp7  <br> License requirements : None */
        public: NXOpen::Expression * Exp7
        (
        );
        /**Returns  the exp8  <br> License requirements : None */
        public: NXOpen::Expression * Exp8
        (
        );
        /**Returns  the exp9  <br> License requirements : None */
        public: NXOpen::Expression * Exp9
        (
        );
        /**Returns  the exp10  <br> License requirements : None */
        public: NXOpen::Expression * Exp10
        (
        );
        /**Returns  the exp11  <br> License requirements : None */
        public: NXOpen::Expression * Exp11
        (
        );
        /**Returns  the exp12  <br> License requirements : None */
        public: NXOpen::Expression * Exp12
        (
        );
        /**Returns  the sketch  <br> License requirements : None */
        public: NXOpen::Sketch * Sketch
        (
        );
        /**Sets  the sketch  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetSketch
        (
            NXOpen::Sketch * sketchTag /** sketchtag */ 
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
#undef EXPORTLIBRARY
#endif
