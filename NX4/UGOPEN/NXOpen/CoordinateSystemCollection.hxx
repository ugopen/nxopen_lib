#ifndef NXOpen_COORDINATESYSTEMCOLLECTION_HXX_INCLUDED
#define NXOpen_COORDINATESYSTEMCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CoordinateSystemCollection.ja
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
    class CoordinateSystemCollection;
    class BasePart;
    class CoordinateSystem;
    class CartesianCoordinateSystem;
    class CylindricalCoordinateSystem;
    class NXMatrix;
    class SphericalCoordinateSystem;
    class Xform;
    /** Represents a collection of coordinate systems  <br> To obtain an instance of this class, refer to @link BasePart BasePart@endlink  <br> */
    class NXOPENCPPEXPORT CoordinateSystemCollection : public TaggedObjectCollection
    {
        private: NXOpen::BasePart* m_owner;
        public: explicit CoordinateSystemCollection(NXOpen::BasePart *owner): m_owner(owner)
        {
        }
        public: tag_t Tag() const;
        class iterator
        {
        public:
            typedef CoordinateSystem * value_type;
            iterator() : m_context(NULL), m_current(NULL_TAG)
            {
            }
            explicit iterator(NXOpen::CoordinateSystemCollection *context) : m_context(context), m_current(NULL_TAG)
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
            NXOpen::CoordinateSystemCollection *m_context;
            tag_t m_current;
            unsigned int m_state[8];
        };
        iterator begin();
        iterator end()
        {
            return iterator(this);
        }
        /** Creates a new cartesian coordinate system  @return  The created CartesianCoordinateSystem   <br> License requirements : None */
        public: NXOpen::CartesianCoordinateSystem * CreateCoordinateSystem
        (
            const NXOpen::Point3d & origin /** Origin of the new coordinate system 
                                             (relative to the absolute coordinate system) */,
            const NXOpen::Matrix3x3 & orientation /** Orientation of the new coordinate system 
                                             (relative to the absolute coordinate system).
                                             Must be orthonormal. */,
            bool is_temporary /** If the coordinate system is temporary, it will not be displayed 
                                          and it will not be saved in the part file */
        );
        /** Creates a new cartesian coordinate system  @return  The created CartesianCoordinateSystem  <br> License requirements : None */
        public: NXOpen::CartesianCoordinateSystem * CreateCoordinateSystem
        (
            const NXOpen::Point3d & origin /** Origin of the new coordinate system 
                                             (relative to the absolute coordinate system */,
            NXOpen::NXMatrix * orientation /** Orientation of the new coordinate system */,
            bool is_temporary /** If the coordinate system is temporary, it will not be displayed
                                          and it will not be saved in the part file */
        );
        /** Creates a CartesianCoordinateSystem from a Xform and update option.  @return  The created CartesianCoordinateSystem  <br> License requirements : None */
        public: NXOpen::CartesianCoordinateSystem * CreateCoordinateSystem
        (
            NXOpen::Xform * xform /** the Xform of the coordinate system */,
            NXOpen::SmartObject::UpdateOption update /**  update option */
        );
        /** Creates a new cylindrical coordinate system  @return  The created CylindricalCoordinateSystem  <br> License requirements : None */
        public: NXOpen::CylindricalCoordinateSystem * CreateCylindricalCoordinateSystem
        (
            const NXOpen::Point3d & origin /** Origin of the new coordinate system 
                                             (relative to the absolute coordinate system */,
            NXOpen::NXMatrix * orientation /** Orientation of the new coordinate system */,
            bool is_temporary /** If the coordinate system is temporary, it will not be displayed
                                          and it will not be saved in the part file */
        );
        /** Creates a CylindricalCoordinateSystem from a Xform and update option.  @return  The created CylindricalCoordinateSystem  <br> License requirements : None */
        public: NXOpen::CylindricalCoordinateSystem * CreateCylindricalCoordinateSystem
        (
            NXOpen::Xform * xform /** the Xform of the coordinate system */,
            NXOpen::SmartObject::UpdateOption update /**  update option */
        );
        /** Creates a new spherical coordinate system  @return  The created SphericalCoordinateSystem  <br> License requirements : None */
        public: NXOpen::SphericalCoordinateSystem * CreateSphericalCoordinateSystem
        (
            const NXOpen::Point3d & origin /** Origin of the new coordinate system 
                                             (relative to the absolute coordinate system */,
            NXOpen::NXMatrix * orientation /** Orientation of the new coordinate system */,
            bool is_temporary /** If the coordinate system is temporary, it will not be displayed
                                          and it will not be saved in the part file */
        );
        /** Creates a SphericalCoordinateSystem from a Xform and update option.  @return  The created SphericalCoordinateSystem  <br> License requirements : None */
        public: NXOpen::SphericalCoordinateSystem * CreateSphericalCoordinateSystem
        (
            NXOpen::Xform * xform /** the Xform of the coordinate system */,
            NXOpen::SmartObject::UpdateOption update /**  update option */
        );
        public: virtual void initialize();
    };
}
#undef EXPORTLIBRARY
#endif