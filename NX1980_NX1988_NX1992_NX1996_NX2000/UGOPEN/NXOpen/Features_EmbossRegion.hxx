#ifndef NXOpen_FEATURES_EMBOSSREGION_HXX_INCLUDED
#define NXOpen_FEATURES_EMBOSSREGION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_EmbossRegion.ja
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
#include <NXOpen/Features_EmbossLimit.hxx>
#include <NXOpen/Features_EmbossProjection.hxx>
#include <NXOpen/Features_EmbossSidewall.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class EmbossRegion;
    }
    class Direction;
    namespace Features
    {
        class EmbossLimit;
    }
    namespace Features
    {
        class EmbossProjection;
    }
    namespace Features
    {
        class EmbossSidewall;
    }
    class Section;
    namespace Features
    {
        class _EmbossRegionBuilder;
        class EmbossRegionImpl;
        /** Represents an emboss region object. 
                 <br>     
                This class provides methods to set and get the various emboss region sub components.
                 <br>                  
                 <br> 
                Following are default values and options:
                 <br>     
          
                 <br> 
                <b>Section</b>    User must set it
                 <br> 
                 <br> 
                <b>Direction</b>    If user do not specify it, it uses section normal as default direction. 
                 <br> 
                 <br> 
                <b>Convexity Option</b>    @link  Features::EmbossRegion::ConvexityOptionMixed   Features::EmbossRegion::ConvexityOptionMixed @endlink 
                 <br>  
                 <br> 
                <b>Emboss Projection</b>    EmbossProjection object
                 <br> 
                 <br> 
                <b>Emboss Sidewall</b>    EmbossSidewall object
                 <br>  
                 <br> 
                <b>Emboss Limit</b> (array)    EmbossLimit object
                 <br> 

            
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  EmbossRegion : public NXOpen::TaggedObject
        {
            /** Describes whether the emboss geometry is above the target("Pad") or below the target("Pocket"), or both("Mixed"). */
            public: enum ConvexityOption
            {
                ConvexityOptionAbove/** Indicates the emboss geometry is above the target("Pad"). */,
                ConvexityOptionBelow/** Indicates the emboss geometry is below the target("Pocket"). */,
                ConvexityOptionMixed/** Indicates the emboss geometry is both above and below the Target("Mixed"). Default creation.*/
            };

            private: EmbossRegionImpl * m_embossregion_impl;
            private: friend class  _EmbossRegionBuilder;
            protected: EmbossRegion();
            public: ~EmbossRegion();
            /**Sets  the section that is composed of chains 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSection
            (
                NXOpen::Section * section /**The section that is composed of chains.  Each Chain will be a tangent list of curves so the Draft angles for sidewalls can be managed properly. */
            );
            /**Returns  the section that is composed of chains 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * Section
            (
            );
            /**Sets   the default direction 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDirection
            (
                NXOpen::Direction * direction /**The default direction for section projection/translation/sidewall/joggle, if they are not specified*/
            );
            /**Returns   the default direction 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * Direction
            (
            );
            /**Sets   the convexity option  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetConvexity
            (
                NXOpen::Features::EmbossRegion::ConvexityOption convexity /**The convexity option. See the comment of @link Features::EmbossRegion::ConvexityOption Features::EmbossRegion::ConvexityOption@endlink  for more details.*/
            );
            /**Returns   the convexity option  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::EmbossRegion::ConvexityOption Convexity
            (
            );
            /**Sets  the emboss projection object
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetProjection
            (
                NXOpen::Features::EmbossProjection * projection /**The emboss projection object*/
            );
            /**Returns  the emboss projection object
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::EmbossProjection * Projection
            (
            );
            /**Sets  the emboss sidewall object 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSidewall
            (
                NXOpen::Features::EmbossSidewall * sidewall /**The emboss sidewall object*/
            );
            /**Returns  the emboss sidewall object 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::EmbossSidewall * Sidewall
            (
            );
            /** The emboss limits 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetLimits
            (
                const std::vector<NXOpen::Features::EmbossLimit *> & limits /**Array of EmbossLimit objects. In NX4, only one limit is supported.*/
            );
            /** The emboss limits  @return Array of EmbossLimit objects. In NX4, only one limit is supported.
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Features::EmbossLimit *> GetLimits
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