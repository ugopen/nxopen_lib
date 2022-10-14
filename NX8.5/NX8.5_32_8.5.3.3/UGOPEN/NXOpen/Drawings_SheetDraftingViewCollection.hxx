#ifndef NXOpen_DRAWINGS_SHEETDRAFTINGVIEWCOLLECTION_HXX_INCLUDED
#define NXOpen_DRAWINGS_SHEETDRAFTINGVIEWCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_SheetDraftingViewCollection.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/ugmath.hxx>
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
        class SheetDraftingViewCollection;
    }
    namespace Drawings
    {
        class DrawingSheet;
    }
    namespace Drawings
    {
        class DraftingView;
    }
    class Direction;
    namespace Drawings
    {
        class BaseView;
    }
    namespace Drawings
    {
        class ProjectedView;
    }
    class ModelingView;
    namespace Drawings
    {
        class SheetDraftingViewCollectionImpl;
        /** Represents a collection of @link Drawings::DraftingView Drawings::DraftingView@endlink s.    <br> Use @link PartCollection::PDMPartManager PartCollection::PDMPartManager@endlink  to get the instance of this class.  <br> 
         <br>  Created in NX3.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  SheetDraftingViewCollection : public TaggedObjectCollection
        {
            private: SheetDraftingViewCollectionImpl * m_sheetdraftingviewcollection_impl;
            private: NXOpen::Drawings::DrawingSheet* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit SheetDraftingViewCollection(NXOpen::Drawings::DrawingSheet *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~SheetDraftingViewCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Drawings::SheetDraftingViewCollection::iterator::copy,initializer)
            class iterator
            {
            public:
                /** Value type associated with iterator*/ 

                typedef Drawings::DraftingView * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Drawings::SheetDraftingViewCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Drawings::SheetDraftingViewCollection *m_context;
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
            /** Finds the @link  Drawings::DraftingView   Drawings::DraftingView @endlink  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.

                    An exception will be thrown if no object can be found with the given journal identifier.  @return  View with this identifier 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::DraftingView * FindObject
            (
                const NXString & journalIdentifier /** Identifier of the drafting view to be found */
            );
            /** Finds the @link  Drawings::DraftingView   Drawings::DraftingView @endlink  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.

                    An exception will be thrown if no object can be found with the given journal identifier.  @return  View with this identifier 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::Drawings::DraftingView * FindObject
            (
                const char * journalIdentifier /** Identifier of the drafting view to be found */
            );
            /** For the selected part adds the base view as well as returns the reference to @link  Drawings::DraftingView   Drawings::DraftingView @endlink . 
                        An imported model view (base view) determines orthographic space on the drawing and is used as a reference to establish the alignment 
                        and scale for all subsequent projected views. @return  Base view 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::BaseView * CreateBaseView
            (
                NXOpen::ModelingView * modelView /** Modeling View to be import as base view. */,
                const NXOpen::Point3d & drawingReferencePoint /** view origin(location) */,
                double viewScale /** view scale */,
                bool inheritClippingBoundry /** if true inherit xyclip */
            );
            /** Lets you add a projected view (Orthoraphic View) for the selected parent view. @return  Projected view 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ProjectedView * CreateProjectedView
            (
                NXOpen::Drawings::DraftingView * parentView /** Selected Parent view */,
                const NXOpen::Point3d & drawingReferencePoint /** view origin(location) */
            );
            /** Lets you add a projected view (A View) for the selected parent view. @return  Projected view 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ProjectedView * CreateProjectedView
            (
                NXOpen::Drawings::DraftingView * parentView /** Selected Parent view */,
                const NXOpen::Point3d & drawingReferencePoint /** view origin(location) */,
                NXOpen::Direction * hingeLine /** hinge line vector */
            );
            /** Lets you add a projected view (A View) for the selected parent view. @return  Projected view 
             <br>  Created in NX5.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ProjectedView * CreateProjectedView
            (
                NXOpen::Drawings::DraftingView * parentView /** Selected Parent view */,
                const NXOpen::Point3d & drawingReferencePoint /** view origin(location) */,
                bool reverseDirection /** reverse direction of projection */
            );
            /** Lets you delete the view 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void DeleteView
            (
                NXOpen::Drawings::DraftingView * currentView /** View to be deleted */
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