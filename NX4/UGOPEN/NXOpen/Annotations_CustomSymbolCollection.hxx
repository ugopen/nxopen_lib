#ifndef NXOpen_ANNOTATIONS_CUSTOMSYMBOLCOLLECTION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_CUSTOMSYMBOLCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_CustomSymbolCollection.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Annotations_CustomSymbolData.hxx>
#include <NXOpen/Annotations_LeaderBundle.hxx>
#include <NXOpen/Annotations_PmiData.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class CustomSymbolCollection;
    }
    namespace Annotations
    {
        class AnnotationManager;
    }
    namespace Annotations
    {
        class CustomSymbol;
    }
    namespace Annotations
    {
        class CustomSymbolData;
    }
    namespace Annotations
    {
        class LeaderBundle;
    }
    namespace Annotations
    {
        class PmiCustomSymbol;
    }
    namespace Annotations
    {
        class PmiData;
    }
    class Xform;
    namespace Annotations
    {
        /** Represents a collection of @link Annotations::CustomSymbol Annotations::CustomSymbol@endlink  objects  <br> To obtain an instance of this class, refer to @link AnnotationManager AnnotationManager@endlink  <br> */
        class NXOPENCPPEXPORT CustomSymbolCollection : public TaggedObjectCollection
        {
            private: NXOpen::Annotations::AnnotationManager* m_owner;
            public: explicit CustomSymbolCollection(NXOpen::Annotations::AnnotationManager *owner): m_owner(owner)
            {
            }
            public: tag_t Tag() const;
            class iterator
            {
            public:
                typedef Annotations::CustomSymbol * value_type;
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::Annotations::CustomSymbolCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Annotations::CustomSymbolCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            iterator begin();
            iterator end()
            {
                return iterator(this);
            }
            /** Creates new CustomSymbolData object  @return  New CustomSymbolData  <br> License requirements : None */
            public: NXOpen::Annotations::CustomSymbolData * NewCustomSymbolData
            (
                const NXString & master_file_name /** Part File name of the master symbol(without the extension)   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Creates a custom symbol  @return  New custom symbol  <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Annotations::CustomSymbol * CreateCustomSymbol
            (
                NXOpen::Annotations::CustomSymbolData * custom_symbol_data /** */,
                const NXOpen::Point3d & origin /** Origin for the custom symbol */,
                NXOpen::Annotations::LeaderBundle * leader /** Specifies the leaders for the custom symbol */
            );
            /** Creates a PMI custom symbol  @return  New PMI custom symbol  <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::PmiCustomSymbol * CreatePmiCustomSymbol
            (
                NXOpen::Annotations::CustomSymbolData * custom_symbol_data /** */,
                NXOpen::Annotations::PmiData * pmi_data /** PMI data */,
                NXOpen::Xform * annotation_plane /** Annotation plane on which the custom symbol lies */,
                const NXOpen::Point3d & origin /** Origin for the custom symbol */,
                NXOpen::Annotations::LeaderBundle * leader /** Specifies the leaders for the custom symbol */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
