#ifndef NXOpen_ANNOTATIONS_SYMMETRICALCENTERLINEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_SYMMETRICALCENTERLINEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_SymmetricalCenterlineBuilder.ja
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
#include <NXOpen/Annotations_CenterlineBuilder.hxx>
#include <NXOpen/Annotations_SymmetricalCenterlineBuilder.hxx>
#include <NXOpen/Annotations_SymmetricalCenterlineSettingsBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class SymmetricalCenterlineBuilder;
    }
    namespace Annotations
    {
        class CenterlineBuilder;
    }
    namespace Annotations
    {
        class SymmetricalCenterlineSettingsBuilder;
    }
    class SelectNXObject;
    namespace Annotations
    {
        class _SymmetricalCenterlineBuilderBuilder;
        class SymmetricalCenterlineBuilderImpl;
        /** Builder for creating Symmetrical Centerline. It creates or edits Symmetrical Centerline  <br> To create a new instance of this class, use @link Annotations::CenterlineCollection::CreateSymmetricalCenterlineBuilder  Annotations::CenterlineCollection::CreateSymmetricalCenterlineBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Settings.Extension </td> <td> 
         
        6.35 (millimeters part), 0.25 (inches part) </td> </tr> 

        <tr><td> 
         
        Settings.Gap </td> <td> 
         
        1.5875 (millimeters part), 0.0625 (inches part) </td> </tr> 

        <tr><td> 
         
        Settings.IndividualDistance </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        Settings.Size </td> <td> 
         
        3.175 (millimeters part), 0.125 (inches part) </td> </tr> 

        <tr><td> 
         
        Settings.Width </td> <td> 
         
        Thin </td> </tr> 

        <tr><td> 
         
        Type </td> <td> 
         
        FromFace </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  SymmetricalCenterlineBuilder : public Annotations::CenterlineBuilder
        {
            /** the valid types of Symmetrical Centerline */
            public: enum Types
            {
                TypesFromFace/** Centerline from face */,
                TypesStartAndEnd/** Centerline from start and end point*/
            };

            private: SymmetricalCenterlineBuilderImpl * m_symmetricalcenterlinebuilder_impl;
            private: friend class  _SymmetricalCenterlineBuilderBuilder;
            protected: SymmetricalCenterlineBuilder();
            public: ~SymmetricalCenterlineBuilder();
            /**Returns  the type of Symmetrical Centerline 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SymmetricalCenterlineBuilder::Types Type
            (
            );
            /**Sets  the type of Symmetrical Centerline 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetType
            (
                NXOpen::Annotations::SymmetricalCenterlineBuilder::Types type /** type */ 
            );
            /**Returns  the start object of Symmetrical Centerline 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * Start
            (
            );
            /**Returns  the end object of Symmetrical Centerline 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * End
            (
            );
            /**Returns  the face object of Symmetrical Centerline 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * Face
            (
            );
            /**Returns  the inherit object
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * Inherit
            (
            );
            /**Returns  the settings builder object for Symmetrical Centerline 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SymmetricalCenterlineSettingsBuilder * Settings
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
