#ifndef NXOpen_MECHATRONICS_EXPRESSIONBLOCKFORMULACOLLECTION_HXX_INCLUDED
#define NXOpen_MECHATRONICS_EXPRESSIONBLOCKFORMULACOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_ExpressionBlockFormulaCollection.ja
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
#include <NXOpen/Mechatronics_ExpressionBlockFormula.hxx>
#include <NXOpen/Mechatronics_ExpressionBlockFormulaBuilder.hxx>
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
        class ExpressionBlockFormulaCollection;
    }
    namespace Mechatronics
    {
        class PhysicsManager;
    }
    namespace Mechatronics
    {
        class ExpressionBlockFormula;
    }
    namespace Mechatronics
    {
        class ExpressionBlockFormulaBuilder;
    }
    namespace Mechatronics
    {
        class ExpressionBlockFormulaCollectionImpl;
        /** Represents a collection of ExpressionBlock Formula.  <br> To obtain an instance of this class, refer to @link NXOpen::Mechatronics::PhysicsManager  NXOpen::Mechatronics::PhysicsManager @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  ExpressionBlockFormulaCollection : public NXOpen::TaggedObjectCollection
        {
            private: ExpressionBlockFormulaCollectionImpl * m_expressionblockformulacollection_impl;
            private: NXOpen::Mechatronics::PhysicsManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit ExpressionBlockFormulaCollection(NXOpen::Mechatronics::PhysicsManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ExpressionBlockFormulaCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Mechatronics::ExpressionBlockFormulaCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::Mechatronics::ExpressionBlockFormula *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Mechatronics::ExpressionBlockFormulaCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOPENCPP_MECHATRONICSEXPORT  value_type operator * () const;
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
                NXOpen::Mechatronics::ExpressionBlockFormulaCollection *m_context;
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
            /** Creates a @link NXOpen::Mechatronics::ExpressionBlockFormulaBuilder NXOpen::Mechatronics::ExpressionBlockFormulaBuilder@endlink . 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::ExpressionBlockFormulaBuilder * CreateExpressionBlockFormulaBuilder
            (
                NXOpen::Mechatronics::ExpressionBlockFormula * expressionBlockFormula /** @link NXOpen::Mechatronics::ExpressionBlockFormula NXOpen::Mechatronics::ExpressionBlockFormula@endlink  to be edited, if NULL then create a new one */
            );
            /** Finds the @link  NXOpen::Mechatronics::ExpressionBlockFormula   NXOpen::Mechatronics::ExpressionBlockFormula @endlink  with the given name.
                        An exception will be thrown if no object can be found with given name.  @return  @link  NXOpen::Mechatronics::ExpressionBlockFormula   NXOpen::Mechatronics::ExpressionBlockFormula @endlink  with this name. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::ExpressionBlockFormula * FindObject
            (
                const NXString & name /** The name of the @link  NXOpen::Mechatronics::ExpressionBlockFormula   NXOpen::Mechatronics::ExpressionBlockFormula @endlink . */
            );
            /** Finds the @link  NXOpen::Mechatronics::ExpressionBlockFormula   NXOpen::Mechatronics::ExpressionBlockFormula @endlink  with the given name.
                        An exception will be thrown if no object can be found with given name.  @return  @link  NXOpen::Mechatronics::ExpressionBlockFormula   NXOpen::Mechatronics::ExpressionBlockFormula @endlink  with this name. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            NXOpen::Mechatronics::ExpressionBlockFormula * FindObject
            (
                const char * name /** The name of the @link  NXOpen::Mechatronics::ExpressionBlockFormula   NXOpen::Mechatronics::ExpressionBlockFormula @endlink . */
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