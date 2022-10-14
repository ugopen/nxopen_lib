#ifndef NXOpen_ANNOTATIONS_MASTERSYMBOLLISTITEMBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_MASTERSYMBOLLISTITEMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_MasterSymbolListItemBuilder.ja
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
#include <NXOpen/Annotations_MasterSymbolListItemBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class MasterSymbolListItemBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Annotations
    {
        class _MasterSymbolListItemBuilderBuilder;
        class MasterSymbolListItemBuilderImpl;
        /**
            Represents a @link Annotations::MasterSymbolListItemBuilder Annotations::MasterSymbolListItemBuilder@endlink 
             <br> To create a new instance of this class, use @link Annotations::CustomSymbolCollection::CreateMasterSymbolListItemBuilder Annotations::CustomSymbolCollection::CreateMasterSymbolListItemBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  MasterSymbolListItemBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /** The Enum for Text Types */
            public: enum TextTypes
            {
                TextTypesMandatory/** mandatory */ ,
                TextTypesArbitrary/** arbitrary */ ,
                TextTypesControlled/** controlled */ ,
                TextTypesPartiallyControlled/** partially controlled */ ,
                TextTypesInteger/** integer */ ,
                TextTypesReal/** real */ 
            };

            private: MasterSymbolListItemBuilderImpl * m_mastersymbollistitembuilder_impl;
            private: friend class  _MasterSymbolListItemBuilderBuilder;
            protected: MasterSymbolListItemBuilder();
            public: ~MasterSymbolListItemBuilder();
            /**Returns  the note title  <br> License requirements : None */
            public: NXString NoteTitle
            (
            );
            /**Sets  the note title  <br> License requirements : drafting ("DRAFTING") */
            public: void SetNoteTitle
            (
                const NXString & noteTitle /** notetitle */ 
            );
            /**Returns  the text type  <br> License requirements : None */
            public: NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypes TextType
            (
            );
            /**Sets  the text type  <br> License requirements : drafting ("DRAFTING") */
            public: void SetTextType
            (
                NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypes textType /** texttype */ 
            );
            /** Returns the  multiple notes for a given Text Type. this property is valid for 
                    @link  Annotations::MasterSymbolListItemBuilder::TextTypesArbitrary   Annotations::MasterSymbolListItemBuilder::TextTypesArbitrary @endlink , 
                    @link  Annotations::MasterSymbolListItemBuilder::TextTypesControlled   Annotations::MasterSymbolListItemBuilder::TextTypesControlled @endlink ,
                    @link  Annotations::MasterSymbolListItemBuilder::TextTypesPartiallyControlled   Annotations::MasterSymbolListItemBuilder::TextTypesPartiallyControlled @endlink 
                     @return   <br> License requirements : None */
            public: std::vector<NXString> GetMultilineString
            (
            );
            /** Sets the multiple notes for the given Text Type  <br> License requirements : drafting ("DRAFTING") */
            public: void SetMultilineString
            (
                const std::vector<NXString> & multilineString /** array of notes */
            );
            /**Returns  the integer min , this property is valid if text type is @link  Annotations::MasterSymbolListItemBuilder::TextTypesInteger   Annotations::MasterSymbolListItemBuilder::TextTypesInteger @endlink   <br> License requirements : None */
            public: int IntegerMin
            (
            );
            /**Sets  the integer min , this property is valid if text type is @link  Annotations::MasterSymbolListItemBuilder::TextTypesInteger   Annotations::MasterSymbolListItemBuilder::TextTypesInteger @endlink   <br> License requirements : drafting ("DRAFTING") */
            public: void SetIntegerMin
            (
                int integerMin /** integermin */ 
            );
            /**Returns  the integer max ,this property is valid if text type is @link  Annotations::MasterSymbolListItemBuilder::TextTypesInteger   Annotations::MasterSymbolListItemBuilder::TextTypesInteger @endlink   <br> License requirements : None */
            public: int IntegerMax
            (
            );
            /**Sets  the integer max ,this property is valid if text type is @link  Annotations::MasterSymbolListItemBuilder::TextTypesInteger   Annotations::MasterSymbolListItemBuilder::TextTypesInteger @endlink   <br> License requirements : drafting ("DRAFTING") */
            public: void SetIntegerMax
            (
                int integerMax /** integermax */ 
            );
            /**Returns  the integer default, this property is valid if text type is @link  Annotations::MasterSymbolListItemBuilder::TextTypesInteger   Annotations::MasterSymbolListItemBuilder::TextTypesInteger @endlink   <br> License requirements : None */
            public: int IntegerDefault
            (
            );
            /**Sets  the integer default, this property is valid if text type is @link  Annotations::MasterSymbolListItemBuilder::TextTypesInteger   Annotations::MasterSymbolListItemBuilder::TextTypesInteger @endlink   <br> License requirements : drafting ("DRAFTING") */
            public: void SetIntegerDefault
            (
                int integerDefault /** integerdefault */ 
            );
            /**Returns  the double min, this property is valid if text type is @link  Annotations::MasterSymbolListItemBuilder::TextTypesReal   Annotations::MasterSymbolListItemBuilder::TextTypesReal @endlink   <br> License requirements : None */
            public: double DoubleMin
            (
            );
            /**Sets  the double min, this property is valid if text type is @link  Annotations::MasterSymbolListItemBuilder::TextTypesReal   Annotations::MasterSymbolListItemBuilder::TextTypesReal @endlink   <br> License requirements : drafting ("DRAFTING") */
            public: void SetDoubleMin
            (
                double doubleMin /** doublemin */ 
            );
            /**Returns  the double max, this property is valid if text type is @link  Annotations::MasterSymbolListItemBuilder::TextTypesReal   Annotations::MasterSymbolListItemBuilder::TextTypesReal @endlink   <br> License requirements : None */
            public: double DoubleMax
            (
            );
            /**Sets  the double max, this property is valid if text type is @link  Annotations::MasterSymbolListItemBuilder::TextTypesReal   Annotations::MasterSymbolListItemBuilder::TextTypesReal @endlink   <br> License requirements : drafting ("DRAFTING") */
            public: void SetDoubleMax
            (
                double doubleMax /** doublemax */ 
            );
            /**Returns  the double default, this property is valid if text type is @link  Annotations::MasterSymbolListItemBuilder::TextTypesReal   Annotations::MasterSymbolListItemBuilder::TextTypesReal @endlink   <br> License requirements : None */
            public: double DoubleDefault
            (
            );
            /**Sets  the double default, this property is valid if text type is @link  Annotations::MasterSymbolListItemBuilder::TextTypesReal   Annotations::MasterSymbolListItemBuilder::TextTypesReal @endlink   <br> License requirements : drafting ("DRAFTING") */
            public: void SetDoubleDefault
            (
                double doubleDefault /** doubledefault */ 
            );
            /**Returns  the note text <br> License requirements : None */
            public: NXString NoteText
            (
            );
            /**Sets  the note text <br> License requirements : drafting ("DRAFTING") */
            public: void SetNoteText
            (
                const NXString & noteText /** notetext */ 
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : None */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif