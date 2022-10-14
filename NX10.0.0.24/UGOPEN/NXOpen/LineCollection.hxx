#ifndef NXOpen_LINECOLLECTION_HXX_INCLUDED
#define NXOpen_LINECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LineCollection.ja
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
#include <NXOpen/SmartObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class LineCollection;
    class BasePart;
    class Line;
    class IParameterizedSurface;
    class LineCollectionImpl;
    /** Represents a collection of lines.  <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  LineCollection : public NXOpen::TaggedObjectCollection
    {
        private: LineCollectionImpl * m_linecollection_impl;
        private: NXOpen::BasePart* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit LineCollection(NXOpen::BasePart *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~LineCollection();
        /** Iterator for accessing the contents of the collection. */
        //lint -sem(NXOpen::LineCollection::iterator::copy,initializer)
        class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::Line *>
        {
        public:
            /** Default constructor */
            iterator() : m_context(NULL), m_current(NULL_TAG)
            {
                // coverity[uninit_member]
            } //lint !e1401 m_state is not initialized
            /// \cond NX_NO_DOC
            explicit iterator(NXOpen::LineCollection *context) : m_context(context), m_current(NULL_TAG)
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
            NXOpen::LineCollection *m_context;
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
        /** Finds the @link  Line   Line @endlink  with the given identifier as recorded in a journal. 
            An object may not return the same value as its JournalIdentifier in different versions of 
            the software. However newer versions of the software should find the same object when 
            FindObject is passed older versions of its journal identifier. In general, this method 
            should not be used in handwritten code and exists to support record and playback of journals.

            An exception will be thrown if no object can be found with the given journal identifier.  @return  
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Line * FindObject
        (
            const NXString & journalIdentifier /** Journal identifier of the line */
        );
        /** Finds the @link  Line   Line @endlink  with the given identifier as recorded in a journal. 
            An object may not return the same value as its JournalIdentifier in different versions of 
            the software. However newer versions of the software should find the same object when 
            FindObject is passed older versions of its journal identifier. In general, this method 
            should not be used in handwritten code and exists to support record and playback of journals.

            An exception will be thrown if no object can be found with the given journal identifier.  @return  
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        NXOpen::Line * FindObject
        (
            const char * journalIdentifier /** Journal identifier of the line */
        );
        /** Create a Axis line base on a Cylider, Cone, Torus or Revolve face  @return  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR geometric_tol ("GDT") */
        public: NXOpen::Line * CreateFaceAxis
        (
            NXOpen::IParameterizedSurface * face /** face */,
            NXOpen::SmartObject::UpdateOption updateOption /** update option */ 
        );
        /** Create a Axis line base on a Cylider, Cone, Torus or Revolve face. If the parent (source) part is
             not the same part that the axis is created in, the parent part is not fully loaded during the creation.  @return  
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR geometric_tol ("GDT") */
        public: NXOpen::Line * CreateFaceAxisNoParentLoadRequired
        (
            NXOpen::IParameterizedSurface * face /** face */,
            NXOpen::SmartObject::UpdateOption updateOption /** update option */ 
        );
        /** Create a Axis line base on a Cylider, Cone, Torus or Revolve face.
                Do not extend the line.  @return  
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR geometric_tol ("GDT") */
        public: NXOpen::Line * CreateFaceAxisNoExtension
        (
            NXOpen::IParameterizedSurface * face /** face */,
            NXOpen::SmartObject::UpdateOption updateOption /** update option */ 
        );
    }; //lint !e1712 default constructor not defined for class  

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