#ifndef NXOpen_ROUTING_CORNERCOLLECTION_HXX_INCLUDED
#define NXOpen_ROUTING_CORNERCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_CornerCollection.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Routing_Corner.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class CornerCollection;
    }
    namespace Routing
    {
        class RouteManager;
    }
    namespace Routing
    {
        class Corner;
    }
    namespace Routing
    {
        class ControlPoint;
    }
    namespace Routing
    {
        /** Represents a collection of @link Routing::Corner Routing::Corner@endlink  objects.  <br> To obtain an instance of this class, refer to @link Routing::RouteManager Routing::RouteManager@endlink  <br> */
        class NXOPENCPPEXPORT CornerCollection : public TaggedObjectCollection
        {
            private: NXOpen::Routing::RouteManager* m_owner;
            public: explicit CornerCollection(NXOpen::Routing::RouteManager *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Routing::Corner * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::Routing::CornerCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                }
                iterator(const iterator &other)
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
                NXOpen::Routing::CornerCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            /** Returns an iterator addressing the first element. */
            iterator begin();
            /** Returns an iterator addressing the last element. */
            iterator end()
            {
                return iterator(this);
            }
            /** Gets the corner information given a @link Routing::ControlPoint Routing::ControlPoint@endlink .  @return  @link Routing::Corner Routing::Corner@endlink  associated
                                                                     with this RCP  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::Corner * GetRcpCornerInfo
            (
                NXOpen::Routing::ControlPoint * rcp /** Object to interrogate */,
                NXOpen::Routing::Corner::Type* corner_type /** Type of corner.*/
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif