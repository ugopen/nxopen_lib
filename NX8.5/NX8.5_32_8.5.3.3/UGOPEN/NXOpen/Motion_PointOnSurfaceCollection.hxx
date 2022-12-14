#ifndef NXOpen_MOTION_POINTONSURFACECOLLECTION_HXX_INCLUDED
#define NXOpen_MOTION_POINTONSURFACECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_PointOnSurfaceCollection.ja
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
#include <NXOpen/Motion_PointOnSurface.hxx>
#include <NXOpen/Motion_PointOnSurfaceBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class PointOnSurfaceCollection;
    }
    namespace Motion
    {
        class MotionManager;
    }
    namespace Motion
    {
        class PointOnSurface;
    }
    namespace Motion
    {
        class PointOnSurfaceBuilder;
    }
    namespace Motion
    {
        class PointOnSurfaceCollectionImpl;
        /** Represents a collection of Point on Surface objects  <br> To obtain an instance of this class, refer to @link Motion::MotionManager  Motion::MotionManager @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  PointOnSurfaceCollection : public TaggedObjectCollection
        {
            private: PointOnSurfaceCollectionImpl * m_pointonsurfacecollection_impl;
            private: NXOpen::Motion::MotionManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit PointOnSurfaceCollection(NXOpen::Motion::MotionManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~PointOnSurfaceCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Motion::PointOnSurfaceCollection::iterator::copy,initializer)
            class iterator
            {
            public:
                /** Value type associated with iterator*/ 

                typedef Motion::PointOnSurface * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Motion::PointOnSurfaceCollection *context) : m_context(context), m_current(NULL_TAG)
                {
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
                NXOPENCPP_MOTIONEXPORT  value_type operator * ();
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
                NXOPENCPP_MOTIONEXPORT  void next();
                NXOpen::Motion::PointOnSurfaceCollection *m_context;
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
            /** Creates a @link Motion::PointOnSurfaceBuilder Motion::PointOnSurfaceBuilder@endlink   @return  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::PointOnSurfaceBuilder * CreatePointOnSurfaceBuilder
            (
                NXOpen::Motion::PointOnSurface * pointonsurface /** pointonsurface */ 
            );
            /** Finds the @link  Motion::PointOnSurface   Motion::PointOnSurface @endlink  with the given name.
                        An exception will be thrown if no object can be found with given name.  @return  @link  Motion::PointOnSurface   Motion::PointOnSurface @endlink  with this name. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::PointOnSurface * FindObject
            (
                const NXString & name /** The name of the @link  Motion::PointOnSurface   Motion::PointOnSurface @endlink . */
            );
            /** Finds the @link  Motion::PointOnSurface   Motion::PointOnSurface @endlink  with the given name.
                        An exception will be thrown if no object can be found with given name.  @return  @link  Motion::PointOnSurface   Motion::PointOnSurface @endlink  with this name. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            NXOpen::Motion::PointOnSurface * FindObject
            (
                const char * name /** The name of the @link  Motion::PointOnSurface   Motion::PointOnSurface @endlink . */
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
