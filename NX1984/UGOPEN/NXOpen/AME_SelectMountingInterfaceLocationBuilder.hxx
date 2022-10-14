#ifndef NXOpen_AME_SELECTMOUNTINGINTERFACELOCATIONBUILDER_HXX_INCLUDED
#define NXOpen_AME_SELECTMOUNTINGINTERFACELOCATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_SelectMountingInterfaceLocationBuilder.ja
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
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libameopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        class SelectMountingInterfaceLocationBuilder;
    }
    class Builder;
    class NXObject;
    namespace AME
    {
        class _SelectMountingInterfaceLocationBuilderBuilder;
        class SelectMountingInterfaceLocationBuilderImpl;
        /** Builder for selecting mounting interface location from graphics window <br> This object does not need a creator  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  SelectMountingInterfaceLocationBuilder : public NXOpen::Builder
        {
            private: SelectMountingInterfaceLocationBuilderImpl * m_selectmountinginterfacelocationbuilder_impl;
            private: friend class  _SelectMountingInterfaceLocationBuilderBuilder;
            protected: SelectMountingInterfaceLocationBuilder();
            public: ~SelectMountingInterfaceLocationBuilder();
            /**Returns  the co-ordinate of fixing placement location
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::Point3d FixingPlacementLocation
            (
            );
            /**Sets  the co-ordinate of fixing placement location
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetFixingPlacementLocation
            (
                const NXOpen::Point3d & targetLocation /** targetlocation */ 
            );
            /**Returns  the tag of selected receptacle object
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::NXObject * SelectedReceptacleObject
            (
            );
            /**Sets  the tag of selected receptacle object
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetSelectedReceptacleObject
            (
                NXOpen::NXObject * selectedObjectTag /** selectedobjecttag */ 
            );
            /**Returns  the logical value whether location is selected
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: bool IsLocationSelected
            (
            );
            /**Sets  the logical value whether location is selected
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetLocationSelected
            (
                bool locationSelectedObject /** locationselectedobject */ 
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