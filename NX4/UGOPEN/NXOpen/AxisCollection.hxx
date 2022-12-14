#ifndef NXOpen_AXISCOLLECTION_HXX_INCLUDED
#define NXOpen_AXISCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AxisCollection.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class AxisCollection;
    class BasePart;
    class Axis;
    class Direction;
    class Point;
    /** Represents a collection of @link Axis Axis@endlink .  <br> To obtain an instance of this class, refer to @link BasePart BasePart@endlink  <br> */
    class NXOPENCPPEXPORT AxisCollection : public TaggedObjectCollection
    {
        private: NXOpen::BasePart* m_owner;
        public: explicit AxisCollection(NXOpen::BasePart *owner): m_owner(owner)
        {
        }
        public: tag_t Tag() const;
        class iterator
        {
        public:
            typedef Axis * value_type;
            iterator() : m_context(NULL), m_current(NULL_TAG)
            {
            }
            explicit iterator(NXOpen::AxisCollection *context) : m_context(context), m_current(NULL_TAG)
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
            NXOpen::AxisCollection *m_context;
            tag_t m_current;
            unsigned int m_state[8];
        };
        iterator begin();
        iterator end()
        {
            return iterator(this);
        }
        /** Creates an @link Axis Axis@endlink  without parameters.  @return  O -> tag of the axis <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: NXOpen::Axis * CreateAxis
        (
            NXOpen::Point * point /** I -> The point that defines the axis*/,
            NXOpen::Direction * direction /** I -> The vector that defines the axis*/,
            NXOpen::SmartObject::UpdateOption update /** I ->
                                   JA_SMART_OBJECT_update_option_within_modeling  
                                   is the only valid option at this time.  
                                   This can only be used by feature update in modeling.*/
        );
        public: virtual void initialize();
    };
}
#undef EXPORTLIBRARY
#endif
