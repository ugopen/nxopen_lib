#ifndef NXOpen_ANIMATIONDESIGNERDEBUGSESSION_HXX_INCLUDED
#define NXOpen_ANIMATIONDESIGNERDEBUGSESSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AnimationDesignerDebugSession.ja
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
    class AnimationDesignerDebugSession;
    class DebugSession;
    class AnimationDesignerBaseValidator;
    class BasePart;
    class AnimationDesignerDebugSessionImpl;
    /** Represents a class that is used for NX Animation Designer Autotest.  This class should not
    be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::DebugSession  NXOpen::DebugSession @endlink  <br> 
     <br>  Created in NX12.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  AnimationDesignerDebugSession
    {
        private: AnimationDesignerDebugSessionImpl * m_animationdesignerdebugsession_impl;
        private: NXOpen::DebugSession* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit AnimationDesignerDebugSession(NXOpen::DebugSession *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~AnimationDesignerDebugSession();
        /** Creates an animation designer validation object.  @return  created validator 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::AnimationDesignerBaseValidator * CreateAnimationDesignerValidator
        (
            NXOpen::BasePart * displayPart /** part being validated */
        );
        /** Sets whether to print the mass peoperty, csys and color to xml file. 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        public: void SetPrintRigidGroupSpecialParameters
        (
            NXOpen::AnimationDesignerBaseValidator * mainValidator /** main animation designer validator */,
            bool printRigidSpecialParams /** printrigidspecialparams */ 
        );
        /** Sets whether to print the point information as referenced geometry. 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        public: void SetPrintPointGeometryInformation
        (
            NXOpen::AnimationDesignerBaseValidator * mainValidator /** main animation designer validator */,
            bool printPointGeomInfo /** printpointgeominfo */ 
        );
        /** Creates the validators for each animation designer object found. 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: void PopulateValidators
        (
            NXOpen::AnimationDesignerBaseValidator * mainValidator /** main animation designer validator */,
            std::vector<NXOpen::AnimationDesignerBaseValidator *> & validators /** created validators */
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
