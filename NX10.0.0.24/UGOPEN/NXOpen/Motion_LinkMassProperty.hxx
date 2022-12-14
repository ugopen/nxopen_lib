#ifndef NXOpen_MOTION_LINKMASSPROPERTY_HXX_INCLUDED
#define NXOpen_MOTION_LINKMASSPROPERTY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_LinkMassProperty.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Motion_LinkMassProperty.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class LinkMassProperty;
    }
    class CoordinateSystem;
    class Expression;
    class Point;
    namespace Motion
    {
        class _LinkMassPropertyBuilder;
        class LinkMassPropertyImpl;
        /**
            Represents a @link NXOpen::Motion::LinkMassProperty NXOpen::Motion::LinkMassProperty@endlink 
            
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  LinkMassProperty : public NXOpen::TaggedObject
        {
            /** Defines mass property type of link */
            public: enum MassPropertyType
            {
                MassPropertyTypeAutomatic/** Mass property automatic generate */,
                MassPropertyTypeUserDefined/** Mass property defined by user */,
                MassPropertyTypeNone/** No mass property  */
            };

            private: LinkMassPropertyImpl * m_linkmassproperty_impl;
            private: friend class  _LinkMassPropertyBuilder;
            protected: LinkMassProperty();
            public: ~LinkMassProperty();
            /**Returns  the mass type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::LinkMassProperty::MassPropertyType MassType
            (
            );
            /**Sets  the mass type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetMassType
            (
                NXOpen::Motion::LinkMassProperty::MassPropertyType massType /** masstype */ 
            );
            /**Returns  the mass center 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * MassCenter
            (
            );
            /**Sets  the mass center 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetMassCenter
            (
                NXOpen::Point * massCenter /** masscenter */ 
            );
            /**Returns  the mass value 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link NXOpen::Motion::LinkMassProperty::MassExpression NXOpen::Motion::LinkMassProperty::MassExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using NXOpen::Motion::LinkMassProperty::MassExpression to query or edit it.") double MassValue
            (
            );
            /**Sets  the mass value 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link NXOpen::Motion::LinkMassProperty::MassExpression NXOpen::Motion::LinkMassProperty::MassExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using NXOpen::Motion::LinkMassProperty::MassExpression to query or edit it.") void SetMassValue
            (
                double massValue /** massvalue */ 
            );
            /**Returns  the inertia csys 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CoordinateSystem * InertiaCsys
            (
            );
            /**Sets  the inertia csys 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetInertiaCsys
            (
                NXOpen::CoordinateSystem * inertiaCsys /** inertiacsys */ 
            );
            /**Returns  the principle moment of inertia about the X axis 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link NXOpen::Motion::LinkMassProperty::IxxExpression NXOpen::Motion::LinkMassProperty::IxxExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using NXOpen::Motion::LinkMassProperty::IxxExpression to query or edit it.") double Ixx
            (
            );
            /**Sets  the principle moment of inertia about the X axis 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link NXOpen::Motion::LinkMassProperty::IxxExpression NXOpen::Motion::LinkMassProperty::IxxExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using NXOpen::Motion::LinkMassProperty::IxxExpression to query or edit it.") void SetIxx
            (
                double ixx /** ixx */ 
            );
            /**Returns  the principle moment of inertia about the Y axis 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link NXOpen::Motion::LinkMassProperty::IyyExpression NXOpen::Motion::LinkMassProperty::IyyExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using NXOpen::Motion::LinkMassProperty::IyyExpression to query or edit it.") double Iyy
            (
            );
            /**Sets  the principle moment of inertia about the Y axis 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link NXOpen::Motion::LinkMassProperty::IyyExpression NXOpen::Motion::LinkMassProperty::IyyExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using NXOpen::Motion::LinkMassProperty::IyyExpression to query or edit it.") void SetIyy
            (
                double iyy /** iyy */ 
            );
            /**Returns  the principle moment of inertia about the Y axis 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link NXOpen::Motion::LinkMassProperty::IzzExpression NXOpen::Motion::LinkMassProperty::IzzExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using NXOpen::Motion::LinkMassProperty::IzzExpression to query or edit it.") double Izz
            (
            );
            /**Sets  the principle moment of inertia about the Y axis 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link NXOpen::Motion::LinkMassProperty::IzzExpression NXOpen::Motion::LinkMassProperty::IzzExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using NXOpen::Motion::LinkMassProperty::IzzExpression to query or edit it.") void SetIzz
            (
                double izz /** izz */ 
            );
            /**Returns  the product of inertia for the X and Y axes 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link NXOpen::Motion::LinkMassProperty::IxyExpression NXOpen::Motion::LinkMassProperty::IxyExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using NXOpen::Motion::LinkMassProperty::IxyExpression to query or edit it.") double Ixy
            (
            );
            /**Sets  the product of inertia for the X and Y axes 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link NXOpen::Motion::LinkMassProperty::IxyExpression NXOpen::Motion::LinkMassProperty::IxyExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using NXOpen::Motion::LinkMassProperty::IxyExpression to query or edit it.") void SetIxy
            (
                double ixy /** ixy */ 
            );
            /**Returns  the product of inertia for the X and Z axes 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link NXOpen::Motion::LinkMassProperty::IxzExpression NXOpen::Motion::LinkMassProperty::IxzExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using NXOpen::Motion::LinkMassProperty::IxzExpression to query or edit it.") double Ixz
            (
            );
            /**Sets  the product of inertia for the X and Z axes 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link NXOpen::Motion::LinkMassProperty::IxzExpression NXOpen::Motion::LinkMassProperty::IxzExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using NXOpen::Motion::LinkMassProperty::IxzExpression to query or edit it.") void SetIxz
            (
                double ixz /** ixz */ 
            );
            /**Returns  the product of inertia for the Y and Z axes 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link NXOpen::Motion::LinkMassProperty::IyzExpression NXOpen::Motion::LinkMassProperty::IyzExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using NXOpen::Motion::LinkMassProperty::IyzExpression to query or edit it.") double Iyz
            (
            );
            /**Sets  the product of inertia for the Y and Z axes 
             <br>  @deprecated Deprecated in NX8.0.0.  Obtain the expression using @link NXOpen::Motion::LinkMassProperty::IyzExpression NXOpen::Motion::LinkMassProperty::IyzExpression@endlink  to query or edit it. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Obtain the expression using NXOpen::Motion::LinkMassProperty::IyzExpression to query or edit it.") void SetIyz
            (
                double iyz /** iyz */ 
            );
            /**Returns  the mass expression 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MassExpression
            (
            );
            /**Returns  the principle moment of inertia expression about the X axis 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * IxxExpression
            (
            );
            /**Returns  the principle moment of inertia expression about the Y axis 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * IyyExpression
            (
            );
            /**Returns  the principle moment of inertia expression about the Z axis 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * IzzExpression
            (
            );
            /**Returns  the product of inertia expression for the X and Y axes  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * IxyExpression
            (
            );
            /**Returns  the product of inertia expression for the X and Z axes 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * IxzExpression
            (
            );
            /**Returns  the product of inertia expression for the Y and Z axes 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * IyzExpression
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
