#ifndef NXOpen_ANNOTATIONS_MATERIALSPECIFICATIONBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_MATERIALSPECIFICATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_MaterialSpecificationBuilder.ja
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
#include <NXOpen/Annotations_MaterialSpecificationBuilder.hxx>
#include <NXOpen/Annotations_PmiAttributeBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class MaterialSpecificationBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeBuilder;
    }
    namespace Annotations
    {
        class _MaterialSpecificationBuilderBuilder;
        class MaterialSpecificationBuilderImpl;
        /** Represents a @link Annotations::MaterialSpecification Annotations::MaterialSpecification@endlink  builder  <br> To create a new instance of this class, use @link Annotations::PmiAttributeCollection::CreateMaterialSpecificationBuilder Annotations::PmiAttributeCollection::CreateMaterialSpecificationBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  MaterialSpecificationBuilder : public Annotations::PmiAttributeBuilder
        {
            private: MaterialSpecificationBuilderImpl * m_materialspecificationbuilder_impl;
            private: friend class  _MaterialSpecificationBuilderBuilder;
            protected: MaterialSpecificationBuilder();
            public: ~MaterialSpecificationBuilder();
            /**Returns  the str title  <br> License requirements : None */
            public: NXString Title
            (
            );
            /**Sets  the str title  <br> License requirements : None */
            public: void SetTitle
            (
                const NXString & title /** title */ 
            );
            /**Returns  the category  <br> License requirements : None */
            public: NXString Category
            (
            );
            /**Sets  the category  <br> License requirements : None */
            public: void SetCategory
            (
                const NXString & category /** category */ 
            );
            /**Returns  the material type  <br> License requirements : None */
            public: NXString MaterialType
            (
            );
            /**Sets  the material type  <br> License requirements : None */
            public: void SetMaterialType
            (
                const NXString & materialType /** materialtype */ 
            );
            /**Returns  the revision  <br> License requirements : None */
            public: NXString AvailableMaterial
            (
            );
            /**Sets  the revision  <br> License requirements : None */
            public: void SetAvailableMaterial
            (
                const NXString & availableMaterial /** availablematerial */ 
            );
            /** Returns the material properties  @return   <br> License requirements : None */
            public: std::vector<NXString> GetMaterialProperties
            (
            );
            /** Sets the material properties  <br> License requirements : None */
            public: void SetMaterialProperties
            (
                const std::vector<NXString> & materialProperties /** materialproperties */ 
            );
            /**Returns  the revision  <br> License requirements : None */
            public: NXString Revision
            (
            );
            /**Sets  the revision  <br> License requirements : None */
            public: void SetRevision
            (
                const NXString & revision /** revision */ 
            );
            /** Returns the nomenclature  @return   <br> License requirements : None */
            public: std::vector<NXString> GetNomenclature
            (
            );
            /** Sets the nomenclature  <br> License requirements : None */
            public: void SetNomenclature
            (
                const std::vector<NXString> & nomenclature /** nomenclature */ 
            );
            /** Returns the open field  @return   <br> License requirements : None */
            public: std::vector<NXString> GetOpenField
            (
            );
            /** Sets the open field  <br> License requirements : None */
            public: void SetOpenField
            (
                const std::vector<NXString> & openField /** openfield */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif