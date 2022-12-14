#ifndef NXOpen_FEATURECOLLECTIONVALIDATOR_HXX_INCLUDED
#define NXOpen_FEATURECOLLECTIONVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     FeatureCollectionValidator.ja
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
#include <NXOpen/IValidator.hxx>
#include <NXOpen/IValidator.hxx>
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
    class FeatureCollectionValidator;
    class IValidator;
    class _FeatureCollectionValidatorBuilder;
    class FeatureCollectionValidatorImpl;
    /** validator for FeatureCollection in a part.  <br> This is a test class.  <br> 
     <br>  Created in NX7.5.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  FeatureCollectionValidator : public NXOpen::TaggedObject, public virtual NXOpen::IValidator
    {
        private: FeatureCollectionValidatorImpl * m_featurecollectionvalidator_impl;
        private: friend class  _FeatureCollectionValidatorBuilder;
        protected: FeatureCollectionValidator();
        public: ~FeatureCollectionValidator();
        /** Get the expression validation option  @return  
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: bool GetValidateExpressions
        (
        );
        /** Set the expression validation option 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetValidateExpressions
        (
            bool validateExpressions /** validateexpressions */ 
        );
        /** Get the shape validation option  @return  
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: bool GetValidateShape
        (
        );
        /** Set the shape validation option 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: void SetValidateShape
        (
            bool validateShape /** validateshape */ 
        );
        /** Get the geometry validation option  @return  
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: bool GetValidateGeometry
        (
        );
        /** Set the geometry validation option 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void SetValidateGeometry
        (
            bool validateGeometry /** validategeometry */ 
        );
        /** Get the geometry validation option  @return  
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: bool GetCompareConvergentMinimumRadius
        (
        );
        /** Set the geometry validation option 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void SetCompareConvergentMinimumRadius
        (
            bool compareConvergentMinimumRadius /** compareconvergentminimumradius */ 
        );
        /** Get the significant tolerance  @return  
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: double GetSignificantDifference
        (
        );
        /** Set the significant tolerance difference 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSignificantDifference
        (
            double significantDifference /** significantdifference */ 
        );
        /** Get the distance tolerance  @return  
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: double GetDistanceTolerance
        (
        );
        /** Set the distance tolerance 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void SetDistanceTolerance
        (
            double distanceTolerance /** distancetolerance */ 
        );
        /** Get the angular tolerance  @return  
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: double GetAngularTolerance
        (
        );
        /** Set the angular tolerance 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void SetAngularTolerance
        (
            double angularTolerance /** angulartolerance */ 
        );
        /** Get the centroid coordinate tolerance  @return  
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: double GetCentroidTolerance
        (
        );
        /** Set the centroid coordinate tolerance 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetCentroidTolerance
        (
            double centroidTolerance /** centroidtolerance */ 
        );
        /** Get the use parasolid error bounds option  @return  
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: bool GetUseParasolidErrorBounds
        (
        );
        /** Set the use parasolid error bounds option 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetUseParasolidErrorBounds
        (
            bool useParasolidErrorBounds /** useparasoliderrorbounds */ 
        );
        /** Get the mass properties percent difference  @return  
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: double GetMassPropPercentDifference
        (
        );
        /** Set the mass properties percent difference 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetMassPropPercentDifference
        (
            double massPropPercentDifference /** massproppercentdifference */ 
        );
        /**Returns  the algorithm to use for validation. 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: virtual NXOpen::ValidatorVersion ValidatorVersion
        (
        );
        /**Sets  the algorithm to use for validation. 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: virtual void SetValidatorVersion
        (
            NXOpen::ValidatorVersion version /** version */ 
        );
        /**Returns  the print level for validation. 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: virtual NXOpen::ValidatorPrintLevel ValidatorPrintLevel
        (
        );
        /**Sets  the print level for validation. 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: virtual void SetValidatorPrintLevel
        (
            NXOpen::ValidatorPrintLevel level /** level */ 
        );
        /** Deletes the validator. 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: virtual void Destroy
        (
        );
        /** Set the ood status of features. 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: virtual void SetValidatorPrintOodStatus
        (
            bool status /** status */ 
        );
    };
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
