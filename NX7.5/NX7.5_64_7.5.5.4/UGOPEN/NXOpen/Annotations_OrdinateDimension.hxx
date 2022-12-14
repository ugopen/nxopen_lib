#ifndef NXOpen_ANNOTATIONS_ORDINATEDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_ORDINATEDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_OrdinateDimension.ja
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
#include <NXOpen/Annotations_ILinearTolerance.hxx>
#include <NXOpen/Annotations_LinearTolerance.hxx>
#include <NXOpen/Annotations_Dimension.hxx>
#include <NXOpen/Dimensions.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class OrdinateDimension;
    }
    namespace Annotations
    {
        class Dimension;
    }
    namespace Annotations
    {
        class ILinearTolerance;
    }
    namespace Annotations
    {
        class LinearTolerance;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class INXObject;
    namespace Annotations
    {
        class _OrdinateDimensionBuilder;
        class OrdinateDimensionImpl;
        /** Represents an ordinate dimension  <br> Abstract class <br> */
        class NXOPENCPPEXPORT  OrdinateDimension : public Annotations::Dimension, public virtual Annotations::ILinearTolerance
        {
             /** Specifies the ordinate dogleg preferences */
            public:
            struct  DoglegPreferences
            {
                public: /** dogleg setting */ NXOpen::Annotations::OrdinateDoglegDefinition DoglegSetting;
                public: /** angle */ double Angle;
                public: /** start offset */ double StartOffset;
                public: /** end offset */ double EndOffset;
                public: /** dogleg option */ NXOpen::Annotations::OrdinateDoglegCreationOption DoglegOption;
                public: DoglegPreferences() :
                    DoglegSetting((NXOpen::Annotations::OrdinateDoglegDefinition)0),
                    Angle(),
                    StartOffset(),
                    EndOffset(),
                    DoglegOption((NXOpen::Annotations::OrdinateDoglegCreationOption)0)
                {
                }
                /** Constructor for the DoglegPreferences struct. */ 
                public: DoglegPreferences(NXOpen::Annotations::OrdinateDoglegDefinition doglegSettingInitial /** dogleg setting */ , 
                        double angleInitial /** angle */ , 
                        double startOffsetInitial /** start offset */ , 
                        double endOffsetInitial /** end offset */ , 
                        NXOpen::Annotations::OrdinateDoglegCreationOption doglegOptionInitial /** dogleg option */ ) :
                    DoglegSetting(doglegSettingInitial),
                    Angle(angleInitial),
                    StartOffset(startOffsetInitial),
                    EndOffset(endOffsetInitial),
                    DoglegOption(doglegOptionInitial)
                {
                }
            };

            private: OrdinateDimensionImpl * m_ordinatedimension_impl;
            private: friend class  _OrdinateDimensionBuilder;
            protected: OrdinateDimension();
            public: ~OrdinateDimension();
            /** Returns the dogleg data for Ordinate Dimension  @return  Dogleg preferences  <br> License requirements : None */
            public: NXOpen::Annotations::OrdinateDimension::DoglegPreferences GetDoglegData
            (
            );
            /** Sets the dogleg data for Ordinate Dimension  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDoglegData
            (
                const NXOpen::Annotations::OrdinateDimension::DoglegPreferences & ordinateDoglegPreferences /** New dogleg preferences */
            );
            /** Returns the tolerance  @return   <br> License requirements : None */
            public: virtual NXOpen::Annotations::LinearTolerance * GetTolerance
            (
            );
            /** Sets the tolerance  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: virtual void SetTolerance
            (
                NXOpen::Annotations::LinearTolerance * tolerance /** tolerance */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
