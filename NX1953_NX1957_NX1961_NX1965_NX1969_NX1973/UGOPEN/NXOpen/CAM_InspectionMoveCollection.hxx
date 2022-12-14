#ifndef NXOpen_CAM_INSPECTIONMOVECOLLECTION_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONMOVECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionMoveCollection.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <iterator>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class InspectionMoveCollection;
    }
    namespace CAM
    {
        class InspectionOperation;
    }
    namespace CAM
    {
        class InspectionMoveSubop;
    }
    namespace CAM
    {
        class InspectionCircularMoveToPointBuilder;
    }
    namespace CAM
    {
        class InspectionDeltaMoveBuilder;
    }
    namespace CAM
    {
        class InspectionLinear5axisMoveToPointBuilder;
    }
    namespace CAM
    {
        class InspectionLinearMoveToPointBuilder;
    }
    namespace CAM
    {
        class InspectionMeasurePointBuilder;
    }
    namespace CAM
    {
        class InspectionPolarGridBuilder;
    }
    namespace CAM
    {
        class InspectionScanArcBuilder;
    }
    namespace CAM
    {
        class InspectionScanCurve5AxisBuilder;
    }
    namespace CAM
    {
        class InspectionScanCurveBuilder;
    }
    namespace CAM
    {
        class InspectionScanHelixBuilder;
    }
    namespace CAM
    {
        class InspectionScanLineBuilder;
    }
    namespace CAM
    {
        class InspectionSensorMassEditBuilder;
    }
    namespace CAM
    {
        class InspectionUVGridBuilder;
    }
    namespace CAM
    {
        class InspectionMoveCollectionImpl;
        /** Represents the Inspection move collection  <br> To obtain an instance of this class, refer to @link NXOpen::CAM::InspectionOperation  NXOpen::CAM::InspectionOperation @endlink  <br> 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionMoveCollection : public NXOpen::TaggedObjectCollection
        {
            private: InspectionMoveCollectionImpl * m_inspectionmovecollection_impl;
            private: NXOpen::CAM::InspectionOperation* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit InspectionMoveCollection(NXOpen::CAM::InspectionOperation *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~InspectionMoveCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::CAM::InspectionMoveCollection::iterator::copy,initializer)
            class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::CAM::InspectionMoveSubop *>
            {
            public:
                /** Default constructor */
                iterator() : m_context(nullptr), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::CAM::InspectionMoveCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                    // coverity[uninit_member]
                }//lint !e1401 m_state is not initialized
                /// \endcond
                /** Copy constructor */
                iterator(const iterator &other): m_context(nullptr), m_current(NULL_TAG)
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
                NXOPENCPP_CAMEXPORT  value_type operator * () const;
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
                NXOPENCPP_CAMEXPORT  void next();
                NXOpen::CAM::InspectionMoveCollection *m_context;
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
            /** Finds the CAM.InspectionMoveSubop object with the given identifier as recorded in a journal.  @return  the found object 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::InspectionMoveSubop * FindObject
            (
                const NXString & sid /** the name of the object */
            );
            /** Finds the CAM.InspectionMoveSubop object with the given identifier as recorded in a journal.  @return  the found object 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            NXOpen::CAM::InspectionMoveSubop * FindObject
            (
                const char * sid /** the name of the object */
            );
            /** Create a CMM Inspection Linear Move To Point sub-operation.   @return  CMM Inspection Linear Move To Point Builder 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::InspectionLinearMoveToPointBuilder * CreateInspectionLinearMoveToPointBuilder
            (
                NXOpen::CAM::InspectionMoveSubop * param /** Inspection Move object */
            );
            /** Create a CMM Inspection Rectangular UV Grid sub-operation.   @return  CMM Inspection UV Grid Builder 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::InspectionUVGridBuilder * CreateInspectionUvgridBuilder
            (
                NXOpen::CAM::InspectionMoveSubop * param /** Inspection Move object */
            );
            /** Create a CMM Inspection Measure Point sub-operation.   @return  CMM Inspection Measure Point Builder 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::InspectionMeasurePointBuilder * CreateInspectionMeasurePointBuilder
            (
                NXOpen::CAM::InspectionMoveSubop * param /** Inspection Move object */
            );
            /** Create a CMM Inspection Scan Curve sub-operation.   @return  CMM Inspection Scan Curve Builder 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::InspectionScanCurveBuilder * CreateInspectionScanCurveBuilder
            (
                NXOpen::CAM::InspectionMoveSubop * param /** Inspection Move object */
            );
            /** Create a CMM Inspection Scan Line sub-operation.   @return  CMM Inspection Scan Line Builder 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::InspectionScanLineBuilder * CreateInspectionScanLineBuilder
            (
                NXOpen::CAM::InspectionMoveSubop * param /** Inspection Move object */
            );
            /** Create a CMM Inspection Scan Arc sub-operation.   @return  CMM Inspection Scan Arc Builder 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::InspectionScanArcBuilder * CreateInspectionScanArcBuilder
            (
                NXOpen::CAM::InspectionMoveSubop * param /** Inspection Move object */
            );
            /** Create a CMM Inspection Delta Move sub-operation.   @return  CMM Inspection Delta Move Builder 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::InspectionDeltaMoveBuilder * CreateInspectionDeltaMoveBuilder
            (
                NXOpen::CAM::InspectionMoveSubop * param /** Inspection Move object */
            );
            /** Create a CMM Inspection 5 Axis Scan Curve sub-operation.   @return  CMM Inspection 5 Axis Scan Curve Builder 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::InspectionScanCurve5AxisBuilder * CreateInspectionScanCurve5axisBuilder
            (
                NXOpen::CAM::InspectionMoveSubop * param /** Inspection Move object */
            );
            /** Create a CMM Inspection subop sensor mass edit dialog builder.   @return  Inspection Subop Sensor Mass Edit builder created 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::InspectionSensorMassEditBuilder * CreateInspectionSensorMassEditBuilder
            (
                NXOpen::CAM::InspectionMoveSubop * param /** Inspection Move object */
            );
            /** Create a CMM Inspection Linear 5axis Move To Point sub-operation.   @return  CMM Inspection Linear 5axis Move To Point Builder 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::InspectionLinear5axisMoveToPointBuilder * CreateInspectionLinear5axisMoveToPointBuilder
            (
                NXOpen::CAM::InspectionMoveSubop * param /** Inspection Move object */
            );
            /** Create a CMM Inspection Scan Helix sub-operation.   @return  CMM Inspection Scan Helix Builder 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::InspectionScanHelixBuilder * CreateInspectionScanHelixBuilder
            (
                NXOpen::CAM::InspectionMoveSubop * param /** Inspection Move object */
            );
            /** Create a CMM Inspection Polar Grid sub-operation.  @return  CMM Inspection Polar Grid Builder 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::InspectionPolarGridBuilder * CreateInspectionPolarGridBuilder
            (
                NXOpen::CAM::InspectionMoveSubop * param /** Inspection Move object */
            );
            /** Create a CMM Inspection Circular Move To Point sub-operation.   @return  CMM Inspection Circular Move To Point Builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::InspectionCircularMoveToPointBuilder * CreateInspectionCircularMoveToPointBuilder
            (
                NXOpen::CAM::InspectionMoveSubop * param /** Inspection Move object */
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif
