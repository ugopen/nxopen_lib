/*
================================================================================

          Copyright (c) 1999-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Feature C++ class definitions.

================================================================================

*/

#ifndef UG_FEATURE_INCLUDED
#define UG_FEATURE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_expression.hxx>
#include <ug_typed.hxx>

#include <ug_vector.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

// This class defines the interface for the manipulation of NX feature objects.
class OPENPPEXPORT UgFeatureObject : public UgTypedObject {

    public:

        // Suppress the given features.
        static void suppress 
        ( 
            const std::vector < UgFeatureObject * > &features
                                            // <I>
                                            // The features to be suppressed.
        );

        // Unsuppress the given features.
        static void unsuppress 
        ( 
            const std::vector < UgFeatureObject * > &features
                                            // <I>
                                            // The features to be unsuppressed.
        );

        // Delete the NX database objects that correspond to the given features.
        static void destroy 
        ( 
            const std::vector < UgFeatureObject * > &features
                                            // <I>
                                            // The features to be deleted.
        );

        // Is the invoking object suppressed ?
        bool isSuppressed ( ) const;

        // Return the name of the invoking object.
        const std::string getName ( ) const;
   
        // Returns true if the invoking object updates before the given feature.
        bool updatesBefore 
        ( 
            const UgFeatureObject *feature  // <I>
                                            // The given feature to compare
                                            // the invoking object against.
        ) const;

        // Return all of the expressions of the invoking object.
        // 'UgExpression::askDescriptor ( )' can be used to
        // get the feature parameter "name" of the expression.
        const std::vector < UgExpression * > askExpressions ( ) const;

        // Suppress the invoking object.
        void suppress ( );

        // Unsuppress the invoking object.
        void unsuppress ( );
        
        // Return the suppression expression of the invoking object.
        UgExpression *getSuppressionExpression ( ) const;

        // Set the suppression expression of the invoking object.
        void setSuppressionExpression
        ( 
            const UgExpression *expression  // <I>
                                            // The expression to be used as
                                            // the suppression expression of
                                            // the invoking object.
        );

        // Reorder the invoking object before the given features.
        void reorderBefore 
        ( 
            const std::vector < UgFeatureObject * > features
                                            // <I>
                                            // The features before the invoking 
                                            // object that are to be reordered 
                                            // after the invoking object.
        );

        // Reorder the invoking object after the given features.
        void reorderAfter 
        ( 
            const std::vector < UgFeatureObject * > features
                                            // <I>
                                            // The features after the invoking
                                            // object that are to be reordered
                                            // before the invoking object.
        );

        // Delete the NX database object that corresponds to the invoking object.
        void destroy ( );

   protected:

        // Construct a UgFeature object
        UgFeatureObject
        ( 
            tag_t tag = NULL_TAG            // The tag of the NX database feature that
                                            // the UgFeature object corresponds to. 
        );

        // Destroy a UgFeature object
        virtual ~UgFeatureObject ( );

    // The UgObject class is a friend to make use of the constructor of this class.
    friend class UgObject;

};

#undef EXPORTLIBRARY

#endif  // UG_FEATURE_INCLUDED
