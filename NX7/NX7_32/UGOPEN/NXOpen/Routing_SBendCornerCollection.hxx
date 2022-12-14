#ifndef NXOpen_ROUTING_SBENDCORNERCOLLECTION_HXX_INCLUDED
#define NXOpen_ROUTING_SBENDCORNERCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_SBendCornerCollection.ja
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
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class SBendCornerCollection;
    }
    namespace Routing
    {
        class RouteManager;
    }
    namespace Routing
    {
        class SBendCorner;
    }
    namespace Routing
    {
        class ControlPoint;
    }
    namespace Routing
    {
        class SplineSegment;
    }
    class Spline;
    namespace Routing
    {
        /** Represents a collection of @link SBendCorner SBendCorner@endlink  objects.  <br> To obtain an instance of this class, refer to @link Routing::RouteManager Routing::RouteManager@endlink  <br> */
        class NXOPENCPPEXPORT SBendCornerCollection : public TaggedObjectCollection
        {
            private: NXOpen::Routing::RouteManager* m_owner;
            public: explicit SBendCornerCollection(NXOpen::Routing::RouteManager *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Routing::SBendCorner * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::Routing::SBendCornerCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::Routing::SBendCornerCollection *m_context;
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
            /** Creates a S-Bend corner between the start rcp and end rcp using a 
                        @link SplineSegment SplineSegment@endlink  and a bend radius.  @return  The newly created S-Bend corner object.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::SBendCorner * CreateCornerBySegBendRadius
            (
                NXOpen::Routing::ControlPoint * startRcp /** Start rcp must not be NULL. */,
                NXOpen::Routing::ControlPoint * endRcp /** End rcp must not be NULL. */,
                NXOpen::Routing::SplineSegment * segment /** Segment representing the path of the S-Bend. */,
                int sbendType /** Valid values: ROUTE_SBEND_TYPE__[1-5]. */,
                double bendRadius /** S-Bend radius. */
            );
            /** Creates a S-Bend corner between the start rcp and end rcp using a 
                        @link SplineSegment SplineSegment@endlink  and a bend ratio.  @return  The newly created S-Bend corner object.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::SBendCorner * CreateCornerBySegBendRatio
            (
                NXOpen::Routing::ControlPoint * startRcp /** Start rcp must not be NULL. */,
                NXOpen::Routing::ControlPoint * endRcp /** End rcp must not be NULL. */,
                NXOpen::Routing::SplineSegment * segment /** Segment representing the path of the S-Bend. */,
                int sbendType /** Valid values: ROUTE_SBEND_TYPE__[1-5]. */,
                double bendRatio /** S-Bend ratio. */
            );
            /** Creates a S-Bend corner between the start rcp and end rcp using a 
                        bend ratio.  @return  The newly created S-Bend Corner  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::SBendCorner * CreateCornerByBendRatio
            (
                NXOpen::Routing::ControlPoint * startRcp /** Start rcp must not be NULL. */,
                NXOpen::Routing::ControlPoint * endRcp /** End rcp must not be NULL. */,
                double bendRatio /** Bend ratio. */,
                int sbendType /** Valid values: ROUTE_SBEND_TYPE__[1-5]. */
            );
            /** Creates a S-Bend corner between the start rcp and end rcp using a 
                        bend radius.  @return  The newly created S-Bend Corner  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::SBendCorner * CreateCornerByBendRadius
            (
                NXOpen::Routing::ControlPoint * startRcp /** Start rcp must not be NULL. */,
                NXOpen::Routing::ControlPoint * endRcp /** End rcp must not be NULL. */,
                double bendRadius /** Bend radius. */,
                int sbendType /** Valid values: ROUTE_SBEND_TYPE_[1-5]. */
            );
            /** Determines if the rcp is associated to an S-Bend corner.  @return  true - The control point is a rcp for
                                                                       a S-Bend corner.
                                                               false - Otherwise  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool IsRcpAssociatedToSBend
            (
                NXOpen::Routing::ControlPoint * rcp /** Control point to be interrogated. */
            );
            /** Enquire the S-Bend Corner that this segment represents.
                         (NULL can be returned, indicating that this segment does not
                         represent a S-Bend Corner.)  @return  S-Bend Corner that segment represents 
                                                               (NULL can be returned,indicating that 
                                                               segment does not represent a S-Bend Corner).  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::SBendCorner * GetSBendAssociatedToSegment
            (
                NXOpen::Routing::SplineSegment * segment /** Segment being queried for the 
                                                                   S-Bend Corner it represents. */
            );
            /** Given a control point, get S-Bend corners pointing to it  @return  Corner objects pointing to the rcp.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Routing::SBendCorner *> GetSBendAssociatedToRcp
            (
                NXOpen::Routing::ControlPoint * rcp /** Input control point */
            );
            /** Gets the S-Bend radius of a rcp associated S-Bend corner.  @return  The bend radius. <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: double GetRcpSBendRadius
            (
                NXOpen::Routing::ControlPoint * rcp /** The control point. */
            );
            /** Gets the bend radius of a segment associated S-Bend corner.  @return  The bend radius.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: double GetSegmentSBendRadius
            (
                NXOpen::Routing::SplineSegment * segment /** The segment associated with the S-Bend corner */
            );
            /** Compute a S-Bend curve given input.   @return  TURE: if S-Bend is possible;  
                                                                   FALSE: otherwise.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool ComputeSBend
            (
                const NXOpen::Point3d & startPnt /** Start point of a S-Bend. */,
                const NXOpen::Point3d & endPnt /** end point of a S-Bend. */,
                const NXOpen::Vector3d & lineVec1 /** First S-Bend defining vector. */,
                const NXOpen::Vector3d & lineVec2 /** Second S-Bend defining vector. */,
                double radius /** Radius to use for a S-Bend */,
                int sbendType /** Valid values: ROUTE_SBEND_TYPE_[1-5]. */,
                NXOpen::Spline ** bendCurve /** S-Bend spline when a valid solution exists;  
                                                                       NULL otherwise. */
            );
            /** Compute a S-Bend parameters given input.  @return  TURE: if S-Bend is possible;  
                                                               FALSE: otherwise.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool ComputeSBendData
            (
                const NXOpen::Point3d & startPnt /** Start point of a S-Bend. */,
                const NXOpen::Point3d & endPnt /** end point of a S-Bend. */,
                const NXOpen::Vector3d & lineVec1 /** First S-Bend defining vector. */,
                const NXOpen::Vector3d & lineVec2 /** Second S-Bend defining vector. */,
                double radius /** Radius to use for a S-Bend */,
                int sbendType /** Valid values: ROUTE_SBEND_TYPE_[1-5]. */,
                NXOpen::Point3d* extensionPt1 /** Location of 1st extension point where
                                                                   bend fillets could be assigned. Value is
                                                                   not valid when no S-Bend is possible.*/,
                NXOpen::Point3d* extensionPt2 /** Location of 2nd extension point where
                                                                   bend fillets could be assigned.*/,
                NXOpen::Point3d* arc1StartPt /** Point where the first bend arc starts. 
                                                                   Only computed if not NULL. */,
                NXOpen::Point3d* arc1EndPt /** Point where the first bend arc ends. 
                                                                   Only computed if not NULL. */,
                NXOpen::Point3d* arc2StartPt /** Point where the second bend arc starts. 
                                                                               Only computed if not NULL. */,
                NXOpen::Point3d* arc2EndPt /** Point where the second bend arc ends. 
                                                                   Only computed if not NULL. */
            );
            /** Edits a selected S-Bend corner between the start rcp and end rcp using a 
                        bend radius.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void EditCornerByBendRadius
            (
                NXOpen::Routing::ControlPoint * startRcp /** Start rcp must not be NULL. */,
                NXOpen::Routing::ControlPoint * endRcp /** End rcp must not be NULL. */,
                double bendRadius /** Bend radius. */,
                int sbendType /** Valid values: ROUTE_SBEND_TYPE_[1-5]. */,
                NXOpen::Routing::SBendCorner * sbend /** S-Bend Corner to be edited. */
            );
            /** Edits a S-Bend corner between the start rcp and end rcp using a 
                        bend ratio.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void EditCornerByBendRatio
            (
                NXOpen::Routing::ControlPoint * startRcp /** Start rcp must not be NULL. */,
                NXOpen::Routing::ControlPoint * endRcp /** End rcp must not be NULL. */,
                double bendRatio /** Bend ratio. */,
                int sbendType /** Valid values: ROUTE_SBEND_TYPE__[1-5]. */,
                NXOpen::Routing::SBendCorner * sbend /** S-Bend Corner to be edited. */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
