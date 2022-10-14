#ifndef NXOpen_FEATURES_SHEETMETAL_BENDLISTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_BENDLISTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_BendListBuilder.ja
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
#include <NXOpen/ObjectList.hxx>
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
            class BendListBuilder;
        }
    }
    class Builder;
    namespace Features
    {
        namespace SheetMetal
        {
            class BendListItemBuilderList;
        }
    }
    class View;
    namespace Features
    {
        namespace SheetMetal
        {
            class _BendListBuilderBuilder;
            class BendListBuilderImpl;
            /** Represents a Sheetmetal Flat Pattern bend list builder class. This builder is used to
                edit the bend sequence ID and bend name of the bends in the bend list. <br> To create a new instance of this class, use @link NXOpen::Features::SheetMetal::SheetmetalManager::CreateBendListBuilder  NXOpen::Features::SheetMetal::SheetmetalManager::CreateBendListBuilder @endlink  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  BendListBuilder : public NXOpen::Builder
            {
                private: BendListBuilderImpl * m_bendlistbuilder_impl;
                private: friend class  _BendListBuilderBuilder;
                protected: BendListBuilder();
                public: ~BendListBuilder();
                /** This will populate the bend list from given flat pattern modeling view
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void PopulateBendListFromView
                (
                    NXOpen::View * flatPatternView /** flatpatternview */ 
                );
                /** This will edit a bend item in the list which has existing bend Id same as input id
                        and assign new bend Id and bend name
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: void EditBendItem
                (
                    int existingBendId /**Existing Bend Id to search*/,
                    int newBendId /**Bend Id to be assigned*/,
                    const NXString & newBendName /**Bend name to be assigned*/
                );
                /** This will edit a bend item in the list which has existing bend Id same as input id
                        and assign new bend Id and bend name
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                void EditBendItem
                (
                    int existingBendId /**Existing Bend Id to search*/,
                    int newBendId /**Bend Id to be assigned*/,
                    const char * newBendName /**Bend name to be assigned*/
                );
                /**Returns  the bend list 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::BendListItemBuilderList * BendList
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