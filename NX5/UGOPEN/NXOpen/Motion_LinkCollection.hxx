#ifndef NXOpen_MOTION_LINKCOLLECTION_HXX_INCLUDED
#define NXOpen_MOTION_LINKCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_LinkCollection.ja
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
#include <NXOpen/Motion_Link.hxx>
#include <NXOpen/Motion_LinkBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class LinkCollection;
    }
    namespace Motion
    {
        class MotionManager;
    }
    namespace Motion
    {
        class Link;
    }
    namespace Motion
    {
        class LinkBuilder;
    }
    namespace Motion
    {
        /** Represents a collection of motion joints  <br> To obtain an instance of this class, refer to @link Motion::MotionManager Motion::MotionManager@endlink  <br> */
        class NXOPENCPPEXPORT LinkCollection : public TaggedObjectCollection
        {
            private: NXOpen::Motion::MotionManager* m_owner;
            public: explicit LinkCollection(NXOpen::Motion::MotionManager *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Motion::Link * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::Motion::LinkCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Motion::LinkCollection *m_context;
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
            /** Creates a @link Motion::LinkBuilder Motion::LinkBuilder@endlink   @return   <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::LinkBuilder * CreateLinkBuilder
            (
                NXOpen::Motion::Link * link /** @link Motion::Link Motion::Link@endlink  to be edited, if NULL then create a new one */
            );
            /** Finds the @link  Motion::Link   Motion::Link @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name.  @return  @link  Motion::Link   Motion::Link @endlink  with this name.  <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::Link * FindObject
            (
                const NXString & name /** The name of the @link  Motion::Link   Motion::Link @endlink .   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif