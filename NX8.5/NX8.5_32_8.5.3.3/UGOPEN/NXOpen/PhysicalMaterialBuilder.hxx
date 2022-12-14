#ifndef NXOpen_PHYSICALMATERIALBUILDER_HXX_INCLUDED
#define NXOpen_PHYSICALMATERIALBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PhysicalMaterialBuilder.ja
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
#include <NXOpen/PhysicalMaterialBuilder.hxx>
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
    class PhysicalMaterialBuilder;
    class Builder;
    namespace CAE
    {
        class PropertyTable;
    }
    class _PhysicalMaterialBuilderBuilder;
    class PhysicalMaterialBuilderImpl;
    /** Represents a @link PhysicalMaterial PhysicalMaterial@endlink  builder  <br> To create a new instance of this class, use @link PhysicalMaterialCollection::CreatePhysicalMaterialBuilder  PhysicalMaterialCollection::CreatePhysicalMaterialBuilder @endlink  <br> 
     <br>  Created in NX6.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  PhysicalMaterialBuilder : public Builder
    {
        private: PhysicalMaterialBuilderImpl * m_physicalmaterialbuilder_impl;
        private: friend class  _PhysicalMaterialBuilderBuilder;
        protected: PhysicalMaterialBuilder();
        public: ~PhysicalMaterialBuilder();
        /**Returns  the material name value.  
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXString Name
        (
        );
        /**Sets  the material name value.  
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetName
        (
            const NXString & name /** name */ 
        );
        /**Sets  the material name value.  
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        void SetName
        (
            const char * name /** name */ 
        );
        /**Returns  the material id value.  
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: int Id
        (
        );
        /**Sets  the material id value.  
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: void SetId
        (
            int id /** id */ 
        );
        /**Returns  the material description value.  
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXString Description
        (
        );
        /**Sets  the material description value.  
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetDescription
        (
            const NXString & description /** description */ 
        );
        /**Sets  the material description value.  
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        void SetDescription
        (
            const char * description /** description */ 
        );
        /**Returns  the property table associated with the material object 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::CAE::PropertyTable * PropertyTable
        (
        );
        /**Returns  the add_to_material_library_toggle value.  If set to true, the material to be added to the 
                    specified material library upon commit 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: bool AddToMaterialLibraryToggle
        (
        );
        /**Sets  the add_to_material_library_toggle value.  If set to true, the material to be added to the 
                    specified material library upon commit 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetAddToMaterialLibraryToggle
        (
            bool toggleValue /** toggle value */ 
        );
        /**Returns  the material library value.  The material libary is the file name where you would like to  
                   save this material upon commit 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXString MaterialLibrary
        (
        );
        /**Sets  the material library value.  The material libary is the file name where you would like to  
                   save this material upon commit 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetMaterialLibrary
        (
            const NXString & name /** name */ 
        );
        /**Sets  the material library value.  The material libary is the file name where you would like to  
                   save this material upon commit 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        void SetMaterialLibrary
        (
            const char * name /** name */ 
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
