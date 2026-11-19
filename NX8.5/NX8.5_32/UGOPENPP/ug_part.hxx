/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Part object C++ class definitions

================================================================================

*/

#ifndef UG_PART_INCLUDED
#define UG_PART_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_attributable.hxx>
#include <ug_constants.hxx>
#include <ug_object.hxx>

#include <ug_string.hxx>
#include <ug_vector.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class PartLoadStatus;
class UgAssemblyNode;
class CoordSys;

// This class defines the interface for the creation and manipulation of
// Unigraphics part files.
class OPENPPEXPORT UgPart : public virtual UgObject, 
                            public UgAttributableObject
{
   
    UG_DECLARE_INTERNAL_CLASS ( UgPart )


    public:

        // Return true if the default unit of the invoking UgPart object is
        // millimeters.  Return false otherwise.
        bool isMillimeters ( ) const;

        // Return true if the default unit of the invoking UgPart object is
        // inches.  Return false otherwise.
        bool isInches ( ) const;
       
        // Return the NX part object that owns the invoking UgPart object.
        // This method implements the pure virtual method defined in
        // UgObject, and for this class this method simply returns the
        // invoking UgPart object.
        UgPart *askOwningPart ( ) const;

        // Return the full file name of the invoking UgPart object.
        const std::string getFullName ( ) const;
 
        // Return the customer definable area of the invoking UgPart object.
        const std::string getCustomerArea ( ) const;

        // Return the customer definable description of the invoking UgPart object.
        const std::string getDescription ( ) const;

        // Return the customer definable status of the invoking UgPart object.
        int getStatus ( ) const;
      
        // Iterate to the first typed object owned by the invoking UgPart object.
        // This method should be used to begin the iteration over typed
        // objects in a part.  If there are no typed objects in the part,
        // this method will return 0.  If there are typed objects in the
        // part, the typed object returned by this method should be passed
        // to the iterateNext() method to continue the iteration.
        UgTypedObject *iterateFirst ( ) const;
        
        // Iterate to the next typed object owned by the invoking UgPart object.
        // Iteration is begun by invocation of the iterateFirst() method.
        // When all typed objects in a part have been returned, this
        // method will return 0.
        UgTypedObject *iterateNext
        (
            const UgTypedObject *prev_object  // <I>
                                              // The previous object as obtained via
                                              // an invocation of either the iterateFirst()
                                              // or iterateNext() methods.
        ) const;

        // Edit the full file name of the invoking UgPart object.
        // The new name chosen cannot be the name of another NX part file
        // on disk, or an exception will be thrown.  The new name will
        // also be the name of the part attribute object in the part.
        void setFullName
        (
            const std::string &file_name      // <I>
                                              // The new file name ( on disk ) for
                                              // the NX part.
        );
        
        // Edit the customer definable area of the invoking UgPart object.
        void setCustomerArea
        (
            const std::string &customer_area  // <I>
                                              // The new customer definable
                                              // area for the NX part.
        );

        // Edit the customer definable description of the invoking UgPart object.
        void setDescription
        (
            const std::string &description    // <I>
                                              // The new customer definable
                                              // description for the NX part.
        );

        // Edit the customer definable status of the invoking UgPart object.
        void setStatus
        (
            int status  // <I>
                        // The new customer definable status for the NX part.
        );

        // Create a UgPart object by creating a new Unigraphics part.
        static UgPart *create
        (
            const std::string &file_name,    // <I>
                                             // The file name ( on disk ) for
                                             // the new NX part.
            UgUnits            units         // <I>
                                             // The units the part's objects
                                             // will be created in.
        );

        // Create a UgPart object by opening an existing Unigraphics part.
        static UgPart *open
        (
            const std::string &file_name,    // <I>
                                             // The file name ( on disk ) of
                                             // the existing NX part.
            PartLoadStatus    *status = 0    // <I>
                                             // The PartLoadStatus object that
                                             // describes the results of this
                                             // operation.  If the default argument
                                             // is used, the PartLoadStatus object is
                                             // not returned.
        );

        // Close the invoking UgPart object.
        // Closing a modified part will not save the changes made to the part.
        void close
        (
            bool part_and_subassemblies  // <I>
                                         // If true, the part and all its 
                                         // subassemblies will be closed.
                                         // If false, only the invoking
                                         // UgPart object will be closed.
        );

        // Save the invoking UgPart object to the disk.
        void save ( );

        // Save the invoking UgPart object to the disk, giving it a new file name. 
        void saveAs
        (
            const std::string &file_name   // <I>
                                           // The new file name ( on disk ) for
                                           // the NX part.
        );

        // Create a UgAssemblyNode object by adding a part to the invoking UgPart
        // object. If the part to add is not already loaded, it is loaded into the
        // current session. The returned object has the invoking UgPart object as
        // its owner.
        UgAssemblyNode *addPart
        (
            const std::string &part_name,     // <I>
                                              // Name of the part to add. Can include a
                                              // directory
            const std::string &ref_set_name,  // <I>
                                              // Name of the reference set to use from
                                              // component part. Can not exceed 30 chars
                                              // Can not include a directory path and 
                                              // should not have a file extension. 
                                              // If Empty, the entire part is used.
            const std::string &related_name,  // <I>
                                              // Name of the new object and all related
                                              // objects that result from this operation,
                                              // Can not exceed 30 chars, can not include
                                              // a directory path and should not have a
                                              // file extension. If empty, the related 
                                              // objects will be unnamed
            const CoordSys    &orientation,   // <I>
                                              // Position and orientation in Absolute
                                              // Coordinates in the invoking object.
            int                layer,         // <I>
                                              //  = -1 Use the original layers <br>
                                              //  =  0 Use the work layer <br>
                                              //  >  0 Specifies the work layer to use
            PartLoadStatus    *status = 0     // <O>
                                              // Returned object that specifies the names
                                              // and error codes of the parts that failed 
                                              // to load. If default is used, this object
                                              // is not returned.
        );

        // Return a std::vector object that contains all of the UgAssemblyNode objects of
        // the given UgPart object under the assembly of the invoking UgPart object.
        const std::vector < UgAssemblyNode * > askAllAssemblyNodes
        (
            const UgPart *part // <I>
                               // UgPart that has UgAssemblyNode objects under the
                               // assembly of the invoking UgPart object.
        ) const;

        // Return the UgAssemblyNode object that has the given related name and is 
        // owned by the invoking UgPart object. Return a zero if no such object exists.
        UgAssemblyNode *askAssemblyNode 
        (
            const std::string &related_name   // <I> 
                                              // Name of the requested UgAssemblyNode object
                                              // Can not exceed 30 chars, can not include
                                              // a directory path and should not have a
                                              // file extension
        ) const;

        // Return true if the given part is a descendant of the invoking UgPart object.
        // The descendent part does not have to be a direct child of the parent.
        // Return true if the descendent part and the invoking UgPart object are the
        // same.
        bool isDescendant
        (
            const UgPart *descendent_part // <I>
                                          // The descendent UgPart object
        ) const;

    protected:

        // Construct a UgPart object
        UgPart
        (
            tag_t tag = NULL_TAG            // The tag of the NX database object that
                                            // the UgPart object corresponds to.
        );

        // Destroy a UgPart object
        virtual ~UgPart ( );

    private:

        // Find the UgAssemblyNode object that corresponds to the specified instance tag
        // and is owned by the invoking UgPart object.  If the UgAssemblyNode object 
        // cannot be found, then this method will throw an exception.
        UgAssemblyNode * findAssemblyNode
        (
            tag_t instance_tag              // <I>
                                            // The instance tag used to find the
                                            // UgAssemblyNode object.
        ) const;

    // The UgReferenceSet class is a friend to make use of the findAssemblyNode ( )
    // method of this class.
    friend class UgReferenceSet;

    // The UgAssemblyNode class is a friend to make use of the findAssemblyNode ( )
    // method of this class.
    friend class UgAssemblyNode;

};

#undef EXPORTLIBRARY

#endif  // UG_PART_INCLUDED
