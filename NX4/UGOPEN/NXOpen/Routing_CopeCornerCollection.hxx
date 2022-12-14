#ifndef NXOpen_ROUTING_COPECORNERCOLLECTION_HXX_INCLUDED
#define NXOpen_ROUTING_COPECORNERCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_CopeCornerCollection.ja
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
        class CopeCornerCollection;
    }
    namespace Routing
    {
        class RouteManager;
    }
    namespace Routing
    {
        class CopeCorner;
    }
    namespace Routing
    {
        class ControlPoint;
    }
    namespace Routing
    {
        class Stock;
    }
    namespace Routing
    {
        /** Represents a collection of @link CopeCorner CopeCorner@endlink  objects.  <br> To obtain an instance of this class, refer to @link RouteManager RouteManager@endlink  <br> */
        class NXOPENCPPEXPORT CopeCornerCollection : public TaggedObjectCollection
        {
            private: NXOpen::Routing::RouteManager* m_owner;
            public: explicit CopeCornerCollection(NXOpen::Routing::RouteManager *owner): m_owner(owner)
            {
            }
            public: tag_t Tag() const;
            class iterator
            {
            public:
                typedef Routing::CopeCorner * value_type;
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::Routing::CopeCornerCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Routing::CopeCornerCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            iterator begin();
            iterator end()
            {
                return iterator(this);
            }
            /** Create a cope corner object at RCP.  @return  The new cope corner object created.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::CopeCorner * CreateCope
            (
                NXOpen::Routing::ControlPoint * rcp /** Route control point to cope. */,
                const std::vector<NXOpen::Routing::Stock *> & stocks /** Stocks on cope */
            );
            /** This routine assigns a new cope corner to the given rcp and stocks  @return  The newly created Cope Corner  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::CopeCorner * AssignCopeCorner
            (
                NXOpen::Routing::ControlPoint * rcp /** Route control point to cope. */,
                const std::vector<NXOpen::Routing::Stock *> & stocks /** Stocks on cope */
            );
            /** This is a utility routine to return corner information given
                         a RCP which is "at" (referenced by) a Cope corner  @return  true  - Given rcp is the rcp of 
            									                  a cope corner.
                                                          false - otherwise  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool GetRcpCornerInfo
            (
                NXOpen::Routing::ControlPoint * rcp /** RCP being used */,
                NXOpen::Routing::CopeCorner ** cop_obj /** The cope corner object, if the input 
                										      RCP is where a cope corner object pointing to. */
            );
            /** This is a utility routine to return cope corners information given
                         a stock   @return  The cope corner objects associated with
                                                          the given stock.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Routing::CopeCorner *> GetCopesAssociatedToStock
            (
                NXOpen::Routing::Stock * stock /** Stock being used */
            );
            /** Given a RCP, get cope corners pointing to it  @return  Corner objects pointing to the rcp.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Routing::CopeCorner *> GetCopesAssociatedToRcp
            (
                NXOpen::Routing::ControlPoint * rcp /** RCP */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
