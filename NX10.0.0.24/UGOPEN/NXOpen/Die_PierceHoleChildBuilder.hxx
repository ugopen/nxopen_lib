#ifndef NXOpen_DIE_PIERCEHOLECHILDBUILDER_HXX_INCLUDED
#define NXOpen_DIE_PIERCEHOLECHILDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_PierceHoleChildBuilder.ja
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
#include <NXOpen/ugmath.hxx>
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
        class PierceHoleChildBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class ILocation;
    class IProfile;
    namespace Die
    {
        class _PierceHoleChildBuilderBuilder;
        class PierceHoleChildBuilderImpl;
        /** Represents a Pierce Hole Child sub feature.  <br> This sub feature is created via the main feature builder.  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_DIEEXPORT  PierceHoleChildBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Settings for the shape type of the pierce hole. */
            public: enum ShapeTypeOption
            {
                ShapeTypeOptionCircular/** circular hole */,
                ShapeTypeOptionRectangular/** rectangular hole */,
                ShapeTypeOptionCurve/** curve defined hole */
            };

            private: PierceHoleChildBuilderImpl * m_pierceholechildbuilder_impl;
            private: friend class  _PierceHoleChildBuilderBuilder;
            protected: PierceHoleChildBuilder();
            public: ~PierceHoleChildBuilder();
            /** Sets the locations of the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetPierceHoleLocation
            (
                const std::vector<NXOpen::ILocation *> & pierceHoleLocations /** pierce hole location */
            );
            /** Gets the locations of the pierce hole  @return  pierce hole location 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::ILocation *> GetPierceHoleLocation
            (
            );
            /** Sets the shape of the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetPierceHoleShape
            (
                NXOpen::Die::DirectionOption direction /** profile direction */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** profile entries */
            );
            /** Gets the shape of the pierce hole  @return  profile entries 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetPierceHoleShape
            (
                NXOpen::Die::DirectionOption* direction /** profile direction */
            );
            /**Sets  the pierce hole direction 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetPierceHoleDirection
            (
                NXOpen::ILocation * pierceHoleDirection /** pierce hole direction */
            );
            /**Returns  the pierce hole direction 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::ILocation * PierceHoleDirection
            (
            );
            /** Sets the slug hole shape of the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetSlugHoleShape
            (
                NXOpen::Die::DirectionOption direction /** profile direction */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** profile entries */
            );
            /** Gets the slug hole shape of the pierce hole  @return  profile entries 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetSlugHoleShape
            (
                NXOpen::Die::DirectionOption* direction /** profile direction */
            );
            /**Sets  the location of breaker holes for the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBreakerHoleLocation
            (
                NXOpen::ILocation * breakerHoleLocation /** breaker hole location */
            );
            /**Returns  the location of breaker holes for the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::ILocation * BreakerHoleLocation
            (
            );
            /** Sets the breaker hole shape of the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBreakerHoleShape
            (
                NXOpen::Die::DirectionOption direction /** profile direction */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** profile entries */
            );
            /** Gets the breaker hole shape of the pierce hole  @return  profile entries 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetBreakerHoleShape
            (
                NXOpen::Die::DirectionOption* direction /** profile direction */
            );
            /**Sets  the breaker hole direction of the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetBreakerHoleDirection
            (
                NXOpen::ILocation * breakerHoleDirection /** breaker hole direction */
            );
            /**Returns  the breaker hole direction of the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::ILocation * BreakerHoleDirection
            (
            );
            /**Sets  the pierce hole shape type 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetShapeType
            (
                NXOpen::Die::PierceHoleChildBuilder::ShapeTypeOption shapeType /** hole type */
            );
            /**Returns  the pierce hole shape type 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::PierceHoleChildBuilder::ShapeTypeOption ShapeType
            (
            );
            /**  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetProfileBlendRadius
            (
                const NXString & profileBlendRadius /** profile blend radius   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetProfileBlendRadius
            (
                const char * profileBlendRadius /** profile blend radius   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the profile blend radius of the pierce hole 
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
            /**Returns  the die clearance of the pierce hole 
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
            /**Returns  the diameter of the pierce hole 
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
            /**Returns  the depth of the pierce hole 
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
            /**Returns  the length of the pierce hole 
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
                const NXString & width /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            void SetWidth
            (
                const char * width /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the width of the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * Width
            (
            );
            /**Sets  the circular slug hole switch of the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCircularSlugHole
            (
                bool circularSlugHole /** circular slug hole */ 
            );
            /**Returns  the circular slug hole switch of the pierce hole 
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
            /**Returns  the slug hole diameter increment of the pierce hole 
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
            /**Returns  the slug hole offset of the pierce hole 
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
            /**Returns  the breaker hole factor of the pierce hole 
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
            /**Returns  the breaker hole offset of the pierce hole 
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
            /**Returns  the breaker hole depth of the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Expression * BreakerHoleDepth
            (
            );
            /**Sets  the display holes option of the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayHoles
            (
                bool displayPierceHoles /** display pierce holes */ 
            );
            /**Returns  the display holes option of the pierce hole 
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
            /**Sets  the design status of the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDesignStatus
            (
                bool designStatus /** design status */ 
            );
            /**Returns  the design status of the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool DesignStatus
            (
            );
            /**Returns  the build status of the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieBuildStatusOption BuildStatus
            (
            );
            /**Sets  the display status of the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayStatus
            (
                bool displayStatus /** display status */ 
            );
            /**Returns  the display status of the pierce hole 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: bool DisplayStatus
            (
            );
            /** Translates the center of the die pierce hole by the specified amount. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void TranslatePierceHoleLocation
            (
                const NXOpen::Vector3d & translateDist /** A scaled vector indicating the distance to translate */
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