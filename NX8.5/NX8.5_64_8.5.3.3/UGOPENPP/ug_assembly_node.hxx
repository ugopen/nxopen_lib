/*
================================================================================

          Copyright (c) 1999-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for UgAssemblyNode C++ class definitions

================================================================================

*/

#ifndef UG_ASSEMBLY_NODE_INCLUDED
#define UG_ASSEMBLY_NODE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_displayable.hxx>
#include <libopenpp_exports.hxx>
#include <ug_vector.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class PartLoadStatus;
class CoordSys;
class UgPart;

// This class defines the interface for the creation and manipulation of
// NX assembly node objects.
class OPENPPEXPORT UgAssemblyNode : public UgDisplayableObject  
{

    UG_DECLARE_INTERNAL_CLASS ( UgAssemblyNode )

    public:

        // Return all the data of the invoking UgAssemblyNode object.
        void askData
        (
            std::string *part_name,    // <O>
                                       // The name of the part file.
            std::string *ref_set_name, // <O>
                                       // The name of the reference set in use. If the reference
                                       // set in use when the invoking object was created was
                                       // "Entire Part", then "None" will be returned here.
            std::string *related_name, // <O>
                                       // The name of the invoking object and all its related
                                       // UgAssemblyNode objects.
            CoordSys    *orientation,  // <O>
                                       // The position and orientation in Absolute Coordinate
                                       // System coordinates in the UgPart object where the
                                       // invoking object was created.
            double      *scale         // <O>
                                       // The scale factor. 
                                       // This value will be non-unity if there is a 
                                       // unit mix (inches/millimeters) between the
                                       // invoking object and its owning UgPart object.
        ) const;

        // Return the name of the reference set in use of the UgAssemblyNode 
        // invoking object.  NOTE: if the component reference set is set to  
        // Entire Part "None" will be returned.
        const std::string getReferenceSetName ( ) const;

        // Return the related name of the invoking UgAssemblyNode object. 
        const std::string getRelatedName ( ) const;
  
        // Return the position and orientation in Absolute Coordinate System coordinates
        // in the UgPart object where the invoking UgAssemblyNode object was created.
        const CoordSys getCoordSys ( ) const;

        // Return the scale factor of the invoking UgAssemblyNode object.
        // This value will be non-unity if there is a unit mix (inches/millimeters)
        // between the invoking object and its owning UgPart object.
        double askScale ( ) const;

        // Edit the name of the reference set used by the invoking UgAssemblyNode object
        // and all its related UgAssemblyNode objects.
        void setReferenceSetName
        (
            const std::string &ref_set_name // <I>
                                            // The name of new reference set of the invoking
                                            // object and all its related UgAssemblyNode
                                            // objects. If the argument is zero-length, the
                                            // entire part is used. If the argument is
                                            // "Empty", none of the part is displayed.
        ); 
        
        // Edit the related name of the invoking UgAssemblyNode object and all its
        // related UgAssemblyNode objects.
        void setRelatedName 
        (
            const std::string &related_name // <I>
                                            // The new related name of the invoking object
                                            // and all its related UgAssemblyNode objects.
        );

        // Edit the orientation of the invoking UgAssemblyNode object and all its
        // related UgAssemblyNode objects.
        void setCoordSys
        (
            const CoordSys &orientation  // <I>
                                         // The new position and orientation in Absolute
                                         // Coordinate System coordinates of the invoking
                                         // object and all its related UgAssemblyNode
                                         // objects.
        );

        // Replace the part of the invoking UgAssemblyNode object with a new part, and
        // return a new UgAssemblyNode object that corresponds to the new part. 
        // The invoking object is no longer valid after returning from this method.
        // The owning UgPart object of the invoking object owns the returned UgAssemblyNode
        // object. If the part to substitute is not already loaded, it is loaded into the
        // current session.
        UgAssemblyNode *substitute
        (
            const std::string &part_name,    // <I>
                                             // The name of the new part to substitute. The
                                             // part name can include a directory.
            const std::string &ref_set_name, // <I>
                                             // The name of the new reference set to use from
                                             // the new part. The name cannot exceed 30
                                             // characters, cannot include a directory path,
                                             // and should not have a file extension. If the
                                             // name is zero-length, the entire part is used
            const std::string &related_name, // <I>
                                             // The new name of the new UgAssemblyNode object
                                             // and all its related UgAssemblyNode objects
                                             // that result from this operation. The name cannot
                                             // exceed 30 characters, cannot include a directory
                                             // path, and should not have a file extension. If
                                             // the name is zero-length, the new UgAssemblyNode
                                             // object and all its related UgAssemblyNode
                                             // objects are unnamed.
            int                layer,        // <I>
                                             //  = -1, Use the original layers <br>
                                             //  =  0, Use the work layer <br>
                                             //  >  0, Specifies the layer to use
            PartLoadStatus    *status = 0    // <O>
                                             // Returned object that specifies the names and
                                             // error codes of the part files that failed to 
                                             // load. If the default argument is used, this
                                             // object is not returned.
        );

        // Remove the invoking UgAssemblyNode object and all its related UgAssemblyNode 
        // objects from an assembly part. The invoking object is no longer valid after
        // returning from this method, and neither are all its related UgAssemblyNode
        // objects.
        void remove ( );

        // Return a std::vector object that contains all of the UgAssemblyNode objects that
        // are under the invoking UgAssemblyNode object.  Return a zero-length std::vector
        // object if the invoking object has no children.
        const std::vector < UgAssemblyNode * > askChildren ( ) const ;

        // Return a std::vector object that contains all of the UgAssemblyNode objects that
        // are related to the invoking UgAssemblyNode object.  The returned std::vector
        // object will always include the invoking object.
        const std::vector < UgAssemblyNode * > askRelated ( ) const;

        // Return the UgPart object that was added to when the invoking UgAssemblyNode
        // object was created.
        UgPart *askRelatedOwningPart ( ) const;

        // Return the UgPart object whose addition to the assembly was responsible for the
        // invoking UgAssemblyNode object. If that UgPart object is unloaded, then 0 is
        // returned.
        UgPart *askPart ( ) const;

        // Return the name of the part whose addition to the assembly was responsible for 
        // the invoking UgAssemblyNode object. If that part is unloaded, then the file name
        // of the part using the current search options is returned. If the part is
        // unloaded and a part file of the correct name can not be found, an zero-length
        // std::string object is returned.
        const std::string askPartName ( ) const;

        // Ensure that the part whose addition to the assembly was responsible for the 
        // invoking UgAssemblyNode object is loaded. If the load of the part fails, then
        // the PartLoadStatus is returned with that information. If the default argument
        // is used, this method will throw an exception if the part fails to load.
        void ensurePartLoaded 
        (
             PartLoadStatus *status = 0  // <O>
                                         // Returned object that specifies the names and
                                         // error codes of the part files that failed to 
                                         // load. If default argument is used, this object
                                         // is not returned
        );

        // Return the count of object occurrences owned by the invoking UgAssemblyNode
        // object.
        int askOccurrenceCount ( ) const;

        // Iterate to the first object occurrence owned by the invoking UgAssemblyNode
        // object.  This method should be used to begin the iteration over object
        // occurrences in a UgAssemblyNode object. If there are no object occurrences in
        // the UgAssemblyNode object, this method will return 0. If there are object
        // occurrences in the UgAssemblyNode object, the object occurrence returned by this
        // method should be passed to iterateNext() to continue the iteration.
        UgDisplayableObject *iterateFirst ( ) const;

        // Iterate to the next object occurrence owned by the invoking UgAssemblyNode object.
        // Iteration is begun by invocation of the iterateFirst() method.  When all object
        // occurrences in the UgAssemblyNode object have been returned, this method will
        // return 0.
        UgDisplayableObject *iterateNext 
        (
             const UgDisplayableObject *prev_object // <I>
                                                    // The previous object as obtained via 
                                                    // an invocation of either the
                                                    // iterateFirst() or iterateNext()
                                                    // methods.
        );

    protected :

        // Construct a UgAssemblyNode object
        UgAssemblyNode
        (
             tag_t tag = NULL_TAG       // The tag of the NX database part occurrence that
                                        // the UgAssemblyNode object corresponds to.
        );

        // Destroy a UgAssemblyNode object
        virtual ~UgAssemblyNode ( );

    private :

        // Returns the NX database instance tag of the invoking UgAssemblyNode object.
        tag_t askInstanceTag ( ) const;
    
};

#undef EXPORTLIBRARY

#endif // UG_ASSEMBLY_NODE_INCLUDED
