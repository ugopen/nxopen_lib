/*******************************************************************************
               Copyright (c) 2003 Unigraphics Solutions Inc.
                      Unpublished - All Rights Reserved


*******************************************************************************/
#ifndef NXOpen_NXEXCEPTION_HXX_INCLUDED
#define NXOpen_NXEXCEPTION_HXX_INCLUDED

#ifdef _MSC_VER
#pragma once
#endif

#include <exception>
#include <string>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4251)
#endif

namespace NXOpen
{
    class NXExceptionImpl;

    /** A base class for exceptions thrown by NXOpen methods */
    class NXOPENCPPEXPORT NXException : public std::exception
    {
    public:
        NXException() = delete; 
        NXException& operator=(const NXException&) = delete;

        /** Copy constructor. */
        NXException(const NXException &other) noexcept;

        /** Destructor. */
        virtual ~NXException() noexcept;

        /** Creates an NXException. */
        static NXException Create(int errorCode);

        /** Creates an NXException based on a message in English.
            The error code is set to zero. */
        static NXException Create(const char* message);
        
        
        /** Creates an NXException based on a message and error code */
        static NXException Create(int errorCode, const char* message );

        /// @cond NX_NO_DOC
        static void ThrowBadTagException();

        static void ThrowUnexpectedSuccess();
        /// @endcond

        /** Gets the error message associated with this exception. */
        const char* Message() const;

        /** Gets the error message associated with this exception.
        Does not throw an exception. */
        virtual const char * what () const throw () { return Message(); }

        /** Gets the error code associated with this exception. */
        int ErrorCode() const;

        /** Assert if the error code is unexpected. */
        void AssertErrorCode(int code) const;

    private:

        explicit NXException(int errorCode);
        explicit NXException(const char *message);
        explicit NXException(int errorCode, const char *message);
        NXExceptionImpl* m_impl;
    };
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif

#undef EXPORTLIBRARY

#endif // NXEXCEPTION_HXX_INCLUDED
