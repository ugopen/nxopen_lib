#ifndef NXOpen_DIE_THROATPARENTBUILDER_HXX_INCLUDED
#define NXOpen_DIE_THROATPARENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_ThroatParentBuilder.ja
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
#include <NXOpen/Die.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_die_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Die
    {
        class ThroatParentBuilder;
    }
    namespace Die
    {
        class ThroatChildBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Die
    {
        class _ThroatParentBuilderBuilder;
        class ThroatParentBuilderImpl;
        /** Represents a Die Throat Parent sub feature.  <br> This sub feature is created via the main feature builder.  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_DIEEXPORT  ThroatParentBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Settings for the type of the throat section. */
            public: enum TypeOption
            {
                TypeOptionWipe/** Throat is built for a wipe operation. */,
                TypeOptionRestrike/** Throat is built for a restrike operation. */
            };

            private: ThroatParentBuilderImpl * m_throatparentbuilder_impl;
            private: friend class  _ThroatParentBuilderBuilder;
            protected: ThroatParentBuilder();
            public: ~ThroatParentBuilder();
            /**Sets  the type of throat sections. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetType
            (
                NXOpen::Die::ThroatParentBuilder::TypeOption type /** type */ 
            );
            /**Returns  the type of throat sections. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::ThroatParentBuilder::TypeOption Type
            (
            );
            /**Sets  the radius to be applied at the back of the throat, top and bottom 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetRadius
            (
                double radius /** radius */ 
            );
            /**Returns  the radius to be applied at the back of the throat, top and bottom 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double Radius
            (
            );
            /**Sets  the step to be applied at the end of the tangential extension of the flange 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetStep
            (
                double step /** step */ 
            );
            /**Returns  the step to be applied at the end of the tangential extension of the flange 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: double Step
            (
            );
            /** Gets the extension attributes, note existance of attributes depends on usage in
                    main feature. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void GetExtensionAttributes
            (
                NXString* title /** Title for attribute. */,
                NXString* value /** Value of attribute. */,
                int* color /** Color of extension faces. */
            );
            /** Sets the extension attributes, note existance of attributes depends on usage in
                    main feature. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetExtensionAttributes
            (
                const NXString & title /** Title for attribute. */,
                const NXString & value /** Value of attribute. */,
                int color /** Color of extension faces. */
            );
            /** Sets the extension attributes, note existance of attributes depends on usage in
                    main feature. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetExtensionAttributes
            (
                const char * title /** Title for attribute. */,
                const char * value /** Value of attribute. */,
                int color /** Color of extension faces. */
            );
            /** Gets the cavity attributes, note existance of attributes depends on usage in
                    main feature. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void GetCavityAttributes
            (
                NXString* title /** Title for attribute. */,
                NXString* value /** Value of attribute. */,
                int* color /** Color of cavity faces. */
            );
            /** Sets the cavity attributes, note existance of attributes depends on usage in
                    main feature. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCavityAttributes
            (
                const NXString & title /** Title for attribute. */,
                const NXString & value /** Value of attribute. */,
                int color /** Color of cavity faces. */
            );
            /** Sets the cavity attributes, note existance of attributes depends on usage in
                    main feature. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetCavityAttributes
            (
                const char * title /** Title for attribute. */,
                const char * value /** Value of attribute. */,
                int color /** Color of cavity faces. */
            );
            /**Sets  the design status of the throat sections, if true the throat sections will be built into the model, if false they will not. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDesignStatus
            (
                bool designStatus /** design status */ 
            );
            /**Returns  the design status of the throat sections, if true the throat sections will be built into the model, if false they will not. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool DesignStatus
            (
            );
            /**Returns  the build status of the throat sections. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieBuildStatusOption BuildStatus
            (
            );
            /**Sets  the display status of the throat sections, if true input data to the throat sections will be displayed, 
                    if false the input data will not be displayed. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayStatus
            (
                bool displayStatus /** display status */ 
            );
            /**Returns  the display status of the throat sections, if true input data to the throat sections will be displayed, 
                    if false the input data will not be displayed. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool DisplayStatus
            (
            );
            /** Creates a child throat section.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::ThroatChildBuilder * CreateChild
            (
            );
            /** Deletes a child throat section. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void DeleteChild
            (
                NXOpen::Die::ThroatChildBuilder * diethroatchild /** diethroatchild */ 
            );
            /** Outputs the child throat sections.  @return  The child throat sections. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::Die::ThroatChildBuilder *> GetChildren
            (
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
