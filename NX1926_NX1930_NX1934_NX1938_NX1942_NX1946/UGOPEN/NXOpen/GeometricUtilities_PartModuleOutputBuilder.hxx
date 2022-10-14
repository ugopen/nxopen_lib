#ifndef NXOpen_GEOMETRICUTILITIES_PARTMODULEOUTPUTBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_PARTMODULEOUTPUTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_PartModuleOutputBuilder.ja
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
#include <NXOpen/GeometricUtilities_PartModuleReferencesBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class PartModuleOutputBuilder;
    }
    class Builder;
    namespace GeometricUtilities
    {
        class PartModuleReferencesBuilder;
    }
    namespace GeometricUtilities
    {
        class _PartModuleOutputBuilderBuilder;
        class PartModuleOutputBuilderImpl;
        /** Represents a @link NXOpen::GeometricUtilities::PartModuleOutputBuilder NXOpen::GeometricUtilities::PartModuleOutputBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::Features::PartModule::CreatePartModuleOutputBuilder  NXOpen::Features::PartModule::CreatePartModuleOutputBuilder @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  PartModuleOutputBuilder : public NXOpen::Builder
        {
            private: PartModuleOutputBuilderImpl * m_partmoduleoutputbuilder_impl;
            private: friend class  _PartModuleOutputBuilderBuilder;
            protected: PartModuleOutputBuilder();
            public: ~PartModuleOutputBuilder();
            /**Returns  the part module output data 
                      <br> 
                     This API is now deprecated.
                     Please use @link NXOpen::GeometricUtilities::PartModuleOutputBuilder1::OutputReferences1 NXOpen::GeometricUtilities::PartModuleOutputBuilder1::OutputReferences1@endlink  instead.
                      <br> 
                    
             <br>  @deprecated Deprecated in NX9.0.0.  Please use @link NXOpen::GeometricUtilities::PartModuleOutputBuilder1::OutputReferences1 NXOpen::GeometricUtilities::PartModuleOutputBuilder1::OutputReferences1@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX9.0.0.  Please use NXOpen::GeometricUtilities::PartModuleOutputBuilder1::OutputReferences1 instead.") NXOpen::GeometricUtilities::PartModuleReferencesBuilder * OutputReferences
            (
            );
            /**Returns  the option indicating whether the part module is to be deactivated. If true, the part module will be deactivated, else, no action is taken
                      <br> 
                     This API is now deprecated.
                     Please use @link NXOpen::Features::PartModule::Activate NXOpen::Features::PartModule::Activate@endlink  instead.
                      <br> 
                    
             <br>  @deprecated Deprecated in NX9.0.0.  Please use @link NXOpen::Features::PartModule::Activate NXOpen::Features::PartModule::Activate@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX9.0.0.  Please use NXOpen::Features::PartModule::Activate instead.") bool Deactivate
            (
            );
            /**Sets  the option indicating whether the part module is to be deactivated. If true, the part module will be deactivated, else, no action is taken
                      <br> 
                     This API is now deprecated.
                     Please use @link NXOpen::Features::PartModule::Activate NXOpen::Features::PartModule::Activate@endlink  instead.
                      <br> 
                    
             <br>  @deprecated Deprecated in NX9.0.0.  Please use @link NXOpen::Features::PartModule::Activate NXOpen::Features::PartModule::Activate@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NX_DEPRECATED("Deprecated in NX9.0.0.  Please use NXOpen::Features::PartModule::Activate instead.") void SetDeactivate
            (
                bool deactivate /** deactivate */ 
            );
            /**Returns  the option indicating whether the part module is to be activated. If true, the part module will be activated, else, no action is taken
                      <br> 
                     This API is now deprecated.
                     Please use @link NXOpen::Features::PartModule::Activate NXOpen::Features::PartModule::Activate@endlink  instead.
                      <br> 
                    
             <br>  @deprecated Deprecated in NX9.0.0.  Please use @link NXOpen::Features::PartModule::Activate NXOpen::Features::PartModule::Activate@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX9.0.0.  Please use NXOpen::Features::PartModule::Activate instead.") bool Activate
            (
            );
            /**Sets  the option indicating whether the part module is to be activated. If true, the part module will be activated, else, no action is taken
                      <br> 
                     This API is now deprecated.
                     Please use @link NXOpen::Features::PartModule::Activate NXOpen::Features::PartModule::Activate@endlink  instead.
                      <br> 
                    
             <br>  @deprecated Deprecated in NX9.0.0.  Please use @link NXOpen::Features::PartModule::Activate NXOpen::Features::PartModule::Activate@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NX_DEPRECATED("Deprecated in NX9.0.0.  Please use NXOpen::Features::PartModule::Activate instead.") void SetActivate
            (
                bool activate /** activate */ 
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