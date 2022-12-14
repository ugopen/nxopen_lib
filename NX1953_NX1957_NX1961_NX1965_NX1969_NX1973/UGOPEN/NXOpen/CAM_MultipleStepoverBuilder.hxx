#ifndef NXOpen_CAM_MULTIPLESTEPOVERBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MULTIPLESTEPOVERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MultipleStepoverBuilder.ja
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
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class MultipleStepoverBuilder;
    }
    class Builder;
    namespace CAM
    {
        class _MultipleStepoverBuilderBuilder;
        class MultipleStepoverBuilderImpl;
        /** Represents a Builder which holds the data for a set of individual number of passes and 
                stepover distance.  <br> This is an abstract class and cannot be instantiated.  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  MultipleStepoverBuilder : public NXOpen::Builder
        {
            private: MultipleStepoverBuilderImpl * m_multiplestepoverbuilder_impl;
            private: friend class  _MultipleStepoverBuilderBuilder;
            protected: MultipleStepoverBuilder();
            public: ~MultipleStepoverBuilder();
            /** Add a new item 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void Add
            (
                int indexAfter /** the index which new item will be added after */,
                int numOfPasses /** the num of passes for new item */,
                double distance /** the distance for new item */,
                int intent /** the intent for new item */
            );
            /** Modify item 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void Modify
            (
                int index /** the index of item to be modified */,
                int numOfPasses /** the new value of num of passes */,
                double distance /** the new value of distance */,
                int intent /** the new value of intent */
            );
            /** Delete a item 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void Delete
            (
                int index /** the index of item to be deleted */
            );
            /** Move up a item 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void MoveUp
            (
                int index /** the index of item to be moved up */
            );
            /** Move down a item 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void MoveDown
            (
                int index /** the index of item to be moved down */
            );
            /** Get number of stepovers  @return  the number of stepover 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: int GetNumberOfStepovers
            (
            );
            /** Get item for the specified stepover index
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void GetData
            (
                int index /** the index of item to be modified */,
                int* numOfPasses /** the new value of num of passes */,
                double* distance /** the new value of distance */,
                int* intent /** the new value of intent */
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
