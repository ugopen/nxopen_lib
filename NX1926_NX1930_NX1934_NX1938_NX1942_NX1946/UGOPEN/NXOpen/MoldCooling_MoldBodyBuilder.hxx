#ifndef NXOpen_MOLDCOOLING_MOLDBODYBUILDER_HXX_INCLUDED
#define NXOpen_MOLDCOOLING_MOLDBODYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MoldCooling_MoldBodyBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_moldcooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace MoldCooling
    {
        class MoldBodyBuilder;
    }
    class Builder;
    class PhysicalMaterial;
    class SelectBodyList;
    namespace MoldCooling
    {
        class _MoldBodyBuilderBuilder;
        class MoldBodyBuilderImpl;
        /** Represents a @link MoldCooling::MoldBodyBuilder MoldCooling::MoldBodyBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::MoldCooling::Manager::CreateMoldBodyBuilder  NXOpen::MoldCooling::Manager::CreateMoldBodyBuilder @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_MOLDCOOLINGEXPORT  MoldBodyBuilder : public NXOpen::Builder
        {
            private: MoldBodyBuilderImpl * m_moldbodybuilder_impl;
            private: friend class  _MoldBodyBuilderBuilder;
            protected: MoldBodyBuilder();
            public: ~MoldBodyBuilder();
            /**Returns  the cavity bodies selection 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBodyList * SelectCavityBodies
            (
            );
            /**Returns  the core bodies selection 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBodyList * SelectCoreBodies
            (
            );
            /**Returns  the selected material for the mold cavity 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PhysicalMaterial * CavityMaterial
            (
            );
            /**Sets  the selected material for the mold cavity 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_mold_cool_basic (" NX Mold Cooling Application") */
            public: void SetCavityMaterial
            (
                NXOpen::PhysicalMaterial * cavityMaterial /** cavitymaterial */ 
            );
            /**Returns  the selected material for the mold core 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PhysicalMaterial * CoreMaterial
            (
            );
            /**Sets  the selected material for the mold core 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_mold_cool_basic (" NX Mold Cooling Application") */
            public: void SetCoreMaterial
            (
                NXOpen::PhysicalMaterial * coreMaterial /** corematerial */ 
            );
            /**Returns  the part bodies selection 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBodyList * SelectPartBodies
            (
            );
            /**Returns  the selected material for the mold part 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PhysicalMaterial * PartMaterial
            (
            );
            /**Sets  the selected material for the mold part 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_mold_cool_basic (" NX Mold Cooling Application") */
            public: void SetPartMaterial
            (
                NXOpen::PhysicalMaterial * partMaterial /** partmaterial */ 
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
