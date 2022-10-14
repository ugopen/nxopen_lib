#ifndef NXOpen_MARKUP_LAYERCOLLECTION_HXX_INCLUDED
#define NXOpen_MARKUP_LAYERCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Markup_LayerCollection.ja
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
#include <NXOpen/Markup_EditAnnotationDisplayBuilder.hxx>
#include <NXOpen/Markup_Layer.hxx>
#include <NXOpen/Markup_LayerBuilder.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_markup_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Markup
    {
        class LayerCollection;
    }
    class BasePart;
    namespace Markup
    {
        class Layer;
    }
    namespace Markup
    {
        class Annotation;
    }
    namespace Markup
    {
        class EditAnnotationDisplayBuilder;
    }
    namespace Markup
    {
        class LayerBuilder;
    }
    namespace Markup
    {
        class LayerCollectionImpl;

        /// \cond NX_NO_DOC 
        /** Represents a @link NXOpen::Markup::LayerCollection NXOpen::Markup::LayerCollection@endlink   <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_MARKUPEXPORT  LayerCollection : public NXOpen::TaggedObjectCollection
        {
            private: LayerCollectionImpl * m_layercollection_impl;
            private: NXOpen::BasePart* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit LayerCollection(NXOpen::BasePart *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~LayerCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Markup::LayerCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::Markup::Layer *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Markup::LayerCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOPENCPP_MARKUPEXPORT  value_type operator * () const;
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
                NXOPENCPP_MARKUPEXPORT  void next();
                NXOpen::Markup::LayerCollection *m_context;
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
            /** Finds the @link NXOpen::Markup::Layer NXOpen::Markup::Layer@endlink  with the given id.
                        An exception will be thrown if no object can be found with given name.  @return  @link NXOpen::Markup::Layer NXOpen::Markup::Layer@endlink  with this id 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Markup::Layer * FindObject
            (
                const NXString & id /** The id of the @link NXOpen::Markup::Layer NXOpen::Markup::Layer@endlink  */
            );
            /** Finds the @link NXOpen::Markup::Layer NXOpen::Markup::Layer@endlink  with the given id.
                        An exception will be thrown if no object can be found with given name.  @return  @link NXOpen::Markup::Layer NXOpen::Markup::Layer@endlink  with this id 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::Markup::Layer * FindObject
            (
                const char * id /** The id of the @link NXOpen::Markup::Layer NXOpen::Markup::Layer@endlink  */
            );
            /** Adds a @link NXOpen::Markup::Layer NXOpen::Markup::Layer@endlink  with a default layer name @return  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Markup::Layer * CreateLayer
            (
            );
            /** Adds a @link NXOpen::Markup::Layer NXOpen::Markup::Layer@endlink  with a customized layer name @return  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Markup::Layer * CreateLayer
            (
                const NXString & layerName /** layername */ 
            );
            /** Adds a @link NXOpen::Markup::Layer NXOpen::Markup::Layer@endlink  with a customized layer name @return  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::Markup::Layer * CreateLayer
            (
                const char * layerName /** layername */ 
            );
            /** Activates a @link NXOpen::Markup::Layer NXOpen::Markup::Layer@endlink  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void MakeActive
            (
                NXOpen::Markup::Layer * layer /** layer */ 
            );
            /** Deactivates a @link NXOpen::Markup::Layer NXOpen::Markup::Layer@endlink  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void MakeInactive
            (
                NXOpen::Markup::Layer * layer /** layer */ 
            );
            /** Gets the active @link NXOpen::Markup::Layer NXOpen::Markup::Layer@endlink 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Markup::Layer * GetActive
            (
            );
            /** Creates a @link NXOpen::Markup::EditAnnotationDisplayBuilder NXOpen::Markup::EditAnnotationDisplayBuilder@endlink   @return  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Markup::EditAnnotationDisplayBuilder * CreateEditAnnotationDisplayBuilder
            (
                const std::vector<NXOpen::Markup::Annotation *> & objects /** objects */ 
            );
            /** Creates a @link NXOpen::Markup::LayerBuilder NXOpen::Markup::LayerBuilder@endlink   @return  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Markup::LayerBuilder * CreateLayerBuilder
            (
                NXOpen::Markup::Layer * layer /** layer */ 
            );
        }; //lint !e1712 default constructor not defined for class  


        /// \endcond 
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