#ifndef NXOpen_CAM_INHERITABLEINTBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INHERITABLEINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InheritableIntBuilder.ja
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
#include <NXOpen/CAM_InheritableIntBuilder.hxx>
#include <NXOpen/CAM_InheritableBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class InheritableIntBuilder;
    }
    namespace CAM
    {
        class InheritableBuilder;
    }
    namespace CAM
    {
        class _InheritableIntBuilderBuilder;
        /** Represents a builder for an inheritable integer value in of a CAM.CAMObject */
        class NXOPENCPPEXPORT InheritableIntBuilder : public CAM::InheritableBuilder
        {
            private: friend class  _InheritableIntBuilderBuilder;
            protected: InheritableIntBuilder();
            /**Returns  the current value  <br> License requirements : None */
            public: int Value
            (
            );
            /**Sets  the current value  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetValue
            (
                int newValue /** the new value */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
