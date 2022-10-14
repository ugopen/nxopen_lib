#ifndef NXOpen_ANNOTATIONS_CENTERLINECOLLECTION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_CENTERLINECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_CenterlineCollection.ja
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
#include <NXOpen/Annotations_AutomaticCenterlineBuilder.hxx>
#include <NXOpen/Annotations_BoltCircleCenterlineBuilder.hxx>
#include <NXOpen/Annotations_CenterMarkBuilder.hxx>
#include <NXOpen/Annotations_Centerline2dBuilder.hxx>
#include <NXOpen/Annotations_Centerline3dBuilder.hxx>
#include <NXOpen/Annotations_CircularCenterlineBuilder.hxx>
#include <NXOpen/Annotations_PmiCenterMarkBuilder.hxx>
#include <NXOpen/Annotations_PmiCenterline3dBuilder.hxx>
#include <NXOpen/Annotations_SymmetricalCenterlineBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class CenterlineCollection;
    }
    namespace Annotations
    {
        class AnnotationManager;
    }
    namespace Annotations
    {
        class Centerline;
    }
    namespace Annotations
    {
        class AutomaticCenterlineBuilder;
    }
    namespace Annotations
    {
        class BoltCircleCenterline;
    }
    namespace Annotations
    {
        class BoltCircleCenterlineBuilder;
    }
    namespace Annotations
    {
        class CenterMark;
    }
    namespace Annotations
    {
        class CenterMarkBuilder;
    }
    namespace Annotations
    {
        class Centerline2d;
    }
    namespace Annotations
    {
        class Centerline2dBuilder;
    }
    namespace Annotations
    {
        class Centerline3d;
    }
    namespace Annotations
    {
        class Centerline3dBuilder;
    }
    namespace Annotations
    {
        class CircularCenterline;
    }
    namespace Annotations
    {
        class CircularCenterlineBuilder;
    }
    namespace Annotations
    {
        class PmiCenterMark;
    }
    namespace Annotations
    {
        class PmiCenterMarkBuilder;
    }
    namespace Annotations
    {
        class PmiCenterline3d;
    }
    namespace Annotations
    {
        class PmiCenterline3dBuilder;
    }
    namespace Annotations
    {
        class SymmetricalCenterline;
    }
    namespace Annotations
    {
        class SymmetricalCenterlineBuilder;
    }
    namespace Annotations
    {
        class CenterlineCollectionImpl;
        /** Represents a collection of @link Annotations::Centerline Annotations::Centerline@endlink  objects  <br> To obtain an instance of this class, refer to @link Annotations::AnnotationManager Annotations::AnnotationManager@endlink  <br> */
        class NXOPENCPPEXPORT  CenterlineCollection : public TaggedObjectCollection
        {
            private: CenterlineCollectionImpl * m_centerlinecollection_impl;
            private: NXOpen::Annotations::AnnotationManager* m_owner;
            /** Constructor */
            public: explicit CenterlineCollection(NXOpen::Annotations::AnnotationManager *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~CenterlineCollection();
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Annotations::Centerline * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::Annotations::CenterlineCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Annotations::CenterlineCollection *m_context;
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
            /** Creates the Symmetrical Centerline builder  @return  SymmetricalCenterlineBuilder object  <br> License requirements : None */
            public: NXOpen::Annotations::SymmetricalCenterlineBuilder * CreateSymmetricalCenterlineBuilder
            (
                NXOpen::Annotations::SymmetricalCenterline * centerline /** @link Annotations::SymmetricalCenterline Annotations::SymmetricalCenterline@endlink  to be edited, if NULL then create a new one */
            );
            /** Creates the BoltCircleCenterline builder  @return  BoltCircleCenterlineBuilder object  <br> License requirements : None */
            public: NXOpen::Annotations::BoltCircleCenterlineBuilder * CreateBoltCircleCenterlineBuilder
            (
                NXOpen::Annotations::BoltCircleCenterline * centerline /** @link Annotations::BoltCircleCenterline Annotations::BoltCircleCenterline@endlink  to be edited, if NULL then create a new one */
            );
            /** Creates the CircularCenterline builder  @return  CircularCenterlineBuilder object  <br> License requirements : None */
            public: NXOpen::Annotations::CircularCenterlineBuilder * CreateCircularCenterlineBuilder
            (
                NXOpen::Annotations::CircularCenterline * centerline /** @link Annotations::CircularCenterline Annotations::CircularCenterline@endlink  to be edited, if NULL then create a new one  */
            );
            /** Creates the CenterMark Builder  @return  CenterMarkBuilder Object  <br> License requirements : None */
            public: NXOpen::Annotations::CenterMarkBuilder * CreateCenterMarkBuilder
            (
                NXOpen::Annotations::CenterMark * centerline /** @link Annotations::CenterMark Annotations::CenterMark@endlink  to be edited, if NULL then create a new one */
            );
            /** Creates the Pmi CenterMark Builder  @return  PmiCenterMarkBuilder Object  <br> License requirements : None */
            public: NXOpen::Annotations::PmiCenterMarkBuilder * CreatePmiCenterMarkBuilder
            (
                NXOpen::Annotations::PmiCenterMark * centerline /** @link Annotations::PmiCenterMark Annotations::PmiCenterMark@endlink  to be edited, if NULL then create a new one */
            );
            /** Creates the 2D Centerline builder  @return  Centerline2dBuilder object  <br> License requirements : None */
            public: NXOpen::Annotations::Centerline2dBuilder * CreateCenterline2dBuilder
            (
                NXOpen::Annotations::Centerline2d * cline /** @link Annotations::Centerline2d Annotations::Centerline2d@endlink  to be edited */
            );
            /** Finds the Centerline with the given name.  An exception will be 
                    thrown if no object can be found with given name  @return  Centerline with this identifier  <br> License requirements : None */
            public: NXOpen::Annotations::Centerline * FindObject
            (
                const NXString & journalIdentifier /** Identifier of the centerline to be found */
            );
            /** Creates the AutomaticCenterlineBuilder  @return  AutomaticCenterlineBuilder object  <br> License requirements : None */
            public: NXOpen::Annotations::AutomaticCenterlineBuilder * CreateAutomaticCenterlineBuilder
            (
            );
            /** Creates the 3D Centerline builder  @return  Annotations.Centerline3dBuilder object  <br> License requirements : None */
            public: NXOpen::Annotations::Centerline3dBuilder * CreateCenterline3dBuilder
            (
                NXOpen::Annotations::Centerline3d * cline /** @link Annotations::Centerline3d Annotations::Centerline3d@endlink  to be edited */
            );
            /** Creates the Pmi 3D Centerline builder  @return  PmiCenterline3dBuilder object  <br> License requirements : None */
            public: NXOpen::Annotations::PmiCenterline3dBuilder * CreatePmiCenterline3dBuilder
            (
                NXOpen::Annotations::PmiCenterline3d * cline /** @link Annotations::PmiCenterline3d Annotations::PmiCenterline3d@endlink  to be edited */
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif