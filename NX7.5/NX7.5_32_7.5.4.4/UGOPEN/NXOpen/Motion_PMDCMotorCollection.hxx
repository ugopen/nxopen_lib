#ifndef NXOpen_MOTION_PMDCMOTORCOLLECTION_HXX_INCLUDED
#define NXOpen_MOTION_PMDCMOTORCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_PMDCMotorCollection.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class PMDCMotorCollection;
    }
    namespace Motion
    {
        class MotionManager;
    }
    namespace Motion
    {
        class PMDCMotor;
    }
    namespace Motion
    {
        class PMDCMotorBuilder;
    }
    namespace Motion
    {
        class PMDCMotorCollectionImpl;
        /** Represents a collection of motion pmdc motor  <br> To obtain an instance of this class, refer to @link Motion::MotionManager Motion::MotionManager@endlink  <br> */
        class NXOPENCPPEXPORT  PMDCMotorCollection : public TaggedObjectCollection
        {
            private: PMDCMotorCollectionImpl * m_pmdcmotorcollection_impl;
            private: NXOpen::Motion::MotionManager* m_owner;
            /** Constructor */
            public: explicit PMDCMotorCollection(NXOpen::Motion::MotionManager *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~PMDCMotorCollection();
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Motion::PMDCMotor * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::Motion::PMDCMotorCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Motion::PMDCMotorCollection *m_context;
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
            /**   Return  @link  Motion::PMDCMotorBuilder   Motion::PMDCMotorBuilder @endlink  object   @return  PMDCMotorBuilder object  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: NXOpen::Motion::PMDCMotorBuilder * CreatePmdcMotorBuilder
            (
                NXOpen::Motion::PMDCMotor * pmdcMotor /** @link  Motion::PMDCMotor   Motion::PMDCMotor @endlink  to be edited, 
                                                                                     if NULL then create a new one */
            );
            /** Finds the @link  Motion::PMDCMotor   Motion::PMDCMotor @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name.  @return    <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: NXOpen::Motion::PMDCMotor * FindObject
            (
                const NXString & name /** name */ 
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
