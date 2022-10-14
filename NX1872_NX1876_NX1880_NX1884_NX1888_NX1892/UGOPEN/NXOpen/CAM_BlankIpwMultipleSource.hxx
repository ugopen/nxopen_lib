#ifndef NXOpen_CAM_BLANKIPWMULTIPLESOURCE_HXX_INCLUDED
#define NXOpen_CAM_BLANKIPWMULTIPLESOURCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_BlankIpwMultipleSource.ja
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
#include <NXOpen/CAM_BlankIpwSet.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ObjectList.hxx>
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
        class BlankIpwMultipleSource;
    }
    namespace CAM
    {
        class BlankIpwSet;
    }
    namespace CAM
    {
        class BlankIpwSetList;
    }
    namespace CAM
    {
        class _BlankIpwMultipleSourceBuilder;
        class BlankIpwMultipleSourceImpl;
        /** represents the blank IPW builder for blank definition  <br> To obtain an instance of this class use the @link NXOpen::CAM::GeometryGroup NXOpen::CAM::GeometryGroup@endlink   <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  BlankIpwMultipleSource : public NXOpen::TaggedObject
        {
            /** the blank IPW status types */
            public: enum StatusTypes
            {
                StatusTypesUpToDate/** blank ipw status up to date*/,
                StatusTypesOutOfDate/** blank ipw status out of date */,
                StatusTypesUnableToUpdate/** blank ipw status unable to update */,
                StatusTypesNone/** blank ipw status none */,
                StatusTypesUnknown/** blank ipw status unknown */
            };

            private: BlankIpwMultipleSourceImpl * m_blankipwmultiplesource_impl;
            private: friend class  _BlankIpwMultipleSourceBuilder;
            protected: BlankIpwMultipleSource();
            public: ~BlankIpwMultipleSource();
            /** Updates the blank IPW  @return  the blank ipw status 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::BlankIpwMultipleSource::StatusTypes Update
            (
            );
            /**Returns  the blank IPW list 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BlankIpwSetList * SetList
            (
            );
            /** Creates an empty blank IPW set @return  the blank ipw set object 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::BlankIpwSet * CreateBlankIpwSet
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