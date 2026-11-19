/*
================================================================================

           Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Expression object C++ class definitions

================================================================================

*/

#ifndef UG_EXPRESSION_INCLUDED
#define UG_EXPRESSION_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_in_part.hxx>
#include <ug_session.hxx>
#include <ug_part.hxx>

#include <ug_string.hxx>
#include <libopenpp_exports.hxx>

// This class defines the interface for the creation and manipulation of
// NX expression objects.  An expression is composed of a std::string object that
// defines the Left Hand Side ( LHS ) and a std::string object that defines the Right
// Hand Side ( RHS ).  A fully formed std::string representation contains the both
// the LHS and the RHS:  LHS=RHS.
class OPENPPEXPORT UgExpression : public UgInPartObject
{

    UG_DECLARE_INTERNAL_CLASS ( UgExpression )

    public:
        
        // Create a UgExpression object by specifying a fully formed string
        // representation of the expression.  
        static UgExpression *create
        ( 
            const std::string  &expression, // <I>
                                            // The fully formed string representation
                                            // of the expression in the form LHS=RHS.
            const UgObject     *part_or_object = UgSession::getWorkPart ( )
                                            // <I>
                                            // This argument defines the owning part of
                                            // the new object.  If the argument is a
                                            // UgPart object, the argument is the owning
                                            // part of the new object.  If the argument
                                            // is not a UgPart object, the part that owns
                                            // the argument is the owning part of the new
                                            // object.
        );

        // Create a UgExpression object by specifying both the LHS string and the
        // RHS string that compose the expression.  
        static UgExpression *create
        ( 
            const std::string  &LHS,        // <I>
                                            // The Left Hand Side of the expression
            const std::string  &RHS,        // <I>
                                            // The Right Hand Side of the expression
            const UgObject     *part_or_object = UgSession::getWorkPart ( )
                                            // <I>
                                            // This argument defines the owning part of
                                            // the new object.  If the argument is a
                                            // UgPart object, the argument is the owning
                                            // part of the new object.  If the argument
                                            // is not a UgPart object, the part that owns
                                            // the argument is the owning part of the new
                                            // object.
        );

        // Create a UgExpression object by specifying the LHS string and a constant
        // value that represents the RHS that compose the expression.  
        static UgExpression *create
        ( 
            const std::string  &LHS,        // <I>
                                            // The Left Hand Side of the expression
            double              RHS,        // <I>
                                            // The constant value for the Right Hand
                                            // Side of the expression
            const UgObject     *part_or_object = UgSession::getWorkPart ( )
                                            // <I>
                                            // This argument defines the owning part of
                                            // the new object.  If the argument is a
                                            // UgPart object, the argument is the owning
                                            // part of the new object.  If the argument
                                            // is not a UgPart object, the part that owns
                                            // the argument is the owning part of the new
                                            // object.
        );

        // Create a unique UgExpression object by specifying both the LHS string and the
        // RHS string that compose the expression.
        // If an expression with the LHS string does not already exist in the specified
        // owning part, then this method behaves the same as the normal create method.
        // If an expression with the LHS string already exists in the specified owning
        // part, then the LHS string will have integers appended to it in sequence
        // until a LHS string is created that does not already exist in the specified
        // owning part; that new LHS string is used to create the UgExpression object.
        // E.g., if LHS is "radius" and there are no expressions in the specified
        // owning part with that LHS, then a new UgExpression object with a LHS of
        // "radius" will be created.  If the method is invoked again with the same LHS,
        // then a new UgExpression object with a LHS of "radius1" will be created.
        static UgExpression *createUnique
        ( 
            const std::string  &LHS,        // <I>
                                            // The Left Hand Side of the expression
            const std::string  &RHS,        // <I>
                                            // The Right Hand Side of the expression
            const UgObject     *part_or_object = UgSession::getWorkPart ( )
                                            // <I>
                                            // This argument defines the owning part of
                                            // the new object.  If the argument is a
                                            // UgPart object, the argument is the owning
                                            // part of the new object.  If the argument
                                            // is not a UgPart object, the part that owns
                                            // the argument is the owning part of the new
                                            // object.
        );

        // Create a unique UgExpression object by specifying the LHS string and a constant
        // value that represents the RHS that compose the expression.  
        // If an expression with the LHS string does not already exist in the specified
        // owning part, then this method behaves the same as the normal create method.
        // If an expression with the LHS string already exists in the specified owning
        // part, then the LHS string will have integers appended to it in sequence
        // until a LHS string is created that does not already exist in the specified
        // owning part; that new LHS string is used to create the UgExpression object.
        // E.g., if LHS is "radius" and there are no expressions in the specified
        // owning part with that LHS, then a new UgExpression object with a LHS of
        // "radius" will be created.  If the method is invoked again with the same LHS,
        // then a new UgExpression object with a LHS of "radius1" will be created.
        static UgExpression *createUnique
        ( 
            const std::string  &LHS,        // <I>
                                            // The Left Hand Side of the expression
            double              RHS,        // <I>
                                            // The constant value for the Right Hand
                                            // Side of the expression
            const UgObject     *part_or_object = UgSession::getWorkPart ( )
                                            // <I>
                                            // This argument defines the owning part of
                                            // the new object.  If the argument is a
                                            // UgPart object, the argument is the owning
                                            // part of the new object.  If the argument
                                            // is not a UgPart object, the part that owns
                                            // the argument is the owning part of the new
                                            // object.
        );

        // Determine if a UgExpression object with the specified LHS exists in the
        // specified owning part.
        static bool isExpression
        (
            const std::string  &LHS,        // <I>
                                            // The Left Hand Side of the expression
            const UgObject     *part_or_object = UgSession::getWorkPart ( )
                                            // <I>
                                            // This argument defines the owning part in
                                            // which to search for the object.  If the
                                            // argument is a UgPart object, the argument
                                            // is the owning part in which to search.
                                            // If the argument is not a UgPart object,
                                            // the part that owns the argument is the
                                            // owning part in which to search.
        );

        // Return the UgExpression of the Left Hand Side.
        // Return 0 if no expression exists with the given Left Hand Side.
        static UgExpression *askExpression 
        (
            const std::string  &LHS,        // <I>
                                            // The Left Hand Side of the expression
            const UgObject     *part_or_object = UgSession::getWorkPart ( )
                                            // <I>
                                            // This argument defines the owning part in
                                            // which to search for the object.  If the
                                            // argument is a UgPart object, the argument
                                            // is the owning part in which to search.
                                            // If the argument is not a UgPart object,
                                            // the part that owns the argument is the
                                            // owning part in which to search.
        );

        // Return the value of the Right Hand Side of the invoking object.
        double askValue ( ) const;

        // Return the descriptor of the Right Hand Side of the invoking object,
        // The descriptor is the parameter "name" of the expression.
        const std::string askDescriptor ( ) const;

        // Return the Left Hand Side of the invoking object.
        const std::string getLHS ( ) const;
 
        // Return the Right Hand Side of the invoking object.
        const std::string getRHS ( ) const;

        // Edit the Left Hand Side of the invoking object.
        // An exception will be thrown if the new LHS chosen for the expression already 
        // exists in the owning part of the invoking object.  Changing the LHS does not
        // affect the associativity between the invoking object and other NX objects.
        // E.g, if the LHS of an expression is "P1" and it controls the width of a
        // block, then changing the LHS of that expression to "WIDTH" will not affect
        // that the expression still controls the width of the block
        void setLHS
        (
            const std::string  &LHS         // <I>
                                            // The new Left Hand Side of the expression
        );
        
        // Edit the Right Hand Side of the invoking object using a std::string.
        void setRHS
        (
            const std::string  &RHS         // <I>
                                            // The new Right Hand Side of the expression
        );

        // Edit the Right Hand Side of the invoking object using a constant value.
        void setRHS
        (
            double              RHS         // <I>
                                            // The new constant value for the Right Hand
                                            // Side of the expression
        );   
        
        // Delete the NX database object that corresponds to the invoking object.
        // This method is provided to satisfy the pure virtual method defined in
        // the class UgInPartObject.
        void destroy ( );

    protected:

        // Construct a UgExpression object
        UgExpression
        (
            tag_t tag = NULL_TAG            // The tag of the NX database expression that
                                            // the UgExpression object corresponds to.
        );

        // Destroy a UgExpression object
        virtual ~UgExpression ( );

};

#undef EXPORTLIBRARY

#endif  // UG_EXPRESSION_INCLUDED
