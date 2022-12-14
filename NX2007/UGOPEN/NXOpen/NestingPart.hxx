#ifndef NXOpen_NESTINGPART_HXX_INCLUDED
#define NXOpen_NESTINGPART_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     NestingPart.ja
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
    class NestingPart;
    class NestingPartImpl;

    /// \cond NX_NO_DOC 
    /** Represents a sheet metal nesting part class.  <br> To create a new instance of this class, use @link NXOpen::Features::SheetMetal::NestingBuilder::CreateNestingPart  NXOpen::Features::SheetMetal::NestingBuilder::CreateNestingPart @endlink  <br> 
     <br>  Created in NX2007.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  NestingPart : public NXOpen::TransientObject
    {
        /** This enum defines the allowed rotation values. */

        /// \cond NX_NO_DOC 
        public: enum Rotations
        {
            RotationsFree/** free */ ,
            RotationsNone/** none */ ,
            RotationsDegrees90/** degrees90 */ ,
            RotationsDegrees180/** degrees180 */ 
        };


        /// \endcond 
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
        /** This enum defines the priority levels for parts. */

        /// \cond NX_NO_DOC 
        public: enum Formats
        {
            FormatsPrt/** prt */ ,
            FormatsDxf/** dxf */ 
        };


        /// \endcond 
        private: NestingPartImpl * m_nestingpart_impl;
        /// \cond NX_NO_DOC 
        public: explicit NestingPart(void *ptr);
        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Free resources associated with the instance. After this method
            is called, it is illegal to use the object. In .NET, this method
            is automatically called when the object is deleted by the garbage
            collector. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~NestingPart();

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the part name. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: NXString Name
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the file format. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::NestingPart::Formats Format
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the material. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: NXString Material
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the part thickness. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: double Thickness
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the part quanity. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: int Quantity
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the part quanity. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : nx_2d_nesting (" NX 2D Nesting") */
        public: void SetQuantity
        (
            int partQuantity /** partquantity */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the part rotation. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::NestingPart::Rotations Rotation
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the part rotation. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : nx_2d_nesting (" NX 2D Nesting") */
        public: void SetRotation
        (
            NXOpen::NestingPart::Rotations rotation /** rotation */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the part rotation tolerance. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: double RotationTolerance
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the part rotation tolerance. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : nx_2d_nesting (" NX 2D Nesting") */
        public: void SetRotationTolerance
        (
            double rotationTolerance /** rotationtolerance */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the value of allow mirror flag. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: bool AllowMirror
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the value of allow mirror flag. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : nx_2d_nesting (" NX 2D Nesting") */
        public: void SetAllowMirror
        (
            bool allowMirror /** allowmirror */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the part priority. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::NestingPart::Priorities Priority
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the part priority. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : nx_2d_nesting (" NX 2D Nesting") */
        public: void SetPriority
        (
            NXOpen::NestingPart::Priorities priority /** priority */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the status. True if part is valid. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: bool IsValid
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Returns  the include flag. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: bool Include
        (
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /**Sets  the include flag. 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : nx_2d_nesting (" NX 2D Nesting") */
        public: void SetInclude
        (
            bool include /** include */ 
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
