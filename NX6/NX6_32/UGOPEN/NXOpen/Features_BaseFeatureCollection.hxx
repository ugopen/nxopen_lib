#ifndef NXOpen_FEATURES_BASEFEATURECOLLECTION_HXX_INCLUDED
#define NXOpen_FEATURES_BASEFEATURECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_BaseFeatureCollection.ja
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
    namespace Features
    {
        class BaseFeatureCollection;
    }
    class BasePart;
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class AssociativeArc;
    }
    namespace Features
    {
        class AssociativeArcBuilder;
    }
    namespace Features
    {
        class AssociativeLine;
    }
    namespace Features
    {
        class AssociativeLineBuilder;
    }
    namespace Features
    {
        class DivideCurveBuilder;
    }
    namespace Features
    {
        class MoveObject;
    }
    namespace Features
    {
        class MoveObjectBuilder;
    }
    namespace Features
    {
        class PointFeatureBuilder;
    }
    namespace Features
    {
        class TrimCornerBuilder;
    }
    namespace Features
    {
        class WaveLinkBuilder;
    }
    namespace Features
    {
        /** This class contains methods for creating builders for features that are owned by a @link BasePart BasePart@endlink 
        that is not necessarily a @link Part Part@endlink .  Note: this collection contains all features in the @link BasePart BasePart@endlink , 
        not just features for which this class contains a method to create the feature's builder.  <br> To obtain an instance of this class, refer to @link BasePart BasePart@endlink  <br> */
        class NXOPENCPPEXPORT BaseFeatureCollection : public TaggedObjectCollection
        {
            private: NXOpen::BasePart* m_owner;
            public: explicit BaseFeatureCollection(NXOpen::BasePart *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Features::Feature * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::Features::BaseFeatureCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Features::BaseFeatureCollection *m_context;
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
            /** Creates a @link Features::TrimCornerBuilder Features::TrimCornerBuilder@endlink   @return  TrimCornerBuilder object  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::TrimCornerBuilder * CreateTrimCornerBuilder
            (
                NXOpen::Features::Feature * trimCorner /** Not used as trim corner is non-associative operation */
            );
            /** Creates a @link Features::DivideCurveBuilder Features::DivideCurveBuilder@endlink   @return  DivideCurveBuilder object <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::DivideCurveBuilder * CreateDivideCurveBuilder
            (
                NXOpen::Features::Feature * divideCurve /** Not used as divide curve is non-associative operation */
            );
            /** Creates a @link Features::AssociativeLineBuilder Features::AssociativeLineBuilder@endlink   @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: NXOpen::Features::AssociativeLineBuilder * CreateAssociativeLineBuilder
            (
                NXOpen::Features::AssociativeLine * associativeLine /** @link Features::AssociativeLine Features::AssociativeLine@endlink  to be edited */
            );
            /** Creates a @link Features::AssociativeArcBuilder Features::AssociativeArcBuilder@endlink   @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: NXOpen::Features::AssociativeArcBuilder * CreateAssociativeArcBuilder
            (
                NXOpen::Features::AssociativeArc * associativeArc /** @link Features::AssociativeArc Features::AssociativeArc@endlink  to be edited */
            );
            /** Creates a @link Features::PointFeatureBuilder Features::PointFeatureBuilder@endlink   @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: NXOpen::Features::PointFeatureBuilder * CreatePointFeatureBuilder
            (
                NXOpen::Features::Feature * point /** @link Features::Feature Features::Feature@endlink  to be edited */
            );
            /** Creates a @link Features::WaveLinkBuilder Features::WaveLinkBuilder@endlink   @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::WaveLinkBuilder * CreateWaveLinkBuilder
            (
                NXOpen::Features::Feature * wavelink /**  Wavelink Feature to be edited */
            );
            /** Creates a @link Features::MoveObjectBuilder Features::MoveObjectBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Features::MoveObjectBuilder * CreateMoveObjectBuilder
            (
                NXOpen::Features::MoveObject * moveObject /** @link Features::MoveObject Features::MoveObject@endlink  to be edited */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
