#ifndef NXOpen_WELD_DATUMICONBUILDER_HXX_INCLUDED
#define NXOpen_WELD_DATUMICONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_DatumIconBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/Weld_DatumCommonBuilder.hxx>
#include <NXOpen/Weld_DatumIconBuilder.hxx>
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class DatumIconBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Weld
    {
        class DatumPin;
    }
    namespace Weld
    {
        class DatumSurface;
    }
    namespace Weld
    {
        class _DatumIconBuilderBuilder;
        class DatumIconBuilderImpl;
        /** Represents a @link Weld::DatumIconBuilder Weld::DatumIconBuilder@endlink  class used to control the part navigator icon for Datum Pin and Surface Locators. This class is used to set the Datum Surface or Datum Pin
                icon, but never both at the same time. If the icon is not being set for a feature, that feature will be set to NULL.
                See example in DatumIconCallback.cxx in ugweld/samples kit. 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  DatumIconBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: DatumIconBuilderImpl * m_datumiconbuilder_impl;
            private: friend class  _DatumIconBuilderBuilder;
            protected: DatumIconBuilder();
            public: ~DatumIconBuilder();
            /**Returns  the DatumSurface feature. This will be NULL if setting the icon for a DatumPin. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::DatumSurface * DatumSurface
            (
            );
            /**Returns  the DatumPin feature. This will be NULL if setting the icon for a DatumSurface 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::DatumPin * DatumPin
            (
            );
            /**Returns  the custom datum type from the customer defaults that was used. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::DatumCommonBuilder::CustomTypes CustomType
            (
            );
            /**Returns  the indicator if this datum was derived from another datum. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool Derived
            (
            );
            /**Returns  the bit map name for the icon to be used. If the bit map cannot be found a default one will be used. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString IconName
            (
            );
            /**Sets  the bit map name for the icon to be used. If the bit map cannot be found a default one will be used. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetIconName
            (
                const NXString & iconName /** iconname */ 
            );
            /**Sets  the bit map name for the icon to be used. If the bit map cannot be found a default one will be used. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            void SetIconName
            (
                const char * iconName /** iconname */ 
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
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
