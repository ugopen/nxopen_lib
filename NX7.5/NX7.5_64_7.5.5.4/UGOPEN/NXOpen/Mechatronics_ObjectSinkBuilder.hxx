#ifndef NXOpen_MECHATRONICS_OBJECTSINKBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_OBJECTSINKBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_ObjectSinkBuilder.ja
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
#include <NXOpen/Mechatronics_ObjectSinkBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Mechatronics
    {
        class ObjectSinkBuilder;
    }
    class Builder;
    namespace Mechatronics
    {
        class SelectCollisionSensorList;
    }
    class SelectNXObjectList;
    namespace Mechatronics
    {
        class _ObjectSinkBuilderBuilder;
        class ObjectSinkBuilderImpl;
        /** Represents a @link Mechatronics::ObjectSink Mechatronics::ObjectSink@endlink  builder.  <br> To create a new instance of this class, use @link Mechatronics::ObjectSinkCollection::CreateObjectSinkBuilder Mechatronics::ObjectSinkCollection::CreateObjectSinkBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  ObjectSinkBuilder : public Builder
        {
            /** the delete option. */
            public: enum DeleteSourceType
            {
                DeleteSourceTypeAnycopiedobjects/** Any copied objects */,
                DeleteSourceTypeSelectedsources/** Selected sources   */
            };

            private: ObjectSinkBuilderImpl * m_objectsinkbuilder_impl;
            private: friend class  _ObjectSinkBuilderBuilder;
            protected: ObjectSinkBuilder();
            public: ~ObjectSinkBuilder();
            /**Returns  the object select. This can be a @link CollisionSensor CollisionSensor@endlink .  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::SelectCollisionSensorList * CollisionSensor
            (
            );
            /**Returns  the option to delete source.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::ObjectSinkBuilder::DeleteSourceType DeleteSource
            (
            );
            /**Sets  the option to delete source.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetDeleteSource
            (
                NXOpen::Mechatronics::ObjectSinkBuilder::DeleteSourceType deleteSource /** deletesource */ 
            );
            /**Returns  the source select.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::SelectNXObjectList * Source
            (
            );
            /**Returns  the name.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXString Name
            (
            );
            /**Sets  the name.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif