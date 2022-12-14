#ifndef NXOpen_DISPLAY_DYNAMICSECTIONCOLLECTION_HXX_INCLUDED
#define NXOpen_DISPLAY_DYNAMICSECTIONCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_DynamicSectionCollection.ja
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
#include <NXOpen/BasePart.hxx>
#include <NXOpen/Display_DynamicSection.hxx>
#include <NXOpen/Display_DynamicSectionBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Display
    {
        class DynamicSectionCollection;
    }
    class BasePart;
    namespace Display
    {
        class DynamicSection;
    }
    namespace Display
    {
        class DynamicSectionBuilder;
    }
    class ModelingView;
    namespace Display
    {
        /** Represents a collection of dynamic section objects  <br> To obtain an instance of this class, refer to @link BasePart BasePart@endlink  <br> */
        class NXOPENCPPEXPORT DynamicSectionCollection : public TaggedObjectCollection
        {
            private: NXOpen::BasePart* m_owner;
            public: explicit DynamicSectionCollection(NXOpen::BasePart *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Display::DynamicSection * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::Display::DynamicSectionCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Display::DynamicSectionCollection *m_context;
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
            /** Creates a @link Display::DynamicSectionBuilder Display::DynamicSectionBuilder@endlink  object if the section 
                        is NULL. Otherwise, a Section object will be edited.
                         <br> 
                        The specified view can be NULL, in which case the section object is not 
                        activated in any view.
                         <br> 
                      @return  section builder  <br> License requirements : None */
            public: NXOpen::Display::DynamicSectionBuilder * CreateSectionBuilder
            (
                NXOpen::Display::DynamicSection * section /** If section is not NULL, 
                                                                                                               then this object will be 
                                                                                                               edited */,
                NXOpen::ModelingView * view /** View to be used for activating the section object */
            );
            /** Creates a @link Display::DynamicSectionBuilder Display::DynamicSectionBuilder@endlink  object that is used
                        to edit a section object in the specified view. If no section object is available
                        for the view, then a new one is created.
                         <br> 
                        The specified view can not be NULL, otherwise an exception will be raised.
                         <br> 
                      @return  section builder  <br> License requirements : None */
            public: NXOpen::Display::DynamicSectionBuilder * CreateSectionBuilder
            (
                NXOpen::ModelingView * view /** View to be used for activating the section object */
            );
            /** Copies the specified dynamic sections in the part. A copy of each
                        specified dynamic section will be created and then added to the part. 
                        It is  ensured that each dynamic section object in the part has a 
                        unique name. Hence, it is possible that the name of a pasted section  
                        object is different from that of the input section object if its name 
                        clashes with an existing section object in the part.
                         <br> 
                        The section objects being copied must have been loaded in the memory.
                        Otherwise this method will throw an exception.
                         <br> 
                     @return  Copied section objects in the part.  <br> License requirements : None */
            public: std::vector<NXOpen::Display::DynamicSection *> CopySections
            (
                const std::vector<NXOpen::Display::DynamicSection *> & sections /** The objects to be pasted in the part */,
                bool deleteOriginals /** Flag indicating whether the input sections should be deleted */
            );
            /** Finds the @link  DynamicSection   DynamicSection @endlink  with the given identifier as 
                        recorded in a journal. An object may not return the same value as its JournalIdentifier
                        in different versions of the software. However newer versions of the software should find 
                        the same object when FindObject is passed older versions of its journal identifier. In general,
                        this method should not be used in handwritten code and exists to support record and 
                        playback of journals.
                         <br> 
                        An exception will be thrown if no object can be found with the given journal identifier. 
                         <br> 
                     @return  Section found  <br> License requirements : None */
            public: NXOpen::Display::DynamicSection * FindObject
            (
                const NXString & journalIdentifier /** Identifier to be found   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
