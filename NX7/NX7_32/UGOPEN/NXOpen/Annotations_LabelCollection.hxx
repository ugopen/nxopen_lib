#ifndef NXOpen_ANNOTATIONS_LABELCOLLECTION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_LABELCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_LabelCollection.ja
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
#include <NXOpen/Annotations_LabelData.hxx>
#include <NXOpen/Annotations_LeaderBundle.hxx>
#include <NXOpen/Annotations_PmiData.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class LabelCollection;
    }
    class Part;
    namespace Annotations
    {
        class Label;
    }
    namespace Annotations
    {
        class LabelData;
    }
    namespace Annotations
    {
        class LeaderBundle;
    }
    namespace Annotations
    {
        class PmiData;
    }
    namespace Annotations
    {
        class PmiLabel;
    }
    class Xform;
    namespace Annotations
    {
        /** Represents a collection of labels 
                <br> 
                This class is now deprecated.
                Please use @link Note Note@endlink  instead.
                 <br> 
             <br> To obtain an instance of this class, refer to @link Part Part@endlink  <br> 
         @deprecated Deprecated in NX6 <br> 
        */
        class NXOPENCPPEXPORT LabelCollection : public TaggedObjectCollection
        {
            private: NXOpen::Part* m_owner;
            public: explicit LabelCollection(NXOpen::Part *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Annotations::Label * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::Annotations::LabelCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
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
                NXOpen::Annotations::LabelCollection *m_context;
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
            /** Creates new LabelData object  @return  New LabelData 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : None */
            public: NXOpen::Annotations::LabelData * NewLabelData
            (
            );
            /** Creates a PMI label  @return  New PMI label 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::PmiLabel * CreatePmiLabel
            (
                NXOpen::Annotations::LabelData * labelData /** Label data */,
                NXOpen::Annotations::PmiData * pmiData /** PMI data */,
                NXOpen::Xform * annotationPlane /** Annotation plane on which the label lies */,
                const NXOpen::Point3d & origin /** Origin for the label */,
                NXOpen::Annotations::LeaderBundle * leader /** Specifies the leaders for the label */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
