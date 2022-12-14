#ifndef NXOpen_MECHATRONICS_FUNCTIONOBJECTCOLLECTION_HXX_INCLUDED
#define NXOpen_MECHATRONICS_FUNCTIONOBJECTCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_FunctionObjectCollection.ja
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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Mechatronics_FunctionObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
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
        class FunctionObjectCollection;
    }
    namespace Mechatronics
    {
        class MechatronicsManager;
    }
    namespace Mechatronics
    {
        class FunctionObjectBuilder;
    }
    namespace Mechatronics
    {
        class AddComponentBuilder;
    }
    namespace Mechatronics
    {
        class FunctionObject;
    }
    namespace Mechatronics
    {
        class FunctionObjectCollectionImpl;
        /** Represents a @link Mechatronics::FunctionObjectCollection Mechatronics::FunctionObjectCollection@endlink   <br> To obtain an instance of this class, refer to @link Mechatronics::MechatronicsManager  Mechatronics::MechatronicsManager @endlink  <br> 
         <br>  Created in NX7.5.1.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  FunctionObjectCollection : public TaggedObjectCollection
        {
            private: FunctionObjectCollectionImpl * m_functionobjectcollection_impl;
            private: NXOpen::Mechatronics::MechatronicsManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit FunctionObjectCollection(NXOpen::Mechatronics::MechatronicsManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~FunctionObjectCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Mechatronics::FunctionObjectCollection::iterator::copy,initializer)
            class iterator
            {
            public:
                /** Value type associated with iterator*/ 

                typedef Mechatronics::FunctionObjectBuilder * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                { // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Mechatronics::FunctionObjectCollection *context) : m_context(context), m_current(NULL_TAG)
                { // coverity[uninit_member]
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
                NXOpen::Mechatronics::FunctionObjectCollection *m_context;
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
            /** Create builder for FunctionObject class  @return @link  FunctionObject   FunctionObject @endlink  object 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::FunctionObjectBuilder * CreateFunctionObjectBuilder
            (
                NXOpen::Mechatronics::FunctionObject * object /** @link Mechatronics::FunctionObject Mechatronics::FunctionObject@endlink  to be edited, if NULL then create a new one */
            );
            /** Creates a @link Mechatronics::AddComponentBuilder Mechatronics::AddComponentBuilder@endlink   @return  
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::AddComponentBuilder * CreateAddComponentBuilder
            (
            );
            /** Finds the @link Mechatronics::FunctionObject Mechatronics::FunctionObject@endlink  object with the given name.  @return  @link Mechatronics::FunctionObject Mechatronics::FunctionObject@endlink  object with this name. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::FunctionObject * FindObject
            (
                const NXString & name /** Name of the Function object, actually it shall be handle. */
            );
            /** Finds the @link Mechatronics::FunctionObject Mechatronics::FunctionObject@endlink  object with the given name.  @return  @link Mechatronics::FunctionObject Mechatronics::FunctionObject@endlink  object with this name. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            NXOpen::Mechatronics::FunctionObject * FindObject
            (
                const char * name /** Name of the Function object, actually it shall be handle. */
            );
            /** Dlete a @link Mechatronics::FunctionObject Mechatronics::FunctionObject@endlink  object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void DeleteFunction
            (
                NXOpen::Mechatronics::FunctionObject * functionObject /** @link Mechatronics::FunctionObject Mechatronics::FunctionObject@endlink  object with this name. */
            );
            /** Rename a @link Mechatronics::FunctionObject Mechatronics::FunctionObject@endlink  object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void RenameFunction
            (
                const NXString & newName /** New name of the Function object. */,
                NXOpen::Mechatronics::FunctionObject * functionObject /** @link Mechatronics::FunctionObject Mechatronics::FunctionObject@endlink  object. */
            );
            /** Rename a @link Mechatronics::FunctionObject Mechatronics::FunctionObject@endlink  object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            void RenameFunction
            (
                const char * newName /** New name of the Function object. */,
                NXOpen::Mechatronics::FunctionObject * functionObject /** @link Mechatronics::FunctionObject Mechatronics::FunctionObject@endlink  object. */
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
