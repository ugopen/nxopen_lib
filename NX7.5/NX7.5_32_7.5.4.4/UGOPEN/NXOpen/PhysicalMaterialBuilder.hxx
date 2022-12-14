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
    /** Represents a @link PhysicalMaterial PhysicalMaterial@endlink  builder  <br> To create a new instance of this class, use @link PhysicalMaterialCollection::CreatePhysicalMaterialBuilder PhysicalMaterialCollection::CreatePhysicalMaterialBuilder@endlink  <br> */
    class NXOPENCPPEXPORT  PhysicalMaterialBuilder : public Builder
    {
        private: PhysicalMaterialBuilderImpl * m_physicalmaterialbuilder_impl;
        private: friend class  _PhysicalMaterialBuilderBuilder;
        protected: PhysicalMaterialBuilder();
        public: ~PhysicalMaterialBuilder();
        /**Returns  the material name value.   <br> License requirements : None */
        public: NXString Name
        (
        );
        /**Sets  the material name value.   <br> License requirements : gateway ("UG GATEWAY") */
        public: void SetName
        (
            const NXString & name /** name */ 
        );
        /**Returns  the material id value.   <br> License requirements : None */
        public: int Id
        (
        );
        /**Sets  the material id value.   <br> License requirements : gateway ("UG GATEWAY") */
        public: void SetId
        (
            int id /** id */ 
        );
        /**Returns  the material description value.   <br> License requirements : None */
        public: NXString Description
        (
        );
        /**Sets  the material description value.   <br> License requirements : gateway ("UG GATEWAY") */
        public: void SetDescription
        (
            const NXString & description /** description */ 
        );
        /**Returns  the property table associated with the material object  <br> License requirements : gateway ("UG GATEWAY") */
        public: NXOpen::CAE::PropertyTable * PropertyTable
        (
        );
        /**Returns  the add_to_material_library_toggle value.  If set to true, the material to be added to the 
                    specified material library upon commit  <br> License requirements : None */
        public: bool AddToMaterialLibraryToggle
        (
        );
        /**Sets  the add_to_material_library_toggle value.  If set to true, the material to be added to the 
                    specified material library upon commit  <br> License requirements : gateway ("UG GATEWAY") */
        public: void SetAddToMaterialLibraryToggle
        (
            bool toggleValue /** toggle value */ 
        );
        /**Returns  the material library value.  The material libary is the file name where you would like to  
                   save this material upon commit  <br> License requirements : None */
        public: NXString MaterialLibrary
        (
        );
        /**Sets  the material library value.  The material libary is the file name where you would like to  
                   save this material upon commit  <br> License requirements : gateway ("UG GATEWAY") */
        public: void SetMaterialLibrary
        (
            const NXString & name /** name */ 
        );
    };
}
#undef EXPORTLIBRARY
#endif
