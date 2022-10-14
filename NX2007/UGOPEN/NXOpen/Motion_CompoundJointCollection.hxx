#ifndef NXOpen_MOTION_COMPOUNDJOINTCOLLECTION_HXX_INCLUDED
#define NXOpen_MOTION_COMPOUNDJOINTCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_CompoundJointCollection.ja
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
#include <NXOpen/Motion_CompoundJointBuilder.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class CompoundJointCollection;
    }
    namespace Motion
    {
        class MotionManager;
    }
    namespace Motion
    {
        class CompoundJoint;
    }
    namespace Motion
    {
        class CompoundJointBuilder;
    }
    namespace Motion
    {
        class CompoundJointCollectionImpl;
        /**  @brief 
                    Represents a collection of Compound Joint objects
                 

         
             <br> To obtain an instance of this class, refer to @link NXOpen::Motion::MotionManager  NXOpen::Motion::MotionManager @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  CompoundJointCollection : public NXOpen::TaggedObjectCollection
        {
            private: CompoundJointCollectionImpl * m_compoundjointcollection_impl;
            private: NXOpen::Motion::MotionManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit CompoundJointCollection(NXOpen::Motion::MotionManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~CompoundJointCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Motion::CompoundJointCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::Motion::CompoundJoint *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Motion::CompoundJointCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                }//lint !e1401 m_state is not initialized
                /// \endcond
                /** Copy constructor */
                iterator(const iterator &other): m_context(nullptr), m_current(NULL_TAG)
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
                NXOPENCPP_MOTIONEXPORT  value_type operator * () const;
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
                NXOpen::Motion::CompoundJointCollection *m_context;
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
                            Creates a @link NXOpen::Motion::CompoundJointBuilder NXOpen::Motion::CompoundJointBuilder@endlink 
                         

             
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::CompoundJointBuilder * CreateCompoundJointBuilder
            (
                NXOpen::Motion::CompoundJoint * compoundJoint /** compoundjoint */ 
            );
            /**  @brief 
                            Creates an @link NXOpen::Motion::CompoundJointBuilder NXOpen::Motion::CompoundJointBuilder@endlink  for multi editing
                         

             
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::CompoundJointBuilder * CreateMultiEditCompoundJointBuilder
            (
                const std::vector<NXOpen::Motion::CompoundJoint *> & compoundJoints /** compoundjoints */ 
            );
            /**  @brief 
                            Finds the @link NXOpen::Motion::CompoundJoint NXOpen::Motion::CompoundJoint@endlink  with the given name.
                         

             
                        
                            An exception will be thrown if no object can be found with the given name.
                        
                     @return  @link NXOpen::Motion::CompoundJoint NXOpen::Motion::CompoundJoint@endlink  with this name. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::CompoundJoint * FindObject
            (
                const NXString & name /** The name of the @link NXOpen::Motion::CompoundJoint NXOpen::Motion::CompoundJoint@endlink . */
            );
            /**  @brief 
                            Finds the @link NXOpen::Motion::CompoundJoint NXOpen::Motion::CompoundJoint@endlink  with the given name.
                         

             
                        
                            An exception will be thrown if no object can be found with the given name.
                        
                     @return  @link NXOpen::Motion::CompoundJoint NXOpen::Motion::CompoundJoint@endlink  with this name. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            NXOpen::Motion::CompoundJoint * FindObject
            (
                const char * name /** The name of the @link NXOpen::Motion::CompoundJoint NXOpen::Motion::CompoundJoint@endlink . */
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