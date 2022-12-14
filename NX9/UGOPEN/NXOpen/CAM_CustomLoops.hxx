#ifndef NXOpen_CAM_CUSTOMLOOPS_HXX_INCLUDED
#define NXOpen_CAM_CUSTOMLOOPS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CustomLoops.ja
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
#include <NXOpen/CAM_CustomLoopSet.hxx>
#include <NXOpen/CAM_CustomLoops.hxx>
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
        class CustomLoops;
    }
    namespace CAM
    {
        class CustomLoopSet;
    }
    namespace CAM
    {
        class CustomLoopSetList;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace CAM
    {
        class _CustomLoopsBuilder;
        class CustomLoopsImpl;
        /**  Represents a CustomLoops object. 
         <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::Features::PatchOpeningsBuilder NXOpen::Features::PatchOpeningsBuilder@endlink  instead. <br>  

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::Features::PatchOpeningsBuilder instead.")  CustomLoops : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: CustomLoopsImpl * m_customloops_impl;
            private: friend class  _CustomLoopsBuilder;
            protected: CustomLoops();
            public: ~CustomLoops();
            /**Returns  the loop set list 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::Features::PatchOpeningsBuilder NXOpen::Features::PatchOpeningsBuilder@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::Features::PatchOpeningsBuilder instead.") NXOpen::CAM::CustomLoopSetList * LoopList
            (
            );
            /** Create a custom loop set @return  the loop set object 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::Features::PatchOpeningsBuilder NXOpen::Features::PatchOpeningsBuilder@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::Features::PatchOpeningsBuilder instead.") NXOpen::CAM::CustomLoopSet * CreateLoopSet
            (
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
