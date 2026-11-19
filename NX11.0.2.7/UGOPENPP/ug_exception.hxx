/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for NX exception C++ class definitions

================================================================================

*/

#ifndef UG_EXCEPTION_INCLUDED
#define UG_EXCEPTION_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_openpp.hxx>

#include <ug_string.hxx>
#include <libopenpp_exports.hxx>

// This class defines the interface for the creation and manipulation of
// NX exception objects.  An instance of this class is thrown whenever an
// Open API function call internal to the Open++ classes returns a
// non-zero error code, or when the Open++ code detects some other
// errors.
class OPENPPEXPORT UgException
{

    public:

        // Construct a UgException object
        UgException
        (
            int error_code              // The error code that caused the exception
        );

        // Destroy a UgException object
        virtual ~UgException ( );

        // Return the error code of the invoking object.
        int askErrorCode ( ) const;

        // Return the error text that explains the error code of the invoking object.
        const std::string askErrorText ( ) const;

        // This method is meant to be used as a convenience routine for 
        // processing errors.  It prints out an error message to a 
        // UgInfoWindow object.  It is also useful in situations 
        // where you cannot throw an exception because you are in a 
        // 'C' environment.  For example, you cannot throw an exception
        // from your infoObject ( ), memberDeletion ( ) and update ( ) 
        // methods in your derived objects since NX is a 'C' main.
        // Remember that a 'C' main cannot catch a 'C++' exception.
        // If the Open API is not initialized then this method will noop.
        void processError ( ) const;
        
        // Throw an exception when an Open API function call indicates a failure.
        // A failure is indicated by a non-zero return value from an Open API
        // function.
        // Example:  UgException::throwOnFailure ( UF_MODL_update ( ) );
        static void throwOnFailure
        (
            int function_result         // <I>
                                        // The result of a function call.  If this
                                        // argument is zero, the method will directly
                                        // return.  If the argument is non-zero, the
                                        // method will construct a UgException object
                                        // with the argument and throw it.
        );

    private:

        // Default constructor that is not implemented
        UgException ( );

        // The exception error code
        int m_error_code;

};

#undef EXPORTLIBRARY

#endif    // UG_EXCEPTION_INCLUDED
