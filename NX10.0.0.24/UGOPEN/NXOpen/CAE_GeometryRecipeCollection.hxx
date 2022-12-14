#ifndef NXOpen_CAE_GEOMETRYRECIPECOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_GEOMETRYRECIPECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_GeometryRecipeCollection.ja
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
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class GeometryRecipeCollection;
    }
    namespace CAE
    {
        class PolygonGeometryManager;
    }
    namespace CAE
    {
        class GeometryRecipe;
    }
    namespace CAE
    {
        class FreezeGeometryBuilder;
    }
    namespace CAE
    {
        class FreezeGeometryRecipe;
    }
    namespace CAE
    {
        class GeometryRecipeCollectionImpl;
        /**  @brief  Provides methods for managing set @link NXOpen::CAE::GeometryRecipe NXOpen::CAE::GeometryRecipe@endlink  

           <br> To obtain an instance of this class, refer to @link NXOpen::CAE::PolygonGeometryManager  NXOpen::CAE::PolygonGeometryManager @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  GeometryRecipeCollection : public NXOpen::TaggedObjectCollection
        {
            private: GeometryRecipeCollectionImpl * m_geometryrecipecollection_impl;
            private: NXOpen::CAE::PolygonGeometryManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit GeometryRecipeCollection(NXOpen::CAE::PolygonGeometryManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~GeometryRecipeCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::CAE::GeometryRecipeCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::CAE::GeometryRecipe *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::CAE::GeometryRecipeCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOPENCPP_CAEEXPORT  value_type operator * ();
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
                NXOPENCPP_CAEEXPORT  void next();
                NXOpen::CAE::GeometryRecipeCollection *m_context;
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
            /** Creates a @link NXOpen::CAE::GeometryRecipeCollection NXOpen::CAE::GeometryRecipeCollection@endlink  instance. @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::FreezeGeometryBuilder * CreateFreezeGeometryBuilder
            (
                NXOpen::CAE::FreezeGeometryRecipe * recipe /** recipe */ 
            );
            /** Finds the @link  NXOpen::CAE::GeometryRecipe   NXOpen::CAE::GeometryRecipe @endlink  with the given identifier as recorded in a journal. 
                        An object may not return the same value as its JournalIdentifier in different versions of 
                        the software. However newer versions of the software should find the same object when 
                        FindObject is passed older versions of its journal identifier. In general, this method 
                        should not be used in handwritten code and exists to support record and playback of journals.

                        An exception will be thrown if no object can be found with the given journal identifier.  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::GeometryRecipe * FindObject
            (
                const NXString & journalIdentifier /** Identifier of the Set you want */
            );
            /** Finds the @link  NXOpen::CAE::GeometryRecipe   NXOpen::CAE::GeometryRecipe @endlink  with the given identifier as recorded in a journal. 
                        An object may not return the same value as its JournalIdentifier in different versions of 
                        the software. However newer versions of the software should find the same object when 
                        FindObject is passed older versions of its journal identifier. In general, this method 
                        should not be used in handwritten code and exists to support record and playback of journals.

                        An exception will be thrown if no object can be found with the given journal identifier.  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            NXOpen::CAE::GeometryRecipe * FindObject
            (
                const char * journalIdentifier /** Identifier of the Set you want */
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
