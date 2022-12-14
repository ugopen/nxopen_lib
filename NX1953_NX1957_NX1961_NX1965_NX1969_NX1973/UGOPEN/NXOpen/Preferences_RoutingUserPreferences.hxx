#ifndef NXOpen_PREFERENCES_ROUTINGUSERPREFERENCES_HXX_INCLUDED
#define NXOpen_PREFERENCES_ROUTINGUSERPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_RoutingUserPreferences.ja
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
        class RoutingUserPreferences;
    }
    namespace Preferences
    {
        class RoutingApplicationView;
    }
    namespace Preferences
    {
        class RoutingUserPreferencesImpl;
        /** Allows access to the User Preferences section of the Routing Application View file.  <br> To obtain an instance of this class, refer to @link NXOpen::Preferences::RoutingApplicationView  NXOpen::Preferences::RoutingApplicationView @endlink  <br> 
         <br>  Created in NX11.0.1.  <br>  
        */
        class NXOPENCPP_PREFERENCESEXPORT  RoutingUserPreferences
        {
            private: RoutingUserPreferencesImpl * m_routinguserpreferences_impl;
            private: NXOpen::Preferences::RoutingApplicationView* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit RoutingUserPreferences(NXOpen::Preferences::RoutingApplicationView *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~RoutingUserPreferences();
            /** Returns the value of the named string user preference from the Application View file.  @return  Was the preference found in the Application View file? 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool GetStringPreference
            (
                const NXString & name /** The name of the user preference. */,
                NXString* value /** The value of the preference, if found. */
            );
            /** Returns the value of the named string user preference from the Application View file.  @return  Was the preference found in the Application View file? 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            bool GetStringPreference
            (
                const char * name /** The name of the user preference. */,
                NXString* value /** The value of the preference, if found. */
            );
            /** Sets the value of the named string user preference in the current NX session. 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetStringPreference
            (
                const NXString & name /** The name of the user preference. */,
                const NXString & value /** The value of the preference. Overwrites any existing value. */
            );
            /** Sets the value of the named string user preference in the current NX session. 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetStringPreference
            (
                const char * name /** The name of the user preference. */,
                const char * value /** The value of the preference. Overwrites any existing value. */
            );
            /** Returns the values of the named string array user preference from the Application View file.  @return  Was the preference found in the Application View file? 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool GetStringArrayPreference
            (
                const NXString & name /** The name of the user preference. */,
                std::vector<NXString> & values /** The values of the preference, if found.  */
            );
            /** Returns the values of the named string array user preference from the Application View file.  @return  Was the preference found in the Application View file? 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            bool GetStringArrayPreference
            (
                const char * name /** The name of the user preference. */,
                std::vector<NXString> & values /** The values of the preference, if found.  */
            );
            /** Sets the values of the named string array user preference in the current NX session. 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetStringArrayPreference
            (
                const NXString & name /** The name of the user preference. */,
                std::vector<NXString> & values /** The values of the preference. Overwrites any existing values.  */
            );
            /** Sets the values of the named string array user preference in the current NX session. 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetStringArrayPreference
            (
                const char * name /** The name of the user preference. */,
                std::vector<NXString> & values /** The values of the preference. Overwrites any existing values.  */
            );
            /** Returns the value of the named integer user preference from the Application View file.  @return  Was the preference found in the Application View file? 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool GetIntegerPreference
            (
                const NXString & name /** The name of the user preference. */,
                int* value /** The value of the preference, if found. */
            );
            /** Returns the value of the named integer user preference from the Application View file.  @return  Was the preference found in the Application View file? 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            bool GetIntegerPreference
            (
                const char * name /** The name of the user preference. */,
                int* value /** The value of the preference, if found. */
            );
            /** Sets the value of the named integer user preference in the current NX session. 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetIntegerPreference
            (
                const NXString & name /** The name of the user preference. */,
                int value /** The value of the preference. Overwrites any existing values. */
            );
            /** Sets the value of the named integer user preference in the current NX session. 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetIntegerPreference
            (
                const char * name /** The name of the user preference. */,
                int value /** The value of the preference. Overwrites any existing values. */
            );
            /** Returns the values of the named integer array user preference from the Application View file.  @return  Was the preference found in the Application View file? 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool GetIntegerArrayPreference
            (
                const NXString & name /** The name of the user preference. */,
                std::vector<int> & values /** The values of the preference, if found.  */
            );
            /** Returns the values of the named integer array user preference from the Application View file.  @return  Was the preference found in the Application View file? 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            bool GetIntegerArrayPreference
            (
                const char * name /** The name of the user preference. */,
                std::vector<int> & values /** The values of the preference, if found.  */
            );
            /** Sets the values of the named integer array user preference in the current NX session. 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetIntegerArrayPreference
            (
                const NXString & name /** The name of the user preference. */,
                const std::vector<int> & values /** The values of the preference. Overwrites any existing values.  */
            );
            /** Sets the values of the named integer array user preference in the current NX session. 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetIntegerArrayPreference
            (
                const char * name /** The name of the user preference. */,
                const std::vector<int> & values /** The values of the preference. Overwrites any existing values.  */
            );
            /** Returns the value of the named double user preference from the Application View file.  @return  Was the preference found in the Application View file? 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool GetDoublePreference
            (
                const NXString & name /** The name of the user preference. */,
                double* value /** The value of the preference, if found. */
            );
            /** Returns the value of the named double user preference from the Application View file.  @return  Was the preference found in the Application View file? 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            bool GetDoublePreference
            (
                const char * name /** The name of the user preference. */,
                double* value /** The value of the preference, if found. */
            );
            /** Sets the value of the named double user preference in the current NX session. 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetDoublePreference
            (
                const NXString & name /** The name of the user preference. */,
                double value /** The value of the preference. Overwrites any existing values. */
            );
            /** Sets the value of the named double user preference in the current NX session. 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetDoublePreference
            (
                const char * name /** The name of the user preference. */,
                double value /** The value of the preference. Overwrites any existing values. */
            );
            /** Returns the values of the named double array user preference from the Application View file.  @return  Was the preference found in the Application View file? 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool GetDoubleArrayPreference
            (
                const NXString & name /** The name of the user preference. */,
                std::vector<double> & values /** The values of the preference, if found.  */
            );
            /** Returns the values of the named double array user preference from the Application View file.  @return  Was the preference found in the Application View file? 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            bool GetDoubleArrayPreference
            (
                const char * name /** The name of the user preference. */,
                std::vector<double> & values /** The values of the preference, if found.  */
            );
            /** Sets the values of the named double array user preference in the current NX session. 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetDoubleArrayPreference
            (
                const NXString & name /** The name of the user preference. */,
                const std::vector<double> & values /** The values of the preference. Overwrites any existing values.  */
            );
            /** Sets the values of the named double array user preference in the current NX session. 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetDoubleArrayPreference
            (
                const char * name /** The name of the user preference. */,
                const std::vector<double> & values /** The values of the preference. Overwrites any existing values.  */
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
