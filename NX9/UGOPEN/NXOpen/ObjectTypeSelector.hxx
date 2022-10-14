#ifndef NXOpen_OBJECTTYPESELECTOR_HXX_INCLUDED
#define NXOpen_OBJECTTYPESELECTOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ObjectTypeSelector.ja
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
    class ObjectTypeSelector;
    class Builder;
    class _ObjectTypeSelectorBuilder;
    class ObjectTypeSelectorImpl;
    /**
        Represents a @link ObjectTypeSelector ObjectTypeSelector@endlink  to be used when filter out the objects
        based on the type during import/export. This can be curves, solids,etc.This class is created using @link DexManager DexManager@endlink .  <br> Creator not available in KF.  <br> 
     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  ObjectTypeSelector : public Builder
    {
        private: ObjectTypeSelectorImpl * m_objecttypeselector_impl;
        private: friend class  _ObjectTypeSelectorBuilder;
        protected: ObjectTypeSelector();
        public: ~ObjectTypeSelector();
        /**Returns  the curves - This should be set to true if curves are desired in the output file
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: bool Curves
        (
        );
        /**Sets  the curves - This should be set to true if curves are desired in the output file
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetCurves
        (
            bool curves /** curves */ 
        );
        /**Returns  the surfaces - This should be set to true if surfaces are desired in the output file
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: bool Surfaces
        (
        );
        /**Sets  the surfaces - This should be set to true if surfaces are desired in the output file
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSurfaces
        (
            bool surfaces /** surfaces */ 
        );
        /**Returns  the solids - This should be set to true if solids are desired in the output file 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: bool Solids
        (
        );
        /**Sets  the solids - This should be set to true if solids are desired in the output file 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSolids
        (
            bool solids /** solids */ 
        );
        /**Returns  the annotations - This should be set to true if annotations are desired in the output file
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: bool Annotations
        (
        );
        /**Sets  the annotations - This should be set to true if annotations are desired in the output file
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetAnnotations
        (
            bool annotations /** annotations */ 
        );
        /**Returns  the structures - This should be set to true if structures are desired in the output file
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: bool Structures
        (
        );
        /**Sets  the structures - This should be set to true if structures are desired in the output file
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetStructures
        (
            bool structures /** structures */ 
        );
        /**Returns  the csys - This should be set to true if coordinate systems are desired in the output file
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: bool Csys
        (
        );
        /**Sets  the csys - This should be set to true if coordinate systems are desired in the output file
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetCsys
        (
            bool csys /** csys */ 
        );
        /**Returns  the product data - This should be set to true if product data are desired in the output file
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: bool ProductData
        (
        );
        /**Sets  the product data - This should be set to true if product data are desired in the output file
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetProductData
        (
            bool productData /** productdata */ 
        );
        /**Returns  the pmi data - This should be set to true if pmi data are desired in the output file
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: bool PmiData
        (
        );
        /**Sets  the pmi data - This should be set to true if pmi data are desired in the output file
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void SetPmiData
        (
            bool pmiData /** pmidata */ 
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