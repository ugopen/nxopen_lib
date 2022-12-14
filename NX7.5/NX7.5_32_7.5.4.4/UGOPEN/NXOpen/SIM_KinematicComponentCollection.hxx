#ifndef NXOpen_SIM_KINEMATICCOMPONENTCOLLECTION_HXX_INCLUDED
#define NXOpen_SIM_KINEMATICCOMPONENTCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SIM_KinematicComponentCollection.ja
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
    namespace SIM
    {
        class KinematicComponentCollection;
    }
    namespace SIM
    {
        class KinematicConfigurator;
    }
    namespace SIM
    {
        class KinematicComponent;
    }
    namespace SIM
    {
        class KinematicComponentBuilder;
    }
    namespace SIM
    {
        class KinematicComponentCollectionImpl;
        /** Represents the SimKimComponent Collection  <br> To obtain an instance of this class, refer to @link SIM::KinematicConfigurator SIM::KinematicConfigurator@endlink  <br> */
        class NXOPENCPPEXPORT  KinematicComponentCollection : public TaggedObjectCollection
        {
            private: KinematicComponentCollectionImpl * m_kinematiccomponentcollection_impl;
            private: NXOpen::SIM::KinematicConfigurator* m_owner;
            /** Constructor */
            public: explicit KinematicComponentCollection(NXOpen::SIM::KinematicConfigurator *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~KinematicComponentCollection();
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef SIM::KinematicComponent * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::SIM::KinematicComponentCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::SIM::KinematicComponentCollection *m_context;
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
            /** Finds the SIM.KinematicComponent object with the given identifier as recorded in a journal. @return  the found object  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: NXOpen::SIM::KinematicComponent * FindObject
            (
                const NXString & sid /** the name of the object */
            );
            /** Creates a builder for a kinematic component  @return  The component builder  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: NXOpen::SIM::KinematicComponentBuilder * CreateComponentBuilder
            (
                NXOpen::SIM::KinematicComponent * parent /** The parent for the new component.
                                                                                                         Can be NULL */,
                NXOpen::SIM::KinematicComponent * comp /** The component to edit. If NULL, a
                                                                                                         new component will be created  */
            );
            /** Creates a builder for a machine base component.  @return  The new machine base component builder  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: NXOpen::SIM::KinematicComponentBuilder * CreateMachineBaseComponentBuilder
            (
                NXOpen::SIM::KinematicComponent * machine /** The machine base component to edit.
                                                                                                    If NULL, then a new machine base component
                                                                                                    is created */
            );
            /** Creates a bulder for tool base component.  @return  The new tool base component builder  <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: NXOpen::SIM::KinematicComponentBuilder * CreateToolBaseComponentBuilder
            (
                NXOpen::SIM::KinematicComponent * tool /** The tool component to edit. If NULL,
                                                                                                    then a new tool base component is 
                                                                                                    created */
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
