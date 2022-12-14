#ifndef NXOpen_MECHATRONICS_PLANARJOINTCOLLECTION_HXX_INCLUDED
#define NXOpen_MECHATRONICS_PLANARJOINTCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_PlanarJointCollection.ja
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
#include <NXOpen/Mechatronics_PlanarJoint.hxx>
#include <NXOpen/Mechatronics_PlanarJointBuilder.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class PlanarJointCollection;
    }
    namespace Mechatronics
    {
        class PhysicsManager;
    }
    namespace Mechatronics
    {
        class PlanarJoint;
    }
    namespace Mechatronics
    {
        class PlanarJointBuilder;
    }
    namespace Mechatronics
    {
        class PlanarJointCollectionImpl;
        /** Represents a collection of Planar Joint.  <br> To obtain an instance of this class, refer to @link NXOpen::Mechatronics::PhysicsManager  NXOpen::Mechatronics::PhysicsManager @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  PlanarJointCollection : public NXOpen::TaggedObjectCollection
        {
            private: PlanarJointCollectionImpl * m_planarjointcollection_impl;
            private: NXOpen::Mechatronics::PhysicsManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit PlanarJointCollection(NXOpen::Mechatronics::PhysicsManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~PlanarJointCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Mechatronics::PlanarJointCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::Mechatronics::PlanarJoint *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Mechatronics::PlanarJointCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOPENCPP_MECHATRONICSEXPORT  value_type operator * ();
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
                NXOPENCPP_MECHATRONICSEXPORT  void next();
                NXOpen::Mechatronics::PlanarJointCollection *m_context;
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
            /**  @brief 
                    Creates a @link NXOpen::Mechatronics::PlanarJointBuilder NXOpen::Mechatronics::PlanarJointBuilder@endlink .
                     

               @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::PlanarJointBuilder * CreatePlanarJointBuilder
            (
                NXOpen::Mechatronics::PlanarJoint * cylinJoint /** @link NXOpen::Mechatronics::PlanarJoint NXOpen::Mechatronics::PlanarJoint@endlink  to be edited, if NULL then create a new one */
            );
            /** Finds the @link  NXOpen::Mechatronics::PlanarJoint   NXOpen::Mechatronics::PlanarJoint @endlink  with the given name.
                        An exception will be thrown if no object can be found with given name.  @return  @link  NXOpen::Mechatronics::PlanarJoint   NXOpen::Mechatronics::PlanarJoint @endlink  with this name. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::PlanarJoint * FindObject
            (
                const NXString & name /** The name of the @link  NXOpen::Mechatronics::PlanarJoint   NXOpen::Mechatronics::PlanarJoint @endlink . */
            );
            /** Finds the @link  NXOpen::Mechatronics::PlanarJoint   NXOpen::Mechatronics::PlanarJoint @endlink  with the given name.
                        An exception will be thrown if no object can be found with given name.  @return  @link  NXOpen::Mechatronics::PlanarJoint   NXOpen::Mechatronics::PlanarJoint @endlink  with this name. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            NXOpen::Mechatronics::PlanarJoint * FindObject
            (
                const char * name /** The name of the @link  NXOpen::Mechatronics::PlanarJoint   NXOpen::Mechatronics::PlanarJoint @endlink . */
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
