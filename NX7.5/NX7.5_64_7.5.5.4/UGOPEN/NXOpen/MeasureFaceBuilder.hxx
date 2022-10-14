#ifndef NXOpen_MEASUREFACEBUILDER_HXX_INCLUDED
#define NXOpen_MEASUREFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MeasureFaceBuilder.ja
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
#include <NXOpen/MeasureBuilder.hxx>
#include <NXOpen/MeasureFaceBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class MeasureFaceBuilder;
    class MeasureBuilder;
    class SelectDisplayableObjectList;
    class _MeasureFaceBuilderBuilder;
    class MeasureFaceBuilderImpl;
    /**
    Represents a @link MeasureFaceBuilder MeasureFaceBuilder@endlink 
     <br> To create a new instance of this class, use @link MeasureManager::CreateMeasureFaceBuilder MeasureManager::CreateMeasureFaceBuilder@endlink  <br> */
    class NXOPENCPPEXPORT  MeasureFaceBuilder : public MeasureBuilder
    {
        private: MeasureFaceBuilderImpl * m_measurefacebuilder_impl;
        private: friend class  _MeasureFaceBuilderBuilder;
        protected: MeasureFaceBuilder();
        public: ~MeasureFaceBuilder();
        /**Returns  the face objects  <br> License requirements : None */
        public: NXOpen::SelectDisplayableObjectList * FaceObjects
        (
        );
    };
}
#undef EXPORTLIBRARY
#endif