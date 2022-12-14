#ifndef NXOpen_ANNOTATIONS_CUSTOMSYMBOLDATA_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_CUSTOMSYMBOLDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_CustomSymbolData.ja
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
#include <NXOpen/Annotations_CustomSymbolTextData.hxx>
#include <NXOpen/CustomSymbols.hxx>
#include <NXOpen/TransientObject.hxx>
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
        class CustomSymbolData;
    }
    namespace Annotations
    {
        class CustomSymbolTextData;
    }
    class Expression;
    namespace Annotations
    {
    }
    namespace Annotations
    {
        class CustomSymbolDataImpl;
        /** Represents custom symbol data 
         <br>  @deprecated Deprecated in NX9.0.0.  Use @link Annotations::DraftingCustomSymbolBuilder Annotations::DraftingCustomSymbolBuilder@endlink  for Drafting Custom Symbol and @link Annotations::PmiCustomSymbolBuilder Annotations::PmiCustomSymbolBuilder@endlink  for PMI Custom Symbol objects. <br>  

         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  NX_DEPRECATED("Deprecated in NX9.0.0.  Use Annotations::DraftingCustomSymbolBuilder for Drafting Custom Symbol and Annotations::PmiCustomSymbolBuilder for PMI Custom Symbol objects.")  CustomSymbolData : public TransientObject
        {
            private: CustomSymbolDataImpl * m_customsymboldata_impl;
            /// \cond NX_NO_DOC 
            public: explicit CustomSymbolData(void *ptr);
            /// \endcond 
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.  
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link Annotations::DraftingCustomSymbolBuilder Annotations::DraftingCustomSymbolBuilder@endlink  for Drafting Custom Symbol and @link Annotations::PmiCustomSymbolBuilder Annotations::PmiCustomSymbolBuilder@endlink  for PMI Custom Symbol objects. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use Annotations::DraftingCustomSymbolBuilder for Drafting Custom Symbol and Annotations::PmiCustomSymbolBuilder for PMI Custom Symbol objects.") virtual ~CustomSymbolData();
            /**Returns  the angle 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link Annotations::DraftingCustomSymbolBuilder Annotations::DraftingCustomSymbolBuilder@endlink  for Drafting Custom Symbol and @link Annotations::PmiCustomSymbolBuilder Annotations::PmiCustomSymbolBuilder@endlink  for PMI Custom Symbol objects. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use Annotations::DraftingCustomSymbolBuilder for Drafting Custom Symbol and Annotations::PmiCustomSymbolBuilder for PMI Custom Symbol objects.") double Angle
            (
            );
            /**Sets  the angle 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link Annotations::DraftingCustomSymbolBuilder Annotations::DraftingCustomSymbolBuilder@endlink  for Drafting Custom Symbol and @link Annotations::PmiCustomSymbolBuilder Annotations::PmiCustomSymbolBuilder@endlink  for PMI Custom Symbol objects. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use Annotations::DraftingCustomSymbolBuilder for Drafting Custom Symbol and Annotations::PmiCustomSymbolBuilder for PMI Custom Symbol objects.") void SetAngle
            (
                double angle /** New angle at which custom symbol will be oriented */
            );
            /**Returns  the scale 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link Annotations::DraftingCustomSymbolBuilder Annotations::DraftingCustomSymbolBuilder@endlink  for Drafting Custom Symbol and @link Annotations::PmiCustomSymbolBuilder Annotations::PmiCustomSymbolBuilder@endlink  for PMI Custom Symbol objects. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use Annotations::DraftingCustomSymbolBuilder for Drafting Custom Symbol and Annotations::PmiCustomSymbolBuilder for PMI Custom Symbol objects.") double Scale
            (
            );
            /**Sets  the scale 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link Annotations::DraftingCustomSymbolBuilder Annotations::DraftingCustomSymbolBuilder@endlink  for Drafting Custom Symbol and @link Annotations::PmiCustomSymbolBuilder Annotations::PmiCustomSymbolBuilder@endlink  for PMI Custom Symbol objects. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use Annotations::DraftingCustomSymbolBuilder for Drafting Custom Symbol and Annotations::PmiCustomSymbolBuilder for PMI Custom Symbol objects.") void SetScale
            (
                double scale /** New scale */
            );
            /**Returns  the scale expression 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link Annotations::DraftingCustomSymbolBuilder Annotations::DraftingCustomSymbolBuilder@endlink  for Drafting Custom Symbol and @link Annotations::PmiCustomSymbolBuilder Annotations::PmiCustomSymbolBuilder@endlink  for PMI Custom Symbol objects. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use Annotations::DraftingCustomSymbolBuilder for Drafting Custom Symbol and Annotations::PmiCustomSymbolBuilder for PMI Custom Symbol objects.") NXOpen::Expression * ScaleExpression
            (
            );
            /**Sets  the scale expression 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link Annotations::DraftingCustomSymbolBuilder Annotations::DraftingCustomSymbolBuilder@endlink  for Drafting Custom Symbol and @link Annotations::PmiCustomSymbolBuilder Annotations::PmiCustomSymbolBuilder@endlink  for PMI Custom Symbol objects. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use Annotations::DraftingCustomSymbolBuilder for Drafting Custom Symbol and Annotations::PmiCustomSymbolBuilder for PMI Custom Symbol objects.") void SetScaleExpression
            (
                NXOpen::Expression * scaleExpression /** New scale expression */
            );
            /**Returns  the text preferences option. This option is only available when creating. 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link Annotations::DraftingCustomSymbolBuilder Annotations::DraftingCustomSymbolBuilder@endlink  for Drafting Custom Symbol and @link Annotations::PmiCustomSymbolBuilder Annotations::PmiCustomSymbolBuilder@endlink  for PMI Custom Symbol objects. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use Annotations::DraftingCustomSymbolBuilder for Drafting Custom Symbol and Annotations::PmiCustomSymbolBuilder for PMI Custom Symbol objects.") NXOpen::Annotations::TextPreferencesOption TextPreferencesOption
            (
            );
            /**Sets  the text preferences option. This option is only available when creating. 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link Annotations::DraftingCustomSymbolBuilder Annotations::DraftingCustomSymbolBuilder@endlink  for Drafting Custom Symbol and @link Annotations::PmiCustomSymbolBuilder Annotations::PmiCustomSymbolBuilder@endlink  for PMI Custom Symbol objects. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use Annotations::DraftingCustomSymbolBuilder for Drafting Custom Symbol and Annotations::PmiCustomSymbolBuilder for PMI Custom Symbol objects.") void SetTextPreferencesOption
            (
                NXOpen::Annotations::TextPreferencesOption option /** New text preferences option */
            );
            /**Returns  the symbol preferences option. This option is only available when creating. 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link Annotations::DraftingCustomSymbolBuilder Annotations::DraftingCustomSymbolBuilder@endlink  for Drafting Custom Symbol and @link Annotations::PmiCustomSymbolBuilder Annotations::PmiCustomSymbolBuilder@endlink  for PMI Custom Symbol objects. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use Annotations::DraftingCustomSymbolBuilder for Drafting Custom Symbol and Annotations::PmiCustomSymbolBuilder for PMI Custom Symbol objects.") NXOpen::Annotations::SymbolPreferencesOption SymbolPreferencesOption
            (
            );
            /**Sets  the symbol preferences option. This option is only available when creating. 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link Annotations::DraftingCustomSymbolBuilder Annotations::DraftingCustomSymbolBuilder@endlink  for Drafting Custom Symbol and @link Annotations::PmiCustomSymbolBuilder Annotations::PmiCustomSymbolBuilder@endlink  for PMI Custom Symbol objects. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use Annotations::DraftingCustomSymbolBuilder for Drafting Custom Symbol and Annotations::PmiCustomSymbolBuilder for PMI Custom Symbol objects.") void SetSymbolPreferencesOption
            (
                NXOpen::Annotations::SymbolPreferencesOption option /** New symbol preferences option */
            );
            /** Return the text data  @return  List of text data objects 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link Annotations::DraftingCustomSymbolBuilder Annotations::DraftingCustomSymbolBuilder@endlink  for Drafting Custom Symbol and @link Annotations::PmiCustomSymbolBuilder Annotations::PmiCustomSymbolBuilder@endlink  for PMI Custom Symbol objects. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use Annotations::DraftingCustomSymbolBuilder for Drafting Custom Symbol and Annotations::PmiCustomSymbolBuilder for PMI Custom Symbol objects.") std::vector<NXOpen::Annotations::CustomSymbolTextData *> GetTextData
            (
            );
            /** Sets the text data 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link Annotations::DraftingCustomSymbolBuilder Annotations::DraftingCustomSymbolBuilder@endlink  for Drafting Custom Symbol and @link Annotations::PmiCustomSymbolBuilder Annotations::PmiCustomSymbolBuilder@endlink  for PMI Custom Symbol objects. <br>  

             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use Annotations::DraftingCustomSymbolBuilder for Drafting Custom Symbol and Annotations::PmiCustomSymbolBuilder for PMI Custom Symbol objects.") void SetTextData
            (
                const std::vector<NXOpen::Annotations::CustomSymbolTextData *> & data /** List of text data objects */
            );
        }; //lint !e1712 default constructor not defined for class  

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
