#ifndef NXOpen_PREFERENCES_ROUTINGPREFERENCES_HXX_INCLUDED
#define NXOpen_PREFERENCES_ROUTINGPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_RoutingPreferences.ja
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
#include <NXOpen/libnxopencpp_preferences_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Preferences
    {
        class RoutingPreferences;
    }
    namespace Preferences
    {
        class SessionPreferences;
    }
    namespace Preferences
    {
        class RoutingPreferencesImpl;
        /** Represents the set of navigation preferences applicable to entire session.  <br> To obtain an instance of this class, refer to @link NXOpen::Preferences::SessionPreferences  NXOpen::Preferences::SessionPreferences @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_PREFERENCESEXPORT  RoutingPreferences
        {
            private: RoutingPreferencesImpl * m_routingpreferences_impl;
            private: NXOpen::Preferences::SessionPreferences* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit RoutingPreferences(NXOpen::Preferences::SessionPreferences *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~RoutingPreferences();
            /**Returns  the next generation routing discipline preference 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: int DisciplineIndex
            (
            );
            /**Sets  the next generation routing discipline preference 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetDisciplineIndex
            (
                int disciplineIndex /** disciplineindex */ 
            );
            /**Returns  the current discipline. A discipline value of "" (the empty string)
                    indicates no current discipline.  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString CurrentDiscipline
            (
            );
            /**Sets  the current discipline. A discipline value of "" (the empty string)
                    indicates no current discipline.  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetCurrentDiscipline
            (
                const NXString & currentDiscipline /** currentdiscipline */ 
            );
            /**Sets  the current discipline. A discipline value of "" (the empty string)
                    indicates no current discipline.  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetCurrentDiscipline
            (
                const char * currentDiscipline /** currentdiscipline */ 
            );
            /** Returns All disciplines available in the current application view. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: std::vector<NXString> GetAllAvailableDisciplines
            (
            );
            /**Returns  the next generation routing port length preference in part units 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: double PortLength
            (
            );
            /**Sets  the next generation routing port length preference in part units 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetPortLength
            (
                double portLength /** portlength */ 
            );
            /**Returns  the next generation routing display connected ports preference 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool DisplayConnectedPorts
            (
            );
            /**Sets  the next generation routing display connected ports preference 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetDisplayConnectedPorts
            (
                bool displayConnectedPorts /** displayconnectedports */ 
            );
            /**Returns  the next generation routing offset expression string preference 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString OffsetExpressionString
            (
            );
            /**Sets  the next generation routing offset expression string preference 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetOffsetExpressionString
            (
                const NXString & offsetExpressionString /** offsetexpressionstring */ 
            );
            /**Sets  the next generation routing offset expression string preference 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetOffsetExpressionString
            (
                const char * offsetExpressionString /** offsetexpressionstring */ 
            );
            /**Returns  the next generation routing stock translucency preference 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: int StockTranslucency
            (
            );
            /**Sets  the next generation routing stock translucency preference 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetStockTranslucency
            (
                int stockTranslucency /** stocktranslucency */ 
            );
            /**Returns  the next generation insulation translucency preference 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: int InsulationTranslucency
            (
            );
            /**Sets  the next generation insulation translucency preference 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetInsulationTranslucency
            (
                int insulationTranslucency /** insulationtranslucency */ 
            );
            /**Returns  the next generation space reservation translucency preference 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: int SpaceReservationTranslucency
            (
            );
            /**Sets  the next generation space reservation translucency preference 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetSpaceReservationTranslucency
            (
                int spaceReservationTranslucency /** spacereservationtranslucency */ 
            );
            /**Returns  the routed system designer stock component folder preference 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString StockComponentFolder
            (
            );
            /**Sets  the routed system designer stock component folder preference 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetStockComponentFolder
            (
                const NXString & stockComponentFolder /** stockcomponentfolder */ 
            );
            /**Sets  the routed system designer stock component folder preference 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetStockComponentFolder
            (
                const char * stockComponentFolder /** stockcomponentfolder */ 
            );
            /**Returns  the routed system designer use preferred port placement preference 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool UsePreferredPortPlacement
            (
            );
            /**Sets  the routed system designer use preferred port placement preference 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetUsePreferredPortPlacement
            (
                bool usePreferredPortPlacement /** usepreferredportplacement */ 
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
