#ifndef NXOpen_ROUTING_BUILTINPATHCOLLECTION_HXX_INCLUDED
#define NXOpen_ROUTING_BUILTINPATHCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_BuiltInPathCollection.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class BuiltInPathCollection;
    }
    namespace Routing
    {
        class RouteManager;
    }
    namespace Routing
    {
        class BuiltInPath;
    }
    class Curve;
    namespace Routing
    {
        /** Represents a collection of @link BuiltInPath BuiltInPath@endlink  objects.  <br> To obtain an instance of this class, refer to @link RouteManager RouteManager@endlink  <br> */
        class NXOPENCPPEXPORT BuiltInPathCollection : public TaggedObjectCollection
        {
            private: NXOpen::Routing::RouteManager* m_owner;
            public: explicit BuiltInPathCollection(NXOpen::Routing::RouteManager *owner): m_owner(owner)
            {
            }
            public: tag_t Tag() const;
            class iterator
            {
            public:
                typedef Routing::BuiltInPath * value_type;
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::Routing::BuiltInPathCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                }
                iterator(const iterator &other)
                {
                    copy(other);
                }
                iterator &operator =(const iterator &other)
                {
                    if (&other != this)
                        copy(other);
                    return *this;
                }
                bool operator ==(const iterator &other) const
                {
                    return m_current == other.m_current && m_context == other.m_context;
                }
                bool operator !=(const iterator &other) const
                {
                    return !operator == (other);
                }
                NXOPENCPPEXPORT  value_type operator * ();
                iterator & operator ++()
                {
                    next();
                    return *this;
                }
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
                NXOpen::Routing::BuiltInPathCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            iterator begin();
            iterator end()
            {
                return iterator(this);
            }
            /** Creates a @link Routing::BuiltInPath Routing::BuiltInPath@endlink  object.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::BuiltInPath * CreateBuiltInPath
            (
                const std::vector<NXOpen::Curve *> & curves /** the array of Curves to be referenced by the Built-In-Path */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
