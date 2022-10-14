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
#include <NXOpen/libnxopencpp_exports.hxx>
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
                The @link Routing::FormboardFrame Routing::FormboardFrame@endlink  is a (not pure) virtual class. 
                It has three subclasses:
                <ul>
                    <li> @link Routing::FormboardFrameCGM Routing::FormboardFrameCGM@endlink  </li>
                    <li> @link Routing::FormboardFramePattern Routing::FormboardFramePattern@endlink  </li>
                    <li> @link Routing::FormboardFrameRectangle Routing::FormboardFrameRectangle@endlink  </li>
                </ul>
                    
                It stores a reference point and frame name. 
                The access methods are implemented in the subclasses
             */
        class NXOPENCPPEXPORT  FormboardFrame : public DisplayableObject
        {
            private: FormboardFrameImpl * m_formboardframe_impl;
            private: friend class  _FormboardFrameBuilder;
            protected: FormboardFrame();
            public: ~FormboardFrame();
            /** Query the formboard frame reference point  @return  Lower left corner  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Point * GetReferencePoint
            (
            );
            /** Query the formboard frame underlying geometry  @return  Underlying geometry  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::DisplayableObject * GetObject
            (
                int* type /** type */ 
            );
            /** Sets the formboard frame reference point  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetReferencePoint
            (
                NXOpen::Point * referencePoint /** Lower left corner */
            );
            /** Sets the name of the formboard frame  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetFrameName
            (
                const NXString & newName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Makes copy of the frame, and moves it to the work layer  @return  Copy of the existing frame  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::FormboardFrame * CopyFrame
            (
            );
            /** Returns the name of the formboard frame  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString GetFrameName
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif