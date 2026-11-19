/*
================================================================================

          Copyright (c) 1999-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Part Load Status and Part Load Failure C++ class definitions

================================================================================

*/

#ifndef PART_LOAD_STATUS_INCLUDED
#define PART_LOAD_STATUS_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_string.hxx>
#include <ug_vector.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

extern "C"
{
// 
typedef struct UF_PART_load_status_s UF_PART_load_status_t;
}

// This class defines the failure of a particular part file
// to load.
class OPENPPEXPORT PartLoadFailure
{

    public:
    
        // Construct a PartLoadFailure object.  This default constructor
        // is necessary because std::vector requires it.
        PartLoadFailure ( );

        // Destroy a PartLoadFailure object.
        ~PartLoadFailure ( );

        // Return the name of the part file that failed to load.
        const std::string askPartFileName ( ) const;

        // Return the status code of the part file that failed to load.
        int  askStatusCode ( ) const;

        // Return the status text of the part file that failed to load.
        const std::string askStatusText ( ) const;

        // Determine the equality of two PartLoadFailure objects.
        // The two objects are considered equal if the file name of the
        // invoking object is identical to the file name of the argument
        // object, AND the status code of the invoking object is equal
        // to the status code of the argument object.
        bool operator==
        (
            const PartLoadFailure &right    // The PartLoadFailure object to
                                            // test for equality against
                                            // the invoking object.
        ) const;

        // Determine the less than quality of two PartLoadFailure objects.
        // The invoking object is the left object and the argument object
        // is the right object.  The invoking object is less than the
        // argument object if the file name of the invoking object is less
        // than the file name of the argument object, AND the status code
        // of the invoking object is less than the status code of the argument
        // object.
        bool operator<
        (
            const PartLoadFailure &right    // The PartLoadFailure object to
                                            // test for less than against
                                            // the invoking object.
        ) const;

    private:

        // Construct a PartLoadFailure object from its components.
        PartLoadFailure
        (
            const std::string  &part_file_name,    // The name of the part
                                                   // file that failed to load.
            int                 status             // The status code of the
                                                   // failure.
        );

        // The file name of the part that failed to load.
        std::string         m_part_name;

        // The load status of the part that failed to load.
        int                 m_status_code;

        // The PartLoadStatus class is a friend to allow it to access
        // the private constructor.
        friend class PartLoadStatus;

};

#if defined ( WIN32 )

//  Because the PartLoadStatus class has a std::vector < PartLoadFailure >
//  as a member variable, Windows NT requires that the template class
//  be fully instantiated and given a dll interface because the
//  PartLoadStatus class has a dll interface.  Without the following
//  statements, warnings like the above will occur:
//
//  warning C4251: 'm_partLoadFailures' : class 'std::vector<class PartLoadFailure>'
//                  needs to have dll-interface to be used by clients of class
//                  'PartLoadStatus'
//
//  <JLM> 25-Jun-09  
//  Remove OPENPPTEMPLATE as part of export header clean-up.  We seem to get the
//  C4251 warnings with or without it.

    template class OPENPPEXPORT std::vector < PartLoadFailure >;

#endif

// This class defines the status of a part load operation.
class OPENPPEXPORT PartLoadStatus
{

    public:
    
        // Construct a PartLoadStatus object.  This default constructor
        // allows an object to be created so that its pointer can
        // be passed to a part load method.
        PartLoadStatus ( );

        // Destroy a PartLoadStatus object.
        ~PartLoadStatus ( );

        // Return true if the load operation failed and was rolled back.
        // Return false otherwise.
        bool isFailure ( ) const;

        // Return the PartLoadFailure objects of all of the part files
        // that failed to load.
        const std::vector < PartLoadFailure > askPartLoadFailures ( ) const;

    private:

        // Construct a PartLoadStatus object from a UG/Open struct.
        PartLoadStatus
        (
            const UF_PART_load_status_t &load_status    // The UG/Open struct from
                                                        // which to create the object.
        );

        // Free the allocated memory of the UG/Open struct.
        static void freeMemory
        (
            UF_PART_load_status_t       &load_status    // <I>   
                                                        // The UG/Open struct whose
                                                        // memory is to be freed.
        );

        // Status of the load operation.  This value is true if
        // any of the parts involved in the load operation failed
        // to load.
        bool                             m_has_failed;

        // The PartLoadFailure objects of all of the parts that failed to load.
        std::vector < PartLoadFailure >  m_part_load_failures;

        // The UgPart class is a friend to allow its load methods to access the
        // private constructor and the private freeMemory ( ) static method.
        friend class UgPart;

        // The UgAssemblyNode class is a friend to allow its load methods to access
        // the private constructor and the private freeMemory ( ) static method.
        friend class UgAssemblyNode;

};

#undef EXPORTLIBRARY

#endif  // PART_LOAD_STATUS_INCLUDED
