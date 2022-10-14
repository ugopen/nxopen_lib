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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Routing_StockData.hxx>
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
        /** Represents a collection of @link Routing::CrossSection Routing::CrossSection@endlink  objects.   <br> To obtain an instance of this class, refer to @link RouteManager RouteManager@endlink  <br> */
        class NXOPENCPPEXPORT CrossSectionCollection : public TaggedObjectCollection
        {
            private: NXOpen::Routing::RouteManager* m_owner;
            public: explicit CrossSectionCollection(NXOpen::Routing::RouteManager *owner): m_owner(owner)
            {
            }
            public: tag_t Tag() const;
            class iterator
            {
            public:
                typedef Routing::CrossSection * value_type;
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::Routing::CrossSectionCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Routing::CrossSectionCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            iterator begin();
            iterator end()
            {
                return iterator(this);
            }
            /** Creates a new @link Routing::CrossSection Routing::CrossSection@endlink  object.  This object
                      defines a profile for sweeping @link Routing::Stock Routing::Stock@endlink  objects.  In
                      order to build stocks using this cross section, the cross section must be
                      contained in a @link Routing::StockData Routing::StockData@endlink  object.
                      @return   <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: NXOpen::Routing::CrossSection * CreateCrossSection
            (
                const std::vector<NXOpen::Curve *> & curves /** */,
                NXOpen::Expression * expression /** Offset value, may be NULL */,
                NXOpen::Routing::StockStyle style /** */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif