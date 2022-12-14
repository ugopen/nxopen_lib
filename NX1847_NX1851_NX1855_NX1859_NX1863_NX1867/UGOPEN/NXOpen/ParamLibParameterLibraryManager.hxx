#ifndef NXOpen_PARAMLIBPARAMETERLIBRARYMANAGER_HXX_INCLUDED
#define NXOpen_PARAMLIBPARAMETERLIBRARYMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ParamLibParameterLibraryManager.ja
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

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class ParamLibParameterLibraryManager;
    class BasePart;
    class ParamLibParameterCollection;
    class ParamLibParameterLibraryManagerImpl;
    /** A manager to deal with all parameter objects   <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
     <br>  Created in NX1847.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  ParamLibParameterLibraryManager
    {
        private: ParamLibParameterLibraryManagerImpl * m_paramlibparameterlibrarymanager_impl;
        private: NXOpen::BasePart* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit ParamLibParameterLibraryManager(NXOpen::BasePart *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~ParamLibParameterLibraryManager();


        /** Returns the @link ParamLibParameterCollection  ParamLibParameterCollection @endlink  belonging to this part 
         <br>  Created in NX1847.0.0.  <br>  
        */
        public: NXOpen::ParamLibParameterCollection *Parameters();
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
