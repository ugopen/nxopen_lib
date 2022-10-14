#ifndef NXOpen_PRESSLINESIMULATION_MOUNTPOINTBUILDER_HXX_INCLUDED
#define NXOpen_PRESSLINESIMULATION_MOUNTPOINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PressLineSimulation_MountPointBuilder.ja
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
#include <NXOpen/libpresslinesimulopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PressLineSimulation
    {
        class MountPointBuilder;
    }
    class Builder;
    class NXObject;
    namespace PressLineSimulation
    {
        class _MountPointBuilderBuilder;
        class MountPointBuilderImpl;
        /** Use this class to mount tools, tooling and parts to interfaces. 
             <br> To create a new instance of this class, use @link NXOpen::PressLineSimulation::ApplicationManager::CreateMountPointBuilder  NXOpen::PressLineSimulation::ApplicationManager::CreateMountPointBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class PRESSLINESIMULOPENCPPEXPORT  MountPointBuilder : public NXOpen::Builder
        {
            /**  @brief  Selection filter for mounting bodies. 

             
                     Use this enum in conjunction with @link PressLineSimulation::MountPointBuilder::SelectionFilter PressLineSimulation::MountPointBuilder::SelectionFilter @endlink and @link PressLineSimulation::MountPointBuilder::SetSelectionFilter PressLineSimulation::MountPointBuilder::SetSelectionFilter @endlink  to 
                    filter the selectable items that should be mounted.*/
            public: enum GeometrySelectionFilterType
            {
                GeometrySelectionFilterTypeOnlyUnmounted/** Only bodies that are not mounted can be selected.*/,
                GeometrySelectionFilterTypeAll/** Everything can be selected.*/
            };

            private: MountPointBuilderImpl * m_mountpointbuilder_impl;
            private: friend class  _MountPointBuilderBuilder;
            protected: MountPointBuilder();
            public: ~MountPointBuilder();
            /**Returns  the geometry selection filter 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PressLineSimulation::MountPointBuilder::GeometrySelectionFilterType SelectionFilter
            (
            );
            /**Sets  the geometry selection filter 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_pls_die_checker (" NX Press Die Checker") OR nx_pls_line_setup (" NX Press Line Setup") */
            public: void SetSelectionFilter
            (
                NXOpen::PressLineSimulation::MountPointBuilder::GeometrySelectionFilterType selectionFilter /** selectionfilter */ 
            );
            /** Returns the display names of the press model line component that the mount point is associated with. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetLineComponentName
            (
            );
            /** Returns the display name of the press model mount point. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetMountPointName
            (
            );
            /** Returns the geometry that will be mounted on commit. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::NXObject *> GetMountedGeometry
            (
            );
            /** Adds to the list of geometry that is mounted on commit. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_pls_die_checker (" NX Press Die Checker") OR nx_pls_line_setup (" NX Press Line Setup") */
            public: bool MountGeometry
            (
                NXOpen::NXObject * geometry /** geometry */ 
            );
            /** Adds to the list of geometry that is unmounted on commit. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_pls_die_checker (" NX Press Die Checker") OR nx_pls_line_setup (" NX Press Line Setup") */
            public: bool UnMountGeometry
            (
                NXOpen::NXObject * geometry /** geometry */ 
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