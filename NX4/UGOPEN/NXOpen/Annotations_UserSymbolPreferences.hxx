#ifndef NXOpen_ANNOTATIONS_USERSYMBOLPREFERENCES_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_USERSYMBOLPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_UserSymbolPreferences.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class UserSymbolPreferences;
    }
    namespace Annotations
    {
    }
    namespace Annotations
    {
        /** Represents preferences related to user-defined symbols */
        class NXOPENCPPEXPORT UserSymbolPreferences : public TransientObject
        {
            /** Specifies whether length and height or scale and aspect ratio is used
                    in specifying the size of the symbol */
            public: enum SizeType
            {
                SizeTypeLengthHeight/** length and height */,
                SizeTypeScaleAspectRatio/** scale and aspect ratio */
            };

            public: explicit UserSymbolPreferences(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~UserSymbolPreferences();
            /** Gets the size preference  <br> License requirements : None */
            public: void GetSize
            (
                NXOpen::Annotations::UserSymbolPreferences::SizeType* size_type /** Specifies whether length and height or scale and aspect ratio is used */,
                double* length_or_scale /** Length or scale */,
                double* height_or_aspect_ratio /** Height or aspect ratio */
            );
            /** Sets the scale and aspect ratio  <br> License requirements : None */
            public: void SetScaleAndAspectRatio
            (
                double scale /** */,
                double aspect_ratio /** */
            );
            /** Sets the length and height  <br> License requirements : None */
            public: void SetLengthAndHeight
            (
                double length /** */,
                double height /** */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif