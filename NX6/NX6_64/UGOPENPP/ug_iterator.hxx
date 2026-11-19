/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for NX Iterator C++ template definitions

================================================================================

*/

#ifndef UG_ITERATOR_INCLUDED
#define UG_ITERATOR_INCLUDED

/*==========================================================================

  ==========================================================================*/

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_expression.hxx>
#include <ug_exception.hxx>
#include <ug_vector.hxx>
#include <ug_session.hxx>
#include <ug_part.hxx>

#include <uf_modl.h>
#include <uf_part.h>
#include <uf_obj.h>
#include <uf.h>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgObject;

// This class defines the interface for the creation and manipulation of
// objects used to facilitate the cycling of objects within a specific
// part, or cycling all of the currently loaded parts within an NX session.
// The construction of an iterator provides a snapshot at a point in time
// with regards to the object being iterated over.  As a result, if a new
// instance of the object being iterated over is created after constructing
// the iterator, it will not be available during the iteration.  More
// significantly, deleting an instance of the object being iterated over 
// after contructing the iterator will cause failures to occur during the
// iteration.
template < class Leaf >         // The UgIterator class allows for the cycling
                                // of objects of this class.  Class Leaf may be
                                // any Leaf Open++ class derived from UgObject,
                                // or a user-defined class that is derived
                                // from a Leaf Open++ class.  If class Leaf is
                                // UgPart, then all open parts in the current
                                // session will be cycled.  If class Leaf is any
                                // other class, then all of the instances of that
                                // particular class within a specified part will
                                // be cycled.
class UgIterator
{

    public:

        // Construct a UgIterator object for objects of class Leaf.  If class Leaf
        // is derived from UgInPartObject, part_or_object specifies the part to iterate
        // over.  If class Leaf is UgPart, part_or_object plays no part in the
        // construction of the UgIterator object.
        UgIterator
        (
            const UgObject  *part_or_object = UgSession::getWorkPart ( )
                                            // This argument defines the part to
                                            // iterate over.  If the argument is a
                                            // UgPart object, the argument is the 
                                            // part to iterate over.  If the argument
                                            // is not a UgPart object, the part that owns
                                            // the argument is the part to iterate over.
        );
    
        // Destroy a UgIterator object.
        ~UgIterator ( );

        // Find the next object of class Leaf in the invoking object.
        void findNext ( );

        // Return a pointer to the current object of class Leaf in the invoking object.
        Leaf *operator* ( ) const;

        // Determine if the invoking object has completed iterating over all objects of
        // class Leaf.
        bool isFinished ( ) const;
        
        // Reinitialize the invoking object to iterate again over objects of class Leaf.
        // This can be useful if all objects of class Leaf in a part different than the
        // part specified in the constructor are to be cycled over.  If class Leaf is
        // derived from UgInPartObject, part_or_object specifies the part to iterate
        // over.  If class Leaf is UgPart, part_or_object plays no part in the 
        // reinitialization of the UgIterator object.
        void reinitialize
        (
            const UgObject *part_or_object = UgSession::getWorkPart ( )
                                            // <I>
                                            // This argument defines the part to
                                            // iterate over.  If the argument is a
                                            // UgPart object, the argument is the 
                                            // part to iterate over.  If the argument
                                            // is not a UgPart object, the part that owns
                                            // the argument is the part to iterate over.
        );

    private:

        // Increment the invoking object to the next object of class Leaf.
        void increment ( );

        // The part being iterated over by the UgIterator object.  This member variable is
        // unused when iterating over UgPart objects.
        const UgPart          *m_part;

        // The current object of class Leaf held by the UgIterator object.
        const Leaf            *m_object;

        // This member variable is used when iterating over UgExpression
        // or UgPart objects.  If class Leaf is UgExpression, m_tags
        // holds all of the expression in m_part.  If class Leaf is
        // UgPart, m_tags holds all the parts in the NX session.
        std::vector < tag_t >  m_tags;

