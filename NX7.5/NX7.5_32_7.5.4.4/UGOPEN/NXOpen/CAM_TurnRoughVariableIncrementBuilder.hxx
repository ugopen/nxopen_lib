#ifndef NXOpen_CAM_TURNROUGHVARIABLEINCREMENTBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TURNROUGHVARIABLEINCREMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_TurnRoughVariableIncrementBuilder.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class TurnRoughVariableIncrementBuilder;
    }
    namespace CAM
    {
        class _TurnRoughVariableIncrementBuilderBuilder;
        class TurnRoughVariableIncrementBuilderImpl;
        /** Represents a Variable Increment Builder */
        class NXOPENCPPEXPORT  TurnRoughVariableIncrementBuilder : public TaggedObject
        {
            private: TurnRoughVariableIncrementBuilderImpl * m_turnroughvariableincrementbuilder_impl;
            private: friend class  _TurnRoughVariableIncrementBuilderBuilder;
            protected: TurnRoughVariableIncrementBuilder();
            public: ~TurnRoughVariableIncrementBuilder();
            /** Add a new item  <br> License requirements : cam_base ("CAM BASE") */
            public: void Add
            (
                int index /** the index which new item will be added after */,
                int numOfPasses /** the num of passes */,
                double increment /** the increment */
            );
            /** Modify a selected item  <br> License requirements : cam_base ("CAM BASE") */
            public: void Modify
            (
                int index /** the index of selected item */,
                int numOfPasses /** the num of passes */,
                double increment /** the increment */
            );
            /** Delete a selected item  <br> License requirements : cam_base ("CAM BASE") */
            public: void Delete
            (
                int index /** the index of selected item */
            );
            /** Move up a selected item  <br> License requirements : cam_base ("CAM BASE") */
            public: void MoveUp
            (
                int index /** the index of selected item */
            );
            /** Move down a selected item  <br> License requirements : cam_base ("CAM BASE") */
            public: void MoveDown
            (
                int index /** the index of selected item */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
