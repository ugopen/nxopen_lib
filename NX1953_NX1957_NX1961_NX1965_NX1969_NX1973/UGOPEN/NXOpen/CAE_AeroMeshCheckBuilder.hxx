#ifndef NXOpen_CAE_AEROMESHCHECKBUILDER_HXX_INCLUDED
#define NXOpen_CAE_AEROMESHCHECKBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AeroMeshCheckBuilder.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/NXColor.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class AeroMeshCheckBuilder;
    }
    class Builder;
    class NXColor;
    class SelectTaggedObjectList;
    namespace CAE
    {
        class _AeroMeshCheckBuilderBuilder;
        class AeroMeshCheckBuilderImpl;
        /** Represents a @link NXOpen::CAE::AeroMeshCheckBuilder NXOpen::CAE::AeroMeshCheckBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateAeroMeshCheckBuilder  NXOpen::CAE::ModelCheckManager::CreateAeroMeshCheckBuilder @endlink  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  AeroMeshCheckBuilder : public NXOpen::Builder
        {
            /** the option indicates the check scope for a aero mesh check command */
            public: enum Scope
            {
                ScopeDisplayed/** check all displayed aero meshes */,
                ScopeSelected/** check selected aero meshes */
            };

             /** Represents the display settings of incorrect aero meshes detected */
            public:
            struct DisplaySettings
            {
                public: /** Whether to show incorrect aero meshes */bool ShowIncorrectMeshes;
                public: /** The display color of incorrect meshes */NXColor* MeshColor;
                public: /** The display line width of incorrect meshes */NXOpen::DisplayableObject::ObjectWidth MeshWidth;
                public: DisplaySettings() :
                    ShowIncorrectMeshes(),
                    MeshColor(),
                    MeshWidth((NXOpen::DisplayableObject::ObjectWidth)0)
                {
                }
                /** Constructor for the DisplaySettings struct. */ 
                public: DisplaySettings(bool showIncorrectMeshesInitial /** Whether to show incorrect aero meshes */, 
                        NXColor* meshColorInitial /** The display color of incorrect meshes */, 
                        NXOpen::DisplayableObject::ObjectWidth meshWidthInitial /** The display line width of incorrect meshes */) :
                    ShowIncorrectMeshes(showIncorrectMeshesInitial),
                    MeshColor(meshColorInitial),
                    MeshWidth(meshWidthInitial)
                {
                }
            };

            private: AeroMeshCheckBuilderImpl * m_aeromeshcheckbuilder_impl;
            private: friend class  _AeroMeshCheckBuilderBuilder;
            protected: AeroMeshCheckBuilder();
            public: ~AeroMeshCheckBuilder();
            /**Returns  the selected objects to be checked. The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink   
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectTaggedObjectList * MeshSelection
            (
            );
            /**Returns  the scope of selection for aero mesh checking 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::AeroMeshCheckBuilder::Scope CheckScope
            (
            );
            /**Sets  the scope of selection for aero mesh checking 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetCheckScope
            (
                NXOpen::CAE::AeroMeshCheckBuilder::Scope checkScope /** Check scope option  */
            );
            /**Returns  the display settings for incorrect aero meshes 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::AeroMeshCheckBuilder::DisplaySettings DisplaySettingsData
            (
            );
            /**Sets  the display settings for incorrect aero meshes 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetDisplaySettingsData
            (
                const NXOpen::CAE::AeroMeshCheckBuilder::DisplaySettings & displaySettings /** Display settings data */
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
