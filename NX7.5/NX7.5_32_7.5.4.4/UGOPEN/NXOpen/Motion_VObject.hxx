#ifndef NXOpen_MOTION_VOBJECT_HXX_INCLUDED
#define NXOpen_MOTION_VOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_VObject.ja
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
#include <NXOpen/Motion.hxx>
#include <NXOpen/Motion_VObject.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class VObject;
    }
    namespace CAE
    {
        class Function;
    }
    class Direction;
    namespace Motion
    {
        class SelectLink;
    }
    class Point;
    namespace Motion
    {
        /** Represents the CSYS type */
        enum VobjectCsysType
        {
            VobjectCsysTypeUserdefined/** User defined csys type */,
            VobjectCsysTypeAbsolute/** Absolute csys type */
        };

    }
    namespace Motion
    {
        class _VObjectBuilder;
        class VObjectImpl;
        /**
            Represents a VObject
            */
        class NXOPENCPPEXPORT  VObject : public TaggedObject
        {
            private: VObjectImpl * m_vobject_impl;
            private: friend class  _VObjectBuilder;
            protected: VObject();
            public: ~VObject();
            /**Returns  the force csys  <br> License requirements : None */
            public: NXOpen::Motion::VobjectCsysType Csys
            (
            );
            /**Sets  the force csys  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetCsys
            (
                NXOpen::Motion::VobjectCsysType csys /** csys */ 
            );
            /**Returns  the action link  <br> License requirements : None */
            public: NXOpen::Motion::SelectLink * ActionLink
            (
            );
            /**Returns  the origin  <br> License requirements : None */
            public: NXOpen::Point * Origin
            (
            );
            /**Sets  the origin  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetOrigin
            (
                NXOpen::Point * origin /** origin */ 
            );
            /**Returns  the direction  <br> License requirements : None */
            public: NXOpen::Direction * Direction
            (
            );
            /**Sets  the direction  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDirection
            (
                NXOpen::Direction * direction /** direction */ 
            );
            /**Returns  the reaction link  <br> License requirements : None */
            public: NXOpen::Motion::SelectLink * ReactionLink
            (
            );
            /**Returns  the value type  <br> License requirements : None */
            public: NXOpen::Motion::ForceValueTypes ValueType
            (
            );
            /**Sets  the value type  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetValueType
            (
                NXOpen::Motion::ForceValueTypes valueType /** valuetype */ 
            );
            /**Returns  the x component function   <br> License requirements : None */
            public: NXOpen::CAE::Function * XFunction
            (
            );
            /**Sets  the x component function   <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetXFunction
            (
                NXOpen::CAE::Function * function /** function */ 
            );
            /**Returns  the y component function   <br> License requirements : None */
            public: NXOpen::CAE::Function * YFunction
            (
            );
            /**Sets  the y component function   <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetYFunction
            (
                NXOpen::CAE::Function * function /** function */ 
            );
            /**Returns  the z component function   <br> License requirements : None */
            public: NXOpen::CAE::Function * ZFunction
            (
            );
            /**Sets  the z component function   <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetZFunction
            (
                NXOpen::CAE::Function * function /** function */ 
            );
            /**Returns  the magnitude function   <br> License requirements : None */
            public: NXOpen::CAE::Function * MagFunction
            (
            );
            /**Sets  the magnitude function   <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetMagFunction
            (
                NXOpen::CAE::Function * function /** function */ 
            );
            /**Returns  the x component constant value  <br> License requirements : None */
            public: double XConstant
            (
            );
            /**Sets  the x component constant value  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetXConstant
            (
                double constant /** constant */ 
            );
            /**Returns  the y component constant value  <br> License requirements : None */
            public: double YConstant
            (
            );
            /**Sets  the y component constant value  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetYConstant
            (
                double constant /** constant */ 
            );
            /**Returns  the z component constant value  <br> License requirements : None */
            public: double ZConstant
            (
            );
            /**Sets  the z component constant value  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetZConstant
            (
                double constant /** constant */ 
            );
            /**Returns  the magnitude constant value  <br> License requirements : None */
            public: double MagConstant
            (
            );
            /**Sets  the magnitude constant value  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetMagConstant
            (
                double constant /** constant */ 
            );
            /**Returns  the display scale  <br> License requirements : None */
            public: double DisplayScale
            (
            );
            /**Sets  the display scale  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDisplayScale
            (
                double displayScale /** displayscale */ 
            );
            /**Returns  the name  <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
