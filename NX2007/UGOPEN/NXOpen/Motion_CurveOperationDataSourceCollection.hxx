#ifndef NXOpen_MOTION_CURVEOPERATIONDATASOURCECOLLECTION_HXX_INCLUDED
#define NXOpen_MOTION_CURVEOPERATIONDATASOURCECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_CurveOperationDataSourceCollection.ja
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
        class CurveOperationDataSourceCollection;
    }
    namespace Motion
    {
        class MotionManager;
    }
    namespace CAE
    {
        class CurveOperationDataSource;
    }
    namespace Motion
    {
        class Graph;
    }
    namespace Motion
    {
        class CurveOperationDataSourceCollectionImpl;
        /** Represents a collection of @link  NXOpen::CAE::CurveOperationDataSource   NXOpen::CAE::CurveOperationDataSource @endlink  elements  <br> To obtain an instance of this class, refer to @link NXOpen::Motion::MotionManager  NXOpen::Motion::MotionManager @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  CurveOperationDataSourceCollection : public NXOpen::TaggedObjectCollection
        {
            private: CurveOperationDataSourceCollectionImpl * m_curveoperationdatasourcecollection_impl;
            private: NXOpen::Motion::MotionManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit CurveOperationDataSourceCollection(NXOpen::Motion::MotionManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~CurveOperationDataSourceCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Motion::CurveOperationDataSourceCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::CAE::CurveOperationDataSource *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Motion::CurveOperationDataSourceCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Motion::CurveOperationDataSourceCollection *m_context;
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
            /** Creates a @link NXOpen::CAE::CurveOperationDataSource NXOpen::CAE::CurveOperationDataSource@endlink .
                        
                        The abscissa graph could be null. It means that x data will come from motion solution.
                        
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::CurveOperationDataSource * Create
            (
                const NXString & name /** name */ ,
                const NXString & description /** description */ ,
                NXOpen::Motion::Graph * abscissaGraph /** x data of the plot will use time when abscissaGraph is not specified*/,
                NXOpen::Motion::Graph * ordinateGraph /** y data of the plot */
            );
            /** Creates a @link NXOpen::CAE::CurveOperationDataSource NXOpen::CAE::CurveOperationDataSource@endlink .
                        
                        The abscissa graph could be null. It means that x data will come from motion solution.
                        
                    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::CAE::CurveOperationDataSource * Create
            (
                const char * name /** name */ ,
                const char * description /** description */ ,
                NXOpen::Motion::Graph * abscissaGraph /** x data of the plot will use time when abscissaGraph is not specified*/,
                NXOpen::Motion::Graph * ordinateGraph /** y data of the plot */
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
