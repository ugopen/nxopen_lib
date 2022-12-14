#ifndef NXOpen_ANNOTATIONS_LOCATORDESIGNATORBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_LOCATORDESIGNATORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_LocatorDesignatorBuilder.ja
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
#include <NXOpen/Annotations_LocatorDesignatorBuilder.hxx>
#include <NXOpen/Annotations_PmiAttributeBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class LocatorDesignatorBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeBuilder;
    }
    class Direction;
    class Point;
    namespace Annotations
    {
        class _LocatorDesignatorBuilderBuilder;
        class LocatorDesignatorBuilderImpl;
        /** Represents a @link Annotations::LocatorDesignator Annotations::LocatorDesignator@endlink  builder  <br> To create a new instance of this class, use @link Annotations::PmiAttributeCollection::CreateLocatorDesignatorBuilder Annotations::PmiAttributeCollection::CreateLocatorDesignatorBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  LocatorDesignatorBuilder : public Annotations::PmiAttributeBuilder
        {
            private: LocatorDesignatorBuilderImpl * m_locatordesignatorbuilder_impl;
            private: friend class  _LocatorDesignatorBuilderBuilder;
            protected: LocatorDesignatorBuilder();
            public: ~LocatorDesignatorBuilder();
            /**Returns  the punch direction  <br> License requirements : None */
            public: NXOpen::Direction * PunchDirection
            (
            );
            /**Sets  the punch direction  <br> License requirements : None */
            public: void SetPunchDirection
            (
                NXOpen::Direction * punchDirection /** punchdirection */ 
            );
            /**Returns  the pin direction  <br> License requirements : None */
            public: NXOpen::Direction * PinDirection
            (
            );
            /**Sets  the pin direction  <br> License requirements : None */
            public: void SetPinDirection
            (
                NXOpen::Direction * pinDirection /** pindirection */ 
            );
            /**Returns  the normal direction  <br> License requirements : None */
            public: NXOpen::Direction * NormalDirection
            (
            );
            /**Sets  the normal direction  <br> License requirements : None */
            public: void SetNormalDirection
            (
                NXOpen::Direction * normalDirection /** normaldirection */ 
            );
            /**Returns  the hot spot  <br> License requirements : None */
            public: NXOpen::Point * HotSpot
            (
            );
            /**Sets  the hot spot  <br> License requirements : None */
            public: void SetHotSpot
            (
                NXOpen::Point * hotSpot /** hotspot */ 
            );
            /**Returns  the str title  <br> License requirements : None */
            public: NXString Title
            (
            );
            /**Sets  the str title  <br> License requirements : None */
            public: void SetTitle
            (
                const NXString & title /** title */ 
            );
            /**Returns  the locatortype  <br> License requirements : None */
            public: NXString LocatorType
            (
            );
            /**Sets  the locatortype  <br> License requirements : None */
            public: void SetLocatorType
            (
                const NXString & locatorType /** locatortype */ 
            );
            /**Returns  the locatorletter  <br> License requirements : None */
            public: NXString LocatorLetter
            (
            );
            /**Sets  the locatorletter  <br> License requirements : None */
            public: void SetLocatorLetter
            (
                const NXString & locatorLetter /** locatorletter */ 
            );
            /**Returns  the coordinateplane  <br> License requirements : None */
            public: NXString CoordinatePlane
            (
            );
            /**Sets  the coordinateplane  <br> License requirements : None */
            public: void SetCoordinatePlane
            (
                const NXString & coordinatePlane /** coordinateplane */ 
            );
            /**Returns  the notetext  <br> License requirements : None */
            public: NXString NoteText
            (
            );
            /**Sets  the notetext  <br> License requirements : None */
            public: void SetNoteText
            (
                const NXString & noteText /** notetext */ 
            );
            /**Returns  the subscript  <br> License requirements : None */
            public: NXString Subscript
            (
            );
            /**Sets  the subscript  <br> License requirements : None */
            public: void SetSubscript
            (
                const NXString & subscript /** subscript */ 
            );
            /**Returns  the hot spot text  <br> License requirements : None */
            public: NXString HotSpotText
            (
            );
            /**Sets  the hot spot text  <br> License requirements : None */
            public: void SetHotSpotText
            (
                const NXString & hotSpotText /** hotspottext */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
