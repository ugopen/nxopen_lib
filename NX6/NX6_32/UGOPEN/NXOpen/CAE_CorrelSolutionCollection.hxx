#ifndef NXOpen_CAE_CORRELSOLUTIONCOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_CORRELSOLUTIONCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CorrelSolutionCollection.ja
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
        class CorrelSolutionCollection;
    }
    namespace CAE
    {
        class CorrelManager;
    }
    namespace CAE
    {
        class CorrelSolution;
    }
    namespace CAE
    {
        class CorrelSolutionBuilder;
    }
    namespace CAE
    {
        /** Represents a collection of correl meta solution  <br> To obtain an instance of this class, refer to @link CAE::CorrelManager CAE::CorrelManager@endlink  <br> */
        class NXOPENCPPEXPORT CorrelSolutionCollection : public TaggedObjectCollection
        {
            private: NXOpen::CAE::CorrelManager* m_owner;
            public: explicit CorrelSolutionCollection(NXOpen::CAE::CorrelManager *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef CAE::CorrelSolution * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::CAE::CorrelSolutionCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::CAE::CorrelSolutionCollection *m_context;
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
            /** Creates the builder object of correl meta solution  @return    <br> License requirements : None */
            public: NXOpen::CAE::CorrelSolutionBuilder * CreateSolutionBuilder
            (
                NXOpen::CAE::CorrelSolution * solution /** solution */ 
            );
            /**Returns  the active solution  <br> License requirements : None */
            public: NXOpen::CAE::CorrelSolution * ActiveSolution
            (
            );
            /**Sets  the active solution  <br> License requirements : None */
            public: void SetActiveSolution
            (
                NXOpen::CAE::CorrelSolution * activeSolution /** active solution */ 
            );
            /** Returns next valid correlation solution name  @return  a  @link CAE::CorrelSolution CAE::CorrelSolution@endlink  valid name  <br> License requirements : None */
            public: NXString GetValidSolutionName
            (
            );
            /** Clones a correl meta solution  @return  the  newly created @link CAE::CorrelSolution CAE::CorrelSolution@endlink    <br> License requirements : None */
            public: NXOpen::CAE::CorrelSolution * CloneSolution
            (
                NXOpen::CAE::CorrelSolution * oldSolution /** the @link CAE::SimSolution CAE::SimSolution@endlink  to be cloned */,
                const NXString & suggestedName /** name to use instead of default name (may be NULL) */
            );
            /** Finds a correl meta solution with specified solution name  @return  Correlation metasolution found  <br> License requirements : None */
            public: NXOpen::CAE::CorrelSolution * FindObject
            (
                const NXString & solutionName /** Solution to be found    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
