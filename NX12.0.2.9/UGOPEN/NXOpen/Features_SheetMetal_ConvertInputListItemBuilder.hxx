#ifndef NXOpen_FEATURES_SHEETMETAL_CONVERTINPUTLISTITEMBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_CONVERTINPUTLISTITEMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_ConvertInputListItemBuilder.ja
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
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class ConvertInputListItemBuilder;
        }
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class ScCollector;
    namespace Features
    {
        namespace SheetMetal
        {
            class _ConvertInputListItemBuilderBuilder;
            class ConvertInputListItemBuilderImpl;
            /**
                    Represents a Sheetmetal convert to sheet metal corner list item builder class.
                    This builder is used to interrogate the corner items in the list.
                     <br> To create a new instance of this class, use @link NXOpen::Features::SheetMetal::ConvertToSheetmetalBuilder::CreateConvertInputListItem  NXOpen::Features::SheetMetal::ConvertToSheetmetalBuilder::CreateConvertInputListItem @endlink  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ConvertInputListItemBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
            {
                private: ConvertInputListItemBuilderImpl * m_convertinputlistitembuilder_impl;
                private: friend class  _ConvertInputListItemBuilderBuilder;
                protected: ConvertInputListItemBuilder();
                public: ~ConvertInputListItemBuilder();
                /**Returns  the corner faces 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::ScCollector * CornerFaces
                (
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
