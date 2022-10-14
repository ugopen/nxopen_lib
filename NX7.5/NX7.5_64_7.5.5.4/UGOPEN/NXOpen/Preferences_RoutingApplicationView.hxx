#ifndef NXOpen_PREFERENCES_ROUTINGAPPLICATIONVIEW_HXX_INCLUDED
#define NXOpen_PREFERENCES_ROUTINGAPPLICATIONVIEW_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_RoutingApplicationView.ja
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
    namespace Preferences
    {
        class RoutingApplicationView;
    }
    namespace Preferences
    {
        class SessionPreferences;
    }
    namespace Preferences
    {
        class RoutingCharacteristics;
    }
    namespace Preferences
    {
        class RoutingElectrical;
    }
    namespace Preferences
    {
        class RoutingLogical;
    }
    namespace Preferences
    {
        class RoutingMechanical;
    }
    namespace Preferences
    {
        class RoutingPart;
    }
    namespace Preferences
    {
        class RoutingPath;
    }
    namespace Preferences
    {
        class RoutingStock;
    }
    namespace Preferences
    {
        class RoutingApplicationViewImpl;
        /** 
                The RoutingApplicationView class contians all of the various preferences and options
                available from the Routing Application View file.  In order to call any of the 
                methods of this class (or it's contained objects), first call 
                @link Preferences::RoutingApplicationView::LoadAppView Preferences::RoutingApplicationView::LoadAppView@endlink  to load defaults
                from the application view file.  
                 <br> To obtain an instance of this class, refer to @link Preferences::SessionPreferences Preferences::SessionPreferences@endlink  <br> */
        class NXOPENCPPEXPORT  RoutingApplicationView
        {
            /** Routing application types */
            public: enum AppType
            {
                AppTypeNone/** Not currently in any of the routing applications. */,
                AppTypeMechanical/** In routing mechanical application. */,
                AppTypeElectrical/** In routing electrical application. */,
                AppTypeLogical/** In routing logical application. */
            };

            private: RoutingApplicationViewImpl * m_routingapplicationview_impl;
            private: NXOpen::Preferences::SessionPreferences* m_owner;
            /** Constructor */
            public: explicit RoutingApplicationView(NXOpen::Preferences::SessionPreferences *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~RoutingApplicationView();
            /**  Loads the preferences from an application view file.  This file may be either
                     a legacy application view file (with a .apv extension) or a new XML style application
                     view file (with a .xml extension).  See the Routing Adminstrator documentation for the
                     format of these files.  Once an application view file is loaded, it cannot be 
                     unloaded.  After loading the file the first time in a session, subsequent loads do not pick 
                     up changes made to the application view file, but it does set the preferences to
                     the cached values loaded from that file.  
                     Here is some example code, after the second call to 
                     @link Preferences::RoutingApplicationView::LoadAppView Preferences::RoutingApplicationView::LoadAppView@endlink  the current defaults
                     are defaults initially read from the mechanical application view.

                      @code 
                        Session.GetSession().Preferences.RoutingApplicationView.LoadAppView ( "ugroute_mech_in.xml" );
                        
                        Session.GetSession().Preferences.RoutingApplicationView.LoadAppView ( "ugroute_elec_in.xml" );
                        
                        Session.GetSession().Preferences.RoutingApplicationView.LoadAppView ( "ugroute_mech_in.xml" );
                        
                      @endcode 
                      <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void LoadAppView
            (
                const NXString & fileName /** filename of application view.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the filename of the current application view.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString Filename
            (
            );
            /**Returns  the application view name.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString Name
            (
            );
            /**Returns  the application view description.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString Description
            (
            );
            /**Returns  the current discipline. A discipline value of "" (the empty string)
                     indicates no current discipline.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString CurrentDiscipline
            (
            );
            /**Sets  the current discipline. A discipline value of "" (the empty string)
                     indicates no current discipline.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetCurrentDiscipline
            (
                const NXString & discipline /** discipline */ 
            );
            /** Returns all of the disciplines available in the current application view.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXString> GetDisciplines
            (
            );
            /**Returns  the current specification for the current discipline. A specification 
                     value of "" (the empty string) indiciates no current specification.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString CurrentSpecification
            (
            );
            /**Sets  the current specification for the current discipline. A specification 
                     value of "" (the empty string) indiciates no current specification.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetCurrentSpecification
            (
                const NXString & currentSpec /** current spec */ 
            );
            /** Returns the specifications available in the current discipline.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXString> GetSpecifications
            (
            );
            /**Sets  the given routing application type. This is only used in the context of routing to execute design rules. 
                    Application type should be set to@link Preferences::RoutingApplicationView::AppTypeNone Preferences::RoutingApplicationView::AppTypeNone@endlink 
                    before exiting from the routing applications.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetApplicationType
            (
                NXOpen::Preferences::RoutingApplicationView::AppType appType /** app type */ 
            );
            /**Returns  the given routing application type. This is only used in the context of routing to execute design rules. 
                    Application type should be set to@link Preferences::RoutingApplicationView::AppTypeNone Preferences::RoutingApplicationView::AppTypeNone@endlink 
                    before exiting from the routing applications.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingApplicationView::AppType ApplicationType
            (
            );


            /** Routing preferences related to parts. */
            public: NXOpen::Preferences::RoutingPart *PartPreferences();
            /** Preferences related to option/required characteristics. */
            public: NXOpen::Preferences::RoutingCharacteristics *CharacteristicPreferences();
            /** Stock preferences structure */
            public: NXOpen::Preferences::RoutingStock *RoutingStock();
            /** Path preferences structure */
            public: NXOpen::Preferences::RoutingPath *RoutingPath();
            /** Routing mechanical preferences */
            public: NXOpen::Preferences::RoutingMechanical *RoutingMechanical();
            /** Routing logical preferences */
            public: NXOpen::Preferences::RoutingLogical *RoutingLogical();
            /** Routing electrical preferences structure */
            public: NXOpen::Preferences::RoutingElectrical *RoutingElectrical();
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif