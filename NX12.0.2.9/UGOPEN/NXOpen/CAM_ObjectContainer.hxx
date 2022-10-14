#ifndef NXOpen_CAM_OBJECTCONTAINER_HXX_INCLUDED
#define NXOpen_CAM_OBJECTCONTAINER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ObjectContainer.ja
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
        class ObjectContainer;
    }
    namespace CAM
    {
        class _ObjectContainerBuilder;
        class ObjectContainerImpl;

        /// \cond NX_NO_DOC 
        /** Represents a Cam Objects Builder 
         <br>  Created in NX9.0.2.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ObjectContainer : public NXOpen::TaggedObject
        {
            private: ObjectContainerImpl * m_objectcontainer_impl;
            private: friend class  _ObjectContainerBuilder;
            protected: ObjectContainer();
            public: ~ObjectContainer();
            /** Cut CAM Objects 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void Cut
            (
                const std::vector<int> & current /** current */ 
            );
            /** Copy CAM Objects 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void Copy
            (
                const std::vector<int> & current /** current */ 
            );
            /** Paste CAM Objects 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void Paste
            (
                const std::vector<int> & current /** current */ 
            );
            /** Paste before CAM Objects 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void PasteBefore
            (
                const std::vector<int> & current /** current */ 
            );
            /** Delete move objects 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: void Delete
            (
                const std::vector<int> & indices /** indices */ 
            );
        };

        /// \endcond 
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