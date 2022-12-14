#ifndef NXOpen_MECHATRONICS_RUNTIMEBUTTONBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_RUNTIMEBUTTONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_RuntimeButtonBuilder.ja
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
#include <NXOpen/Mechatronics_CollisionShapeBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class RuntimeButtonBuilder;
    }
    namespace Mechatronics
    {
        class CollisionShapeBuilder;
    }
    class NXColor;
    class NXObject;
    class SelectNXObjectList;
    namespace Mechatronics
    {
        class _RuntimeButtonBuilderBuilder;
        class RuntimeButtonBuilderImpl;
        /** Represents a @link NXOpen::Mechatronics::RuntimeButton NXOpen::Mechatronics::RuntimeButton@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Mechatronics::RuntimeButtonCollection::CreateRuntimeButtonBuilder  NXOpen::Mechatronics::RuntimeButtonCollection::CreateRuntimeButtonBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  RuntimeButtonBuilder : public NXOpen::Mechatronics::CollisionShapeBuilder
        {
            /** the button type. */
            public: enum ButtonTypes
            {
                ButtonTypesTrigger/** Trigger */,
                ButtonTypesSwitcher/** Switcher */
            };

            /** the initial value type. */
            public: enum InitialValues
            {
                InitialValuesTrue/** True */,
                InitialValuesFalse/** False */
            };

            private: RuntimeButtonBuilderImpl * m_runtimebuttonbuilder_impl;
            private: friend class  _RuntimeButtonBuilderBuilder;
            protected: RuntimeButtonBuilder();
            public: ~RuntimeButtonBuilder();
            /**Returns  the geometries. This can be a @link NXOpen::Assemblies::ComponentAssembly NXOpen::Assemblies::ComponentAssembly@endlink , @link NXOpen::Point NXOpen::Point@endlink 
                    , bodies and curves. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::SelectNXObjectList * Geometry
            (
            );
            /** Sets the geometries. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetGeometry
            (
                const std::vector<NXOpen::NXObject *> & geometries /** Input geometries*/
            );
            /**Returns  the name. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXString Name
            (
            );
            /**Sets  the name. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns  the type of button type trigger or switcher 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::RuntimeButtonBuilder::ButtonTypes ButtonType
            (
            );
            /**Sets  the type of button type trigger or switcher 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetButtonType
            (
                NXOpen::Mechatronics::RuntimeButtonBuilder::ButtonTypes buttonType /** buttontype */ 
            );
            /**Returns  the initial button status ,true or false 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::RuntimeButtonBuilder::InitialValues InitialValue
            (
            );
            /**Sets  the initial button status ,true or false 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetInitialValue
            (
                NXOpen::Mechatronics::RuntimeButtonBuilder::InitialValues initialValue /** initialvalue */ 
            );
            /**Returns  whether override active status geometry color ,true or false 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: bool OverrideActiveStatusColor
            (
            );
            /**Sets  whether override active status geometry color ,true or false 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetOverrideActiveStatusColor
            (
                bool overrideActive /** overrideactive */ 
            );
            /**Returns  the active status color. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::NXColor * ActiveStatusColor
            (
            );
            /**Sets  the active status color. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetActiveStatusColor
            (
                NXOpen::NXColor * color /** color */ 
            );
            /**Returns  whether override inactive status geometry color ,true or false 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: bool OverrideInactiveStatusColor
            (
            );
            /**Sets  whether override inactive status geometry color ,true or false 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetOverrideInactiveStatusColor
            (
                bool overrideInactive /** overrideinactive */ 
            );
            /**Returns  the inactive status color. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::NXColor * InactiveStatusColor
            (
            );
            /**Sets  the inactive status color. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetInactiveStatusColor
            (
                NXOpen::NXColor * color /** color */ 
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
