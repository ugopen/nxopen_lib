#ifndef NXOpen_HUMANHANDSHAPEDATA_HXX_INCLUDED
#define NXOpen_HUMANHANDSHAPEDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     HumanHandShapeData.ja
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
#include <NXOpen/TransientObject.hxx>
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
    class HumanHandShapeData;
    class HumanHandShapeDataImpl;
    /** Represent hand shape data 
     <br>  Created in NX4.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  HumanHandShapeData : public NXOpen::TransientObject
    {
        /** This enum represents the hand shape data type of human */
        public: enum HandOpt
        {
            HandOptLeft/** left */ ,
            HandOptRight/** right */ ,
            HandOptBoth/** both */ 
        };

        private: HumanHandShapeDataImpl * m_humanhandshapedata_impl;
        /// \cond NX_NO_DOC 
        public: explicit HumanHandShapeData(void *ptr);
        /// \endcond 
        /** Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~HumanHandShapeData();
        /**Returns  the hand type 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
        public: NXOpen::HumanHandShapeData::HandOpt HandType
        (
        );
        /**Returns  the name of the hand shape in the list 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
        public: NXString HandshapeName
        (
        );
        /**Returns  the value for applying the hand shape 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
        public: double HandshapeValue
        (
        );
    }; //lint !e1712 default constructor not defined for class  

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
