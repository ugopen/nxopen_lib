#ifndef NXOpen_DIE_PIERCEHOLEPARENTBUILDER_HXX_INCLUDED
#define NXOpen_DIE_PIERCEHOLEPARENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_PierceHoleParentBuilder.ja
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
        class PierceHoleParentBuilder;
    }
    namespace Die
    {
        class PierceHoleChildBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Die
    {
        class _PierceHoleParentBuilderBuilder;
        class PierceHoleParentBuilderImpl;
        /** Represents a Pierce Hole Parent sub feature.  <br> This sub feature is created via the main feature builder.  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_DIEEXPORT  PierceHoleParentBuilder : public Features::FeatureBuilder
        {
            private: PierceHoleParentBuilderImpl * m_pierceholeparentbuilder_impl;
            private: friend class  _PierceHoleParentBuilderBuilder;
            protected: PierceHoleParentBuilder();
            public: ~PierceHoleParentBuilder();
            /**  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetProfileBlendRadius
            (
                const NXString & profileBlendRadius /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetProfileBlendRadius
            (
                const char * profileBlendRadius /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the profile blend radius of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * ProfileBlendRadius
            (
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDieClearance
            (
                const NXString & dieClearance /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetDieClearance
            (
                const char * dieClearance /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the die clearance of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * DieClearance
            (
            );
            /**  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDiameter
            (
                const NXString & diameter /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetDiameter
            (
                const char * diameter /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the diameter of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * Diameter
            (
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDepth
            (
                const NXString & depth /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetDepth
            (
                const char * depth /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the depth of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * Depth
            (
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetLength
            (
                const NXString & length /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetLength
            (
                const char * length /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the length of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * Length
            (
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetWidth
            (
                const NXString & pierceHoleWidth /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetWidth
            (
                const char * pierceHoleWidth /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the width of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * Width
            (
            );
            /**Sets  the common slug hole switch of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCommonSlugHole
            (
                bool commonSlugHole /** common slug hole */ 
            );
            /**Returns  the common slug hole switch of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool CommonSlugHole
            (
            );
            /**Sets  the circular slug hole switch of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCircularSlugHole
            (
                bool circularSlugHole /** circular slug hole */ 
            );
            /**Returns  the circular slug hole switch of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool CircularSlugHole
            (
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetSlugHoleDiameterIncrement
            (
                const NXString & slugHoleDiameterIncrement /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetSlugHoleDiameterIncrement
            (
                const char * slugHoleDiameterIncrement /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the slug hole diameter increment of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * SlugHoleDiameterIncrement
            (
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetSlugHoleOffset
            (
                const NXString & slugHoleOffset /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetSlugHoleOffset
            (
                const char * slugHoleOffset /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the slug hole offset of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * SlugHoleOffset
            (
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBreakerHoleFactor
            (
                const NXString & breakerHoleFactor /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetBreakerHoleFactor
            (
                const char * breakerHoleFactor /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the breaker hole factor of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * BreakerHoleFactor
            (
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBreakerHoleOffset
            (
                const NXString & breakerHoleOffset /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetBreakerHoleOffset
            (
                const char * breakerHoleOffset /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the breaker hole offset of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * BreakerHoleOffset
            (
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBreakerHoleDepth
            (
                const NXString & breakerHoleDepth /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetBreakerHoleDepth
            (
                const char * breakerHoleDepth /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the breaker hole depth of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * BreakerHoleDepth
            (
            );
            /**Sets  the display holes option of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayHoles
            (
                bool displayPierceHoles /** display pierce holes */ 
            );
            /**Returns  the display holes option of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool DisplayHoles
            (
            );
            /** Gets the hole attributes, note existance of attributes depends on usage in
                    main feature 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void GetHoleAttributes
            (
                NXString* title /** title for attribute */,
                NXString* value /** value of attribute */,
                int* color /** color of hole faces */,
                NXString* diameterTitle /** title for diameter attribute */
            );
            /** Sets the hole attributes, note existance of attributes depends on usage in
                    main feature 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetHoleAttributes
            (
                const NXString & title /** title for attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & value /** value of attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int color /** color of hole faces */,
                const NXString & diameterTitle /** title for diameter attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the hole attributes, note existance of attributes depends on usage in
                    main feature 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetHoleAttributes
            (
                const char * title /** title for attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * value /** value of attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int color /** color of hole faces */,
                const char * diameterTitle /** title for diameter attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the slug hole attributes, note existance of attributes depends on usage in
                    main feature 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void GetSlugHoleAttributes
            (
                NXString* title /** title for attribute */,
                NXString* value /** value of attribute */,
                int* color /** color of hole faces */,
                NXString* diameterTitle /** title for diameter attribute */
            );
            /** Sets the slug hole attributes, note existance of attributes depends on usage in
                    main feature 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetSlugHoleAttributes
            (
                const NXString & title /** title for attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & value /** value of attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int color /** color of hole faces */,
                const NXString & diameterTitle /** title for diameter attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the slug hole attributes, note existance of attributes depends on usage in
                    main feature 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetSlugHoleAttributes
            (
                const char * title /** title for attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * value /** value of attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int color /** color of hole faces */,
                const char * diameterTitle /** title for diameter attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the breaker hole attributes, note existance of attributes depends on usage in
                    main feature 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void GetBreakerHoleAttributes
            (
                NXString* title /** title for attribute */,
                NXString* value /** value of attribute */,
                int* color /** color of hole faces */,
                NXString* diameterTitle /** title for diameter attribute */
            );
            /** Sets the breaker hole attributes, note existance of attributes depends on usage in
                    main feature 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBreakerHoleAttributes
            (
                const NXString & title /** title for attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & value /** value of attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int color /** color of hole faces */,
                const NXString & diameterTitle /** title for diameter attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the breaker hole attributes, note existance of attributes depends on usage in
                    main feature 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetBreakerHoleAttributes
            (
                const char * title /** title for attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * value /** value of attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int color /** color of hole faces */,
                const char * diameterTitle /** title for diameter attribute   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Sets  the design status of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDesignStatus
            (
                bool designStatus /** design status */ 
            );
            /**Returns  the design status of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool DesignStatus
            (
            );
            /**Returns  the build status of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieBuildStatusOption BuildStatus
            (
            );
            /**Sets  the display status of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayStatus
            (
                bool displayStatus /** display status */ 
            );
            /**Returns  the display status of pierce holes 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool DisplayStatus
            (
            );
            /** Creates a child pierce hole  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::PierceHoleChildBuilder * CreateChild
            (
            );
            /** Deletes a child pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void DeleteChild
            (
                NXOpen::Die::PierceHoleChildBuilder * dieholechild /** dieholechild */ 
            );
            /** Outputs the pierce hole children  @return  children 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::Die::PierceHoleChildBuilder *> GetChildren
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
