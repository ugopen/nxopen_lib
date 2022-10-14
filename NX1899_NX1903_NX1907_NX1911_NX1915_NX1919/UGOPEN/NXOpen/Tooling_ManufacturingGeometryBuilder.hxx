#ifndef NXOpen_TOOLING_MANUFACTURINGGEOMETRYBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_MANUFACTURINGGEOMETRYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_ManufacturingGeometryBuilder.ja
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
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class ManufacturingGeometryBuilder;
    }
    class Builder;
    class ScCollector;
    namespace Tooling
    {
        class _ManufacturingGeometryBuilderBuilder;
        class ManufacturingGeometryBuilderImpl;
        /** Represents a builder to be used to create manufacturing geometry. <br> To create a new instance of this class, use @link NXOpen::Tooling::ManufacturingGeometryCollection::CreateBuilder  NXOpen::Tooling::ManufacturingGeometryCollection::CreateBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Translucency </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  ManufacturingGeometryBuilder : public NXOpen::Builder
        {
            private: ManufacturingGeometryBuilderImpl * m_manufacturinggeometrybuilder_impl;
            private: friend class  _ManufacturingGeometryBuilderBuilder;
            protected: ManufacturingGeometryBuilder();
            public: ~ManufacturingGeometryBuilder();
            /**Returns  the face to use as the region faces of the geometry groups.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") OR die_engineering ("DIE ENGINEERING") OR ug_die_design ("Die Design") OR nx_electrode_wizard ("NX Electrode Wizard") OR nx_engineering_die_wizard ("NX Engineering Die Wizard") */
            public: NXOpen::ScCollector * Face
            (
            );
            /** Returns the face color. @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") OR die_engineering ("DIE ENGINEERING") OR ug_die_design ("Die Design") OR nx_electrode_wizard ("NX Electrode Wizard") OR nx_engineering_die_wizard ("NX Engineering Die Wizard") */
            public: int GetFaceColor
            (
            );
            /** Sets the face color.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") OR die_engineering ("DIE ENGINEERING") OR ug_die_design ("Die Design") OR nx_electrode_wizard ("NX Electrode Wizard") OR nx_engineering_die_wizard ("NX Engineering Die Wizard") */
            public: void SetFaceColor
            (
                int faceColor /** facecolor */ 
            );
            /**Returns  the translucency to specify the group faces display.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") OR die_engineering ("DIE ENGINEERING") OR ug_die_design ("Die Design") OR nx_electrode_wizard ("NX Electrode Wizard") OR nx_engineering_die_wizard ("NX Engineering Die Wizard") */
            public: int Translucency
            (
            );
            /**Sets  the translucency to specify the group faces display.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") OR die_engineering ("DIE ENGINEERING") OR ug_die_design ("Die Design") OR nx_electrode_wizard ("NX Electrode Wizard") OR nx_engineering_die_wizard ("NX Engineering Die Wizard") */
            public: void SetTranslucency
            (
                int translucency /** translucency */ 
            );
            /** Sets the initialize geometry.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") OR die_engineering ("DIE ENGINEERING") OR ug_die_design ("Die Design") OR nx_electrode_wizard ("NX Electrode Wizard") OR nx_engineering_die_wizard ("NX Engineering Die Wizard") */
            public: void InitializeGeometry
            (
            );
            /** Create a new sub node.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") OR die_engineering ("DIE ENGINEERING") OR ug_die_design ("Die Design") OR nx_electrode_wizard ("NX Electrode Wizard") OR nx_engineering_die_wizard ("NX Engineering Die Wizard") */
            public: void CreateNewSubNode
            (
                int selNode /** The tree new created sub node */
            );
            /** Sets the initialize content. 
                        Parameter initialize_way indicate the different invoke entry 
                        initialize_way == 0 : Run from Electrode Design Wizard
                        initialize_way == 1 : Run from Progressive Die Wizard
                        initialize_way == 2 : Run from Mold Wizard
                        initialize_way == 3 : Run from Die Design
                        initialize_way == 4 : Run from Engineering Die Wizard.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") OR die_engineering ("DIE ENGINEERING") OR ug_die_design ("Die Design") OR nx_electrode_wizard ("NX Electrode Wizard") OR nx_engineering_die_wizard ("NX Engineering Die Wizard") */
            public: void InitializeContent
            (
                int initializeWay /** initialize way */ 
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