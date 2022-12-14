#ifndef NXOpen_DISPLAY_DYNAMICSECTION_HXX_INCLUDED
#define NXOpen_DISPLAY_DYNAMICSECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_DynamicSection.ja
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
#include <NXOpen/Display_DynamicSection.hxx>
#include <NXOpen/Display_IDynamicSectionCutCreator.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Update.hxx>
#include <NXOpen/libnxopencpp_display_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Display
    {
        class DynamicSection;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    namespace Display
    {
        class DynamicSectionCut;
    }
    namespace Display
    {
        class IDynamicSectionCutCreator;
    }
    class INXObject;
    class NXObject;
    class View;
    namespace Display
    {
        class _DynamicSectionBuilder;
        class DynamicSectionImpl;
        /** Represents a dynamic section  <br> To create or edit an instance of this class, use @link NXOpen::Display::DynamicSectionBuilder  NXOpen::Display::DynamicSectionBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DISPLAYEXPORT  DynamicSection : public NXOpen::NXObject, public virtual NXOpen::Display::IDynamicSectionCutCreator
        {
            private: DynamicSectionImpl * m_dynamicsection_impl;
            private: friend class  _DynamicSectionBuilder;
            protected: DynamicSection();
            public: ~DynamicSection();
            /** Updates the section-cuts (curves) associated with the dynamic 
                        section object if they are out-of-date.
                        
                         <br> 
                        If the section object is out-of-date, then it is first logged for 
                        update. If update option is @link NXOpen::Update::OptionNow NXOpen::Update::OptionNow@endlink , 
                        then the update is performed immediately. If the user wants to update 
                        multiple section objects, then it is optimal to specify the update option 
                        as @link NXOpen::Update::OptionLater NXOpen::Update::OptionLater@endlink  and perform 
                        update at the end using @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                         <br> 
                        
                         <br> 
                        An valid undo mark @link NXOpen::Session::UndoMarkId NXOpen::Session::UndoMarkId@endlink  must have been 
                        set so that the session can be rolled back successfully if an error occurs.
                        See @link NXOpen::Session::SetUndoMark NXOpen::Session::SetUndoMark@endlink .
                         <br> 
                    
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void UpdateSectionCuts
            (
                NXOpen::Update::Option updateOption /** Update option */
            );
            /** Finds the @link  NXOpen::Display::DynamicSectionCut   NXOpen::Display::DynamicSectionCut @endlink  
                    with the given identifier as recorded in a journal. An object may 
                    not return the same value as its JournalIdentifier in different 
                    versions of  the software. However newer versions of the software 
                    should find the same object when FindObject is passed older versions 
                    of its journal identifier. In general, this method should not be 
                    used in handwritten code and exists to support record and playback 
                    of journals.

                    An exception will be thrown if no object can be found with the 
                    given journal identifier.  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXOpen::Display::DynamicSectionCut * Find
            (
                const NXString & journalIdentifier /** Journal identifier */
            );
            /** Finds the @link  NXOpen::Display::DynamicSectionCut   NXOpen::Display::DynamicSectionCut @endlink  
                    with the given identifier as recorded in a journal. An object may 
                    not return the same value as its JournalIdentifier in different 
                    versions of  the software. However newer versions of the software 
                    should find the same object when FindObject is passed older versions 
                    of its journal identifier. In general, this method should not be 
                    used in handwritten code and exists to support record and playback 
                    of journals.

                    An exception will be thrown if no object can be found with the 
                    given journal identifier.  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            virtual NXOpen::Display::DynamicSectionCut * Find
            (
                const char * journalIdentifier /** Journal identifier */
            );
            /** Gets section-cuts generated by the sectioning the model shown
                        in the specified view. 

                        View must belong to the same part as the section-cut creator. If
                        no view is specified, then section-cuts generated from the 
                        sectionable entities in the part are returned.
                        
                        If a view is specified, then @link NXOpen::Assemblies::Explosion NXOpen::Assemblies::Explosion@endlink 
                        active in the view is used to get section-cuts for the explosion.
                        If the view does not have any active explosion, then
                        section-cuts generated from the sectionable entities in the part 
                        are returned. 
                     
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: virtual void GetSectionCuts
            (
                NXOpen::NXObject * contextOccurrence /** This can be NULL. If non NULL, then this must
                                    be an occurrence.
                                 */,
                NXOpen::View * view /** view */ ,
                std::vector<NXOpen::Display::DynamicSectionCut *> & sectionCuts /** sectioncuts */ 
            );
        };
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
