#ifndef NXOpen_OFFSETCOLLECTION_HXX_INCLUDED
#define NXOpen_OFFSETCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     OffsetCollection.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/SmartObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class OffsetCollection;
    class BasePart;
    class Offset;
    class Direction;
    class Scalar;
    class Xform;
    /**
    Represents a collection of @link Offset Offset@endlink . 
     <br> To obtain an instance of this class, refer to @link BasePart BasePart@endlink  <br> */
    class NXOPENCPPEXPORT OffsetCollection : public TaggedObjectCollection
    {
        private: NXOpen::BasePart* m_owner;
        public: explicit OffsetCollection(NXOpen::BasePart *owner): m_owner(owner)
        {
        }
        public: tag_t Tag() const;
        class iterator
        {
        public:
            typedef Offset * value_type;
            iterator() : m_context(NULL), m_current(NULL_TAG)
            {
            }
            explicit iterator(NXOpen::OffsetCollection *context) : m_context(context), m_current(NULL_TAG)
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
            NXOpen::OffsetCollection *m_context;
            tag_t m_current;
            unsigned int m_state[8];
        };
        iterator begin();
        iterator end()
        {
            return iterator(this);
        }
        /** 
           Create an @link Offset Offset@endlink  without parameters.
            @return    <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: NXOpen::Offset * CreateOffset
        (
            const NXOpen::Point3d & origin /**  Point of Offset */,
            const NXOpen::Vector3d & vector /**  Offset vector */,
            NXOpen::SmartObject::UpdateOption update_option /**  */
        );
        /**
           Create an @link Offset Offset@endlink  using X, Y and Z deltas.
            @return    <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: NXOpen::Offset * CreateOffsetRectangular
        (
            NXOpen::Scalar * delta_x /**  */,
            NXOpen::Scalar * delta_y /**  */,
            NXOpen::Scalar * delta_z /**  */,
            NXOpen::SmartObject::UpdateOption update_option /**  */
        );
        /** 
           Creates a smart cylindrical @link Offset Offset@endlink . 
           The radius, angle, and zdelta are the three parameters of cylindrical coordinates.
            @return    <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: NXOpen::Offset * CreateOffsetCylindrical
        (
            NXOpen::Scalar * radius /**  */,
            NXOpen::Scalar * angle /**  Angle in radians */,
            NXOpen::Scalar * delta_z /**  Delta along axis of cylinder */,
            NXOpen::SmartObject::UpdateOption update_option /**  */
        );
        /**
           Creates a smart spherical @link Offset Offset@endlink .
           The radius, angle1, and angle2 are the three parameters of spherical coordinates.
            @return    <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: NXOpen::Offset * CreateOffsetSpherical
        (
            NXOpen::Scalar * radius /**  */,
            NXOpen::Scalar * angle1 /**  Longitude angle in radians */,
            NXOpen::Scalar * angle2 /**  Colatitude angle in radians */,
            NXOpen::SmartObject::UpdateOption update_option /**  */
        );
        /**
           Creates an @link Offset Offset@endlink  using a Smart @link Direction Direction@endlink  and distance.
            @return    <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: NXOpen::Offset * CreateOffsetVector
        (
            NXOpen::Direction * direction /**  */,
            NXOpen::Scalar * distance /** Distance along direction */,
            NXOpen::SmartObject::UpdateOption update_option /**  */
        );
        /**
           Creates a @link Offset Offset@endlink  via an extract @link Offset Offset@endlink  with optional transformation.
            @return    <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: NXOpen::Offset * CreateOffset
        (
            NXOpen::Offset * offset_in /** Offset extract */,
            NXOpen::Xform * xform /**  Optional transformation */,
            NXOpen::SmartObject::UpdateOption update_option /**  */
        );
        public: virtual void initialize();
    };
}
#undef EXPORTLIBRARY
#endif
