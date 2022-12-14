#ifndef NXOpen_CAE_MESHCOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_MESHCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_MeshCollection.ja
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
        class MeshCollection;
    }
    namespace CAE
    {
        class FEModel;
    }
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        class DependentMesh;
    }
    namespace CAE
    {
        class DependentMeshBuilder;
    }
    namespace CAE
    {
        class MappedMesh;
    }
    namespace CAE
    {
        class MappedMeshBuilder;
    }
    namespace CAE
    {
        /**  @brief  Creates Meshes@link CAE::MeshCollection CAE::MeshCollection@endlink  in a fem part  

           <br> To obtain an instance of this class, refer to @link CAE::FEModel CAE::FEModel@endlink  <br> */
        class NXOPENCPPEXPORT MeshCollection : public TaggedObjectCollection
        {
            private: NXOpen::CAE::FEModel* m_owner;
            public: explicit MeshCollection(NXOpen::CAE::FEModel *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef CAE::Mesh * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::CAE::MeshCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::CAE::MeshCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            /** Returns an iterator addressing the first element. */
            iterator begin();
            /** Returns an iterator addressing the last element. */
            iterator end()
            {
                return iterator(this);
            }
            /** Finds the @link CAE::Mesh CAE::Mesh@endlink  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.

                    An exception will be thrown if no object can be found with the given journal identifier.  @return  mesh  with this identifier  <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::CAE::Mesh * FindObject
            (
                const NXString & journal_identifier /** Mesh name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Creates a mapped mesh builder 
                      @return  Mapped Mesh Builder is created  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::MappedMeshBuilder * CreateMappedMeshBuilder
            (
                NXOpen::CAE::MappedMesh * mapped_mesh /** Mapped Mesh entity to be edited, if NULL then create a new one */
            );
            /** Creates a dependent mesh builder 
                      @return  Dependent Mesh Builder is created  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::DependentMeshBuilder * CreateDependentMeshBuilder
            (
                NXOpen::CAE::DependentMesh * dependent_mesh /** Dependent Mesh entity to be edited, if NULL then create a new one */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
