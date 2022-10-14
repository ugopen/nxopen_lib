#ifndef NXOpen_TOOLING_DEFINELIFTERBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_DEFINELIFTERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_DefineLifterBuilder.ja
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
        class DefineLifterBuilder;
    }
    class Builder;
    class Direction;
    class SelectDisplayableObjectList;
    namespace Tooling
    {
        class _DefineLifterBuilderBuilder;
        class DefineLifterBuilderImpl;
        /** Represents a @link NXOpen::Tooling::DefineLifterBuilder NXOpen::Tooling::DefineLifterBuilder@endlink  to create different types of lifter objects, which
            are used for kinematic motion.  <br> To create a new instance of this class, use @link NXOpen::Tooling::ProgressiveDieManager::CreateDefineLifterBuilder  NXOpen::Tooling::ProgressiveDieManager::CreateDefineLifterBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  DefineLifterBuilder : public NXOpen::Builder
        {
            /** Specifies the lifter types */
            public: enum Types
            {
                TypesGenericLifter/** Generic lifter type*/,
                TypesLifteronLifter/** Lifter on lifter type */
            };

            private: DefineLifterBuilderImpl * m_definelifterbuilder_impl;
            private: friend class  _DefineLifterBuilderBuilder;
            protected: DefineLifterBuilder();
            public: ~DefineLifterBuilder();
            /**Returns  the type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::DefineLifterBuilder::Types Type
            (
            );
            /**Sets  the type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetType
            (
                NXOpen::Tooling::DefineLifterBuilder::Types type /** type */ 
            );
            /**Returns  the lifter body which is the body needed for motion simulation 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * LifterBodies
            (
            );
            /**Returns  the lifter vector that the lifter body moves along 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * LifterVector
            (
            );
            /**Sets  the lifter vector that the lifter body moves along 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetLifterVector
            (
                NXOpen::Direction * lifterVector /** liftervector */ 
            );
            /**Returns  the lifter drive body which drives the lifter body 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * LifterDriveBodies
            (
            );
            /**Returns  the lifter drive vector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * LifterDriveVector
            (
            );
            /**Sets  the lifter drive vector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetLifterDriveVector
            (
                NXOpen::Direction * lifterDriveVector /** lifterdrivevector */ 
            );
            /**Returns  the lifter name 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXString LifterName
            (
            );
            /**Sets  the lifter name 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetLifterName
            (
                const NXString & lifterName /** liftername */ 
            );
            /**Sets  the lifter name 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            void SetLifterName
            (
                const char * lifterName /** liftername */ 
            );
            /**Returns  the main lifter bodies 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * MainLifterBodies
            (
            );
            /**Returns  the main lifter vector that the main lifter moves along
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * MainLifterVector
            (
            );
            /**Sets  the main lifter vector that the main lifter moves along
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetMainLifterVector
            (
                NXOpen::Direction * mainLifterVector /** mainliftervector */ 
            );
            /**Returns  the main lifter drive body that drives the lifter body
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * MainLifterDriveBodies
            (
            );
            /**Returns  the main lifter drive vector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * MainLifterDriveVector
            (
            );
            /**Sets  the main lifter drive vector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetMainLifterDriveVector
            (
                NXOpen::Direction * mainLifterDriveVector /** mainlifterdrivevector */ 
            );
            /**Returns  the lifter on body which is driven by the main lifter body 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * LifterOnBodies
            (
            );
            /**Returns  the lifter on lifter drive vector, it's driven by the main lifter 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * LifterOnDriveVector
            (
            );
            /**Sets  the lifter on lifter drive vector, it's driven by the main lifter 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetLifterOnDriveVector
            (
                NXOpen::Direction * lifterOnDriveVector /** lifterondrivevector */ 
            );
            /**Returns  the lifter on lifter vector, which the lifter on lifter moves along 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * LifterOnLifterVector
            (
            );
            /**Sets  the lifter on lifter vector, which the lifter on lifter moves along 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetLifterOnLifterVector
            (
                NXOpen::Direction * lifterOnLifterVector /** lifteronliftervector */ 
            );
            /**Returns  the lifter on name 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXString LifterOnName
            (
            );
            /**Sets  the lifter on name 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetLifterOnName
            (
                const NXString & lifterOnName /** lifteronname */ 
            );
            /**Sets  the lifter on name 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            void SetLifterOnName
            (
                const char * lifterOnName /** lifteronname */ 
            );
            /** Delete the generic lifter 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void DeleteGenericLifter
            (
                const NXString & lifterName /** liftername */ 
            );
            /** Delete the generic lifter 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            void DeleteGenericLifter
            (
                const char * lifterName /** liftername */ 
            );
            /** Delete the lifter on lifter 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void DeleteLifterOnLifter
            (
                const NXString & lifterName /** liftername */ 
            );
            /** Delete the lifter on lifter 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            void DeleteLifterOnLifter
            (
                const char * lifterName /** liftername */ 
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