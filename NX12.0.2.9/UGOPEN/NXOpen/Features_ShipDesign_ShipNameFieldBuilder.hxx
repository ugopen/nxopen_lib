#ifndef NXOpen_FEATURES_SHIPDESIGN_SHIPNAMEFIELDBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_SHIPNAMEFIELDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_ShipNameFieldBuilder.ja
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
            class ShipNameFieldBuilder;
        }
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Features
    {
        namespace ShipDesign
        {
            /** Field Type */
            enum ShipnameFieldBuilderType
            {
                ShipnameFieldBuilderTypeFixed/** Field with an unchanging string */,
                ShipnameFieldBuilderTypeOption/** Field whose value can be one of several strings */,
                ShipnameFieldBuilderTypeIndex/** Field which will have a number generated */,
                ShipnameFieldBuilderTypeAny/** Field whose value will be a user enterred string */,
                ShipnameFieldBuilderTypePositionInformation/** Field which is generated from mold face plane indicate part location */,
                ShipnameFieldBuilderTypeContextAttributeMap/** Field whose value comes from context attribute*/,
                ShipnameFieldBuilderTypeSectionInformation/** Field whose value comes from section */,
                ShipnameFieldBuilderTypeAttributeMap/** Field value comes from part attribute value whose attribute title configured by "key" value from "source" part */,
                ShipnameFieldBuilderTypeParentPartPosition/** Field value is parent part position information */,
                ShipnameFieldBuilderTypeFrameName/**Field which is generated from mold face using frame name indicate part location */,
                ShipnameFieldBuilderTypePortOrStarboard/**Field indicates which locate port side or starboard side */,
                ShipnameFieldBuilderTypeNone/** Unknown Field Type */
            };

        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class _ShipNameFieldBuilderBuilder;
            class ShipNameFieldBuilderImpl;
            /** A field, combined with other fields, to generate a name for a Ship Basic Design Object such as a Deck.

                        The ShipNameFieldBuilder class contains the information used to generate a name for a
                        Basic Design object, such as a Deck, Bulkhead, Stiffener System, etc. 
                            @code 
                        Fields can be one of four types:
                            1) Fixed            A string with an unchangeable value
                            2) Any              A user entered string value
                            3) Option           A predefined set of strings from which the user can choose one
                            4) Index            A system generated, leading zeros, number which pretends to provide
                                                name uniqueness.
                         @endcode 
                        There may be as many Fixed, Any, and Option fields as the user deems appropriate.
                        There may be only one Index field.

                        The fields for a particular Ship object type @link NXOpen::Features::ShipDesign::ShipNamesBuilder NXOpen::Features::ShipDesign::ShipNamesBuilder@endlink  are defined in
                        a "recipes" file which specifies, for a particular object type, the fields and their values.
                        See ShipNamesRecipes.xml in UGII_BASE_DIR/nxship/data for details on the recipes.
                         @code 
                        A sample recipe might be defined having the following fields:

                            Type            Value
                            --------        --------
                            Fixed           "TBH-"
                            Option          "Port", "Starboard", "None"
                            Fixed           "-"
                            Index           nnnnnn @endcode 
                     <br> This is an abstract class and cannot be instantiated  <br> 
             <br>  Created in NX9.0.2.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ShipNameFieldBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
            {
                private: ShipNameFieldBuilderImpl * m_shipnamefieldbuilder_impl;
                private: friend class  _ShipNameFieldBuilderBuilder;
                protected: ShipNameFieldBuilder();
                public: ~ShipNameFieldBuilder();
                /**Returns  the field value. 
                 <br>  Created in NX9.0.2.  <br>  
                 <br> License requirements : None */
                public: NXString Value
                (
                );
                /**Sets  the field value. 
                 <br>  Created in NX9.0.2.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetValue
                (
                    const NXString & newValue /** newvalue */ 
                );
                /**Sets  the field value. 
                 <br>  Created in NX9.0.2.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                void SetValue
                (
                    const char * newValue /** newvalue */ 
                );
                /** Get the valid option values for an Option type field. No values
                                are returned (and the count is set to zero) if this is not an
                                option field  @return  
                 <br>  Created in NX9.0.2.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXString> GetOptionValues
                (
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
