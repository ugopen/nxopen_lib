#ifndef NXOpen_ROUTING_BENDCORNERCOLLECTION_HXX_INCLUDED
#define NXOpen_ROUTING_BENDCORNERCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_BendCornerCollection.ja
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
#include <iterator>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/Routing_CornerTypeBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_routing_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Routing
    {
        class BendCornerCollection;
    }
    namespace Routing
    {
        class RouteManager;
    }
    namespace Routing
    {
        class BendCorner;
    }
    class NXObject;
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
        class BendCornerCollectionImpl;
        /** Represents a collection of @link NXOpen::Routing::BendCorner NXOpen::Routing::BendCorner@endlink  objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  BendCornerCollection : public NXOpen::TaggedObjectCollection
        {
            /** Option for creating a bend using a bend table or using radius or ratio */
            public: enum Type
            {
                TypeRadiusRatio/** Using radius or ratio to
                                                                       create a bend corner. */,
                TypeTable/**  Using a bend table to create a
                                                                       bend corner. */
            };

            private: BendCornerCollectionImpl * m_bendcornercollection_impl;
            private: NXOpen::Routing::RouteManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit BendCornerCollection(NXOpen::Routing::RouteManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~BendCornerCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Routing::BendCornerCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::Routing::BendCorner *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Routing::BendCornerCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                }//lint !e1401 m_state is not initialized
                /// \endcond
                /** Copy constructor */
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
                NXOPENCPP_ROUTINGEXPORT  value_type operator * ();
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
                NXOPENCPP_ROUTINGEXPORT  void next();
                NXOpen::Routing::BendCornerCollection *m_context;
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
            /** Create a bend corner object at a Control Point.  @return  The new bend corner. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::BendCorner * CreateCorner
            (
                NXOpen::Routing::ControlPoint * rcp /** Route control point to bend. */,
                NXOpen::Routing::CornerTypeBuilder::BendMethods bendMethod /** Enumerated bend method. */,
                double bendRatio /** Bend ratio is used only if bend method is set to
                                                                                    @link NXOpen::Routing::CornerTypeBuilder::BendMethodsRatioToDiameter NXOpen::Routing::CornerTypeBuilder::BendMethodsRatioToDiameter@endlink .
                                                                                    Must be greater than 0.5. */,
                double bendRadius /** Radius of bend corner arc, used only if bend method is set to
                                                                                    @link NXOpen::Routing::CornerTypeBuilder::BendMethodsRadius NXOpen::Routing::CornerTypeBuilder::BendMethodsRadius@endlink .
                                                                                    Must be greater than 0. */
            );
            /** Create a bend corner object at a Control Point.  @return  The new bend corner. 
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link Routing::BendCornerCollection::CreateCorner Routing::BendCornerCollection::CreateCorner@endlink  instead. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NX_DEPRECATED("Deprecated in NX8.5.0.  Use Routing::BendCornerCollection::CreateCorner instead.") NXOpen::Routing::BendCorner * Create
            (
                NXOpen::Routing::ControlPoint * rcp /** Route control point to bend. */,
                bool useBendRatio /** TRUE: use bend ratio calculation,
                                                       FALSE: use given radius */,
                double bendRatio /** Bend ratio only used if use_bend_ratio is
                                                       TRUE. Must be greater than 0.5. */,
                double bendRadius /** Radius of bend corner arc, only used if
                                                       use_bend_ratio is FALSE. Must be greater than
                                                       0. */
            );
            /** This routine assigns a bend corner to the given input RCP object using
                        a bend table entry. This "assignment" can involve the removal of an existing
                        corner at this location and the creation of a new corner.  The
                        application view must be loaded before attempting to assign a
                        bend corner of this type.   @return  The newly created Bend Corner 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::BendCorner * AssignCornerByBendTable
            (
                NXOpen::Routing::ControlPoint * rcp /** Control point to assign corner to.
                                                          NULL not allowed. */,
                const NXString & bendTable /** The bend table entry that
                                                          is used to create bend corner */
            );
            /** This routine assigns a bend corner to the given input RCP object using
                        a bend table entry. This "assignment" can involve the removal of an existing
                        corner at this location and the creation of a new corner.  The
                        application view must be loaded before attempting to assign a
                        bend corner of this type.   @return  The newly created Bend Corner 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            NXOpen::Routing::BendCorner * AssignCornerByBendTable
            (
                NXOpen::Routing::ControlPoint * rcp /** Control point to assign corner to.
                                                          NULL not allowed. */,
                const char * bendTable /** The bend table entry that
                                                          is used to create bend corner */
            );
            /** This routine assigns a new bend corner to the given input bend corner object using
                        bend ratio. This "assignment" can involve the removal of an existing
                        corner at this location and the creation of a new corner.  @return  The newly created Bend Corner 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::BendCorner * AssignCornerByBendRatio
            (
                NXOpen::Routing::ControlPoint * bendCrn /** Input bend corner.  */,
                double bendRatio /** Bend ratio must be greater than 0.5. */
            );
            /** This routine assigns a new bend corner to the given input bend corner object using
                        bend radius. This "assignment" can involve the removal of an existing
                        corner at this location and the creation of a new corner.  @return  The newly created Bend Corner 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::BendCorner * AssignCornerByBendRadius
            (
                NXOpen::Routing::ControlPoint * bendCrn /** Input bend corner. */,
                double bendRadius /** Radius of bend corner arc. */
            );
            /** Enquire the Bend Corner that this segment represents.
                        (NULL can be returned, indicating that this segment does not
                        represent a Bend Corner.)  @return  Bend Corner that segment represents
                                                  (NULL can be returned,indicating that
                                                  segment does not represent a Bend Corner). 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::BendCorner * GetBendAssociatedToSegment
            (
                NXOpen::Routing::ISegment * segment /** Segment being queried for the
                                                      Bend Corner it represents. */
            );
            /** Returns all the corners connected to the given objects, if any.
                        Can find corners from @link NXOpen::Routing::ControlPoint NXOpen::Routing::ControlPoint@endlink s,
                        @link NXOpen::Routing::ISegment NXOpen::Routing::ISegment@endlink s, or @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink . @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: std::vector<NXOpen::Routing::BendCorner *> GetBendCornersFromObjects
            (
                const std::vector<NXOpen::NXObject *> & objects /** objects */ 
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif
