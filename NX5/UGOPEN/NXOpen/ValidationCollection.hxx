#ifndef NXOpen_VALIDATIONCOLLECTION_HXX_INCLUDED
#define NXOpen_VALIDATIONCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationCollection.ja
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
#include <NXOpen/Validation.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class ValidationCollection;
    class Part;
    class Validation;
    class NXObject;
    /**
     Represents a collection of  @link Validation Validation@endlink .
     <br> To obtain an instance of this class, refer to @link Part Part@endlink  <br> */
    class NXOPENCPPEXPORT ValidationCollection : public TaggedObjectCollection
    {
        private: NXOpen::Part* m_owner;
        public: explicit ValidationCollection(NXOpen::Part *owner): m_owner(owner)
        {
        }
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        /** Iterator for accessing the contents of the collection. */
        class iterator
        {
        public:
            typedef Validation * value_type;
            /** Default constructor */
            iterator() : m_context(NULL), m_current(NULL_TAG)
            {
            }
            explicit iterator(NXOpen::ValidationCollection *context) : m_context(context), m_current(NULL_TAG)
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
            NXOpen::ValidationCollection *m_context;
            tag_t m_current;
            unsigned int m_state[8];
        };
        /** Returns an iterator addressing the first element. */
        iterator begin();
        /** Returns an iterator addressing the last element. */
        iterator end()
        {
            return iterator(this);
        }
        /** Create a new validation object  @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: NXOpen::Validation * Create
        (
            const NXString & source /** source where the rules are define   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            NXOpen::Validation::InputType type /** selects the kind of validation object */
        );
        public: virtual void initialize();
    };
}
#undef EXPORTLIBRARY
#endif
