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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <iterator>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/SmartObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class CoordinateSystemCollection;
    class BasePart;
    class CoordinateSystem;
    class CartesianCoordinateSystem;
    class CylindricalCoordinateSystem;
    class Direction;
    class NXMatrix;
    class Point;
    class SphericalCoordinateSystem;
    class Xform;
    class CoordinateSystemCollectionImpl;
    /** @brief  Represents a collection of @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink . 

     

    Iterating this collection only returns live uncondemned objects contained in the owning part
    of the collection. Note that @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink  is a smart object and many smart objects are condemned as they
    only exist to support other objects and are not displayed.  <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  CoordinateSystemCollection : public NXOpen::TaggedObjectCollection
    {
        private: CoordinateSystemCollectionImpl * m_coordinatesystemcollection_impl;
        private: NXOpen::BasePart* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit CoordinateSystemCollection(NXOpen::BasePart *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~CoordinateSystemCollection();
        /** Iterator for accessing the contents of the collection. */
        //lint -sem(NXOpen::CoordinateSystemCollection::iterator::copy,initializer)
        class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::CoordinateSystem *>
        {
        public:
            /** Default constructor */
            iterator() : m_context(nullptr), m_current(NULL_TAG)
            {
                // coverity[uninit_member]
            } //lint !e1401 m_state is not initialized
            /// \cond NX_NO_DOC
            explicit iterator(NXOpen::CoordinateSystemCollection *context) : m_context(context), m_current(NULL_TAG)
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
            NXOPENCPPEXPORT  value_type operator * () const;
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
            NXOpen::CoordinateSystemCollection *m_context;
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
        /** Creates a new cartesian coordinate system  @return  The created CartesianCoordinateSystem  
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::CartesianCoordinateSystem * CreateCoordinateSystem
        (
            const NXOpen::Point3d & origin /** Origin of the new coordinate system 
                                             (relative to the absolute coordinate system) */,
            const NXOpen::Matrix3x3 & orientation /** Orientation of the new coordinate system 
                                             (relative to the absolute coordinate system).
                                             Must be orthonormal. */,
            bool isTemporary /** If the coordinate system is temporary, it will not be displayed 
                                          and it will not be saved in the part file */
        );
        /** Creates a new cartesian coordinate system  @return  The created CartesianCoordinateSystem  
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::CartesianCoordinateSystem * CreateCoordinateSystem
        (
            const NXOpen::Point3d & origin /** Origin of the new coordinate system 
                                             (relative to the absolute coordinate system) */,
            const NXOpen::Vector3d & xDirection /** x direction of the new coordinate system 
                                             (relative to the absolute coordinate system) */,
            const NXOpen::Vector3d & yDirection /** y direction of the new coordinate system 
                                             (relative to the absolute coordinate system) */
        );
        /** Creates a new cylindrical coordinate system  @return  The created CylindricalCoordinateSystem  
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::CylindricalCoordinateSystem * CreateCylindricalCoordinateSystem
        (
            const NXOpen::Point3d & origin /** Origin of the new coordinate system 
                                             (relative to the absolute coordinate system) */,
            const NXOpen::Vector3d & xDirection /** x direction of the new coordinate system 
                                             (relative to the absolute coordinate system) */,
            const NXOpen::Vector3d & yDirection /** y direction of the new coordinate system 
                                             (relative to the absolute coordinate system) */
        );
        /** Creates a new spherical coordinate system  @return  The created SphericalCoordinateSystem  
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SphericalCoordinateSystem * CreateSphericalCoordinateSystem
        (
            const NXOpen::Point3d & origin /** Origin of the new coordinate system 
                                             (relative to the absolute coordinate system) */,
            const NXOpen::Vector3d & xDirection /** x direction of the new coordinate system 
                                             (relative to the absolute coordinate system) */,
            const NXOpen::Vector3d & yDirection /** y direction of the new coordinate system 
                                             (relative to the absolute coordinate system) */
        );
        /** Creates a new cartesian coordinate system  @return  The created CartesianCoordinateSystem 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::CartesianCoordinateSystem * CreateCoordinateSystem
        (
            const NXOpen::Point3d & origin /** Origin of the new coordinate system 
                                             (relative to the absolute coordinate system */,
            NXOpen::NXMatrix * orientation /** Orientation of the new coordinate system */,
            bool isTemporary /** If the coordinate system is temporary, it will not be displayed
                                          and it will not be saved in the part file */
        );
        /** Creates a CartesianCoordinateSystem from a Xform and update option.  @return  The created CartesianCoordinateSystem 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::CartesianCoordinateSystem * CreateCoordinateSystem
        (
            NXOpen::Xform * xform /** the Xform of the coordinate system */,
            NXOpen::SmartObject::UpdateOption update /**  update option */
        );
        /** Creates a new cylindrical coordinate system  @return  The created CylindricalCoordinateSystem 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::CylindricalCoordinateSystem * CreateCylindricalCoordinateSystem
        (
            const NXOpen::Point3d & origin /** Origin of the new coordinate system 
                                             (relative to the absolute coordinate system */,
            NXOpen::NXMatrix * orientation /** Orientation of the new coordinate system */,
            bool isTemporary /** If the coordinate system is temporary, it will not be displayed
                                          and it will not be saved in the part file */
        );
        /** Creates a CylindricalCoordinateSystem from a Xform and update option.  @return  The created CylindricalCoordinateSystem 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::CylindricalCoordinateSystem * CreateCylindricalCoordinateSystem
        (
            NXOpen::Xform * xform /** the Xform of the coordinate system */,
            NXOpen::SmartObject::UpdateOption update /**  update option */
        );
        /** Creates a new spherical coordinate system  @return  The created SphericalCoordinateSystem 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SphericalCoordinateSystem * CreateSphericalCoordinateSystem
        (
            const NXOpen::Point3d & origin /** Origin of the new coordinate system 
                                             (relative to the absolute coordinate system */,
            NXOpen::NXMatrix * orientation /** Orientation of the new coordinate system */,
            bool isTemporary /** If the coordinate system is temporary, it will not be displayed
                                          and it will not be saved in the part file */
        );
        /** Creates a SphericalCoordinateSystem from a Xform and update option.  @return  The created SphericalCoordinateSystem 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SphericalCoordinateSystem * CreateSphericalCoordinateSystem
        (
            NXOpen::Xform * xform /** the Xform of the coordinate system */,
            NXOpen::SmartObject::UpdateOption update /**  update option */
        );
        /** Outputs origin and directions of a cartesian coordinate system, if it is defined by point and two directions. 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void GetOriginAndDirections
        (
            NXOpen::CoordinateSystem * csystem /** csystem */ ,
            NXOpen::Point ** origin /** Origin, if exists */,
            NXOpen::Direction ** direction1 /** First direction, if exists */,
            NXOpen::Direction ** direction2 /** Second direction, if exists */
        );
    }; //lint !e1712 default constructor not defined for class  

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
