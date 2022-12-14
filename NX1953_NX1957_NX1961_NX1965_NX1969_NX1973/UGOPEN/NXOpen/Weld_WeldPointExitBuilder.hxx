#ifndef NXOpen_WELD_WELDPOINTEXITBUILDER_HXX_INCLUDED
#define NXOpen_WELD_WELDPOINTEXITBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_WeldPointExitBuilder.ja
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
        class WeldPointExitBuilder;
    }
    namespace Features
    {
        class Feature;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Weld
    {
        class _WeldPointExitBuilderBuilder;
        class WeldPointExitBuilderImpl;
        /** Represents a @link NXOpen::Weld::WeldPointExitBuilder NXOpen::Weld::WeldPointExitBuilder@endlink  class used to pass welding object from the Weld Point command to a user callback. This object is not used on edit. 
         <br>  Created in NX8.0.2.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  WeldPointExitBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** The command name used for the newly created features. */
            public: enum CommandName
            {
                CommandNameNone/** No command. Used to initialize value. */,
                CommandNameWeldPoint/** Weld Point command */,
                CommandNameDatumLocator/** Datum Locator command  */,
                CommandNameMeasurementLocator/** Measurement Locator command   */,
                CommandNameJointmark/** Joint Mark command   */,
                CommandNameWeldPointWizard/** Weld Point Wizard command */,
                CommandNameEasySpot/** Easy Spot. User selected OK. Features exist to process. */,
                CommandNameEasySpotSelected/** Easy Spot. User selected Create Features From Selection. */,
                CommandNameEasySpotApply/** Easy Spot. User selected Apply */,
                CommandNameEasySpotEnded/** Easy Spot. User selected OK or Cancel. No new features created. */
            };

            /** The method use to create the features. */
            public: enum MethodUsed
            {
                MethodUsedNone/** No method specified. Used to initialize value. */,
                MethodUsedMirror/** Feature was created using the mirror method. */,
                MethodUsedTranslate/** Feature was created using the translate method. */,
                MethodUsedGuideCurve/** Feature was created using the guide curves method. */,
                MethodUsedPoints/** Feature was created using the points method. */,
                MethodUsedGuideCurveMovedOff/** Feature was created using the guide curves method, but user moved it off. */
            };

            /** The information about whether the feature was modified, newly created, or unused. */
            public: enum FeatureStatus
            {
                FeatureStatusModified/** An existing feature was modified. */,
                FeatureStatusNewlyCreated/** A new feature was created.        */,
                FeatureStatusNotUsed/** A feature to move was specified, but changes to spacing options caused this feature not to be used. */
            };

             /**  @brief  Structure used to identify newly created features.  

              */
            public:
            struct FeatureInfo
            {
                public: /** the newly created or edited feature */NXOpen::Features::Feature * Feature;
                public: /** the method used to create the feature */NXOpen::Weld::WeldPointExitBuilder::MethodUsed MethodUsed;
                public: /** the parent if method used was mirror or translate */NXOpen::Features::Feature * Parent;
                public: /** true if a new feature, false if an existing feature was edited. */bool IsNewlyCreated;
                public: FeatureInfo() :
                    Feature(),
                    MethodUsed((NXOpen::Weld::WeldPointExitBuilder::MethodUsed)0),
                    Parent(),
                    IsNewlyCreated()
                {
                }
                /** Constructor for the FeatureInfo struct. */ 
                public: FeatureInfo(NXOpen::Features::Feature * featureInitial /** the newly created or edited feature */, 
                        NXOpen::Weld::WeldPointExitBuilder::MethodUsed methodUsedInitial /** the method used to create the feature */, 
                        NXOpen::Features::Feature * parentInitial /** the parent if method used was mirror or translate */, 
                        bool isNewlyCreatedInitial /** true if a new feature, false if an existing feature was edited. */) :
                    Feature(featureInitial),
                    MethodUsed(methodUsedInitial),
                    Parent(parentInitial),
                    IsNewlyCreated(isNewlyCreatedInitial)
                {
                }
            };

             /**  @brief  Structure used to identify newly created, edited, and unused features.  

              */
            public:
            struct FeatureDetails
            {
                public: /** the newly created, edited, or unused feature */NXOpen::Features::Feature * Feature;
                public: /** the method used to create the feature */NXOpen::Weld::WeldPointExitBuilder::MethodUsed MethodUsed;
                public: /** the parent if method used was mirror or translate */NXOpen::Features::Feature * Parent;
                public: /** Indicates if the feature was modified, newly created, or unused. */NXOpen::Weld::WeldPointExitBuilder::FeatureStatus IsNewlyCreated;
                public: FeatureDetails() :
                    Feature(),
                    MethodUsed((NXOpen::Weld::WeldPointExitBuilder::MethodUsed)0),
                    Parent(),
                    IsNewlyCreated((NXOpen::Weld::WeldPointExitBuilder::FeatureStatus)0)
                {
                }
                /** Constructor for the FeatureDetails struct. */ 
                public: FeatureDetails(NXOpen::Features::Feature * featureInitial /** the newly created, edited, or unused feature */, 
                        NXOpen::Weld::WeldPointExitBuilder::MethodUsed methodUsedInitial /** the method used to create the feature */, 
                        NXOpen::Features::Feature * parentInitial /** the parent if method used was mirror or translate */, 
                        NXOpen::Weld::WeldPointExitBuilder::FeatureStatus isNewlyCreatedInitial /** Indicates if the feature was modified, newly created, or unused. */) :
                    Feature(featureInitial),
                    MethodUsed(methodUsedInitial),
                    Parent(parentInitial),
                    IsNewlyCreated(isNewlyCreatedInitial)
                {
                }
            };

            private: WeldPointExitBuilderImpl * m_weldpointexitbuilder_impl;
            private: friend class  _WeldPointExitBuilderBuilder;
            protected: WeldPointExitBuilder();
            public: ~WeldPointExitBuilder();
            /**Returns  the command name that was last used to create features. This callback is not called on edit. 
             <br>  Created in NX8.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::WeldPointExitBuilder::CommandName CommandUsed
            (
            );
            /** Gets the information for the newly created, or edited features. 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::Weld::WeldPointExitBuilder::GetFeatureDetails NXOpen::Weld::WeldPointExitBuilder::GetFeatureDetails@endlink  instead. <br>  

             <br>  Created in NX8.0.2.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::Weld::WeldPointExitBuilder::GetFeatureDetails instead.") void GetFeatureInformation
            (
                std::vector<NXOpen::Weld::WeldPointExitBuilder::FeatureInfo> & features /** features created */
            );
            /** Gets the information for the newly created, edited or unused features. 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: void GetFeatureDetails
            (
                std::vector<NXOpen::Weld::WeldPointExitBuilder::FeatureDetails> & features /** features created */
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
