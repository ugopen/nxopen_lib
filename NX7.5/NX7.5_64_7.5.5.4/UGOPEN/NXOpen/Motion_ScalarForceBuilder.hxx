#ifndef NXOpen_MOTION_SCALARFORCEBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_SCALARFORCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_ScalarForceBuilder.ja
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
#include <NXOpen/Motion.hxx>
#include <NXOpen/Motion_MotionBuilder.hxx>
#include <NXOpen/Motion_ScalarForceBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class ScalarForceBuilder;
    }
    namespace CAE
    {
        class Function;
    }
    namespace Motion
    {
        class MotionBuilder;
    }
    namespace Motion
    {
        class SelectLink;
    }
    class Point;
    namespace Motion
    {
        class _ScalarForceBuilderBuilder;
        class ScalarForceBuilderImpl;
        /**Represents a @link Motion::ScalarForceBuilder Motion::ScalarForceBuilder@endlink  <br> To create a new instance of this class, use @link Motion::ScalarForceCollection::CreateScalarForceBuilder Motion::ScalarForceCollection::CreateScalarForceBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  ScalarForceBuilder : public Motion::MotionBuilder
        {
            private: ScalarForceBuilderImpl * m_scalarforcebuilder_impl;
            private: friend class  _ScalarForceBuilderBuilder;
            protected: ScalarForceBuilder();
            public: ~ScalarForceBuilder();
            /**Returns  the action link  <br> License requirements : None */
            public: NXOpen::Motion::SelectLink * ActionLink
            (
            );
            /**Returns  the action point  <br> License requirements : None */
            public: NXOpen::Point * ActionPoint
            (
            );
            /**Sets  the action point  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetActionPoint
            (
                NXOpen::Point * actionPoint /** actionpoint */ 
            );
            /**Returns  the reaction link  <br> License requirements : None */
            public: NXOpen::Motion::SelectLink * ReactionLink
            (
            );
            /**Returns  the reaction point  <br> License requirements : None */
            public: NXOpen::Point * ReactionPoint
            (
            );
            /**Sets  the reaction point  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetReactionPoint
            (
                NXOpen::Point * reactionPoint /** reactionpoint */ 
            );
            /**Returns  the value type  <br> License requirements : None */
            public: NXOpen::Motion::ForceValueTypes ValueType
            (
            );
            /**Sets  the value type  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetValueType
            (
                NXOpen::Motion::ForceValueTypes valueType /** valuetype */ 
            );
            /**Returns  the constant value  <br> License requirements : None */
            public: double ConstantValue
            (
            );
            /**Sets  the constant value  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetConstantValue
            (
                double constantValue /** constantvalue */ 
            );
            /**Returns  the function   <br> License requirements : None */
            public: NXOpen::CAE::Function * Function
            (
            );
            /**Sets  the function   <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFunction
            (
                NXOpen::CAE::Function * function /** function */ 
            );
            /**Returns  the name  <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif