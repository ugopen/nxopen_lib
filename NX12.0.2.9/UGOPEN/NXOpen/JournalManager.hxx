#ifndef NXOpen_JOURNALMANAGER_HXX_INCLUDED
#define NXOpen_JOURNALMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     JournalManager.ja
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
#include <NXOpen/Preferences_SessionUserInterface.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class JournalManager;
    class Session;
    class JournalManagerImpl;
    /**  @brief Represents the JournalManager which is used to query data about journals when recording and 
    replaying journal files. 

     

    The language NX is setup to, or currently recording can be determined from 
    @link NXOpen::Preferences::SessionUserInterface::JournalLanguage NXOpen::Preferences::SessionUserInterface::JournalLanguage@endlink .
     <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
     <br>  Created in NX11.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  JournalManager
    {
        private: JournalManagerImpl * m_journalmanager_impl;
        private: NXOpen::Session* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit JournalManager(NXOpen::Session *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~JournalManager();
        /**Returns  the flag indicating if a Journal is replaying inside of NX.  If true, a journal is running. This will only return true if 
              we are replaying a journal using the Play Journal dialog inside a NX interactive session.
              This will be limited to only VB, C#, and Python journals replaying. 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: bool IsJournalRunning
        (
        );
        /**Returns  the flag indicating if a Journal is recording.  If true, a journal is recording. 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: bool IsJournalRecording
        (
        );
        /**   @brief Inserts the passed in string into a journal.  

          If this is called when not journaling,
            this method does nothing.
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void InsertUserDefinedCode
        (
            const NXString & userDefinedCode /** user defined code to be inserted into the journal */
        );
        /**   @brief Inserts the passed in string into a journal.  

          If this is called when not journaling,
            this method does nothing.
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        void InsertUserDefinedCode
        (
            const char * userDefinedCode /** user defined code to be inserted into the journal */
        );
        /**  @brief Inserts string as a comment into the journal. 

         
            The comment with appropriate markups for the language being recorded so it will be a comment.  If this is called when not journaling,
            this method does nothing. 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void InsertComment
        (
            const NXString & comment /** comment to be inserted into the journal */
        );
        /**  @brief Inserts string as a comment into the journal. 

         
            The comment with appropriate markups for the language being recorded so it will be a comment.  If this is called when not journaling,
            this method does nothing. 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        void InsertComment
        (
            const char * comment /** comment to be inserted into the journal */
        );
        /**Returns  the flag to indicate if journal calls should be paused Pauses/UnPauses recording of calls to journal. 
             When this method is called from journal file playing, the pause will end automatically after it it is done replaying.  This is true if the 
             journal is run inside of NX using the Play Journal functionality or using the methods NXOpen.JournalManager.PlayDotNetJournal or 
             NXOpen.JournalManager.PlayPythonJournal called from the executing journal.  In other words, if you start recording a journal, and 
             then play a journal (through Play Journal Dialog or method call) which calls this method.  The journal will be only 
             paused while it is playing, and then once that journal is done playing journaling will resume.     

             When this method is called from a NXOpen DLL it will persist after DLL is run or has returned control to NX for those programs that are not immediately 
             unloaded after running.  This can have an impact on Redo if this DLL is run outside of Journal record scenario.

             
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: bool PauseJournal
        (
        );
        /**Sets  the flag to indicate if journal calls should be paused Pauses/UnPauses recording of calls to journal. 
             When this method is called from journal file playing, the pause will end automatically after it it is done replaying.  This is true if the 
             journal is run inside of NX using the Play Journal functionality or using the methods NXOpen.JournalManager.PlayDotNetJournal or 
             NXOpen.JournalManager.PlayPythonJournal called from the executing journal.  In other words, if you start recording a journal, and 
             then play a journal (through Play Journal Dialog or method call) which calls this method.  The journal will be only 
             paused while it is playing, and then once that journal is done playing journaling will resume.     

             When this method is called from a NXOpen DLL it will persist after DLL is run or has returned control to NX for those programs that are not immediately 
             unloaded after running.  This can have an impact on Redo if this DLL is run outside of Journal record scenario.

             
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SetPauseJournal
        (
            bool isJournalRunning /** isjournalrunning */ 
        );
        /**Returns  the flag to indicate if Blockstyler journal calls should be paused.  If true BlockStyler calls will not be recorded to the journal. 
             When this method is called from journal file playing, the pause will end automatically after it it is done replaying.  This is true if the 
             journal is run inside of NX using the Play Journal functionality or using the methods NXOpen.JournalManager.PlayDotNetJournal or 
             NXOpen.JournalManager.PlayPythonJournal called from the executing journal.  In other words, if you start recording a journal, and 
             then play a journal (through Play Journal Dialog or method call) which calls this method.  The journal will be only 
             paused while it is playing, and then once that journal is done playing journaling will resume.     

             When this method is called from a NXOpen DLL it will persist after DLL is run or has returned control to NX for those programs that are not immediately 
             unloaded after running.  This can have an impact on Redo if this DLL is run outside of Journal record scenario.
             
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: bool PauseJournalingOfBlockStylerCalls
        (
        );
        /**Sets  the flag to indicate if Blockstyler journal calls should be paused.  If true BlockStyler calls will not be recorded to the journal. 
             When this method is called from journal file playing, the pause will end automatically after it it is done replaying.  This is true if the 
             journal is run inside of NX using the Play Journal functionality or using the methods NXOpen.JournalManager.PlayDotNetJournal or 
             NXOpen.JournalManager.PlayPythonJournal called from the executing journal.  In other words, if you start recording a journal, and 
             then play a journal (through Play Journal Dialog or method call) which calls this method.  The journal will be only 
             paused while it is playing, and then once that journal is done playing journaling will resume.     

             When this method is called from a NXOpen DLL it will persist after DLL is run or has returned control to NX for those programs that are not immediately 
             unloaded after running.  This can have an impact on Redo if this DLL is run outside of Journal record scenario.
             
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SetPauseJournalingOfBlockStylerCalls
        (
            bool pauseBlockStylerCalls /** pauseblockstylercalls */ 
        );
        /**Returns   @brief  the language the journal will be recored in.  

          This is a convenience querry, as this will return the 
            same value as  @link NXOpen::Preferences::SessionUserInterface::JournalLanguage NXOpen::Preferences::SessionUserInterface::JournalLanguage@endlink 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Preferences::SessionUserInterface::JournalLanguageType JournalLanguage
        (
        );
        /**  @brief Start recording a journal file. 

         
              
              This will record a journal file in the language specified by @link NXOpen::Preferences::SessionUserInterface::SetJournalLanguage NXOpen::Preferences::SessionUserInterface::SetJournalLanguage@endlink .
              The proper exentsion will be added based upon the preference.

              An error will be thrown if a journal is already recording.

              
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : dotnet_author (".NET API Author") */
        public: void RecordJournal
        (
            const NXString & filename /** path to record journal file.  The extension will be added automatically based upon the preferences. */
        );
        /**  @brief Start recording a journal file. 

         
              
              This will record a journal file in the language specified by @link NXOpen::Preferences::SessionUserInterface::SetJournalLanguage NXOpen::Preferences::SessionUserInterface::SetJournalLanguage@endlink .
              The proper exentsion will be added based upon the preference.

              An error will be thrown if a journal is already recording.

              
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : dotnet_author (".NET API Author") */
        void RecordJournal
        (
            const char * filename /** path to record journal file.  The extension will be added automatically based upon the preferences. */
        );
        /**  @brief Stops Recording a journal file. 

         

                An error will be thrown if this is called and NX is not currently recording.  

              
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : dotnet_author (".NET API Author") */
        public: void StopRecordingJournal
        (
        );
    }; //lint !e1712 default constructor not defined for class  

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