#ifndef NXOpen_CAM_MOVECOLLECTION_HXX_INCLUDED
#define NXOpen_CAM_MOVECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MoveCollection.ja
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
    namespace CAM
    {
        class MoveCollection;
    }
    namespace CAM
    {
        class Operation;
    }
    namespace CAM
    {
        class Move;
    }
    namespace CAM
    {
        class AlongMachineAxisMoveBuilder;
    }
    namespace CAM
    {
        class AlongMcsAxisMoveBuilder;
    }
    namespace CAM
    {
        class AlongToolAxisMoveBuilder;
    }
    namespace CAM
    {
        class CircularAboutAxisMoveBuilder;
    }
    namespace CAM
    {
        class DeltaMoveBuilder;
    }
    namespace CAM
    {
        class MoveToPointBuilder;
    }
    namespace CAM
    {
        class NormalToToolAxisMoveBuilder;
    }
    namespace CAM
    {
        class ProbeCalibrateLengthMoveBuilder;
    }
    namespace CAM
    {
        class ProbeCalibrateSphereMoveBuilder;
    }
    namespace CAM
    {
        class ProbeCalibrateStylusMoveBuilder;
    }
    namespace CAM
    {
        class ProbeClearanceMoveBuilder;
    }
    namespace CAM
    {
        class ProbeInspectBorebossMoveBuilder;
    }
    namespace CAM
    {
        class ProbeInspectPointMoveBuilder;
    }
    namespace CAM
    {
        class ProbeInspectSurfacePointMoveBuilder;
    }
    namespace CAM
    {
        class RotaryPointMoveBuilder;
    }
    namespace CAM
    {
        class RotaryPolarMoveBuilder;
    }
    namespace CAM
    {
        class RotateToolMoveBuilder;
    }
    namespace CAM
    {
        class UdeMoveBuilder;
    }
    namespace CAM
    {
        class VectorDistanceMoveBuilder;
    }
    namespace CAM
    {
        /** Represents the move collection  <br> To obtain an instance of this class, refer to @link CAM::Operation CAM::Operation@endlink  <br> */
        class NXOPENCPPEXPORT MoveCollection : public TaggedObjectCollection
        {
            private: NXOpen::CAM::Operation* m_owner;
            public: explicit MoveCollection(NXOpen::CAM::Operation *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef CAM::Move * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::CAM::MoveCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::CAM::MoveCollection *m_context;
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
            /** Finds the CAM.Operation object with the given identifier as recorded in a journal. @return  the found object  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::Move * FindObject
            (
                const NXString & sid /** the name of the object   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Create a Move to Point.   @return  Move To Point Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::MoveToPointBuilder * CreateMoveToPointBuilder
            (
                NXOpen::CAM::Move * param /** Move Object*/
            );
            /** Create a Delta Move.   @return  Delta Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::DeltaMoveBuilder * CreateDeltaMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move Object */
            );
            /** Create a Vector Distance Move.   @return  Delta Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::VectorDistanceMoveBuilder * CreateVectorDistanceMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move Object */
            );
            /** Create a Move Along Tool Axis  @return  Along Tool Axis Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::AlongToolAxisMoveBuilder * CreateAlongToolAxisMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move Object */
            );
            /** Create a Move Normal to Tool Axis    @return  Normal To Tool Axis Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NormalToToolAxisMoveBuilder * CreateNormalToToolAxisMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move Object */
            );
            /** Create a Move to MCS Position   @return  MCS Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::AlongMcsAxisMoveBuilder * CreateAlongMcsAxisMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move Object */
            );
            /** Create a Rotary Move to Point.   @return  Rotary Point Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::RotaryPointMoveBuilder * CreateRotaryPointMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move Object */
            );
            /** Create a Rotary Polar Move.   @return  Rotary Polar Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::RotaryPolarMoveBuilder * CreateRotaryPolarMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move Object */
            );
            /** Create a Circular Move.   @return   <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::CircularAboutAxisMoveBuilder * CreateCircularAboutAxisMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move Object */
            );
            /** Create a Move To Machine Position.   @return  Machine Position Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::AlongMachineAxisMoveBuilder * CreateAlongMachineAxisMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move Object */
            );
            /** Create a UDE Move.   @return  Ude Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::UdeMoveBuilder * CreateUdeMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move Object */
            );
            /** Create a Rotate Tool Move.   @return  Rotate Tool Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::RotateToolMoveBuilder * CreateRotateToolMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move Object */,
                NXOpen::CAM::Move * insertAfterTag /** Preceeding move  */
            );
            /** Create a Probe Calibrate Length Move.   @return  Probe Calibrate Length Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::ProbeCalibrateLengthMoveBuilder * CreateProbeCalibrateLengthMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move object */
            );
            /** Create a Probe Calibrate Stylus Move.   @return  Probe Calibrate Stylus Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::ProbeCalibrateStylusMoveBuilder * CreateProbeCalibrateStylusMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move object */
            );
            /** Create a Probe Calibrate on Sphere Move.   @return  Probe Calibrate Sphere Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::ProbeCalibrateSphereMoveBuilder * CreateProbeCalibrateSphereMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move object */
            );
            /** Create a Probe Inspect Point Move.   @return  Probe Inspect Point Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::ProbeInspectPointMoveBuilder * CreateProbeInspectPointMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move object */
            );
            /** Create a Probe Inspect Surface Point Move.   @return  Probe Inspect Surface Point Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::ProbeInspectSurfacePointMoveBuilder * CreateProbeInspectSurfacePointMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move object */
            );
            /** Create a Probe Inspect Bore-Boss Move.   @return  Probe Inspect Bore-boss Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::ProbeInspectBorebossMoveBuilder * CreateProbeInspectBorebossMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move object */
            );
            /** Create a Probe Clearance Plane Change.   @return  Probe Clearance Move Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::ProbeClearanceMoveBuilder * CreateProbeClearanceMoveBuilder
            (
                NXOpen::CAM::Move * param /** Move object */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif