#ifndef NXOpen_DRAWINGS_HINGELINEBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_HINGELINEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_HingeLineBuilder.ja
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
#include <NXOpen/Drawings_HingeLineBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class HingeLineBuilder;
    }
    class Direction;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Drawings
    {
        class _HingeLineBuilderBuilder;
        class HingeLineBuilderImpl;
        /**
            Represents a Drawings.HingeLineBuilder. A hinge line is a line displayed on the parent 
            view and used as a reference to rotate a child view in proper orthographic space.
            */
        class NXOPENCPPEXPORT  HingeLineBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /** Specifies the hinge line vector option */
            public: enum Hingeline
            {
                HingelineInferred/** The option to infer a hinge line based on parent, child view position */,
                HingelineDefined/** The option for selecting hinge line using vector construction tools */
            };

            private: HingeLineBuilderImpl * m_hingelinebuilder_impl;
            private: friend class  _HingeLineBuilderBuilder;
            protected: HingeLineBuilder();
            public: ~HingeLineBuilder();
            /**Returns  the vector option: Inferred or Defined  <br> License requirements : None */
            public: NXOpen::Drawings::HingeLineBuilder::Hingeline VectorOption
            (
            );
            /**Sets  the vector option: Inferred or Defined  <br> License requirements : None */
            public: void SetVectorOption
            (
                NXOpen::Drawings::HingeLineBuilder::Hingeline vectorOption /** vectoroption */ 
            );
            /**Returns  the direction for the hinge line  <br> License requirements : None */
            public: NXOpen::Direction * SpecifyVector
            (
            );
            /**Sets  the direction for the hinge line  <br> License requirements : None */
            public: void SetSpecifyVector
            (
                NXOpen::Direction * specifyVector /** specifyvector */ 
            );
            /**Returns  the reverse direction setting  <br> License requirements : None */
            public: bool ReverseDirection
            (
            );
            /**Sets  the reverse direction setting  <br> License requirements : None */
            public: void SetReverseDirection
            (
                bool reverseDirection /** reversedirection */ 
            );
            /**Returns  the infer associative setting  <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the infer associative setting  <br> License requirements : None */
            public: void SetAssociative
            (
                bool associative /** associative */ 
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