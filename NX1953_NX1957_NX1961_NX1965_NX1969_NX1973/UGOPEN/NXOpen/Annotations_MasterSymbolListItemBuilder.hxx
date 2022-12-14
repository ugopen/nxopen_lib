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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

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
            Represents a @link NXOpen::Annotations::MasterSymbolListItemBuilder NXOpen::Annotations::MasterSymbolListItemBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::Annotations::CustomSymbolCollection::CreateMasterSymbolListItemBuilder  NXOpen::Annotations::CustomSymbolCollection::CreateMasterSymbolListItemBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  MasterSymbolListItemBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** The Enum for Text Types */
            public: enum TextTypes
            {
                TextTypesMandatory/** mandatory */ ,
                TextTypesArbitrary/** arbitrary */ ,
                TextTypesControlled/** controlled */ ,
                TextTypesPartiallyControlled/** partially controlled */ ,
                TextTypesInteger/** integer */ ,
                TextTypesReal/** real */ ,
                TextTypesRule/** rule */ 
            };

            private: MasterSymbolListItemBuilderImpl * m_mastersymbollistitembuilder_impl;
            private: friend class  _MasterSymbolListItemBuilderBuilder;
            protected: MasterSymbolListItemBuilder();
            public: ~MasterSymbolListItemBuilder();
            /**Returns  the note title 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString NoteTitle
            (
            );
            /**Sets  the note title 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetNoteTitle
            (
                const NXString & noteTitle /** notetitle */ 
            );
            /**Sets  the note title 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void SetNoteTitle
            (
                const char * noteTitle /** notetitle */ 
            );
            /**Returns  the text type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypes TextType
            (
            );
            /**Sets  the text type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetTextType
            (
                NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypes textType /** texttype */ 
            );
            /** Returns the  multiple notes for a given Text Type. this property is valid for 
                    @link  NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesArbitrary   NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesArbitrary @endlink , 
                    @link  NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesControlled   NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesControlled @endlink ,
                    @link  NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesPartiallyControlled   NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesPartiallyControlled @endlink 
                    
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetMultilineString
            (
            );
            /** Sets the multiple notes for the given Text Type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetMultilineString
            (
                const std::vector<NXString> & multilineString /** array of notes */
            );
            /**Returns  the integer min , this property is valid if text type is @link  NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesInteger   NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesInteger @endlink  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: int IntegerMin
            (
            );
            /**Sets  the integer min , this property is valid if text type is @link  NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesInteger   NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesInteger @endlink  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetIntegerMin
            (
                int integerMin /** integermin */ 
            );
            /**Returns  the integer max ,this property is valid if text type is @link  NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesInteger   NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesInteger @endlink  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: int IntegerMax
            (
            );
            /**Sets  the integer max ,this property is valid if text type is @link  NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesInteger   NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesInteger @endlink  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetIntegerMax
            (
                int integerMax /** integermax */ 
            );
            /**Returns  the integer default, this property is valid if text type is @link  NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesInteger   NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesInteger @endlink  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: int IntegerDefault
            (
            );
            /**Sets  the integer default, this property is valid if text type is @link  NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesInteger   NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesInteger @endlink  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetIntegerDefault
            (
                int integerDefault /** integerdefault */ 
            );
            /**Returns  the double min, this property is valid if text type is @link  NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesReal   NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesReal @endlink  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double DoubleMin
            (
            );
            /**Sets  the double min, this property is valid if text type is @link  NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesReal   NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesReal @endlink  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetDoubleMin
            (
                double doubleMin /** doublemin */ 
            );
            /**Returns  the double max, this property is valid if text type is @link  NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesReal   NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesReal @endlink  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double DoubleMax
            (
            );
            /**Sets  the double max, this property is valid if text type is @link  NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesReal   NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesReal @endlink  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetDoubleMax
            (
                double doubleMax /** doublemax */ 
            );
            /**Returns  the double default, this property is valid if text type is @link  NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesReal   NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesReal @endlink  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double DoubleDefault
            (
            );
            /**Sets  the double default, this property is valid if text type is @link  NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesReal   NXOpen::Annotations::MasterSymbolListItemBuilder::TextTypesReal @endlink  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetDoubleDefault
            (
                double doubleDefault /** doubledefault */ 
            );
            /**Returns  the first line of note text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString NoteText
            (
            );
            /**Sets  the first line of note text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetNoteText
            (
                const NXString & noteText /** notetext */ 
            );
            /**Sets  the first line of note text 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void SetNoteText
            (
                const char * noteText /** notetext */ 
            );
            /**Returns  the note rule 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Rule
            (
            );
            /**Sets  the note rule 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_layout ("NX Layout") */
            public: void SetRule
            (
                const NXString & rule /** rule */ 
            );
            /**Sets  the note rule 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_layout ("NX Layout") */
            void SetRule
            (
                const char * rule /** rule */ 
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not yet implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
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
