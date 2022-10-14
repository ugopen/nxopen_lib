#ifndef NXOpen_AME_SNAP3DMODELSBUILDER_HXX_INCLUDED
#define NXOpen_AME_SNAP3DMODELSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_Snap3DModelsBuilder.ja
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
#include <NXOpen/AME_SelectMountingInterfaceLocationBuilder.hxx>
#include <NXOpen/AME_AMEBaseBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class Snap3DModelsBuilder;
    }
    namespace AME
    {
        class AMEBaseBuilder;
    }
    namespace AME
    {
        class SelectMountingInterfaceLocationBuilder;
    }
    class SelectTaggedObjectList;
    namespace AME
    {
        class _Snap3DModelsBuilderBuilder;
        class Snap3DModelsBuilderImpl;
        /** Represents a Snap3DModelsBuilder class Builder   <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateSnap3dmodelsBuilder  NXOpen::AME::AMEManager::CreateSnap3dmodelsBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  Snap3DModelsBuilder : public NXOpen::AME::AMEBaseBuilder
        {
            private: Snap3DModelsBuilderImpl * m_snap3dmodelsbuilder_impl;
            private: friend class  _Snap3DModelsBuilderBuilder;
            protected: Snap3DModelsBuilder();
            public: ~Snap3DModelsBuilder();
            /**Returns  the Target node selection 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::SelectTaggedObjectList * Select3dModel
            (
            );
            /**Returns  the co-ordinate of target location
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectMountingInterfaceLocationBuilder * SelectMountingInterfaceLocation
            (
            );
            /**Sets  the co-ordinate of target location
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetSelectMountingInterfaceLocation
            (
                NXOpen::AME::SelectMountingInterfaceLocationBuilder * targetLocation /** targetlocation */ 
            );
            /**Returns  the fixingInterface of selected product
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString FixingInterface
            (
            );
            /**Sets  the fixingInterface of selected product
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetFixingInterface
            (
                const NXString & fixingInterface /** fixinginterface */ 
            );
            /**Sets  the fixingInterface of selected product
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetFixingInterface
            (
                const char * fixingInterface /** fixinginterface */ 
            );
            /** Update product 3d model preview
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void UpdateProduct3DModelPreview
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