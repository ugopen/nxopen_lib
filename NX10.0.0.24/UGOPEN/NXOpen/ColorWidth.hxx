#ifndef NXOpen_COLORWIDTH_HXX_INCLUDED
#define NXOpen_COLORWIDTH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ColorWidth.ja
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
#include <NXOpen/ColorWidth.hxx>
#include <NXOpen/TaggedObject.hxx>
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
    class ColorWidth;
    class _ColorWidthBuilder;
    class ColorWidthImpl;
    /**
        Represents a @link NXOpen::ColorWidth NXOpen::ColorWidth@endlink  used by @link NXOpen::WidthDefinition NXOpen::WidthDefinition@endlink  to 
        define a custom width for each color.  This class contains an index into the color array and
        a custom width value assigned to the indexed color.
        
     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  ColorWidth : public NXOpen::TaggedObject
    {
        private: ColorWidthImpl * m_colorwidth_impl;
        private: friend class  _ColorWidthBuilder;
        protected: ColorWidth();
        public: ~ColorWidth();
        /**Returns  the width associated with the color 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: double Width
        (
        );
        /**Sets  the width associated with the color 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetWidth
        (
            double width /** width */ 
        );
        /**Returns  the width entry source.  This will be -1 if this color is not a custom width,
                otherwise it will be a value greater than 0 to index into the color array. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: int WidthSource
        (
        );
        /**Sets  the width entry source.  This will be -1 if this color is not a custom width,
                otherwise it will be a value greater than 0 to index into the color array. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetWidthSource
        (
            int widthSource /** widthsource */ 
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
