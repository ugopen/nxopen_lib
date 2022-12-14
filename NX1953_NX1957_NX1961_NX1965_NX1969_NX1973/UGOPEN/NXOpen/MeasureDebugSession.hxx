#ifndef NXOpen_MEASUREDEBUGSESSION_HXX_INCLUDED
#define NXOpen_MEASUREDEBUGSESSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MeasureDebugSession.ja
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
    class MeasureDebugSession;
    class DebugSession;
    class BasePart;
    class MeasureBaseValidator;
    class TaggedObject;
    class MeasureDebugSessionImpl;
    /** Represents a class that is used for NX Measure Autotest.  This class should not
    be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::DebugSession  NXOpen::DebugSession @endlink  <br> 
     <br>  Created in NX1847.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  MeasureDebugSession
    {
        private: MeasureDebugSessionImpl * m_measuredebugsession_impl;
        private: NXOpen::DebugSession* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit MeasureDebugSession(NXOpen::DebugSession *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~MeasureDebugSession();
        /** Create a measure validation object. Doubles will have the following tolerances assigned: if 0.0, then always uses absolute tolerance. If not equal to 0.0, then use relative tolerance unless the isAbsoluteTolerance is true.  @return  created validator 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::MeasureBaseValidator * CreateMeasureValidator
        (
            NXOpen::BasePart * displayPart /** part being validated */,
            int validateMask /** validatemask */ ,
            double absoluteTolerance /** absolutetolerance */ ,
            double relativeTolerance /** relativetolerance */ ,
            bool isAbsoluteTolerance /** isabsolutetolerance */ 
        );
        /** Set measure features to the main validator prepare for validate. 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void SetMeasureFeatures
        (
            NXOpen::MeasureBaseValidator * mainValidator /** main measure validator */,
            const std::vector<NXOpen::TaggedObject *> & measureFeatures /** prepare measure features for validate */
        );
        /** Create the validators for each measure feature found. 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateValidators
        (
            NXOpen::MeasureBaseValidator * mainValidator /** main measure validator */,
            std::vector<NXOpen::MeasureBaseValidator *> & validators /** created validators */
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
