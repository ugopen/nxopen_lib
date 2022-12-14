#ifndef NXOpen_NESTINGSTOCK_HXX_INCLUDED
#define NXOpen_NESTINGSTOCK_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     NestingStock.ja
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
    class NestingStock;
    class NestingStockImpl;

    /// \cond NX_NO_DOC 
    /** Represents a sheet metal nesting stock class.  <br> To create a new instance of this class, use @link NXOpen::Features::SheetMetal::NestingBuilder::CreateNestingStock  NXOpen::Features::SheetMetal::NestingBuilder::CreateNestingStock @endlink  <br> 
     <br>  Created in NX2007.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  NestingStock : public NXOpen::TransientObject
    {
        /** This enum defines the priority levels for parts. */

        /// \cond NX_NO_DOC 
        public: enum Priorities
        {
            PrioritiesLowest/** lowest */ ,
            PrioritiesLow/** low */ ,
            PrioritiesNormal/** normal */ ,
            PrioritiesHigh/** high */ ,
            PrioritiesHighest/** highest */ 
        };


        /// \endcond 
        private: NestingStockImpl * m_nestingstock_impl;
        /// \cond NX_NO_DOC 
        public: explicit NestingStock(void *ptr);
        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Free resources associated with the instance. After this method
            is called, it is illegal to use the object. In .NET, this method
            is automatically called when the object is deleted by the garbage
            collector. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~NestingStock();

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the stock name. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: NXString Name
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the stock length. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: double Length
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the stock length. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : nx_2d_nesting (" NX 2D Nesting") */
        public: void SetLength
        (
            double length /** length */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the stock width. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: double Width
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the stock width. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : nx_2d_nesting (" NX 2D Nesting") */
        public: void SetWidth
        (
            double width /** width */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the stock thickness. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: double Thickness
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the stock thickness. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : nx_2d_nesting (" NX 2D Nesting") */
        public: void SetThickness
        (
            double thickness /** thickness */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the stock quanity. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: int Quantity
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the stock quanity. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : nx_2d_nesting (" NX 2D Nesting") */
        public: void SetQuantity
        (
            int quantity /** quantity */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the stock priority. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::NestingStock::Priorities Priority
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the stock priority. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : nx_2d_nesting (" NX 2D Nesting") */
        public: void SetPriority
        (
            NXOpen::NestingStock::Priorities priority /** priority */ 
        );

        /// \endcond 
    }; //lint !e1712 default constructor not defined for class  


    /// \endcond 
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
