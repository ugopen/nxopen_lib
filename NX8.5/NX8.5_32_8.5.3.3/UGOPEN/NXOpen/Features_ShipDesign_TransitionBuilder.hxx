#ifndef NXOpen_FEATURES_SHIPDESIGN_TRANSITIONBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_TRANSITIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_TransitionBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Features_ShipDesign_TransitionBuilder.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace ShipDesign
        {
            class TransitionBuilder;
        }
    }
    class Builder;
    namespace Features
    {
        namespace ShipDesign
        {
            class _TransitionBuilderBuilder;
            class TransitionBuilderImpl;
            /**   
                      This is to create a @link Features::ShipDesign::TransitionBuilder Features::ShipDesign::TransitionBuilder@endlink  which is used to create Detail Design elements from Basic Design elements.
                      <br> To create a new instance of this class, use @link Features::ShipCollection::CreateTransitionBuilder  Features::ShipCollection::CreateTransitionBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            TransitionMethod </td> <td> 
             
            UpdateExisting </td> </tr> 

            <tr><td> 
             
            TransitionType </td> <td> 
             
            Section </td> </tr> 

            </table>  

             <br>  Created in NX8.5.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  TransitionBuilder : public Builder
            {
                /** Transition Type. 
                              Section type means the basic design elements in speicified ship section will be transitioned.
                              Frame type means specified basic design elements will be transitioned. */
                public: enum TransitionTypes
                {
                    TransitionTypesSection/** section */ ,
                    TransitionTypesFrame/** frame */ 
                };

                /** Transition Method.
                              Create New method means all transition will begin with a scratch
                              Update Existing method means to update previous transitioned result 
                             */
                public: enum TransitionMethods
                {
                    TransitionMethodsUpdateExisting/** update existing */ ,
                    TransitionMethodsCreateNew/** create new */ 
                };

                private: TransitionBuilderImpl * m_transitionbuilder_impl;
                private: friend class  _TransitionBuilderBuilder;
                protected: TransitionBuilder();
                public: ~TransitionBuilder();
                /**Returns  the transition type. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::TransitionBuilder::TransitionTypes TransitionType
                (
                );
                /**Sets  the transition type. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetTransitionType
                (
                    NXOpen::Features::ShipDesign::TransitionBuilder::TransitionTypes type /** type */ 
                );
                /** The section block part file name. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetSectionBlockParts
                (
                    std::vector<NXString> & sectionParts /** sectionparts */ 
                );
                /** Set frame part names. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetFrameParts
                (
                    std::vector<NXString> & framePartFilenames /** framepartfilenames */ 
                );
                /**Returns  the transition method. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::TransitionBuilder::TransitionMethods TransitionMethod
                (
                );
                /**Sets  the transition method. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetTransitionMethod
                (
                    NXOpen::Features::ShipDesign::TransitionBuilder::TransitionMethods method /** method */ 
                );
            };
        }
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
