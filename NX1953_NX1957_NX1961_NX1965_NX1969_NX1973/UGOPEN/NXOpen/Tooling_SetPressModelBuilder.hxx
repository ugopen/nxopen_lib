#ifndef NXOpen_TOOLING_SETPRESSMODELBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_SETPRESSMODELBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_SetPressModelBuilder.ja
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
        class SetPressModelBuilder;
    }
    class Builder;
    namespace Tooling
    {
        class _SetPressModelBuilderBuilder;
        class SetPressModelBuilderImpl;
        /** Represents a @link Tooling::SetPressModelBuilder Tooling::SetPressModelBuilder@endlink  to set and load the press model.  <br> To create a new instance of this class, use @link NXOpen::Tooling::AutoDieCollection::CreateSetPressModelBuilder  NXOpen::Tooling::AutoDieCollection::CreateSetPressModelBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        StrokesPerMinute </term> <description> 
         
        0 </description> </item> 

        </list> 

         <br>  Created in NX10.0.2.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  SetPressModelBuilder : public NXOpen::Builder
        {
            private: SetPressModelBuilderImpl * m_setpressmodelbuilder_impl;
            private: friend class  _SetPressModelBuilderBuilder;
            protected: SetPressModelBuilder();
            public: ~SetPressModelBuilder();
            /**Returns  the target directory to store cloned press model
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXString TargetDirectory
            (
            );
            /**Sets  the target directory to store cloned press model
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : nx_dievalidation ("DIE VALIDATION") */
            public: void SetTargetDirectory
            (
                const NXString & pathName /** pathname */ 
            );
            /**Sets  the target directory to store cloned press model
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : nx_dievalidation ("DIE VALIDATION") */
            void SetTargetDirectory
            (
                const char * pathName /** pathname */ 
            );
            /**Returns  the path to clone available press model
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXString PressModelPath
            (
            );
            /**Sets  the path to clone available press model
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : nx_dievalidation ("DIE VALIDATION") */
            public: void SetPressModelPath
            (
                const NXString & pressModelPath /** pressmodelpath */ 
            );
            /**Sets  the path to clone available press model
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : nx_dievalidation ("DIE VALIDATION") */
            void SetPressModelPath
            (
                const char * pressModelPath /** pressmodelpath */ 
            );
            /**Returns  the strokes per minute of press model
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: double StrokesPerMinute
            (
            );
            /**Sets  the strokes per minute of press model
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : nx_dievalidation ("DIE VALIDATION") */
            public: void SetStrokesPerMinute
            (
                double strokesPerMinute /** strokesperminute */ 
            );
            /**Returns  the name suffix add to the press model parts
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXString NameSuffix
            (
            );
            /**Sets  the name suffix add to the press model parts
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : nx_dievalidation ("DIE VALIDATION") */
            public: void SetNameSuffix
            (
                const NXString & nameSuffix /** namesuffix */ 
            );
            /**Sets  the name suffix add to the press model parts
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : nx_dievalidation ("DIE VALIDATION") */
            void SetNameSuffix
            (
                const char * nameSuffix /** namesuffix */ 
            );
            /** Sets the press model name user selected in the list box
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : nx_dievalidation ("DIE VALIDATION") */
            public: void SetPressModelName
            (
                const NXString & pressModelName /** pressmodelname */ 
            );
            /** Sets the press model name user selected in the list box
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : nx_dievalidation ("DIE VALIDATION") */
            void SetPressModelName
            (
                const char * pressModelName /** pressmodelname */ 
            );
            /** Initializes the available press models from press model path
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : nx_dievalidation ("DIE VALIDATION") */
            public: void InitializeAvailablePressModels
            (
                const NXString & pressModelPath /** pressmodelpath */ 
            );
            /** Initializes the available press models from press model path
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : nx_dievalidation ("DIE VALIDATION") */
            void InitializeAvailablePressModels
            (
                const char * pressModelPath /** pressmodelpath */ 
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
