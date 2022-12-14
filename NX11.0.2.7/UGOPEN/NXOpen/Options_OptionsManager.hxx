#ifndef NXOpen_OPTIONS_OPTIONSMANAGER_HXX_INCLUDED
#define NXOpen_OPTIONS_OPTIONSMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Options_OptionsManager.ja
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
#include <NXOpen/Options_ChangeList.hxx>
#include <NXOpen/Options_DraftingStandardChangeList.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_options_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Options
    {
        class OptionsManager;
    }
    class Session;
    namespace Options
    {
        class ChangeList;
    }
    namespace Options
    {
        class DraftingStandardChangeList;
    }
    namespace Options
    {
        /** Describes type of an option. */
        enum OptionType
        {
            OptionTypeInt/** Option value is an integer number */,
            OptionTypeReal/** Option value is a real number */,
            OptionTypeString/** Option value is an ascii string */,
            OptionTypeStringList/** Option value is a list of ascii strings */,
            OptionTypeLogical/** Option value is logical */,
            OptionTypeUtf8string/** Option value is a utf8 string */,
            OptionTypeUtf8stringList/** Option value is a list of utf8 strings */,
            OptionTypeReorderSelList/** Option value is a list which can be selected and re-ordered */
        };

    }
    namespace Options
    {
        class OptionsManagerImpl;
        /** 
            Manages options. 
             <br> 
            OptionsManager methods use an option name as a unique identifier for
            accessing individual options and throw an error if an option with a given name is not
            found.  All existing option names are listed in the Online Documentation.
             <br> 
             <br> 
            If a level parameter is not supplied to a query method then the option value effective in
            current session is returned.  If a level parameter is supplied then then value
            that is stored at the specified level is returned. This may not be the same as the value
            effective in the current session and may take effect only after the session is restarted.
             <br> 
             <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_OPTIONSEXPORT  OptionsManager
        {
            private: OptionsManagerImpl * m_optionsmanager_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit OptionsManager(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~OptionsManager();
            /** Gets the value of an @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  option. 
                        Throws an error if option type is not @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink . 
                     @return  Option value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: int GetIntValue
            (
                const NXString & name /** Option name. */
            );
            /** Gets the value of an @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  option. 
                        Throws an error if option type is not @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink . 
                     @return  Option value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            int GetIntValue
            (
                const char * name /** Option name. */
            );
            /** Gets the value of a @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  option. 
                        Throws an error if the option is not of type @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink .
                      @return  Option value. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: double GetRealValue
            (
                const NXString & name /** Option name. */
            );
            /** Gets the value of a @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  option. 
                        Throws an error if the option is not of type @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink .
                      @return  Option value. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            double GetRealValue
            (
                const char * name /** Option name. */
            );
            /** Gets the value of a @link  Options::OptionTypeString   Options::OptionTypeString @endlink  option. 
                        Throws an error if the option is not of type @link  Options::OptionTypeString   Options::OptionTypeString @endlink .
                     @return  Option value. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetStringValue
            (
                const NXString & name /** Option name. */
            );
            /** Gets the value of a @link  Options::OptionTypeString   Options::OptionTypeString @endlink  option. 
                        Throws an error if the option is not of type @link  Options::OptionTypeString   Options::OptionTypeString @endlink .
                     @return  Option value. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            NXString GetStringValue
            (
                const char * name /** Option name. */
            );
            /** Gets the value of a @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink  option. 
                        Throws an error if the option is not of type @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink .
                     @return  Option utf8 value. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetUtf8stringValue
            (
                const NXString & name /** Option name. */
            );
            /** Gets the value of a @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink  option. 
                        Throws an error if the option is not of type @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink .
                     @return  Option utf8 value. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            NXString GetUtf8stringValue
            (
                const char * name /** Option name. */
            );
            /** Gets the value of a @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink  option. 
                        Throws an error if the option is not of type @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink .
                     @return  Option value. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetStringListValue
            (
                const NXString & name /** Option name. */
            );
            /** Gets the value of a @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink  option. 
                        Throws an error if the option is not of type @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink .
                     @return  Option value. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            std::vector<NXString> GetStringListValue
            (
                const char * name /** Option name. */
            );
            /** Gets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option. 
                        Throws an error if the option is not of type @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
                     @return  Option value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetReorderSelectableStringListValue
            (
                const NXString & name /** Option name. */,
                std::vector<bool> & selection /** the selection bit */
            );
            /** Gets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option. 
                        Throws an error if the option is not of type @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
                     @return  Option value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            std::vector<NXString> GetReorderSelectableStringListValue
            (
                const char * name /** Option name. */,
                std::vector<bool> & selection /** the selection bit */
            );
            /** Gets the value of a @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink  option. 
                        Throws an error if the option is not of type @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink .  @return  Option value. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: bool GetLogicalValue
            (
                const NXString & name /** Option name. */
            );
            /** Gets the value of a @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink  option. 
                        Throws an error if the option is not of type @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink .  @return  Option value. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            bool GetLogicalValue
            (
                const char * name /** Option name. */
            );
            /** Gets the value of an @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  option at the specified level. 
                        Throws an error if the option is not of type @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink .
                     @return  Option value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: int GetIntValue
            (
                const NXString & name /** Option name. */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Gets the value of an @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink  option at the specified level. 
                        Throws an error if the option is not of type @link  Options::OptionTypeInt   Options::OptionTypeInt @endlink .
                     @return  Option value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            int GetIntValue
            (
                const char * name /** Option name. */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Gets the value of a @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  option at the specified level. 
                        Throws an error if the option is not of type @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink .
                     @return  Option value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: double GetRealValue
            (
                const NXString & name /** Option name. */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Gets the value of a @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink  option at the specified level. 
                        Throws an error if the option is not of type @link  Options::OptionTypeReal   Options::OptionTypeReal @endlink .
                     @return  Option value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            double GetRealValue
            (
                const char * name /** Option name. */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Gets the value of a @link  Options::OptionTypeString   Options::OptionTypeString @endlink  option at the specified level. 
                        Throws an error if the option is not of type @link  Options::OptionTypeString   Options::OptionTypeString @endlink .
                     @return  Option value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetStringValue
            (
                const NXString & name /** Option name. */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Gets the value of a @link  Options::OptionTypeString   Options::OptionTypeString @endlink  option at the specified level. 
                        Throws an error if the option is not of type @link  Options::OptionTypeString   Options::OptionTypeString @endlink .
                     @return  Option value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            NXString GetStringValue
            (
                const char * name /** Option name. */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Gets the value of a @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink  option at the specified level. 
                        Throws an error if the option is not of type @link  Options::OptionTypeString   Options::OptionTypeString @endlink .
                     @return  Option value 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetUtf8stringValue
            (
                const NXString & name /** Option name. */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Gets the value of a @link  Options::OptionTypeUtf8string   Options::OptionTypeUtf8string @endlink  option at the specified level. 
                        Throws an error if the option is not of type @link  Options::OptionTypeString   Options::OptionTypeString @endlink .
                     @return  Option value 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            NXString GetUtf8stringValue
            (
                const char * name /** Option name. */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Gets the value of a @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink  option at the specified level. 
                        Throws an error if the option is not of type @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink .
                     @return  Option value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetStringListValue
            (
                const NXString & name /** Option name. */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Gets the value of a @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink  option at the specified level. 
                        Throws an error if the option is not of type @link  Options::OptionTypeStringList   Options::OptionTypeStringList @endlink .
                     @return  Option value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            std::vector<NXString> GetStringListValue
            (
                const char * name /** Option name. */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Gets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option at the specified level. 
                        Throws an error if the option is not of type @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
                     @return  Option value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetReorderSelectableStringListValue
            (
                const NXString & name /** Option name. */,
                NXOpen::Options::LevelType level /** Options level. */,
                std::vector<bool> & selection /** the selection bit */
            );
            /** Gets the value of a @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink  option at the specified level. 
                        Throws an error if the option is not of type @link  Options::OptionTypeReorderSelList   Options::OptionTypeReorderSelList @endlink .
                     @return  Option value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            std::vector<NXString> GetReorderSelectableStringListValue
            (
                const char * name /** Option name. */,
                NXOpen::Options::LevelType level /** Options level. */,
                std::vector<bool> & selection /** the selection bit */
            );
            /** Gets the value of a @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink  option at the specified level.  
                        Throws an error if the option is not of type @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink .
                     @return  Option value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: bool GetLogicalValue
            (
                const NXString & name /** Option name. */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Gets the value of a @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink  option at the specified level.  
                        Throws an error if the option is not of type @link  Options::OptionTypeLogical   Options::OptionTypeLogical @endlink .
                     @return  Option value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            bool GetLogicalValue
            (
                const char * name /** Option name. */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Creates an instance of @link  NXOpen::Options::ChangeList   NXOpen::Options::ChangeList @endlink  class, in order to edit a set of options. 
                    It is not possible to create an instance of @link  NXOpen::Options::ChangeList   NXOpen::Options::ChangeList @endlink  for @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  level, 
                    or for a level that is not defined or is not writeable.   @return  An instanse of @link  NXOpen::Options::ChangeList   NXOpen::Options::ChangeList @endlink  class 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Options::ChangeList * NewOptionsChangeList
            (
                NXOpen::Options::LevelType level /** Options level.  */,
                NXOpen::Options::LevelLockedByDefault lockedByDefault /** Specifies whether Options level is locked by default. 
                            Ignored at @link  Options::LevelTypeUser   Options::LevelTypeUser @endlink  level as locks at @link  Options::LevelTypeUser   Options::LevelTypeUser @endlink  level are not supported. 
                            If specified default lock status is different from the current one, then all exisitng locks are cleared.  */
            );
            /** Creates an instance of @link  NXOpen::Options::DraftingStandardChangeList   NXOpen::Options::DraftingStandardChangeList @endlink  class, in order to edit a set of options. 
                    It is not possible to create an instance of @link  NXOpen::Options::DraftingStandardChangeList   NXOpen::Options::DraftingStandardChangeList @endlink  for @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  level, 
                    or for a level that is not defined or is not writeable.   @return  An instanse of @link  NXOpen::Options::DraftingStandardChangeList   NXOpen::Options::DraftingStandardChangeList @endlink  class 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Options::DraftingStandardChangeList * NewOptionsDraftingStandardChangeList
            (
                NXOpen::Options::LevelType level /** Options level.  */,
                const NXString & filename /** Specifies the filename to save/save as.*/
            );
            /** Creates an instance of @link  NXOpen::Options::DraftingStandardChangeList   NXOpen::Options::DraftingStandardChangeList @endlink  class, in order to edit a set of options. 
                    It is not possible to create an instance of @link  NXOpen::Options::DraftingStandardChangeList   NXOpen::Options::DraftingStandardChangeList @endlink  for @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  level, 
                    or for a level that is not defined or is not writeable.   @return  An instanse of @link  NXOpen::Options::DraftingStandardChangeList   NXOpen::Options::DraftingStandardChangeList @endlink  class 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::Options::DraftingStandardChangeList * NewOptionsDraftingStandardChangeList
            (
                NXOpen::Options::LevelType level /** Options level.  */,
                const char * filename /** Specifies the filename to save/save as.*/
            );
            /** Gets the names of all available options.  @return  List of names of all available options. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetAllOptions
            (
            );
            /** Returns true if the option value is locked at the specified level. 
                        Locks are not supported at @link  Options::LevelTypeUser   Options::LevelTypeUser @endlink  and @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  levels.  @return  Lock status 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsValueLocked
            (
                const NXString & name /** Option name */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Returns true if the option value is locked at the specified level. 
                        Locks are not supported at @link  Options::LevelTypeUser   Options::LevelTypeUser @endlink  and @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  levels.  @return  Lock status 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            bool IsValueLocked
            (
                const char * name /** Option name */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Returns true if the option value exists at the specified level. Always true for the @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  level.  @return  True if value is set 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsValueSet
            (
                const NXString & name /** Option name */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Returns true if the option value exists at the specified level. Always true for the @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  level.  @return  True if value is set 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            bool IsValueSet
            (
                const char * name /** Option name */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Returns then user comment at the specified level. User comments are not supported at the @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  level.  @return  User comment text. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetUserComment
            (
                const NXString & name /** Option name */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Returns then user comment at the specified level. User comments are not supported at the @link  Options::LevelTypeShipped   Options::LevelTypeShipped @endlink  level.  @return  User comment text. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            NXString GetUserComment
            (
                const char * name /** Option name */,
                NXOpen::Options::LevelType level /** Options level. */
            );
            /** Returns an option's type.  @return  Option type 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Options::OptionType GetOptionType
            (
                const NXString & name /** Option name */
            );
            /** Returns an option's type.  @return  Option type 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::Options::OptionType GetOptionType
            (
                const char * name /** Option name */
            );
            /** Returns true if the option's values at the specified level are locked by default.
                        Locked by default means that if an option value does not exist at this level, 
                        then it is locked.
                     @return  True if options values are locked by default 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsLevelLockedByDefault
            (
                NXOpen::Options::LevelType level /** Options level. */
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
