#ifndef NXOpen_COLORDEFINITION_HXX_INCLUDED
#define NXOpen_COLORDEFINITION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ColorDefinition.ja
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
#include <NXOpen/ColorDefinition.hxx>
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
    class ColorDefinition;
     /** Specifies rgb values for color */

    struct  ColorDefinitionRgb
    {
        public: /** red color value */double Red;
        public: /** green color value */double Green;
        public: /** blue color value */double Blue;
        public: ColorDefinitionRgb() :
            Red(),
            Green(),
            Blue()
        {
        }
        /** Constructor for the ColorDefinitionRgb struct. */ 
        public: ColorDefinitionRgb(double redInitial /** red color value */, 
                double greenInitial /** green color value */, 
                double blueInitial /** blue color value */) :
            Red(redInitial),
            Green(greenInitial),
            Blue(blueInitial)
        {
        }
    };

    class _ColorDefinitionBuilder;
    class ColorDefinitionImpl;
    /**
        Represents a @link NXOpen::ColorDefinition NXOpen::ColorDefinition@endlink , which is a representation of one color
        on an NX color palette.  Each color has an index into the palette, a name, rgb values, and an
        optional favorite index.
        
     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  ColorDefinition : public NXOpen::TaggedObject
    {
        private: ColorDefinitionImpl * m_colordefinition_impl;
        private: friend class  _ColorDefinitionBuilder;
        protected: ColorDefinition();
        public: ~ColorDefinition();
        /**Returns  the color index.  This is an number ranging from 0 to 216, each color on the 
                color palette must have a unique index. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: int ColorIndex
        (
        );
        /**Sets  the color index.  This is an number ranging from 0 to 216, each color on the 
                color palette must have a unique index. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetColorIndex
        (
            int colorIdx /** coloridx */ 
        );
        /**Returns  the color name. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXString ColorName
        (
        );
        /**Sets  the color name. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetColorName
        (
            const NXString & colorName /** colorname */ 
        );
        /**Sets  the color name. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        void SetColorName
        (
            const char * colorName /** colorname */ 
        );
        /** Gets the color values.  This is an array of 3 doubles containing the RGB values
                    of the color.
                 @return  
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ColorDefinitionRgb GetColorValues
        (
        );
        /** Sets the color values.  This is an array of 3 doubles containing the RGB values
                    of the color.
                
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetColorValues
        (
            const NXOpen::ColorDefinitionRgb & colorVals /** colorvals */ 
        );
        /**Returns  the favorite index.  The favorite index is a unique number between 0 and 29 
                    specifing the index into the favorite color array.  If the color is not a 
                    favorite, it has an index of -1.
                
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: int FavoriteIndex
        (
        );
        /**Sets  the favorite index.  The favorite index is a unique number between 0 and 29 
                    specifing the index into the favorite color array.  If the color is not a 
                    favorite, it has an index of -1.
                
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetFavoriteIndex
        (
            int favoriteIdx /** favoriteidx */ 
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
