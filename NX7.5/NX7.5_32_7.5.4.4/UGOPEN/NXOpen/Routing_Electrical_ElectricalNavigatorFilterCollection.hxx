#ifndef NXOpen_ROUTING_ELECTRICAL_ELECTRICALNAVIGATORFILTERCOLLECTION_HXX_INCLUDED
#define NXOpen_ROUTING_ELECTRICAL_ELECTRICALNAVIGATORFILTERCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_Electrical_ElectricalNavigatorFilterCollection.ja
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
#include <NXOpen/Routing_Electrical_ElectricalFormat.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        namespace Electrical
        {
            class ElectricalNavigatorFilterCollection;
        }
    }
    namespace Routing
    {
        class RouteManager;
    }
    namespace Routing
    {
        namespace Electrical
        {
            class ElectricalNavigatorFilter;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class ElectricalNavigatorFilterCollectionImpl;
            /** Represents a Routing @link ElectricalNavigatorFilterCollection ElectricalNavigatorFilterCollection@endlink  object.
                      <br> To obtain an instance of this class, refer to @link Routing::RouteManager Routing::RouteManager@endlink  <br> */
            class NXOPENCPPEXPORT  ElectricalNavigatorFilterCollection : public TaggedObjectCollection
            {
                private: ElectricalNavigatorFilterCollectionImpl * m_electricalnavigatorfiltercollection_impl;
                private: NXOpen::Routing::RouteManager* m_owner;
                /** Constructor */
                public: explicit ElectricalNavigatorFilterCollection(NXOpen::Routing::RouteManager *owner);
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                public: ~ElectricalNavigatorFilterCollection();
                /** Iterator for accessing the contents of the collection. */
                class iterator
                {
                public:
                    typedef Routing::Electrical::ElectricalNavigatorFilter * value_type;
                    /** Default constructor */
                    iterator() : m_context(NULL), m_current(NULL_TAG)
                    {
                    }//lint !e1401 m_state is not initialized 
                    explicit iterator(NXOpen::Routing::Electrical::ElectricalNavigatorFilterCollection *context) : m_context(context), m_current(NULL_TAG)
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
                    NXOpen::Routing::Electrical::ElectricalNavigatorFilterCollection *m_context;
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
                /** Creates a @link Routing::Electrical::ElectricalNavigatorFilter Routing::Electrical::ElectricalNavigatorFilter@endlink  object.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::Electrical::ElectricalNavigatorFilter * CreateFilter
                (
                    const NXString & name /** Name of the filter   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                    const NXString & clause /** Clause of the filter   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** Get the displayed @link Routing::Electrical::ElectricalNavigatorFilter Routing::Electrical::ElectricalNavigatorFilter@endlink  object
                                for the given navigator type  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::Electrical::ElectricalNavigatorFilter * GetDisplayFilter
                (
                    NXOpen::Routing::Electrical::ElectricalFormat::Type type /** type */ 
                );
                /** Set the @link Routing::Electrical::ElectricalNavigatorFilter Routing::Electrical::ElectricalNavigatorFilter@endlink  object as 
                                displayed filter for given navigator type.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void SetDisplayFilter
                (
                    NXOpen::Routing::Electrical::ElectricalFormat::Type type /** type */ ,
                    NXOpen::Routing::Electrical::ElectricalNavigatorFilter * filter /** filter */ 
                );
            }; //lint !e1712 default constructor not defined for class  

        }
    }
}
#undef EXPORTLIBRARY
#endif
