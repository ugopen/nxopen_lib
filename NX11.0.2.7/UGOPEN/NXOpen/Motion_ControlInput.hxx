#ifndef NXOpen_MOTION_CONTROLINPUT_HXX_INCLUDED
#define NXOpen_MOTION_CONTROLINPUT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_ControlInput.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class ControlInput;
    }
    namespace Motion
    {
        class ControlPortCollection;
    }
    class NXObject;
    namespace Motion
    {
        class _ControlInputBuilder;
        class ControlInputImpl;
        /** Represents a Control Input motion object. Control input can measure multiple kinematic variables
                between links and it can create multiple ports to store the value of each measured kinematic variable.  <br> To create or edit an instance of this class, use @link NXOpen::Motion::ControlInputBuilder  NXOpen::Motion::ControlInputBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  ControlInput : public NXOpen::NXObject
        {
            private: ControlInputImpl * m_controlinput_impl;
            private: friend class  _ControlInputBuilder;
            protected: ControlInput();
            public: ~ControlInput();


            /** Returns the @link Motion::ControlPortCollection  Motion::ControlPortCollection @endlink  belonging to this element 
             <br>  Created in NX11.0.0.  <br>  
            */
            public: NXOpen::Motion::ControlPortCollection *ControlPorts();
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