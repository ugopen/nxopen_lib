#ifndef NXOpen_SKETCHOPERATIONBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHOPERATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchOperationBuilder.ja
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
#include <NXOpen/SketchFoundRelation.hxx>
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
    class SketchOperationBuilder;
    class Builder;
    class SketchFoundRelation;
    class SketchRelation;
    class _SketchOperationBuilderBuilder;
    class SketchOperationBuilderImpl;
    /** Represents a @link NXOpen::SketchOperationBuilder NXOpen::SketchOperationBuilder@endlink . This is the base class of various sketch operation builders such as
            @link SketchEditDimensionValueBuilder SketchEditDimensionValueBuilder@endlink  or @link SketchMakeRelationBuilder SketchMakeRelationBuilder@endlink  and cannot be created on its own.  <br> Create an instance of child builder classes instead  <br> 
     <br>  Created in NX1847.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchOperationBuilder : public NXOpen::Builder
    {
        private: SketchOperationBuilderImpl * m_sketchoperationbuilder_impl;
        private: friend class  _SketchOperationBuilderBuilder;
        protected: SketchOperationBuilder();
        public: ~SketchOperationBuilder();
        /** Calculate the relations needed based on the operation inputs. Return the found relations for further processing.  @return  
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: std::vector<NXOpen::SketchFoundRelation *> FindRelations
        (
        );
        /** Relax or unrelax a relation found in the operation.  True to relax, false to unrelax. 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void SetRelationRelaxState
        (
            NXOpen::SketchRelation * relation /** relation */ ,
            bool relax /** relax */ 
        );
        /** Clears all relaxed relations and locked objects (if present). 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void RestoreOperation
        (
        );
        /** Returns the configuration data of the internal solver operation. The caller should free the char pointer configurationData after use 
         <br>  Created in NX1980.0.0.  <br>  
         <br> License requirements : None */
        public: NXString ExportSolverConfiguration
        (
            int* numStringSize /** numstringsize */ 
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