#ifndef NXOpen_ANIMATIONDESIGNER_CONTACTCOLLECTION_HXX_INCLUDED
#define NXOpen_ANIMATIONDESIGNER_CONTACTCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AnimationDesigner_ContactCollection.ja
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
#include <NXOpen/AnimationDesigner_Contact.hxx>
#include <NXOpen/AnimationDesigner_ContactBuilder.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libanimationdesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AnimationDesigner
    {
        class ContactCollection;
    }
    namespace AnimationDesigner
    {
        class AnimationDesignerManager;
    }
    namespace AnimationDesigner
    {
        class Contact;
    }
    namespace AnimationDesigner
    {
        class ContactBuilder;
    }
    class Part;
    namespace AnimationDesigner
    {
        class ContactCollectionImpl;
        /** Represents a collection of Contact objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class ANIMATIONDESIGNEROPENCPPEXPORT  ContactCollection : public NXOpen::TaggedObjectCollection
        {
            private: ContactCollectionImpl * m_contactcollection_impl;
            private: NXOpen::AnimationDesigner::AnimationDesignerManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit ContactCollection(NXOpen::AnimationDesigner::AnimationDesignerManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ContactCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::AnimationDesigner::ContactCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::AnimationDesigner::Contact *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::AnimationDesigner::ContactCollection *context) : m_context(context), m_current(NULL_TAG)
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
                ANIMATIONDESIGNEROPENCPPEXPORT  value_type operator * ();
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
                ANIMATIONDESIGNEROPENCPPEXPORT  void next();
                NXOpen::AnimationDesigner::ContactCollection *m_context;
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
            /** Creates a @link NXOpen::AnimationDesigner::ContactBuilder NXOpen::AnimationDesigner::ContactBuilder@endlink .  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: NXOpen::AnimationDesigner::ContactBuilder * CreateContactBuilder
            (
                NXOpen::Part * part /** part */ ,
                NXOpen::AnimationDesigner::Contact * contactFace /** @link NXOpen::AnimationDesigner::Contact NXOpen::AnimationDesigner::Contact@endlink  to be edited, if NULL then create a new one */
            );
            /** Finds the @link  NXOpen::AnimationDesigner::Contact   NXOpen::AnimationDesigner::Contact @endlink  with the given name.
                        An exception will be thrown if no object can be found with given name.  @return  @link  NXOpen::AnimationDesigner::Contact   NXOpen::AnimationDesigner::Contact @endlink  with this name. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: NXOpen::AnimationDesigner::Contact * FindObject
            (
                NXOpen::Part * part /** part */ ,
                const NXString & name /** The name of the @link  NXOpen::AnimationDesigner::Contact   NXOpen::AnimationDesigner::Contact @endlink . */
            );
            /** Finds the @link  NXOpen::AnimationDesigner::Contact   NXOpen::AnimationDesigner::Contact @endlink  with the given name.
                        An exception will be thrown if no object can be found with given name.  @return  @link  NXOpen::AnimationDesigner::Contact   NXOpen::AnimationDesigner::Contact @endlink  with this name. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            NXOpen::AnimationDesigner::Contact * FindObject
            (
                NXOpen::Part * part /** part */ ,
                const char * name /** The name of the @link  NXOpen::AnimationDesigner::Contact   NXOpen::AnimationDesigner::Contact @endlink . */
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