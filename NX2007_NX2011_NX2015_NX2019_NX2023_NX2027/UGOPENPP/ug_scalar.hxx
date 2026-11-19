/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Scalar C++ class definitions.

================================================================================

*/

#ifndef UG_SCALAR_INCLUDED
#define UG_SCALAR_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_session.hxx>
#include <ug_typed.hxx>
#include <ug_smart.hxx>
#include <ug_part.hxx>

#include <ug_string.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgExpression;

// This class defines the interface for the creation and manipulation of
// NX scalar objects.
class OPENPPEXPORT UgScalar : public UgTypedObject, 
                                   public UgSmartObject
{

    UG_DECLARE_INTERNAL_CLASS ( UgScalar )

    public:

        // This enum defines the dimensionality units that are available to scalar objects.
        // Associating the correct dimensionality to a scalar allows the scalar to be
        // correctly converted when the part is converted from one unit to another.
        enum Dimensionality
        {
            NoDimensionality  = UF_SO_scalar_dimensionality_none,           //
                                                // The scalar has no dimensionality units; it
                                                // is a pure number.
            Length            = UF_SO_scalar_dimensionality_length,         //
                                                // The scalar has the dimensionality of length.
            Area              = UF_SO_scalar_dimensionality_area,           //
                                                // The scalar has the dimensionality of area,
                                                // or length squared.
            Volume            = UF_SO_scalar_dimensionality_volume          //
                                                // The scalar has the dimensionality of volume,
                                                // or length cubed.
        };

        // Create a dimensioned UgScalar object from a constant double value.
        static UgScalar *create 
        ( 
            UpdateOption        update_option,  // <I>
                                                // The option that specifies the update behavior
                                                // of the scalar.
            Dimensionality      dimensionality, // <I> 
                                                // The dimension of the scalar.
            double              value,          // <I>
                                                // The double constant that represents the value
                                                // of the scalar.
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

        // Create a dimensioned UgScalar object from an expression object.
        static UgScalar *create 
        ( 
            UpdateOption        update_option,  // <I>
                                                // The option that specifies the update behavior
                                                // of the scalar.
            Dimensionality      dimensionality, // <I> 
                                                // The dimension of the scalar.
            const UgExpression *expression,     // <I>
                                                // The expression that represents the value
                                                // of the scalar.
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

        // Return the expression of the invoking object.
        UgExpression *askExpression ( ) const;

        // Return the value of the invoking object.
        double getValue ( ) const;

        // Edit the value of the invoking object.
        void setValue
        (
            double value                    // <I>
                                            // The new value of the scalar.
        );

        // Replace the parameters of the invoking object with the parameters of
        // a given UgSmart object, and then delete input UgSmart object.
        void replaceParameters
        (
            UgScalar *scalar                // <I>
                                            // The UgScalar object that supplies the
                                            // replacing parameters.
        );

    protected:

        // Initialize a UgScalar object by actually creating an NX database scalar
        // from a constant double value.
        void initialize 
        ( 
            UpdateOption    update_option,      // <I>
                                                // The option that specifies the update behavior
                                                // of the scalar.
            Dimensionality  dimensionality,     // <I> 
                                                // The dimension of the scalar.
            double          value,              // <I>
                                                // The double constant that represents the value
                                                // of the scalar.
            const UgObject *part_or_object = UgSession::getWorkPart ( )
                                                // <I>
                                                // This argument defines the owning part of
                                                // the new object.  If the argument is a
                                                // UgPart object, the argument is the owning
                                                // part of the new object.  If the argument
                                                // is not a UgPart object, the part that owns
                                                // the argument is the owning part of the new
                                                // object.
        );

        // Initialize a UgScalar object by actually creating an NX database scalar
        // from an expression object.
        void initialize 
        ( 
            UpdateOption        update_option,  // <I>
                                                // The option that specifies the update behavior
                                                // of the scalar.
            Dimensionality      dimensionality, // <I> 
                                                // The dimension of the scalar.
            const UgExpression *expression,     // <I>
                                                // The expression that represents the value
                                                // of the scalar.
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

        // Construct a UgScalar object
        UgScalar
        (
            tag_t tag = NULL_TAG            // The tag of the NX database scalar that the
                                            // UgScalar object corresponds to.
        );

        // Destroy a UgScalar object
        virtual ~UgScalar ( );

};

#undef EXPORTLIBRARY

#endif  // UG_SCALAR_INCLUDED
