#ifndef NXOpen_ASSEMBLIES_EXPLOSIONCOLLECTION_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_EXPLOSIONCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_ExplosionCollection.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Assemblies
    {
        class ExplosionCollection;
    }
    namespace Assemblies
    {
        class ComponentAssembly;
    }
    namespace Assemblies
    {
        class Explosion;
    }
    namespace Assemblies
    {
        /** Represents a collection of explosions  <br> To obtain an instance of this class, refer to @link ComponentAssembly ComponentAssembly@endlink  <br> */
        class NXOPENCPPEXPORT ExplosionCollection : public TaggedObjectCollection
        {
            private: NXOpen::Assemblies::ComponentAssembly* m_owner;
            public: explicit ExplosionCollection(NXOpen::Assemblies::ComponentAssembly *owner): m_owner(owner)
            {
            }
            public: tag_t Tag() const;
            class iterator
            {
            public:
                typedef Assemblies::Explosion * value_type;
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::Assemblies::ExplosionCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                }
                iterator(const iterator &other)
                {
                    copy(other);
                }
                iterator &operator =(const iterator &other)
                {
                    if (&other != this)
                        copy(other);
                    return *this;
                }
                bool operator ==(const iterator &other) const
                {
                    return m_current == other.m_current && m_context == other.m_context;
                }
                bool operator !=(const iterator &other) const
                {
                    return !operator == (other);
                }
                NXOPENCPPEXPORT  value_type operator * ();
                iterator & operator ++()
                {
                    next();
                    return *this;
                }
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
                NXOpen::Assemblies::ExplosionCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            iterator begin();
            iterator end()
            {
                return iterator(this);
            }
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
