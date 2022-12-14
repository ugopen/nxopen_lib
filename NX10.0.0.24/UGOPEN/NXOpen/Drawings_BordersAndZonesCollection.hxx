#ifndef NXOpen_DRAWINGS_BORDERSANDZONESCOLLECTION_HXX_INCLUDED
#define NXOpen_DRAWINGS_BORDERSANDZONESCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_BordersAndZonesCollection.ja
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
#include <NXOpen/Drawings_BordersAndZonesBuilder.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_drawings_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drawings
    {
        class BordersAndZonesCollection;
    }
    class DraftingManager;
    namespace Drawings
    {
        class BordersAndZones;
    }
    namespace Drawings
    {
        class BordersAndZonesBuilder;
    }
    namespace Drawings
    {
        class BordersAndZonesCollectionImpl;
        /** Represents a collection of @link NXOpen::Drawings::BordersAndZones NXOpen::Drawings::BordersAndZones@endlink  objects  <br> To obtain an instance of this class, refer to @link NXOpen::DraftingManager  NXOpen::DraftingManager @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  BordersAndZonesCollection : public NXOpen::TaggedObjectCollection
        {
            private: BordersAndZonesCollectionImpl * m_bordersandzonescollection_impl;
            private: NXOpen::DraftingManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit BordersAndZonesCollection(NXOpen::DraftingManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~BordersAndZonesCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Drawings::BordersAndZonesCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::Drawings::BordersAndZones *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Drawings::BordersAndZonesCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOPENCPP_DRAWINGSEXPORT  value_type operator * ();
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
                NXOPENCPP_DRAWINGSEXPORT  void next();
                NXOpen::Drawings::BordersAndZonesCollection *m_context;
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
            /**  Finds the @link  NXOpen::Drawings::BordersAndZones   NXOpen::Drawings::BordersAndZones @endlink  with the given name. 
                         An exception will be thrown if no object can be found with the given name.  @return   Borders and zones object 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::BordersAndZones * FindObject
            (
                const NXString & name /** Drawing sheet name */
            );
            /**  Finds the @link  NXOpen::Drawings::BordersAndZones   NXOpen::Drawings::BordersAndZones @endlink  with the given name. 
                         An exception will be thrown if no object can be found with the given name.  @return   Borders and zones object 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::Drawings::BordersAndZones * FindObject
            (
                const char * name /** Drawing sheet name */
            );
            /** Creates a borders and zones builder  @return  BordersAndZonesBuilder object 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Drawings::BordersAndZonesBuilder * CreateBordersAndZonesBuilder
            (
                NXOpen::Drawings::BordersAndZones * bordersAndZones /** @link NXOpen::Drawings::BordersAndZones NXOpen::Drawings::BordersAndZones@endlink  to be redefined, if NULL then creates a new one */
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
