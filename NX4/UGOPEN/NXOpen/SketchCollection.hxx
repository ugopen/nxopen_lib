#ifndef NXOpen_SKETCHCOLLECTION_HXX_INCLUDED
#define NXOpen_SKETCHCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchCollection.ja
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
#include <NXOpen/type.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class SketchCollection;
    class Part;
    class Sketch;
    class IReferenceAxis;
    class ISurface;
    class NXObject;
    class SmartObject;
    /** Represents a collection of sketches  <br> To obtain an instance of this class, refer to @link Part Part@endlink  <br> */
    class NXOPENCPPEXPORT SketchCollection : public TaggedObjectCollection
    {
        private: NXOpen::Part* m_owner;
        public: explicit SketchCollection(NXOpen::Part *owner): m_owner(owner)
        {
        }
        public: tag_t Tag() const;
        class iterator
        {
        public:
            typedef Sketch * value_type;
            iterator() : m_context(NULL), m_current(NULL_TAG)
            {
            }
            explicit iterator(NXOpen::SketchCollection *context) : m_context(context), m_current(NULL_TAG)
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
            NXOpen::SketchCollection *m_context;
            tag_t m_current;
            unsigned int m_state[8];
        };
        iterator begin();
        iterator end()
        {
            return iterator(this);
        }
        /**
            Creates a sketch
             @return  the new sketch  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: NXOpen::Sketch * CreateSketch
        (
            const NXString & name /** Name of the sketch.  The name will be converted to upper case. If this is an empty string or NULL, a name will be provided by the system.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            NXOpen::ISurface * attachment_plane /** A face or datum plane that the sketch will be attached to.  Must be planar. */,
            NXOpen::IReferenceAxis * reference_axis /** Can be a datum axis, edge, datum plane, face, or NULL.
                                                                    If it is an edge, the edge must be a line segment.  If it is a face, the
                                                                    face must be a plane.  If NULL, the reference_direction is used instead */,
            const NXOpen::Vector3d & reference_direction /** If reference_axis is NULL,
                                                          this parameter sets the reference direction of the sketch.
                                                          In this case, this parameter must not be (0,0,0).
                                                          If reference_axis is not NULL
                                                          and this parameter is not (0,0,0), this parameter
                                                          determines whether the reference direction should be
                                                          in the same direction as reference_axis
                                                          or in the opposite direction. If this parameter is (0,0,0),
                                                          this parameter is not used.  */,
            NXOpen::AxisOrientation reference_axis_orientation /** indicates whether the reference axis is horizontal or vertical */,
            NXOpen::Sense reference_axis_sense /** Ignored unless reference_direction
                                       is (0,0,0) and reference_axis is an edge or datum axis.
                                       This parameter indicates whether the reference axis should
                                       be in the same direction as reference_axis or in the opposite
                                       direction */,
            NXOpen::PlaneNormalOrientation normal_orientation /** whether the sketch's Z-axis should be outward or inward */
        );
        /**
            Creates a sketch. This function takes in an argument for the view to create the sketch in a 
            drafting member view.
             @return  the new sketch  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: NXOpen::Sketch * CreateSketch
        (
            const NXString & name /** Name of the sketch.  The name will be converted to upper case. If this is an empty string or NULL, a name will be provided by the system.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            NXOpen::ISurface * attachment_plane /** A face or datum plane that the sketch will be attached to.  Must be planar. */,
            NXOpen::IReferenceAxis * reference_axis /** Can be a datum axis, edge, datum plane, face, or NULL.
                                                                    If it is an edge, the edge must be a line segment.  If it is a face, the
                                                                    face must be a plane.  If NULL, the reference_direction is used instead */,
            const NXOpen::Vector3d & reference_direction /** If reference_axis is NULL,
                                                          this parameter sets the reference direction of the sketch.
                                                          In this case, this parameter must not be (0,0,0).
                                                          If reference_axis is not NULL
                                                          and this parameter is not (0,0,0), this parameter
                                                          determines whether the reference direction should be
                                                          in the same direction as reference_axis
                                                          or in the opposite direction. If this parameter is (0,0,0),
                                                          this parameter is not used.  */,
            NXOpen::AxisOrientation reference_axis_orientation /** indicates whether the reference axis is horizontal or vertical */,
            NXOpen::Sense reference_axis_sense /** Ignored unless reference_direction
                                       is (0,0,0) and reference_axis is an edge or datum axis.
                                       This parameter indicates whether the reference axis should
                                       be in the same direction as reference_axis or in the opposite
                                       direction */,
            NXOpen::PlaneNormalOrientation normal_orientation /** whether the sketch's Z-axis should be outward or inward */,
            NXOpen::NXObject * view /** View of the drafting view in which the sketch needsto be created */
        );
        /** Finds the @link  Sketch   Sketch @endlink  with the given name. 
            
            An exception will be thrown if no object can be found with the given name.
             @return  Sketch with this name  <br> License requirements : None */
        public: NXOpen::Sketch * FindObject
        (
            const NXString & name /** The name of the @link Sketch Sketch@endlink    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Returns the sketch that owns the specified geometry  @return  The sketch that owns the geometry  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: NXOpen::Sketch * GetOwningSketch
        (
            NXOpen::SmartObject * geometry /** */
        );
        public: virtual void initialize();
    };
}
#undef EXPORTLIBRARY
#endif