        // The index into the std::vector for either UgExpression or UgPart iterators.
        int                    m_index;

};

// ****************************************************************************
// Class implementation for UgIterator
// ****************************************************************************

// ****************************************************************************
// ****************************************************************************
// Do *_NOT_* rely on implementation details of the template!  The template
// implementation may change in the future.  Confine yourself to the public
// interface to the template.
// ****************************************************************************
// ****************************************************************************

// create a UgIterator for objects of class Leaf

template < class Leaf >
UgIterator < Leaf >::UgIterator ( const UgObject *part_or_object )
{
    reinitialize ( part_or_object );
}

// destroy a UgIterator for objects of class Leaf

template < class Leaf >
UgIterator < Leaf >::~UgIterator ( )
{
}

// find the next object of class Leaf in a UgIterator

template < class Leaf >
void UgIterator < Leaf >::findNext (  )
{    
    if ( m_object != 0 )
    {
        increment ( );
    }
}

// return a pointer to the current object of class Leaf in a UgIterator

template < class Leaf >
Leaf *UgIterator < Leaf >::operator* ( ) const
{
    return const_cast < Leaf * > ( m_object );
}

// is a UgIterator finished with all objects of class Leaf

template < class Leaf >
bool UgIterator < Leaf >::isFinished ( ) const
{
    return ( m_object == 0 );
}

// reinitialize a UgIterator for class Leaf

template < class Leaf >
void UgIterator < Leaf >::reinitialize ( const UgObject *part_or_object )
{
    m_part   =  part_or_object->askOwningPart ( );
    m_object =  0;
    m_index  = -1;
    
    m_tags.resize ( 0 );

    increment ( );
}

// increment a UgIterator to the next object of class Leaf

template < class Leaf >
void UgIterator < Leaf >::increment ( )
{
    int type = Leaf::askObjectType ( );                            
    
    if ( ( type != UF_OBJ_EXPR_TYPE ) && ( type != UF_OBJ_PART_TYPE ) )
    {
        tag_t tag = NULL_TAG;
        
        if ( m_object != 0 )
        {
            tag = m_object->getTag ( );
        }
        
        do
        {
            UgException::throwOnFailure ( UF_OBJ_cycle_objs_in_part ( m_part->getTag ( ), type, &tag ) );
            
            if ( tag == NULL_TAG ) 
            {
                m_object = 0;
            }
            else
            {
                UgObject *object = UgObject::find ( tag );
                m_object = dynamic_cast < Leaf * > ( object );
            }                 
        } while ( ( m_object == 0 ) && ( tag != 0 ) );
    }
    else // UF_OBJ_EXPR_TYPE || UF_OBJ_PART_TYPE
    {
        if ( m_object == 0 )
        {
            if ( type == UF_OBJ_EXPR_TYPE )
            {
                int    n_expressions;
                tag_t *expressions;
            
                UgException::throwOnFailure ( UF_MODL_ask_exps_of_part ( m_part->getTag ( ), &n_expressions, &expressions ) );
            
                m_tags.resize ( n_expressions );
            
                for ( int i = 0; i < n_expressions; i++ )
                {
                    m_tags [ i ] = expressions [ i ];
                }
            
                UF_free ( expressions );
            }
            else // UF_OBJ_PART_TYPE
            {
                int n_parts = UF_PART_ask_num_parts ( );
            
                m_tags.resize ( n_parts );
            
                for ( int i = 0; i < n_parts; i++ )
                {
                    m_tags [ i ] = UF_PART_ask_nth_part ( i );
                }
            }
        }

        m_index++;
        
        if ( m_index < m_tags.size ( ) )
        {
            UgObject *object = UgObject::find ( m_tags [ m_index ] );   
            m_object = dynamic_cast < Leaf * > ( object );
        }
        else
        {
            m_object =  0;
            m_index  = -1;
        }
    }
}

#endif  // UG_ITERATOR_INCLUDED
