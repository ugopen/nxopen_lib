#ifndef NXOpen_MODLUTILS_SELECTOBJECTDIMLIST_HXX_INCLUDED
#define NXOpen_MODLUTILS_SELECTOBJECTDIMLIST_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ModlUtils_SelectObjectDimList.ja
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
#include <NXOpen/ModlUtils_SelectObjectDimListItem.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/libnxopencpp_modlutils_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace ModlUtils
    {
        class SelectObjectDimList;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace ModlUtils
    {
        class SelectObjectDimListItem;
    }
    namespace ModlUtils
    {
        class SelectObjectDimListItemList;
    }
    namespace ModlUtils
    {
        class _SelectObjectDimListBuilder;
        class SelectObjectDimListImpl;
        /** the builder for a list of @link ModlUtils::SelectObjectDimListItem ModlUtils::SelectObjectDimListItem@endlink  objects 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_MODLUTILSEXPORT  SelectObjectDimList : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: SelectObjectDimListImpl * m_selectobjectdimlist_impl;
            private: friend class  _SelectObjectDimListBuilder;
            protected: SelectObjectDimList();
            public: ~SelectObjectDimList();
            /**Returns  a list of @link ModlUtils::SelectObjectDimListItem ModlUtils::SelectObjectDimListItem@endlink  objects 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ModlUtils::SelectObjectDimListItemList * List
            (
            );
            /** Creates a @link ModlUtils::SelectObjectDimListItem ModlUtils::SelectObjectDimListItem@endlink  
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ModlUtils::SelectObjectDimListItem * CreateSelectObjectDimListItem
            (
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not yet implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
            (
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
