#ifndef NXOpen_PARASOLIDIMPORTER_HXX_INCLUDED
#define NXOpen_PARASOLIDIMPORTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ParasolidImporter.ja
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
#include <NXOpen/BaseImporter.hxx>
#include <NXOpen/ObjectTypeSelector.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class ParasolidImporter;
    class BaseImporter;
    class ObjectTypeSelector;
    class _ParasolidImporterBuilder;
    class ParasolidImporterImpl;
    /**
        Represents a @link NXOpen::ParasolidImporter NXOpen::ParasolidImporter@endlink  to be used when importing the Parasolid Data
        This class is created using @link NXOpen::DexManager NXOpen::DexManager@endlink .
         @link Builder::Commit Builder::Commit@endlink  returns NULL.
     <br> To create a new instance of this class, use @link NXOpen::DexManager::CreateParasolidImporter  NXOpen::DexManager::CreateParasolidImporter @endlink  <br> 
    Default values.
    <list type="table"> 
     
    <listheader><term> 
    Property</term>  <description> 
    Value</description> </listheader>
    <item><term> 
     
    FlattenAssembly </term> <description> 
     
    1 </description> </item> 

    <item><term> 
     
    TargetLayer </term> <description> 
     
    1 </description> </item> 

    <item><term> 
     
    UseActiveLayer </term> <description> 
     
    1 </description> </item> 

    </list> 

     <br>  Created in NX2007.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  ParasolidImporter : public NXOpen::BaseImporter
    {
        private: ParasolidImporterImpl * m_parasolidimporter_impl;
        private: friend class  _ParasolidImporterBuilder;
        protected: ParasolidImporter();
        public: ~ParasolidImporter();
        /**Returns  the objectTypes - the subcomponent used to set object types filters. Used to filter objects based on the types 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ObjectTypeSelector * ObjectTypes
        (
        );
        /**Returns  the use active layer - set this to true to import data to the current active layer 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: bool UseActiveLayer
        (
        );
        /**Sets  the use active layer - set this to true to import data to the current active layer 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: void SetUseActiveLayer
        (
            bool useActiveLayer /** useactivelayer */ 
        );
        /**Returns  the target layer to import data to 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: int TargetLayer
        (
        );
        /**Sets  the target layer to import data to 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: void SetTargetLayer
        (
            int targetLayer /** targetlayer */ 
        );
        /**Returns  the flatten assembly - set this to true to flatten the assembly 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: bool FlattenAssembly
        (
        );
        /**Sets  the flatten assembly - set this to true to flatten the assembly 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: void SetFlattenAssembly
        (
            bool flattenAssembly /** flattenassembly */ 
        );
    };
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
