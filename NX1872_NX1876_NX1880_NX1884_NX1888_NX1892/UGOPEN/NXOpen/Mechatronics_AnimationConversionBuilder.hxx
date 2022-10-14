#ifndef NXOpen_MECHATRONICS_ANIMATIONCONVERSIONBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_ANIMATIONCONVERSIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_AnimationConversionBuilder.ja
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
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class AnimationConversionBuilder;
    }
    class Builder;
    class NXObject;
    namespace Mechatronics
    {
        class _AnimationConversionBuilderBuilder;
        class AnimationConversionBuilderImpl;
        /** Represents a @link Mechatronics::AnimationConversionBuilder Mechatronics::AnimationConversionBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Mechatronics::PhysicsManager::CreateAnimationConversionBuilder  NXOpen::Mechatronics::PhysicsManager::CreateAnimationConversionBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  AnimationConversionBuilder : public NXOpen::Builder
        {
            private: AnimationConversionBuilderImpl * m_animationconversionbuilder_impl;
            private: friend class  _AnimationConversionBuilderBuilder;
            protected: AnimationConversionBuilder();
            public: ~AnimationConversionBuilder();
            /**  @brief  Returns the tentatively converting physics objects.  

              
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void GetTentativePhysics
            (
                std::vector<NXOpen::NXObject *> & physics /** physics */ 
            );
            /**  @brief  Enables the conversion of objects. If it is impossible, the objects will keep unable status.  

              
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void EnableObjectsConversion
            (
                const std::vector<NXOpen::NXObject *> & physics /** physics */ ,
                bool enable /** enable */ 
            );
            /**Returns  the associative. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: bool Associative
            (
            );
            /**Sets  the associative. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
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