#ifndef NXOpen_ANNOTATIONS_IAPPENDEDTEXT_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_IAPPENDEDTEXT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_IAppendedText.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Annotations_AppendedText.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class IAppendedText;
    }
    namespace Annotations
    {
        class AppendedText;
    }
    class INXObject;
    namespace Annotations
    {
        /** Represents an object that has appended text */
        class NXOPENCPPEXPORT IAppendedText : public virtual INXObject
        {
            /** Returns the appended text  @return  Appended text  <br> License requirements : None */
            public: virtual NXOpen::Annotations::AppendedText * GetAppendedText
            (
            ) = 0;
            /** Sets the appended text  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: virtual void SetAppendedText
            (
                NXOpen::Annotations::AppendedText * appended_text /** Appended text */
            ) = 0;
        };
    }
}
#undef EXPORTLIBRARY
#endif
