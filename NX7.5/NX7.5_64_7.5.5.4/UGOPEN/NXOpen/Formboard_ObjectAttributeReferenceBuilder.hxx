#ifndef NXOpen_FORMBOARD_OBJECTATTRIBUTEREFERENCEBUILDER_HXX_INCLUDED
#define NXOpen_FORMBOARD_OBJECTATTRIBUTEREFERENCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Formboard_ObjectAttributeReferenceBuilder.ja
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
#include <NXOpen/Annotations_LeaderBuilder.hxx>
#include <NXOpen/Annotations_OriginBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Formboard_ObjectAttributeReferenceBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Formboard
    {
        class ObjectAttributeReferenceBuilder;
    }
    namespace Annotations
    {
        class LeaderBuilder;
    }
    namespace Annotations
    {
        class OriginBuilder;
    }
    class Builder;
    class SelectNXObject;
    namespace Formboard
    {
        class _ObjectAttributeReferenceBuilderBuilder;
        class ObjectAttributeReferenceBuilderImpl;
        /** Builder for "object attribute" used in formboard which enbles user to create
                annotation in drafting functionality. It creates a tabular note and displays
                object attributes of a single object selected by user.
             <br> To create a new instance of this class, use @link Formboard::FormboardManager::CreateObjectAttributeReferenceBuilder Formboard::FormboardManager::CreateObjectAttributeReferenceBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        EnumType </td> <td> 
         
        None </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  ObjectAttributeReferenceBuilder : public Builder
        {
            /** Enum which defines types of leader user wants to associate with the annotation.
                        User can either create no leader or one or two leader for the annotation when picking 
                        the associated object.
                    */
            public: enum LeaderType
            {
                LeaderTypeNone/** No leader for annotation of selected object.*/,
                LeaderTypeSingleLocation/** Single leader for the annotation of selected object.*/,
                LeaderTypeStartandEndLocations/** Two leaders for annotation with start and end location.*/
            };

            private: ObjectAttributeReferenceBuilderImpl * m_objectattributereferencebuilder_impl;
            private: friend class  _ObjectAttributeReferenceBuilderBuilder;
            protected: ObjectAttributeReferenceBuilder();
            public: ~ObjectAttributeReferenceBuilder();
            /**Returns  the object selected by user to associated annotation  <br> License requirements : None */
            public: NXOpen::SelectNXObject * ObjectSelection
            (
            );
            /**Returns  the enum type  <br> License requirements : None */
            public: NXOpen::Formboard::ObjectAttributeReferenceBuilder::LeaderType EnumType
            (
            );
            /**Sets  the enum type  <br> License requirements : None */
            public: void SetEnumType
            (
                NXOpen::Formboard::ObjectAttributeReferenceBuilder::LeaderType enumType /** enumtype */ 
            );
            /**Returns  the comp origin  <br> License requirements : None */
            public: NXOpen::Annotations::OriginBuilder * CompOrigin
            (
            );
            /**Returns  the @link Annotations::LeaderBuilder Annotations::LeaderBuilder@endlink  for the annotation  <br> License requirements : None */
            public: NXOpen::Annotations::LeaderBuilder * AnnotLeader
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
