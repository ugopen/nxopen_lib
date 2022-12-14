#ifndef NXOpen_MECHATRONICS_OBJECTSOURCEBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_OBJECTSOURCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_ObjectSourceBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Mechatronics_ObjectSourceBuilder.hxx>
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
        class ObjectSourceBuilder;
    }
    class Builder;
    class Expression;
    class NXObject;
    class SelectNXObjectList;
    namespace Mechatronics
    {
        class _ObjectSourceBuilderBuilder;
        class ObjectSourceBuilderImpl;
        /** Represents a @link Mechatronics::ObjectSource Mechatronics::ObjectSource@endlink  builder.  <br> To create a new instance of this class, use @link Mechatronics::ObjectSourceCollection::CreateObjectSourceBuilder  Mechatronics::ObjectSourceCollection::CreateObjectSourceBuilder @endlink  <br> 
         <br>  Created in NX7.5.1.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  ObjectSourceBuilder : public Builder
        {
            /** Trigger Option in copy event. */
            public: enum CopyEventTriggerOption
            {
                CopyEventTriggerOptionTimeBased/** TimeBased*/,
                CopyEventTriggerOptionOncePerActivation/** OncePerActivation*/
            };

            private: ObjectSourceBuilderImpl * m_objectsourcebuilder_impl;
            private: friend class  _ObjectSourceBuilderBuilder;
            protected: ObjectSourceBuilder();
            public: ~ObjectSourceBuilder();
            /**Returns  the object select. This can be a @link RigidBody RigidBody@endlink  or @link Assemblies::ComponentAssembly Assemblies::ComponentAssembly@endlink .
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::SelectNXObjectList * ObjectToCopy
            (
            );
            /** Sets the objects to be copied.
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetObjectsToCopy
            (
                const std::vector<NXOpen::NXObject *> & objects /** Objects to be copied*/
            );
            /**Returns  the event option. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::ObjectSourceBuilder::CopyEventTriggerOption CopyEventTrigger
            (
            );
            /**Sets  the event option. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetCopyEventTrigger
            (
                NXOpen::Mechatronics::ObjectSourceBuilder::CopyEventTriggerOption copyEventTrigger /** copyeventtrigger */ 
            );
            /**Returns  the time interval. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Expression * TimeInterval
            (
            );
            /**Returns  the start offset. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Expression * StartOffset
            (
            );
            /**Returns  the name. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXString Name
            (
            );
            /**Sets  the name. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            void SetName
            (
                const char * name /** name */ 
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
