#ifndef NXOpen_DRAWINGUTILS_HXX_INCLUDED
#define NXOpen_DRAWINGUTILS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     DrawingUtils.ja
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
#include <NXOpen/Drafting_DrawingAutomationWizard.hxx>
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
    class DrawingUtils;
    class Session;
    namespace Drafting
    {
        class DrawingAutomationWizard;
    }
    class DrawingUtilsImpl;
    /** Contains various drawing utility methods  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
     <br>  Created in NX8.5.3.  <br>  
    */
    class NXOPENCPPEXPORT  DrawingUtils
    {
        public: /** User defined method that is called whenever Booklet Wizard is committed. 
         <br>  Created in NX8.5.3.  <br>  
         <br> License requirements : None */
        typedef NXOpen::Callback1<int, NXOpen::Drafting::DrawingAutomationWizard *> DrawingAutomationWizardHandler;
        private: DrawingUtilsImpl * m_drawingutils_impl;
        private: NXOpen::Session* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit DrawingUtils(NXOpen::Session *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~DrawingUtils();
        /** Registers a user defined method that is called whenever Booklet Wizard is committed.  @return  identifier of registered method (used to unregister the method) 
         <br>  Created in NX8.5.3.  <br>  
         <br> License requirements : None */
        public: int AddDrawingAutomationWizardHandler
        (
            const NXOpen::DrawingUtils::DrawingAutomationWizardHandler&  handler /** method to register */
        );
        /** Unregisters a user defined method that is called whenever Booklet Wizard is committed. 
         <br>  Created in NX8.5.3.  <br>  
         <br> License requirements : None */
        public: void RemoveDrawingAutomationWizardHandler
        (
            int id /** identifier for method to unregister */
        );
        /** Constructs a new DrawingAutomationWizard object.  @return  data for wizard callback 
         <br>  Created in NX8.5.3.  <br>  
         <br> License requirements : None */
        public: NXOpen::Drafting::DrawingAutomationWizard * NewDrawingAutomationWizard
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
