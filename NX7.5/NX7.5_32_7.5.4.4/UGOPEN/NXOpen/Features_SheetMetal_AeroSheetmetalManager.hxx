#ifndef NXOpen_FEATURES_SHEETMETAL_AEROSHEETMETALMANAGER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_AEROSHEETMETALMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_AeroSheetmetalManager.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class AeroSheetmetalManager;
        }
    }
    namespace Features
    {
        class FeatureCollection;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class AeroFlangeBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class AeroJoggleBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class AeroLighteningCutoutBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class AeroReformBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class AeroUnformBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class FlatPatternBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class FlatSolidBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class AeroSheetmetalManagerImpl;
            /** Provides methods for manipulating the Knowledge Fusion rules in a part  <br> To obtain an instance of this class, refer to @link Features::FeatureCollection Features::FeatureCollection@endlink  <br> */
            class NXOPENCPPEXPORT  AeroSheetmetalManager
            {
                private: AeroSheetmetalManagerImpl * m_aerosheetmetalmanager_impl;
                private: NXOpen::Features::FeatureCollection* m_owner;
                /** Constructor */
                public: explicit AeroSheetmetalManager(NXOpen::Features::FeatureCollection *owner);
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                public: ~AeroSheetmetalManager();
                /** Create flange builder 
                             @return  AeroFlangeBuilder object  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                public: NXOpen::Features::SheetMetal::AeroFlangeBuilder * CreateFlangeBuilder
                (
                    NXOpen::Features::Feature * aerosmFlange /** @link Features::SheetMetal::AeroFlangeBuilder Features::SheetMetal::AeroFlangeBuilder@endlink 
                                                                      to be edited, if NULL  then create a new one */
                );
                /** Create joggle builder 
                             @return  AeroJoggleBuilder object  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: NXOpen::Features::SheetMetal::AeroJoggleBuilder * CreateJoggleBuilder
                (
                    NXOpen::Features::Feature * aerosmJoggle /** @link Features::SheetMetal::AeroJoggleBuilder Features::SheetMetal::AeroJoggleBuilder@endlink 
                                                                      to be edited, if NULL  then create a new one */
                );
                /** Create unform builder 
                             @return  AeroUnformBuilder object  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                public: NXOpen::Features::SheetMetal::AeroUnformBuilder * CreateUnformBuilder
                (
                    NXOpen::Features::Feature * aerosmUnform /** @link Features::SheetMetal::AeroUnformBuilder Features::SheetMetal::AeroUnformBuilder@endlink 
                                                                      to be edited, if NULL  then create a new one */
                );
                /** Create reform builder 
                             @return  AeroReformBuilder object  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                public: NXOpen::Features::SheetMetal::AeroReformBuilder * CreateReformBuilder
                (
                    NXOpen::Features::Feature * aerosmReform /** @link Features::SheetMetal::AeroReformBuilder Features::SheetMetal::AeroReformBuilder@endlink 
                                                                      to be edited, if NULL  then create a new one */
                );
                /** Create flat solid builder 
                             @return  FlatSolidBuilder object  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: NXOpen::Features::SheetMetal::FlatSolidBuilder * CreateFlatSolidBuilder
                (
                    NXOpen::Features::Feature * aerosmUnform /** @link Features::SheetMetal::FlatSolidBuilder Features::SheetMetal::FlatSolidBuilder@endlink 
                                                                      to be edited, if NULL  then create a new one */
                );
                /** Creates a @link Features::SheetMetal::AeroLighteningCutoutBuilder Features::SheetMetal::AeroLighteningCutoutBuilder@endlink   @return  AeroLighteningCutoutBuilder object <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: NXOpen::Features::SheetMetal::AeroLighteningCutoutBuilder * CreateAeroLighteningCutoutBuilder
                (
                    NXOpen::Features::Feature * aeroLighteningCutout /** @link Features::Feature Features::Feature@endlink  to be edited */
                );
                /** Creates a @link Features::SheetMetal::FlatPatternBuilder Features::SheetMetal::FlatPatternBuilder@endlink   @return  FlatPatternBuilder object  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: NXOpen::Features::SheetMetal::FlatPatternBuilder * CreateFlatPatternBuilder
                (
                    NXOpen::Features::Feature * aerosmUnform /** @link Features::Feature Features::Feature@endlink 
                                                                                                to be edited, if NULL  then create a new one */
                );
            }; //lint !e1712 default constructor not defined for class  

        }
    }
}
#undef EXPORTLIBRARY
#endif
