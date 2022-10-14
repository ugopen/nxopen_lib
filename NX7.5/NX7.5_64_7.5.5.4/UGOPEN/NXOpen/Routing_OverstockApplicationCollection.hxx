#ifndef NXOpen_ROUTING_OVERSTOCKAPPLICATIONCOLLECTION_HXX_INCLUDED
#define NXOpen_ROUTING_OVERSTOCKAPPLICATIONCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_OverstockApplicationCollection.ja
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
#include <NXOpen/Routing_CharacteristicList.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class OverstockApplicationCollection;
    }
    namespace Routing
    {
        class RouteManager;
    }
    namespace Routing
    {
        class OverstockApplication;
    }
    class Expression;
    class Point;
    namespace Routing
    {
        class CharacteristicList;
    }
    namespace Routing
    {
        class ControlPoint;
    }
    namespace Routing
    {
        class ISegment;
    }
    namespace Routing
    {
        class Overstock;
    }
    namespace Routing
    {
        class Stock;
    }
    namespace Routing
    {
        /** Available operations to perform for Overstock Applications */
        enum Operation
        {
            OperationCreate/** Create overstock */,
            OperationEdit/** Edit existing overstock */
        };

        /** Available application methods for Overstock Applications for a given Overstock */
        enum Method
        {
            MethodEntireSegments/** Cover all given segments */,
            MethodInterval/** Cover the given segments intermittently */,
            MethodPointToPoint/** Cover the given segments from one point to another */,
            MethodPointAndLength/** Cover the given segments a point for a length */
        };

        /** Available overstock stock types for Overstock Applications for a given Overstock */
        enum StockType
        {
            StockTypeUnknown/** Unknown overstock type */,
            StockTypeFixedCrossSection/** Fixed cross section, e.g., conduit */,
            StockTypeWrapped/** Wrapped, e.g., electrical tape */,
            StockTypeSleeved/** Sleeved, e.g., woven nylon */,
            StockTypeFlagged/** Flagged, e.g., paper flag */
        };

        /** Available application methods for wrapped overstock */
        enum WrapApplicationType
        {
            WrapApplicationTypeUnknown/** Unknown wrap application */,
            WrapApplicationTypeSpot/** Spot wrap application, i.e., 100% overlap */,
            WrapApplicationTypeOverlapped/** Overlapping spiral wrap application, e.g., [0-100)% overlap */,
            WrapApplicationTypeGapped/** Barber pole spiral wrap application, e.g., no overlap */
        };

        /** Available definitions for the point location for the Point and Length application method */
        enum PointDefinition
        {
            PointDefinitionStart/** The point defines the start of the overstock application. */,
            PointDefinitionMiddle/** The point defines the middle of the overstock application. */,
            PointDefinitionEnd/** The point defines the end of the overstock application. */
        };

    }
    namespace Routing
    {
        class OverstockApplicationCollectionImpl;
        /** Represents a collection of @link Routing::OverstockApplication Routing::OverstockApplication@endlink  objects.  <br> To obtain an instance of this class, refer to @link Routing::RouteManager Routing::RouteManager@endlink  <br> */
        class NXOPENCPPEXPORT  OverstockApplicationCollection : public TaggedObjectCollection
        {
            private: OverstockApplicationCollectionImpl * m_overstockapplicationcollection_impl;
            private: NXOpen::Routing::RouteManager* m_owner;
            /** Constructor */
            public: explicit OverstockApplicationCollection(NXOpen::Routing::RouteManager *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~OverstockApplicationCollection();
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Routing::OverstockApplication * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::Routing::OverstockApplicationCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Routing::OverstockApplicationCollection *m_context;
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
            /** Creates the @link Routing::MethodEntireSegments Routing::MethodEntireSegments@endlink 
                        overstock. Specify the type of overstock to create (for example fixed cross section,
                        wrapped, sleeved, or flagged) in the overstock part characteristic list using
                        the "OVERSTOCK_TYPE" characteristic. Spot wrapping is not allowed for entire segments.  @return   <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: NXOpen::Routing::OverstockApplication * CreateOverstockApplication
            (
                NXOpen::Routing::ControlPoint * startControlPoint /** Control Point at the
                                                                                                                                       start of the set of
                                                                                                                                       segments */,
                const std::vector<NXOpen::Routing::ISegment *> & segments /** Segments to cover with
                                                                                                                                   overstock */,
                const std::vector<NXOpen::Routing::Stock *> & stocks /** Stocks to cover with overstock */,
                NXOpen::Routing::CharacteristicList * overstockPart /** overstock part */ ,
                NXOpen::Routing::WrapApplicationType stockWrapType /** stock wrap type */ ,
                NXOpen::Expression * wrapValue /** wrap value */ 
            );
            /** Creates an @link Routing::OverstockApplication Routing::OverstockApplication@endlink  using the Interval method of application.
                        Specify the type of overstock to create (for example fixed cross section,
                        wrapped, sleeved, or flagged) in the overstock part characteristic list using
                        the "OVERSTOCK_TYPE" characteristic.  @return   <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: NXOpen::Routing::OverstockApplication * CreateOverstockApplication
            (
                NXOpen::Routing::ControlPoint * startControlPoint /** Control Point at the start
                                                                                                                                      of the set of segments */,
                const std::vector<NXOpen::Routing::ISegment *> & segments /** Segments to cover with overstock */,
                const std::vector<NXOpen::Routing::Stock *> & stocks /** Stocks to cover with overstock */,
                NXOpen::Expression * startOffset /** start offset */ ,
                NXOpen::Expression * endOffset /** end offset */ ,
                NXOpen::Expression * pieceLength /** piece length */ ,
                NXOpen::Expression * gap /** gap */ ,
                NXOpen::Expression * numberOfPieces /** number of pieces */ ,
                NXOpen::Point * startPoint /** Point at the start offset
                                                                                                                                    location along the set of
                                                                                                                                    segments */,
                NXOpen::Routing::CharacteristicList * overstockPart /** overstock part */ ,
                NXOpen::Routing::WrapApplicationType stockWrapType /** stock wrap type */ ,
                NXOpen::Expression * wrapValue /** wrap value */ 
            );
            /** Creates an @link Routing::OverstockApplication Routing::OverstockApplication@endlink  using the
                        Point to Point method of application. Specify the type of overstock to create (for example fixed cross section,
                        wrapped, sleeved, or flagged) in the overstock part characteristic list using
                        the "OVERSTOCK_TYPE" characteristic.   @return   <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: NXOpen::Routing::OverstockApplication * CreateOverstockApplication
            (
                NXOpen::Routing::ControlPoint * startControlPoint /** Control Point at the
                                                                                                                           start of the set
                                                                                                                           of segments */,
                const std::vector<NXOpen::Routing::ISegment *> & segments /** Segments to cover
                                                                                                                        with overstock */,
                const std::vector<NXOpen::Routing::Stock *> & stocks /** Stocks to cover with overstock */,
                NXOpen::Point * startPoint /** point at the start of the piece
                                                                                                             of overstock */,
                NXOpen::Point * endPoint /** point at the end of the piece
                                                                                                             of overstock */,
                NXOpen::Routing::CharacteristicList * overstockPart /** overstock part */ ,
                NXOpen::Routing::WrapApplicationType stockType /** stock type */ ,
                NXOpen::Expression * wrapValue /** wrap value */ 
            );
            /** Creates the @link Routing::MethodPointAndLength Routing::MethodPointAndLength@endlink 
                        overstock by the Point and Length method. Specify the type of overstock to create (for example fixed cross section,
                        wrapped, sleeved, or flagged) in the overstock part characteristic list using
                        the "OVERSTOCK_TYPE" characteristic.  @return   <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: NXOpen::Routing::OverstockApplication * CreateOverstockApplication
            (
                NXOpen::Routing::ControlPoint * startControlPoint /** Control Point
                                                                                                                                       at the start of
                                                                                                                                       the set of
                                                                                                                                       segments */,
                const std::vector<NXOpen::Routing::ISegment *> & segments /** Segments to cover
                                                                                                                                   with overstock */,
                const std::vector<NXOpen::Routing::Stock *> & stocks /** Stocks to cover with overstock */,
                NXOpen::Point * definingPoint /** defining point */ ,
                NXOpen::Routing::PointDefinition definingDirection /** location of the defining point. */,
                NXOpen::Expression * pieceLength /** piece length */ ,
                NXOpen::Routing::CharacteristicList * overstockPart /** overstock part */ ,
                NXOpen::Routing::WrapApplicationType stockWrapType /** stock wrap type */ ,
                NXOpen::Expression * wrapValue /** wrap value */ 
            );
            /** Converts an existing @link Routing::Overstock Routing::Overstock@endlink  to
                        @link Routing::MethodEntireSegments Routing::MethodEntireSegments@endlink  overstock.
                     @return   <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: NXOpen::Routing::OverstockApplication * ConvertOverstockApplication
            (
                NXOpen::Routing::ControlPoint * startControlPoint /** Control Point at the
                                                                                                                             start of the set of
                                                                                                                             segments */,
                const std::vector<NXOpen::Routing::ISegment *> & segments /** Segments to cover with
                                                                                                                         overstock */,
                const std::vector<NXOpen::Routing::Stock *> & stocks /** Stocks to cover with overstock */,
                NXOpen::Routing::CharacteristicList * overstockPart /** overstock part */ ,
                NXOpen::Routing::CharacteristicList * reqOptCharxList /** List of optional and required characteristics to be
                                                                                                                                     applied on the overstock. */,
                NXOpen::Expression * wrapValue /** wrap value */ ,
                const std::vector<NXOpen::Routing::Overstock *> & overstocks /** overstocks */ 
            );
            /** Converts an existing @link Routing::Overstock Routing::Overstock@endlink  to
                        @link Routing::MethodInterval Routing::MethodInterval@endlink  overstock.
                     @return   <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: NXOpen::Routing::OverstockApplication * ConvertOverstockApplication
            (
                NXOpen::Routing::ControlPoint * startControlPoint /** Control Point at the start
                                                                                                                            of the set of segments */,
                const std::vector<NXOpen::Routing::ISegment *> & segments /** Segments to cover with overstock */,
                const std::vector<NXOpen::Routing::Stock *> & stocks /** Stocks to cover with overstock */,
                NXOpen::Expression * startOffset /** start offset */ ,
                NXOpen::Expression * endOffset /** end offset */ ,
                NXOpen::Expression * pieceLength /** piece length */ ,
                NXOpen::Expression * gap /** gap */ ,
                NXOpen::Expression * numberOfPieces /** number of pieces */ ,
                NXOpen::Point * startPoint /** Point at the start offset
                                                                                                                          location along the set of
                                                                                                                          segments */,
                NXOpen::Routing::CharacteristicList * overstockPart /** overstock part */ ,
                NXOpen::Routing::CharacteristicList * reqOptCharxList /** List of optional and required characteristics to be
                                                                                                                                     applied on the overstock. */,
                NXOpen::Expression * wrapValue /** wrap value */ ,
                const std::vector<NXOpen::Routing::Overstock *> & overstocks /** overstocks */ 
            );
            /** Converts an existing @link Routing::Overstock Routing::Overstock@endlink  to
                        @link Routing::MethodPointToPoint Routing::MethodPointToPoint@endlink  overstock. 
                     @return   <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: NXOpen::Routing::OverstockApplication * ConvertOverstockApplication
            (
                NXOpen::Routing::ControlPoint * startControlPoint /** Control Point at the
                                                                                                                           start of the set
                                                                                                                           of segments */,
                const std::vector<NXOpen::Routing::ISegment *> & segments /** Segments to cover
                                                                                                                        with overstock */,
                const std::vector<NXOpen::Routing::Stock *> & stocks /** Stocks to cover with overstock */,
                NXOpen::Point * startPoint /** point at the start of the piece
                                                                                                             of overstock */,
                NXOpen::Point * endPoint /** point at the end of the piece
                                                                                                             of overstock */,
                NXOpen::Routing::CharacteristicList * overstockPart /** overstock part */ ,
                NXOpen::Routing::CharacteristicList * reqOptCharxList /** List of optional and required characteristics to be
                                                                                                                                    applied on the overstock. */,
                NXOpen::Expression * wrapValue /** wrap value */ ,
                const std::vector<NXOpen::Routing::Overstock *> & overstocks /** overstocks */ 
            );
            /** Converts an existing @link Routing::Overstock Routing::Overstock@endlink  to
                        @link Routing::MethodPointAndLength Routing::MethodPointAndLength@endlink  overstock. 
                     @return   <br> License requirements : routing_mechanical ("Routing Mechanical") OR routing_electrical ("Routing Electrical") OR routing_combined ("Routing Combined") */
            public: NXOpen::Routing::OverstockApplication * ConvertOverstockApplication
            (
                NXOpen::Routing::ControlPoint * startControlPoint /** Control Point
                                                                                                                                   at the start of
                                                                                                                                   the set of
                                                                                                                                   segments */,
                const std::vector<NXOpen::Routing::ISegment *> & segments /** Segments to cover
                                                                                                                               with overstock */,
                const std::vector<NXOpen::Routing::Stock *> & stocks /** Stocks to cover with overstock */,
                NXOpen::Point * definingPoint /** defining point */ ,
                NXOpen::Routing::PointDefinition definingDirection /** location of the defining point. */,
                NXOpen::Expression * pieceLength /** piece length */ ,
                NXOpen::Routing::CharacteristicList * overstockPart /** overstock part */ ,
                NXOpen::Routing::CharacteristicList * reqOptCharxList /** List of optional and required characteristics to be
                                                                                                                                           applied on the overstock. */,
                NXOpen::Expression * wrapValue /** wrap value */ ,
                const std::vector<NXOpen::Routing::Overstock *> & overstocks /** overstocks */ 
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif