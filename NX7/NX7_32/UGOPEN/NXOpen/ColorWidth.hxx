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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/ColorWidth.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class ColorWidth;
    class _ColorWidthBuilder;
    /**
        Represents a @link ColorWidth ColorWidth@endlink  used by @link WidthDefinition WidthDefinition@endlink  to 
        define a custom width for each color.  This class contains an index into the color array and
        a custom width value assigned to the indexed color.
        */
    class NXOPENCPPEXPORT ColorWidth : public TaggedObject
    {
        private: friend class  _ColorWidthBuilder;
        protected: ColorWidth();
        /**Returns  the width associated with the color  <br> License requirements : None */
        public: double Width
        (
        );
        /**Sets  the width associated with the color  <br> License requirements : None */
        public: void SetWidth
        (
            double width /** width */ 
        );
        /**Returns  the width entry source.  This will be -1 if this color is not a custom width,
                otherwise it will be a value greater than 0 to index into the color array.  <br> License requirements : None */
        public: int WidthSource
        (
        );
        /**Sets  the width entry source.  This will be -1 if this color is not a custom width,
                otherwise it will be a value greater than 0 to index into the color array.  <br> License requirements : None */
        public: void SetWidthSource
        (
            int widthSource /** widthsource */ 
        );
    };
}
#undef EXPORTLIBRARY
#endif