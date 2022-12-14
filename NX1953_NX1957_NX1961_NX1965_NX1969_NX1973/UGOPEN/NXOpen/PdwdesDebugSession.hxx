#ifndef NXOpen_PDWDESDEBUGSESSION_HXX_INCLUDED
#define NXOpen_PDWDESDEBUGSESSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PdwdesDebugSession.ja
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
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class PdwdesDebugSession;
    class DebugSession;
    class BasePart;
    class PdwdesBaseValidator;
    class PdwdesDebugSessionImpl;

    /// \cond NX_NO_DOC 
    /** Represents a class that is used for NX Progressive Die Autotest.  This class should not
    be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::DebugSession  NXOpen::DebugSession @endlink  <br> 
     <br>  Created in NX12.0.2.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  PdwdesDebugSession
    {
        private: PdwdesDebugSessionImpl * m_pdwdesdebugsession_impl;
        private: NXOpen::DebugSession* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit PdwdesDebugSession(NXOpen::DebugSession *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~PdwdesDebugSession();

        /// \cond NX_NO_DOC 
        /** Create a progressive die validation object.  @return  created validator 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        public: NXOpen::PdwdesBaseValidator * CreateProgressiveDieValidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Create the validators for each progressive die feature found. 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        public: void PopulateValidators
        (
            NXOpen::PdwdesBaseValidator * mainValidator /** main progressive die validator */,
            std::vector<NXOpen::PdwdesBaseValidator *> & validators /** created validators */
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Sets the category name to validate 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        public: void SetCategoryName
        (
            NXOpen::PdwdesBaseValidator * mainValidator /** main progressive die validator */,
            const NXString & categoryName /** categoryname */ 
        );
        /** Sets the category name to validate 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        void SetCategoryName
        (
            NXOpen::PdwdesBaseValidator * mainValidator /** main progressive die validator */,
            const char * categoryName /** categoryname */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Sets the absolute tolerance used by xml double value comparison. 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        public: void SetAbsoluteTolerance
        (
            NXOpen::PdwdesBaseValidator * mainValidator /** main progressive die validator */,
            double absoluteTolerance /** absolutetolerance */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Sets the relative tolerance used by xml double value comparison. 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        public: void SetRelativeTolerance
        (
            NXOpen::PdwdesBaseValidator * mainValidator /** main progressive die validator */,
            double relativeTolerance /** relativetolerance */ 
        );

        /// \endcond 

        /// \cond NX_NO_DOC 
        /** Sets whether the tolerance used by xml double value comparison is absolute. 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        public: void SetIsAbsoluteTolerance
        (
            NXOpen::PdwdesBaseValidator * mainValidator /** main progressive die validator */,
            bool isAbsoluteTolerance /** isabsolutetolerance */ 
        );

        /// \endcond 
    }; //lint !e1712 default constructor not defined for class  


    /// \endcond 
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
