#ifndef NXOpen_MECHATRONICS_COLLISIONSENSORCOLLECTION_HXX_INCLUDED
#define NXOpen_MECHATRONICS_COLLISIONSENSORCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_CollisionSensorCollection.ja
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
#include <NXOpen/Mechatronics_CollisionSensor.hxx>
#include <NXOpen/Mechatronics_CollisionSensorBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Mechatronics
    {
        class CollisionSensorCollection;
    }
    namespace Mechatronics
    {
        class PhysicsManager;
    }
    namespace Mechatronics
    {
        class CollisionSensor;
    }
    namespace Mechatronics
    {
        class CollisionSensorBuilder;
    }
    namespace Mechatronics
    {
        class CollisionSensorCollectionImpl;
        /** Represents a collection of Collision Sensor.  <br> To obtain an instance of this class, refer to @link Mechatronics::PhysicsManager Mechatronics::PhysicsManager@endlink  <br> */
        class NXOPENCPPEXPORT  CollisionSensorCollection : public TaggedObjectCollection
        {
            private: CollisionSensorCollectionImpl * m_collisionsensorcollection_impl;
            private: NXOpen::Mechatronics::PhysicsManager* m_owner;
            /** Constructor */
            public: explicit CollisionSensorCollection(NXOpen::Mechatronics::PhysicsManager *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~CollisionSensorCollection();
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Mechatronics::CollisionSensor * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::Mechatronics::CollisionSensorCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Mechatronics::CollisionSensorCollection *m_context;
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
            /** Creates a @link Mechatronics::CollisionSensorBuilder Mechatronics::CollisionSensorBuilder@endlink .  @return   <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::CollisionSensorBuilder * CreateCollisionSensorBuilder
            (
                NXOpen::Mechatronics::CollisionSensor * triggerBody /** @link Mechatronics::CollisionSensor Mechatronics::CollisionSensor@endlink  to be edited, if NULL then create a new one */
            );
            /** Finds the @link  Mechatronics::CollisionSensor   Mechatronics::CollisionSensor @endlink  with the given name.
                        An exception will be thrown if no object can be found with given name.  @return  @link  Mechatronics::CollisionSensor   Mechatronics::CollisionSensor @endlink  with this name.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::CollisionSensor * FindObject
            (
                const NXString & name /** The name of the @link  Mechatronics::CollisionSensor   Mechatronics::CollisionSensor @endlink . */
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
