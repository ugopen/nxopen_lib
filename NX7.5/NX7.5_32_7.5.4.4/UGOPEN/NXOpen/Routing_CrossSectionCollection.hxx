#ifndef NXOpen_ROUTING_CROSSSECTIONCOLLECTION_HXX_INCLUDED
#define NXOpen_ROUTING_CROSSSECTIONCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_CrossSectionCollection.ja
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
#include <NXOpen/Routing_StockData.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class CrossSectionCollection;
    }
    namespace Routing
    {
        class RouteManager;
    }
    namespace Routing
    {
        class CrossSection;
    }
    class Curve;
    class Expression;
    namespace Routing
    {
        class CrossSectionCollectionImpl;
        /** Represents a collection of @link Routing::CrossSection Routing::CrossSection@endlink  objects.   <br> To obtain an instance of this class, refer to @link Routing::RouteManager Routing::RouteManager@endlink  <br> */
        class NXOPENCPPEXPORT  CrossSectionCollection : public TaggedObjectCollection
        {
            private: CrossSectionCollectionImpl * m_crosssectioncollection_impl;
            private: NXOpen::Routing::RouteManager* m_owner;
            /** Constructor */
            public: explicit CrossSectionCollection(NXOpen::Routing::RouteManager *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~CrossSectionCollection();
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Routing::CrossSection * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::Routing::CrossSectionCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Routing::CrossSectionCollection *m_context;
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
            /** Creates a new @link Routing::CrossSection Routing::CrossSection@endlink  object.  This object
                      defines a profile for sweeping @link Routing::Stock Routing::Stock@endlink  objects. In
                      order to build stocks using this cross section, the cross section must be
                      contained in a @link Routing::StockData Routing::StockData@endlink  object.
                      @return   <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: NXOpen::Routing::CrossSection * CreateCrossSection
            (
                const std::vector<NXOpen::Curve *> & crossCurves /** cross curves */ ,
                NXOpen::Expression * offset /** First Offset value, may be NULL */,
                NXOpen::Expression * secondOffset /** Second Offset value, may be NULL */,
                NXOpen::Routing::StockStyle style /** style */ 
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif