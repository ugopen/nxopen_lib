#ifndef NXOpen_ROUTING_FORMBOARDFRAME_HXX_INCLUDED
#define NXOpen_ROUTING_FORMBOARDFRAME_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_FormboardFrame.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/libnxopencpp_routing_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Routing
    {
        class FormboardFrame;
    }
    class DisplayableObject;
    class Point;
    namespace Routing
    {
        class _FormboardFrameBuilder;
        class FormboardFrameImpl;
        /**
                The @link NXOpen::Routing::FormboardFrame NXOpen::Routing::FormboardFrame@endlink  is a (not pure) virtual class. 
                It has three subclasses:
                <ul>
                    <li> @link NXOpen::Routing::FormboardFrameCGM NXOpen::Routing::FormboardFrameCGM@endlink  </li>
                    <li> @link NXOpen::Routing::FormboardFramePattern NXOpen::Routing::FormboardFramePattern@endlink  </li>
                    <li> @link NXOpen::Routing::FormboardFrameRectangle NXOpen::Routing::FormboardFrameRectangle@endlink  </li>
                </ul>
                    
                It stores a reference point and frame name. 
                The access methods are implemented in the subclasses
             
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  FormboardFrame : public NXOpen::DisplayableObject
        {
            private: FormboardFrameImpl * m_formboardframe_impl;
            private: friend class  _FormboardFrameBuilder;
            protected: FormboardFrame();
            public: ~FormboardFrame();
            /** Query the formboard frame reference point  @return  Lower left corner 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: NXOpen::Point * GetReferencePoint
            (
            );
            /** Query the formboard frame underlying geometry  @return  Underlying geometry 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: NXOpen::DisplayableObject * GetObject
            (
                int* type /** type */ 
            );
            /** Sets the formboard frame reference point 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: void SetReferencePoint
            (
                NXOpen::Point * referencePoint /** Lower left corner */
            );
            /** Sets the name of the formboard frame 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: void SetFrameName
            (
                const NXString & newName /** new name */ 
            );
            /** Sets the name of the formboard frame 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            void SetFrameName
            (
                const char * newName /** new name */ 
            );
            /** Makes copy of the frame, and moves it to the work layer  @return  Copy of the existing frame 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: NXOpen::Routing::FormboardFrame * CopyFrame
            (
            );
            /** Returns the name of the formboard frame 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : routing_harness ("Routing Harness") */
            public: NXString GetFrameName
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