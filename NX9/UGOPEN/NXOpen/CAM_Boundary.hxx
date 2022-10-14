#ifndef NXOpen_CAM_BOUNDARY_HXX_INCLUDED
#define NXOpen_CAM_BOUNDARY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_Boundary.ja
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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CAM_Boundary.hxx>
#include <NXOpen/CAM_BoundaryMillingSet.hxx>
#include <NXOpen/CAM_BoundarySet.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
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
        class Boundary;
    }
    namespace CAM
    {
        class BoundaryMillingSet;
    }
    namespace CAM
    {
        class BoundarySet;
    }
    namespace CAM
    {
        class BoundarySetList;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class TaggedObject;
    namespace CAM
    {
        class _BoundaryBuilder;
        class BoundaryImpl;
        /** Represents a CAM boundary object 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  Boundary : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: BoundaryImpl * m_boundary_impl;
            private: friend class  _BoundaryBuilder;
            protected: Boundary();
            public: ~Boundary();
            /**Returns  the boundary list 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundarySetList * BoundaryList
            (
            );
            /** Create an empty boundary set @return  the boundary set object 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::BoundarySet * CreateBoundarySet
            (
            );
            /** Create an empty milling boundary set @return  the milling boundary set object 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::BoundaryMillingSet * CreateBoundaryMillingSet
            (
            );
            /** Append the face boundary  @return  array of the appended face boundary set objects 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: std::vector<NXOpen::CAM::BoundarySet *> AppendFaceBoundary
            (
                NXOpen::TaggedObject * face /** the face to create boundaries*/,
                bool ignoreHole /** flag to ignore holes in face */,
                bool ignoreIsland /** flag to ignore islands on face */,
                bool ignoreChamfer /** flag to ignore chamfers on face */,
                NXOpen::CAM::BoundarySet::ToolSideTypes toolSide /** tool side for the face boundary */
            );
            /** Remove the face boundaries 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void RemoveFaceBoundary
            (
                NXOpen::TaggedObject * face /** the face to be removed */
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
            (
            );
        };
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