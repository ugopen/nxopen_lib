#ifndef NXOpen_DRAWINGS_DRAFTINGVIEWCOLLECTION_HXX_INCLUDED
#define NXOpen_DRAWINGS_DRAFTINGVIEWCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_DraftingViewCollection.ja
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
#include <NXOpen/Drawings_BaseViewBuilder.hxx>
#include <NXOpen/Drawings_DetailViewBuilder.hxx>
#include <NXOpen/Drawings_DrawingViewBuilder.hxx>
#include <NXOpen/Drawings_ProjectedViewBuilder.hxx>
#include <NXOpen/Drawings_SectionInViewBuilder.hxx>
#include <NXOpen/Drawings_SectionViewBuilder.hxx>
#include <NXOpen/Drawings_StandardViewsBuilder.hxx>
#include <NXOpen/Drawings_UpdateViewsBuilder.hxx>
#include <NXOpen/Drawings_ViewCopyTo3dBuilder.hxx>
#include <NXOpen/Drawings_ViewProjectionBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class DraftingViewCollection;
    }
    class Part;
    namespace Drawings
    {
        class DraftingView;
    }
    namespace Drawings
    {
        class BaseView;
    }
    namespace Drawings
    {
        class BaseViewBuilder;
    }
    namespace Drawings
    {
        class DetailView;
    }
    namespace Drawings
    {
        class DetailViewBuilder;
    }
    namespace Drawings
    {
        class DrawingSheet;
    }
    namespace Drawings
    {
        class DrawingView;
    }
    namespace Drawings
    {
        class DrawingViewBuilder;
    }
    namespace Drawings
    {
        class ProjectedView;
    }
    namespace Drawings
    {
        class ProjectedViewBuilder;
    }
    namespace Drawings
    {
        class SectionInViewBuilder;
    }
    namespace Drawings
    {
        class SectionView;
    }
    namespace Drawings
    {
        class SectionViewBuilder;
    }
    namespace Drawings
    {
        class StandardViewsBuilder;
    }
    namespace Drawings
    {
        class UpdateViewsBuilder;
    }
    namespace Drawings
    {
        class ViewCopyTo3dBuilder;
    }
    namespace Drawings
    {
        class ViewProjectionBuilder;
    }
    class ModelingView;
    class View;
    namespace Drawings
    {
        /** Represents a collection of @link Drawings::DraftingView Drawings::DraftingView@endlink s.    <br> To obtain an instance of this class, refer to @link Part Part@endlink  <br> */
        class NXOPENCPPEXPORT DraftingViewCollection : public TaggedObjectCollection
        {
            /** Specifies which drafting views to update. */
            public: enum ViewUpdateOption
            {
                ViewUpdateOptionAll/** Updates all views in scope (part or drawing sheet).*/,
                ViewUpdateOptionOutOfDate/** Updates all out of date views in scope (part or drawing sheet).*/,
                ViewUpdateOptionOutOfDateAutomatic/** Updates all out of date automatic views in scope (part or drawing sheet).*/
            };

            private: NXOpen::Part* m_owner;
            public: explicit DraftingViewCollection(NXOpen::Part *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Drawings::DraftingView * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::Drawings::DraftingViewCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Drawings::DraftingViewCollection *m_context;
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
            /** Updates drafting views in the part determined by an update option.
                        For example, to update all out of date views in a part, pass in
                        @link Drawings::DraftingViewCollection::ViewUpdateOptionOutOfDate Drawings::DraftingViewCollection::ViewUpdateOptionOutOfDate@endlink .
                     <br> License requirements : drafting ("DRAFTING") */
            public: void UpdateViews
            (
                NXOpen::Drawings::DraftingViewCollection::ViewUpdateOption updateOption /** View update option */
            );
            /** Updates drafting views in a sheet determined by an update option.
                        For example, to update all out of date views on the sheet, pass in
                        @link Drawings::DraftingViewCollection::ViewUpdateOptionOutOfDate Drawings::DraftingViewCollection::ViewUpdateOptionOutOfDate@endlink .
                     <br> License requirements : drafting ("DRAFTING") */
            public: void UpdateViews
            (
                NXOpen::Drawings::DraftingViewCollection::ViewUpdateOption updateOption /** View update option */,
                NXOpen::Drawings::DrawingSheet * drawing /** drawing */ 
            );
            /** Updates the drafting views.  The views in list can be spread
                        amongst multiple sheets, but they must all belong to the same part.
                     <br> License requirements : drafting ("DRAFTING") */
            public: void UpdateViews
            (
                const std::vector<NXOpen::Drawings::DraftingView *> & views /** views */ 
            );
            /** Finds the @link  Drawings::DraftingView   Drawings::DraftingView @endlink  with the given identifier as recorded in a journal.
                    An object may not return the same value as its JournalIdentifier in different versions of
                    the software. However newer versions of the software should find the same object when
                    FindObject is passed older versions of its journal identifier. In general, this method
                    should not be used in handwritten code and exists to support record and playback of journals.

                    An exception will be thrown if no object can be found with the given journal identifier.  @return  View with this identifier  <br> License requirements : None */
            public: NXOpen::Drawings::DraftingView * FindObject
            (
                const NXString & journalIdentifier /** Identifier of the drafting view to be found   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Find the parent cut (sectioned) model view of a drawing member view.
                        If the parent view is not a cut model view, NULL is returned.  @return   <br> License requirements : None */
            public: NXOpen::ModelingView * GetParentOfView
            (
                NXOpen::View * view /** view */ 
            );
            /** Creates the Update Views Builder  @return   <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Drawings::UpdateViewsBuilder * CreateUpdateViewsBuilder
            (
            );
            /** Creates the Base View Builder  @return   <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Drawings::BaseViewBuilder * CreateBaseViewBuilder
            (
                NXOpen::Drawings::BaseView * view /** the base view to be edited,
                                                                              if NULL, then create a base view */
            );
            /** Creates the Projected View Builder  @return   <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Drawings::ProjectedViewBuilder * CreateProjectedViewBuilder
            (
                NXOpen::Drawings::ProjectedView * view /** the projected view to be edited,
                                                                                   if NULL, then create a projected view */
            );
            /** Creates the Section View Builder  @return   <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Drawings::SectionViewBuilder * CreateSectionViewBuilder
            (
                NXOpen::Drawings::SectionView * view /** the section view to be edited,
                                                                                 if NULL, then create a section view */
            );
            /** Creates the Section In View Builder  @return   <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Drawings::SectionInViewBuilder * CreateSectionInViewBuilder
            (
            );
            /** Creates a DrawingViewBuilder  @return   <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Drawings::DrawingViewBuilder * CreateDrawingViewBuilder
            (
                NXOpen::Drawings::DrawingView * drawingview /** the drawing view to be edited,
                                                                                        if NULL, then create a drawing view */
            );
            /** Creates a @link Drawings::DetailViewBuilder Drawings::DetailViewBuilder@endlink   @return   <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Drawings::DetailViewBuilder * CreateDetailViewBuilder
            (
                NXOpen::Drawings::DetailView * view /** @link Drawings::DetailView Drawings::DetailView@endlink  to be edited, if NULL  then create a new one */
            );
            /** Creates a @link Drawings::ViewCopyTo3dBuilder Drawings::ViewCopyTo3dBuilder@endlink   @return   <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Drawings::ViewCopyTo3dBuilder * CreateCopyTo3dBuilder
            (
            );
            /** Creates a StandardViewsBuilder  @return   <br> License requirements : nx_drafting_plus ("Drafting Plus") */
            public: NXOpen::Drawings::StandardViewsBuilder * CreateStandardViewsBuilder
            (
            );
            /** Creates a @link Drawings::ViewProjectionBuilder Drawings::ViewProjectionBuilder@endlink   @return   <br> License requirements : nx_drafting_plus ("Drafting Plus") */
            public: NXOpen::Drawings::ViewProjectionBuilder * CreateViewProjectionBuilder
            (
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif