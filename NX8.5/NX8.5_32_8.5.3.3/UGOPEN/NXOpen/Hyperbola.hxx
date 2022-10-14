#ifndef NXOpen_HYPERBOLA_HXX_INCLUDED
#define NXOpen_HYPERBOLA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Hyperbola.ja
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
#include <NXOpen/Conic.hxx>
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
    class Hyperbola;
    class Conic;
    class _HyperbolaBuilder;
    class HyperbolaImpl;
    /** Represents a hyperbola curve.   <br> To create a new instance of this class, use @link CurveCollection::CreateHyperbola  CurveCollection::CreateHyperbola @endlink  <br> 
     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  Hyperbola : public Conic
    {
        private: HyperbolaImpl * m_hyperbola_impl;
        private: friend class  _HyperbolaBuilder;
        protected: Hyperbola();
        public: ~Hyperbola();
        /**Returns  the semi-transverse length. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: double SemiTransverseLength
        (
        );
        /**Returns  the semi-conjugate length. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: double SemiConjugateLength
        (
        );
        /**Returns  the minimum DY width. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: double MinimumDY
        (
        );
        /**Returns  the maximum DY width. 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: double MaximumDY
        (
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