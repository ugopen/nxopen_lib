#ifndef NXOpen_ANNOTATIONS_BUSINESSMODIFIERCOLLECTION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_BUSINESSMODIFIERCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_BusinessModifierCollection.ja
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
    namespace Annotations
    {
        class BusinessModifierCollection;
    }
    namespace Annotations
    {
        class AnnotationManager;
    }
    namespace Annotations
    {
        class BusinessModifier;
    }
    namespace Annotations
    {
        class CustomerValueBusinessModifier;
    }
    namespace Annotations
    {
        class RevisionBusinessModifier;
    }
    namespace Annotations
    {
        class SafetyClassBusinessModifier;
    }
    namespace Annotations
    {
        class UrlBusinessModifier;
    }
    namespace Annotations
    {
        /** Represents a collection of @link Annotations::BusinessModifier Annotations::BusinessModifier@endlink  objects  <br> To obtain an instance of this class, refer to @link AnnotationManager AnnotationManager@endlink  <br> */
        class NXOPENCPPEXPORT BusinessModifierCollection : public TaggedObjectCollection
        {
            private: NXOpen::Annotations::AnnotationManager* m_owner;
            public: explicit BusinessModifierCollection(NXOpen::Annotations::AnnotationManager *owner): m_owner(owner)
            {
            }
            public: tag_t Tag() const;
            class iterator
            {
            public:
                typedef Annotations::BusinessModifier * value_type;
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::Annotations::BusinessModifierCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Annotations::BusinessModifierCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            iterator begin();
            iterator end()
            {
                return iterator(this);
            }
            /** Creates a URL business modifier  @return  New url business modifier  <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::UrlBusinessModifier * CreateUrlBusinessModifier
            (
                const NXString & modifier_name /** Knowledge fusion name of modifier */
            );
            /** Creates a customer value business modifier   @return  New customer value business modifier  <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::CustomerValueBusinessModifier * CreateCustomerValueBusinessModifier
            (
                const NXString & modifier_name /** Knowledge fusion name of modifier */
            );
            /** Creates a revision business modifier  @return  New revision business modifier  <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::RevisionBusinessModifier * CreateRevisonBusinessModifier
            (
                const NXString & modifier_name /** Knowledge fusion name of modifier */
            );
            /** Creates a safety class business modifier  @return  New safety class business modifier  <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::SafetyClassBusinessModifier * CreateSafetyClassBusinessModifier
            (
                const NXString & modifier_name /** Knowledge fusion name of modifier */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
