#ifndef NXOpen_MODELINGVIEWCOLLECTION_HXX_INCLUDED
#define NXOpen_MODELINGVIEWCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ModelingViewCollection.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class ModelingViewCollection;
    class BasePart;
    class ModelingView;
    /** Represents a collection of @link ModelingView ModelingView@endlink s.
     <br> To obtain an instance of this class, refer to @link BasePart BasePart@endlink  <br> */
    class NXOPENCPPEXPORT ModelingViewCollection : public TaggedObjectCollection
    {
        private: NXOpen::BasePart* m_owner;
        public: explicit ModelingViewCollection(NXOpen::BasePart *owner): m_owner(owner)
        {
        }
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        /** Iterator for accessing the contents of the collection. */
        class iterator
        {
        public:
            typedef ModelingView * value_type;
            /** Default constructor */
            iterator() : m_context(NULL), m_current(NULL_TAG)
            {
            }//lint !e1401 m_state is not initialized 
            explicit iterator(NXOpen::ModelingViewCollection *context) : m_context(context), m_current(NULL_TAG)
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
            NXOpen::ModelingViewCollection *m_context;
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
        /** Finds the @link  ModelingView   ModelingView @endlink  with the given identifier
            as recorded in a journal.  An object may not return the same value as its
            JournalIdentifier in different versions of the software.  However,
            newer versions of the software should find the same object when 
            FindObject is passed older versions of its journal identifier. In general,
            this method should not be used in handwritten code and exists to
            support record and playback of journals.

            An exception will be thrown if no object can be found with the given
            journal identifier.  @return  View with this identifier  <br> License requirements : None */
        public: NXOpen::ModelingView * FindObject
        (
            const NXString & journalIdentifier /** Identifier of the modeling view to be found   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /**Returns  the work view of the part.  <br> License requirements : None */
        public: NXOpen::ModelingView * WorkView
        (
        );
        public: virtual void initialize();
    };
}
#undef EXPORTLIBRARY
#endif
