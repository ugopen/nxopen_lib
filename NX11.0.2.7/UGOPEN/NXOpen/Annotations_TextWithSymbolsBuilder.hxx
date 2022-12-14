#ifndef NXOpen_ANNOTATIONS_TEXTWITHSYMBOLSBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_TEXTWITHSYMBOLSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_TextWithSymbolsBuilder.ja
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
#include <NXOpen/Annotations_TextWithSymbolsBuilder.hxx>
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
        class TextWithSymbolsBuilder;
    }
    namespace Annotations
    {
        class BaseCustomSymbol;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class NXObject;
    namespace Annotations
    {
        class _TextWithSymbolsBuilderBuilder;
        class TextWithSymbolsBuilderImpl;
        /** Represents a @link NXOpen::Annotations::TextWithSymbolsBuilder NXOpen::Annotations::TextWithSymbolsBuilder@endlink  which collects
                internationalized text strings from the user for processing on an annotation object.
              <br> This is a sub-builder class and cannot be directly instantiated  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  TextWithSymbolsBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** sizing method for embedded user-defined symbols */
            public: enum SymbolSizingMethod
            {
                SymbolSizingMethodScaleAndAspectRatio/** Size using scale and aspect ratio */,
                SymbolSizingMethodLengthAndHeight/** Size using length and height */
            };

            /** Enum for the symbol preferences */
            public: enum SymbolPreferencesType
            {
                SymbolPreferencesTypeUseCurrent/** Use Current*/,
                SymbolPreferencesTypeUseDefinition/** Use Definition*/
            };

            /** Enum for the symbol alignment */
            public: enum SymbolAlignmentType
            {
                SymbolAlignmentTypeNone/** None */,
                SymbolAlignmentTypeTop/** Top */,
                SymbolAlignmentTypeMiddle/** Middle */,
                SymbolAlignmentTypeBottom/** Bottom */,
                SymbolAlignmentTypeAnchorPoint/** Anchor Point */
            };

            private: TextWithSymbolsBuilderImpl * m_textwithsymbolsbuilder_impl;
            private: friend class  _TextWithSymbolsBuilderBuilder;
            protected: TextWithSymbolsBuilder();
            public: ~TextWithSymbolsBuilder();
            /** Returns the text of the annotation  @return  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetText
            (
            );
            /** Sets the text of the annotation 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetText
            (
                const std::vector<NXString> & text /** text */ 
            );
            /**Returns  the method in which embedded user-defined symbols are scaled 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethod SymbolSizeMethod
            (
            );
            /**Sets  the method in which embedded user-defined symbols are scaled 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetSymbolSizeMethod
            (
                NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethod symbolSizeMethod /** symbolsizemethod */ 
            );
            /**Returns  the scale of the embedded user-defined symbols if the symbol size method is
                        @link NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodScaleAndAspectRatio NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodScaleAndAspectRatio@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double SymbolScale
            (
            );
            /**Sets  the scale of the embedded user-defined symbols if the symbol size method is
                        @link NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodScaleAndAspectRatio NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodScaleAndAspectRatio@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetSymbolScale
            (
                double symbolScale /** symbolscale */ 
            );
            /**Returns  the aspect ratio of the embedded user-defined symbols if the symbol size method is
                       @link NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodScaleAndAspectRatio NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodScaleAndAspectRatio@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double SymbolAspectRatio
            (
            );
            /**Sets  the aspect ratio of the embedded user-defined symbols if the symbol size method is
                       @link NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodScaleAndAspectRatio NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodScaleAndAspectRatio@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetSymbolAspectRatio
            (
                double symbolAspectRatio /** symbolaspectratio */ 
            );
            /**Returns  the length of the embedded user-defined symbols if the symbol size method is
                        @link NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodLengthAndHeight NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodLengthAndHeight@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double SymbolLength
            (
            );
            /**Sets  the length of the embedded user-defined symbols if the symbol size method is
                        @link NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodLengthAndHeight NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodLengthAndHeight@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetSymbolLength
            (
                double symbolLength /** symbollength */ 
            );
            /**Returns  the height of the embedded user-defined symbols if the symbol size method is
                        @link NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodLengthAndHeight NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodLengthAndHeight@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double SymbolHeight
            (
            );
            /**Sets  the height of the embedded user-defined symbols if the symbol size method is
                        @link NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodLengthAndHeight NXOpen::Annotations::TextWithSymbolsBuilder::SymbolSizingMethodLengthAndHeight@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetSymbolHeight
            (
                double symbolHeight /** symbolheight */ 
            );
            /**Returns  the scale of the custom symbols  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double CustomSymbolScale
            (
            );
            /**Sets  the scale of the custom symbols  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetCustomSymbolScale
            (
                double customSymbolScale /** customsymbolscale */ 
            );
            /** Adds a symbol 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void AddSymbol
            (
                NXOpen::NXObject * newObject /** symbol instance object */,
                const NXString & name /** symbol name */,
                int lineNo /** line number to insert token with index from 1 */,
                int cursorPos /** cursor position in the line with index from 1 */
            );
            /** Adds a symbol 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void AddSymbol
            (
                NXOpen::NXObject * newObject /** symbol instance object */,
                const char * name /** symbol name */,
                int lineNo /** line number to insert token with index from 1 */,
                int cursorPos /** cursor position in the line with index from 1 */
            );
            /** Removes specified symbol 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void RemoveSymbol
            (
                const NXString & path /** Symbol name */
            );
            /** Removes specified symbol 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void RemoveSymbol
            (
                const char * path /** Symbol name */
            );
            /** Retrieves the embedded custom symbols  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Annotations::BaseCustomSymbol *> GetEmbeddedCustomSymbols
            (
            );
            /**Returns  the symbol preferences 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::TextWithSymbolsBuilder::SymbolPreferencesType SymbolPreferences
            (
            );
            /**Sets  the symbol preferences 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetSymbolPreferences
            (
                NXOpen::Annotations::TextWithSymbolsBuilder::SymbolPreferencesType symbolPreferences /** symbolpreferences */ 
            );
            /** Get the alignement of embedded symbol correspoding to symbol name @return  Symbol Alignment 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::TextWithSymbolsBuilder::SymbolAlignmentType GetSymbolAlignment
            (
                const NXString & symbolName /** Symbol Name */
            );
            /** Get the alignement of embedded symbol correspoding to symbol name @return  Symbol Alignment 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            NXOpen::Annotations::TextWithSymbolsBuilder::SymbolAlignmentType GetSymbolAlignment
            (
                const char * symbolName /** Symbol Name */
            );
            /** Set the alignement on embedded symbol correspoding to symbol name
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetSymbolAlignment
            (
                const NXString & symbolName /** Symbol Name */,
                NXOpen::Annotations::TextWithSymbolsBuilder::SymbolAlignmentType symbolAlignment /** Symbol Alignment */
            );
            /** Set the alignement on embedded symbol correspoding to symbol name
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void SetSymbolAlignment
            (
                const char * symbolName /** Symbol Name */,
                NXOpen::Annotations::TextWithSymbolsBuilder::SymbolAlignmentType symbolAlignment /** Symbol Alignment */
            );
            /** Adds an attribute reference 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void AddAttributeReference
            (
                NXOpen::NXObject * ownerTag /** object that owns the attribute.  If we are trying to reference a part attribute
                                                                          then this should be the part object */,
                const NXString & title /** title of attribute */,
                bool displayTokens /** True to display using TC tokens.
                                                                          False to display as plain text. */,
                int lineNo /** line number to insert token with index from 1 */,
                int cursorPos /** cursor position in the line with index from 1 */
            );
            /** Adds an attribute reference 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void AddAttributeReference
            (
                NXOpen::NXObject * ownerTag /** object that owns the attribute.  If we are trying to reference a part attribute
                                                                          then this should be the part object */,
                const char * title /** title of attribute */,
                bool displayTokens /** True to display using TC tokens.
                                                                          False to display as plain text. */,
                int lineNo /** line number to insert token with index from 1 */,
                int cursorPos /** cursor position in the line with index from 1 */
            );
            /** Adds an expression reference 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void AddExpressionReference
            (
                const NXString & expName /** expression name */,
                const NXString & format /** format to use for displaying an expression.
                                                          'A' for displaying the expression formula, or
                                                          'm.n' where 'm' is the minimum number of characters displayed
                                                          and 'n' is the number of decimal places to display */,
                int lineNo /** line number to insert token with index from 1 */,
                int cursorPos /** cursor position in the line with index from 1 */
            );
            /** Adds an expression reference 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            void AddExpressionReference
            (
                const char * expName /** expression name */,
                const char * format /** format to use for displaying an expression.
                                                          'A' for displaying the expression formula, or
                                                          'm.n' where 'm' is the minimum number of characters displayed
                                                          and 'n' is the number of decimal places to display */,
                int lineNo /** line number to insert token with index from 1 */,
                int cursorPos /** cursor position in the line with index from 1 */
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
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
