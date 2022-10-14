#ifndef NXOpen_CAE_FUNCTIONCOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_FUNCTIONCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FunctionCollection.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class FunctionCollection;
    }
    class BasePart;
    namespace CAE
    {
        class Function;
    }
    namespace CAE
    {
        class FunctionBuilder;
    }
    namespace CAE
    {
        /** Represents a collection of function objects  <br> To obtain an instance of this class, refer to @link BasePart BasePart@endlink  <br> */
        class NXOPENCPPEXPORT FunctionCollection : public TaggedObjectCollection
        {
            private: NXOpen::BasePart* m_owner;
            public: explicit FunctionCollection(NXOpen::BasePart *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef CAE::Function * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::CAE::FunctionCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::CAE::FunctionCollection *m_context;
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
            /** Return @link  CAE::FunctionBuilder   CAE::FunctionBuilder @endlink  object   @return   <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: NXOpen::CAE::FunctionBuilder * CreateFunctionBuilder
            (
                NXOpen::CAE::Function * function /** function */ 
            );
            /** Copies a @link  CAE::Function   CAE::Function @endlink  in the Scenario database of Motion Simulation and
                        Advanced Simulation.  @return   <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: NXOpen::CAE::Function * Copy
            (
                NXOpen::CAE::Function * sourceFunction /** source function */ ,
                const NXString & destinationFunctionName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Delete a @link  CAE::Function   CAE::Function @endlink  in the Scenario database of Motion Simulation and
                        Advanced Simulation.  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void Delete
            (
                NXOpen::CAE::Function * deleteFunction /** the function to be deleted */
            );
            /** Finds the @link  CAE::Function   CAE::Function @endlink  with the given name.
                        An exception will be thrown if no object can be found with given name.  @return   <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: NXOpen::CAE::Function * FindObject
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif