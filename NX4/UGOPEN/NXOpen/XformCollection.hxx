#ifndef NXOpen_XFORMCOLLECTION_HXX_INCLUDED
#define NXOpen_XFORMCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     XformCollection.ja
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
    class XformCollection;
    class BasePart;
    class Xform;
    namespace Assemblies
    {
        class Component;
    }
    namespace Assemblies
    {
        class Explosion;
    }
    class CoordinateSystem;
    class Direction;
    class DisplayableObject;
    class NXObject;
    class Offset;
    class Point;
    class Scalar;
    /** Represents a collection of smart xforms.  <br> To obtain an instance of this class, refer to @link BasePart BasePart@endlink  <br> */
    class NXOPENCPPEXPORT XformCollection : public TaggedObjectCollection
    {
        private: NXOpen::BasePart* m_owner;
        public: explicit XformCollection(NXOpen::BasePart *owner): m_owner(owner)
        {
        }
        public: tag_t Tag() const;
        class iterator
        {
        public:
            typedef Xform * value_type;
            iterator() : m_context(NULL), m_current(NULL_TAG)
            {
            }
            explicit iterator(NXOpen::XformCollection *context) : m_context(context), m_current(NULL_TAG)
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
            NXOpen::XformCollection *m_context;
            tag_t m_current;
            unsigned int m_state[8];
        };
        iterator begin();
        iterator end()
        {
            return iterator(this);
        }
        /** 
             Creates a Xform without parameters. 
             @return    <br> License requirements : None */
        public: NXOpen::Xform * CreateXform
        (
            const NXOpen::Point3d & origin /**   Origin point */,
            const NXOpen::Vector3d & x_direction /**   X direction */,
            const NXOpen::Vector3d & y_direction /**   Y direction */,
            NXOpen::SmartObject::UpdateOption update_option /**   */,
            double scale /**  */
        );
        /**
            Creates a Xform that based off the model space coordinate system.  
            The X and Y Axes are the X and Y Axes of the absolute transform.  The origin is the 
            origin of the absolute transform.
             @return    <br> License requirements : None */
        public: NXOpen::Xform * CreateXform
        (
            NXOpen::SmartObject::UpdateOption update_option /**   */,
            double scale /**   */
        );
        /** Create a Xform based on three points. 
             The origin is the first point, the X-Axis is the vector from the first to the
              second point, and the Y-Axis is the vector from the first to the third 
              point. 
             @return    <br> License requirements : None */
        public: NXOpen::Xform * CreateXform
        (
            NXOpen::Point * point1 /**  */,
            NXOpen::Point * point2 /**  */,
            NXOpen::Point * point3 /** */,
            NXOpen::SmartObject::UpdateOption update_option /**   */,
            double scale /**   */
        );
        /** Creates a Xform by three planes. These can be either planar faces for datum planes. 
            Defines a xform based on the three input planes. The X-Axis is normal of the first 
            plane, the Y-Axis is normal of the second plane, the origin is the intersection of the three plane.
            The plane can either be a planar @link Face Face@endlink  or a @link DatumPlane DatumPlane@endlink . 
             @return    <br> License requirements : None */
        public: NXOpen::Xform * CreateXform
        (
            NXOpen::DisplayableObject * plane1 /** */,
            NXOpen::DisplayableObject * plane2 /** */,
            NXOpen::DisplayableObject * plane3 /** */,
            NXOpen::SmartObject::UpdateOption update_option /**   */,
            double scale /**   */
        );
        /** Creates a Xform by picking up a point from an existing coordinate system
             @return  Xform  <br> License requirements : None */
        public: NXOpen::Xform * CreateXform
        (
            NXOpen::CoordinateSystem * csys /** Existing coordinate system */,
            NXOpen::Point * point0 /** Start point */,
            NXOpen::Point * point1 /** End point */,
            NXOpen::Scalar * rotation_scalar_x /** Scalar of X rotation */,
            NXOpen::Scalar * rotation_scalar_y /** Scalar of Y rotation */,
            NXOpen::Scalar * rotation_scalar_z /** Scalar of Z rotation */,
            int rotation_option /** Determine the sequence of applying rotation and translation.
                                                                         If the value is 0, then a translation is first applied.
                                                                         Otherwise, a roation is first applied.
                                                                     */,
            NXOpen::SmartObject::UpdateOption update_option /** Update option of smart object */,
            double scale /** Xform scalar */
        );
        /** Creates a Xform by offsetting an existing coordinate system through 
                a translation and a rotation
             @return  Xform  <br> License requirements : None */
        public: NXOpen::Xform * CreateXform
        (
            NXOpen::CoordinateSystem * csys /** Existing coordinate system */,
            NXOpen::Offset * point0 /** Start point */,
            NXOpen::Offset * point1 /** End point */,
            NXOpen::Scalar * rotation_scalar_x /** Scalar of X rotation */,
            NXOpen::Scalar * rotation_scalar_y /** Scalar of Y rotation */,
            NXOpen::Scalar * rotation_scalar_z /** Scalar of Z rotation */,
            int rotation_option /** Determine the sequence of applying rotation and translation.
                                                                         If the value is 0, then a translation is first applied.
                                                                         Otherwise, a roation is first applied.
                                                                     */,
            NXOpen::SmartObject::UpdateOption update_option /** Update option of smart object */,
            double scale /** Xform scalar */
        );
        /** Creates a Xform based on a point and two vectors. 

         @return    <br> License requirements : None */
        public: NXOpen::Xform * CreateXform
        (
            NXOpen::Point * origin /**  */,
            NXOpen::Direction * x_direction /**  */,
            NXOpen::Direction * y_direction /**   */,
            NXOpen::SmartObject::UpdateOption update_option /**   */,
            double scale /**   */
        );
        /** Creates a Xform based on two vectors. The X and Y Axes are vectors, with the
        origin being the vector intersection point.   
         @return    <br> License requirements : None */
        public: NXOpen::Xform * CreateXform
        (
            NXOpen::Direction * x_direction /** */,
            NXOpen::Direction * y_direction /**  */,
            NXOpen::SmartObject::UpdateOption update_option /**   */,
            double scale /**   */
        );
        /** Creates a Xform based on a plane and a vector.  The X-Axis is the plane normal 
         direction, the Y-Axis is the direction of the projection of the vector onto the plane, 
         and the origin is the intersection of the plane and the vector.  The plane can 
         either be a planar @link Face Face@endlink  or 
         a @link DatumPlane DatumPlane@endlink .  
         
         @return    <br> License requirements : None */
        public: NXOpen::Xform * CreateXform
        (
            NXOpen::DisplayableObject * plane /** */,
            NXOpen::Direction * axis /**  */,
            NXOpen::SmartObject::UpdateOption update_option /**   */,
            double scale /**   */
        );
        /** TO_DO_NX4_JA Create a Xform by a point and a Z-axis. 
        The X-Axis is the vector from the Z-Axis vector to the point; 
        the Y-Axis is computed from the X and Z axis; the origin is the 
        intersection of the three vectors.
        [version_created("3")]
        extern int API_OVERLOAD(JA_XFORM_COLLECTION_create_xform,_by_x_point_z_axis)
        (
            tag_t part API_THIS,
            tag_t x_point API_IN API_TYPE(Point), 
            tag_t z_axis API_IN  API_TYPE(AXIS) FIX ME IMPLEMENT AXIS , 
            JA_SMART_OBJECT_update_option update_option API_IN, 
            tag_t *xform API_RESULT API_TYPE(Xform)
        );
         @return   <br> License requirements : None */
        public: NXOpen::Xform * CreateXformFromCurrentView
        (
            NXOpen::SmartObject::UpdateOption update_option /** */,
            double scale /** */
        );
        /** Creates an Xform based on an object and an explosion.
             @return  Xform  <br> License requirements : None */
        public: NXOpen::Xform * CreateXform
        (
            NXOpen::NXObject * object /** NX object */,
            NXOpen::Assemblies::Explosion * explosion /** Explosion */,
            NXOpen::SmartObject::UpdateOption update_option /** Update option of smart object */
        );
        /** Creates an Xform based on the delta difference between the source and
                destination components in the explosion.
             @return  Xform  <br> License requirements : None */
        public: NXOpen::Xform * CreateXform
        (
            NXOpen::Assemblies::Explosion * explosion /** Explosion */,
            NXOpen::Assemblies::Component * source_component /** Source component */,
            NXOpen::Assemblies::Component * dest_component /** Destination component */,
            NXOpen::SmartObject::UpdateOption update_option /** Update option of smart object */
        );
        public: virtual void initialize();
    };
}
#undef EXPORTLIBRARY
#endif
