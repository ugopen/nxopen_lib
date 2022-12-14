#ifndef NXOpen_ROUTING_STOCKCOLLECTION_HXX_INCLUDED
#define NXOpen_ROUTING_STOCKCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_StockCollection.ja
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
#include <NXOpen/Routing_CharacteristicList.hxx>
#include <NXOpen/Routing_Stock.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class StockCollection;
    }
    namespace Routing
    {
        class RouteManager;
    }
    namespace Routing
    {
        class Stock;
    }
    namespace Assemblies
    {
        class Component;
    }
    class NXObject;
    namespace Routing
    {
        class Anchor;
    }
    namespace Routing
    {
        class CharacteristicList;
    }
    namespace Routing
    {
        class CrossSection;
    }
    namespace Routing
    {
        class ISegment;
    }
    namespace Routing
    {
        class StockData;
    }
    namespace Routing
    {
        /** Represents a collection of @link Routing::Stock Routing::Stock@endlink  objects.   <br> To obtain an instance of this class, refer to @link Routing::RouteManager Routing::RouteManager@endlink  <br> */
        class NXOPENCPPEXPORT StockCollection : public TaggedObjectCollection
        {
            private: NXOpen::Routing::RouteManager* m_owner;
            public: explicit StockCollection(NXOpen::Routing::RouteManager *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Routing::Stock * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::Routing::StockCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Routing::StockCollection *m_context;
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
            /** Creates a @link Routing::Stock Routing::Stock@endlink  object.  @return  The resulting array of newly created @link Routing::Stock Routing::Stock@endlink 
                                                        objects.  <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: std::vector<NXOpen::Routing::Stock *> CreateStock
            (
                NXOpen::Routing::StockData * stockData /** The @link Routing::StockData Routing::StockData@endlink  that defines the stock */,
                NXOpen::Routing::Anchor * anchor /** The @link Routing::Anchor Routing::Anchor@endlink  from the input 
                                                           @link Routing::StockData Routing::StockData@endlink  to use, NULL is allowed for
                                                           no anchor. */,
                NXOpen::Routing::CrossSection * crossSection /** The @link Routing::CrossSection Routing::CrossSection@endlink  from the input 
                                                           @link Routing::StockData Routing::StockData@endlink  to use, NULL is not allowed. */,
                const std::vector<NXOpen::Routing::ISegment *> & segments /** The array of @link Routing::ISegment Routing::ISegment@endlink  curves that
                                                                the stock must cover. */
            );
            /** Returns the @link Routing::Stock Routing::Stock@endlink  that controls the given component.  
                        Only returns a @link Routing::Stock Routing::Stock@endlink  if the input component is a component created 
                        by a Stock as Components stock object.  @return  Returns NULL if the input component is not controlled
                                                        by a @link Routing::Stock Routing::Stock@endlink   <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: NXOpen::Routing::Stock * GetComponentStock
            (
                NXOpen::Assemblies::Component * component /** component */ 
            );
            /**  Converts a part file from Legacy Stock into Stock as Components.  Converts all stocks
                         whose use is @link NXOpen::Routing::StockUseLegacyStock NXOpen::Routing::StockUseLegacyStock@endlink  into @link NXOpen::Routing::StockUseStockAsComponent NXOpen::Routing::StockUseStockAsComponent@endlink 
                         stocks by creating components for each stock.  After calling this routine, all new stocks in this part
                         will have components associated with them.   <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: void ConvertToStockAsComponents
            (
                NXOpen::Routing::ComponentName nameType /** Naming scheme to use for components.  Calls 
                                                                               @link Routing::Stock::RenameComponent Routing::Stock::RenameComponent@endlink  on 
                                                                               each new stock component if input is 
                                                                               @link Routing::ComponentNamePermanent Routing::ComponentNamePermanent@endlink . */
            );
            /** Creates stock on the given segments. The segments do not need to be in order, and don't
                    necessarily have to form a single path.  <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: void AddStock
            (
                NXOpen::Routing::CharacteristicList * stockPart /** Characteristic list used to find the appropriate
                                                                                                                      @link Routing::StockData Routing::StockData@endlink  for building the stock.  
                                                                                                                      See @link Routing::StockDataCollection::CreateStockData Routing::StockDataCollection::CreateStockData@endlink . */,
                NXOpen::Routing::CharacteristicList * dataCharx /** The list of optional and required characteristics to apply to the new stock. */,
                const std::vector<NXOpen::Routing::ISegment *> & segments /** segments */ ,
                const NXString & routeLevel /** Routing level.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Removes all stocks (excluding flexed stocks) from the input set of segments.  <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: void RemoveStock
            (
                const std::vector<NXOpen::Routing::ISegment *> & segments /** segments */ 
            );
            /** Calls the STOCK_COMPONENT_NAME plugin function to rename a set of stock component parts.  <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: void RenameStockComponents
            (
                const std::vector<NXOpen::Routing::Stock *> & stocks /** stocks */ 
            );
            /** Update the bundle stock if the @link Routing::Filler Routing::Filler@endlink  stock is created underneath it.  <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: void UpdateBundleStockForFiller
            (
                const std::vector<NXOpen::Routing::ISegment *> & segments /** segments */ 
            );
            /** Set the length of the @link Routing::Stock Routing::Stock@endlink  to which a
                        @link Assemblies::Component Assemblies::Component@endlink  object is attached.  <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: void SetAttachedStockLength
            (
                NXOpen::Assemblies::Component * partOcc /** part occ */ 
            );
            /** Sets the reference @link Routing::Stock Routing::Stock@endlink  information based 
                        on the @link Routing::Stock Routing::Stock@endlink  associated with this object.  <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: void SetReferenceStockFromObject
            (
                NXOpen::NXObject * object /** object */ 
            );
            /** Resets the reference @link Routing::Stock Routing::Stock@endlink  information to NULL. The information
                        attributes are rotation, twist, negate, flip, port and anchor. They determine the default 
                        creation options for the new stock. This information is used during path creation.  <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: void ResetReferenceStock
            (
            );
            /** Creates stock @link Routing::Stock Routing::Stock@endlink  on the given segments. The segments do not need to be in order, and don't
                    necessarily have to form a single path. Returns created stock and number of stock  <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: void AddStock
            (
                NXOpen::Routing::CharacteristicList * stockPart /** Characteristic list used to find the appropriate
                                                                                                                      @link Routing::StockData Routing::StockData@endlink  for building the stock.  
                                                                                                                      See @link Routing::StockDataCollection::CreateStockData Routing::StockDataCollection::CreateStockData@endlink . */,
                NXOpen::Routing::CharacteristicList * dataCharx /** The list of optional and required characteristics to apply to the new stock. */,
                const std::vector<NXOpen::Routing::ISegment *> & segments /** segments */ ,
                const NXString & routeLevel /** Routing level.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                std::vector<NXOpen::Routing::Stock *> & stocks /** Array of stocks created */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
