/*******************************************************************************
               Copyright (c) 2003 Unigraphics Solutions Inc.
                      Unpublished - All Rights Reserved


*******************************************************************************/
#ifndef NXOpen_NXSTRING_HXX_INCLUDED
#define NXOpen_NXSTRING_HXX_INCLUDED

#ifdef _MSC_VER
#pragma once
#endif

#include <stddef.h>
#include <string>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    /** An internationalized NX text string */
    class NXOPENCPPEXPORT NXString 
    {
    public:
        /** Specifies the language mode */
        enum  NXStringMode { UTF8 /** UTF8*/, Locale /** Locale */ };

        NXString() : native_text(NULL), utf8_text(NULL), mode(Locale)
        {
        }

        /** Creates an NXString from an encoded character array. If mode == NXStringUTF8, 
            the character array is assumed to be UTF8. If mode == NXStringLocale, the
            character array is assumed to be in the current locale's encoding. 
        **/
        NXString(const char* text, NXStringMode mode = Locale);   //lint !e1931 
        /**         **/

        /** Creates an NXString from a std:string. If mode == NXStringUTF8, 
            the string is assumed to be UTF8. If mode == NXStringLocale, the
            string is assumed to be in the current locale's encoding. 
        **/
        NXString(const std::string &text, NXStringMode mode = Locale); //lint !e1931 
        /**         **/

        /** Copy constructor */
        NXString(const NXString& other);
        /** Assignment operator */
        NXString& operator= (const NXString& other);

        /** NXString destructor */
        ~NXString();

        /** Returns the mode that was used to create this string.  NXString objects
        returned from the NX API will have the mode set according to the underlying
        implementation. This if a member-funtion GetName() returns an NXString in
        NXStringLocale mode, the underlying name is stored in a locale-specific
        encoding. If the string is returned in NXStringUTF8 mode, the underlying
        name is stored internally in UTF8 mode. */
        NXStringMode GetMode() const;

        /** Identical to GetMode() but with old name. Deprecated. */
        NXStringMode getMode() const
        {
            return GetMode();
        }        

        /** Returns the text that was passed into the constructor. */
        const char *GetText() const;

        /** Identical to GetText() but with old name. Deprecated. */
        const char *getText() const
        {
            return GetText();
        }        

        /** Returns the text in the encoding supported by the current locale */
        const char *GetLocaleText() const;

        /** Identical to GetLocaleText() but with old name. Deprecated. */
        const char *getLocaleText() const
        {
            return GetLocaleText();
        }        

        /** Returns the text in UTF_8 encoding */
        const char *GetUTF8Text() const;

        /** Identical to GetUTF8Text() but with old name. Deprecated. */
        const char *getUTF8Text() const
        {
            return GetUTF8Text();
        }
        
        /** Concatenate two strings. The second argument is treated as text in the current locale. 
        The return value is a string of the same mode as the first argument */
        friend NXOPENCPPEXPORT NXString operator + (const NXString &a, const char *b);

        /** Concatenate two strings. The first argument is treated as text in the current locale. 
        The return value is a string of the same mode as the second argument */
        friend NXOPENCPPEXPORT NXString operator + (const char * a, const NXString &b);

        /** Append the argument to this string. The argument is treated as text in the current locale. 
        **/
        NXString & operator += (const char *s);

        /**         **/

        /** Append the argument to this string. This string stays in the same mode. If this string
            is in locale mode and the argument is a UTF8 string then the result may lose characters
            that can not be represented in the current locale. */
        NXString & operator += (const NXString &s);


    private:
        mutable char *native_text;
        mutable void *utf8_text;
        NXStringMode mode;
       
    };

    /** Concatenate two strings. If both arguments have locale mode the result is in locale mode too.
        If either argument is UTF8 the result is in UTF8 mode. */
    extern NXOPENCPPEXPORT NXString operator + (const NXString &a, const NXString &b);

}

#undef EXPORTLIBRARY

#endif
