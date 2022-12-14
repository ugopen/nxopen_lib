#ifndef NXOpen_GEOMETRICUTILITIES_BLENDSTOPSHORTBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_BLENDSTOPSHORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_BlendStopshortBuilder.ja
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
#include <NXOpen/GeometricUtilities_OnPathDimensionBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class BlendStopshortBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class OnPathDimensionBuilder;
    }
    namespace GeometricUtilities
    {
        class _BlendStopshortBuilderBuilder;
        class BlendStopshortBuilderImpl;
        /**
            Represents a @link NXOpen::GeometricUtilities::BlendStopshortBuilder NXOpen::GeometricUtilities::BlendStopshortBuilder@endlink 
            
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  BlendStopshortBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** This enum represents the choice for stopshort option. The default choice is 'At Distance'. */
            public: enum Choices
            {
                ChoicesAtDistance/** Distance */,
                ChoicesAtIntersection/** Intersection */
            };

            private: BlendStopshortBuilderImpl * m_blendstopshortbuilder_impl;
            private: friend class  _BlendStopshortBuilderBuilder;
            protected: BlendStopshortBuilder();
            public: ~BlendStopshortBuilder();
            /**Returns  the Stopshort option choice. Choose from 'At Distance' or 'At Intersection'. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BlendStopshortBuilder::Choices Choice
            (
            );
            /**Sets  the Stopshort option choice. Choose from 'At Distance' or 'At Intersection'. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetChoice
            (
                NXOpen::GeometricUtilities::BlendStopshortBuilder::Choices mChoice /** mchoice */ 
            );
            /**Returns  the @link NXOpen::GeometricUtilities::BlendStopshortBuilder NXOpen::GeometricUtilities::BlendStopshortBuilder@endlink  subobject. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * OnPath
            (
            );
            /** Destructor for @link NXOpen::GeometricUtilities::BlendStopshortBuilder NXOpen::GeometricUtilities::BlendStopshortBuilder@endlink  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void Destroy
            (
            );
            /** Flip the builder path for @link NXOpen::GeometricUtilities::BlendStopshortBuilder NXOpen::GeometricUtilities::BlendStopshortBuilder@endlink  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void FlipPath
            (
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
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
