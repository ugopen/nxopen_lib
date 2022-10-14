#ifndef NXOpen_MECHATRONICS_SLIDINGJOINTCOLLECTION_HXX_INCLUDED
#define NXOpen_MECHATRONICS_SLIDINGJOINTCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_SlidingJointCollection.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Mechatronics_SlidingJoint.hxx>
#include <NXOpen/Mechatronics_SlidingJointBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Mechatronics
    {
        class SlidingJointCollection;
    }
    namespace Mechatronics
    {
        class PhysicsManager;
    }
    namespace Mechatronics
    {
        class SlidingJoint;
    }
    namespace Mechatronics
    {
        class SlidingJointBuilder;
    }
    namespace Mechatronics
    {
        class SlidingJointCollectionImpl;
        /** Represents a collection of Sliding Joint.  <br> To obtain an instance of this class, refer to @link Mechatronics::PhysicsManager Mechatronics::PhysicsManager@endlink  <br> */
        class NXOPENCPPEXPORT  SlidingJointCollection : public TaggedObjectCollection
        {
            private: SlidingJointCollectionImpl * m_slidingjointcollection_impl;
            private: NXOpen::Mechatronics::PhysicsManager* m_owner;
            /** Constructor */
            public: explicit SlidingJointCollection(NXOpen::Mechatronics::PhysicsManager *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~SlidingJointCollection();
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Mechatronics::SlidingJoint * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::Mechatronics::SlidingJointCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                iterator(const iterator &other): m_context(NULL), m_current(NULL_TAG)
                {
                    copy(other);
                }
                /** Copy constructor */
                iterator &operator =(const iterator &other)
                {
                    if (&other != this)
                        copy(other);
                    return *this;
                }
                /** Tests if the iterator objects on the left side and the right side of the operator are equal. */
                bool operator ==(const iterator &other) const
                {
                    return m_current == other.m_current && m_context == other.m_context;
                }
                /** Tests if the iterator objects on the left side and the right side of the operator are not equal. */
                bool operator !=(const iterator &other) const
                {
                    return !operator == (other);
                }
                /** Return the element currently pointed to by the iterator. */
                NXOPENCPPEXPORT  value_type operator * ();
                /** Points the iterator to next element. */
                iterator & operator ++()
                {
                    next();
                    return *this;
                }
                /** Points the iterator to next element. */
                iterator operator ++(int)
                {
                    iterator tmp(*this);
                    ++*this;
                    return tmp;
                }
            private:
                void copy(const iterator &other)
                {
                    m_context = other.m_context;
                    m_current = other.m_current;
                    for (int i = 0; i < sizeof(m_state)/sizeof(m_state[0]); i++)
                         m_state[i] = other.m_state[i];
                }
                NXOPENCPPEXPORT  void next();
                NXOpen::Mechatronics::SlidingJointCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            /** Returns an iterator addressing the first element. */
            iterator begin();
            /** Returns an iterator addressing one past the last element. */
            iterator end()
            {
                return iterator(this);
            }
            /** Creates a @link Mechatronics::SlidingJointBuilder Mechatronics::SlidingJointBuilder@endlink .  @return   <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::SlidingJointBuilder * CreateSlidingJointBuilder
            (
                NXOpen::Mechatronics::SlidingJoint * slide /** @link Mechatronics::SlidingJoint Mechatronics::SlidingJoint@endlink  to be edited, if NULL then create a new one */
            );
            /** Finds the @link  Mechatronics::SlidingJoint   Mechatronics::SlidingJoint @endlink  with the given name.
                        An exception will be thrown if no object can be found with given name.  @return  @link  Mechatronics::SlidingJoint   Mechatronics::SlidingJoint @endlink  with this name.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::SlidingJoint * FindObject
            (
                const NXString & name /** The name of the @link  Mechatronics::SlidingJoint   Mechatronics::SlidingJoint @endlink . */
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif