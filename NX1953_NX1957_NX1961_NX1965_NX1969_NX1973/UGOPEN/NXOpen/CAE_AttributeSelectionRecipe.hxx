#ifndef NXOpen_CAE_ATTRIBUTESELECTIONRECIPE_HXX_INCLUDED
#define NXOpen_CAE_ATTRIBUTESELECTIONRECIPE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AttributeSelectionRecipe.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/CAE_SelectionRecipe.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class AttributeSelectionRecipe;
    }
    namespace CAE
    {
        class SelectionRecipe;
    }
    class Expression;
    class Unit;
    namespace CAE
    {
        class _AttributeSelectionRecipeBuilder;
        class AttributeSelectionRecipeImpl;
        /**  @brief  Represents a Selection Recipe based on attributes.  

          <br> To obtain an instance of this object use one of the creators in @link NXOpen::CAE::SelectionRecipeCollection NXOpen::CAE::SelectionRecipeCollection@endlink .  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  AttributeSelectionRecipe : public NXOpen::CAE::SelectionRecipe
        {
            private: AttributeSelectionRecipeImpl * m_attributeselectionrecipe_impl;
            private: friend class  _AttributeSelectionRecipeBuilder;
            protected: AttributeSelectionRecipe();
            public: ~AttributeSelectionRecipe();
            /**Returns  the presence of the name attribute. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::HasNameAttribute CAE::SelRecipeAttributeStrategy::HasNameAttribute@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use CAE::SelRecipeAttributeStrategy::HasNameAttribute instead.") bool HasNameAttribute
            (
            );
            /**Returns  the name attribute. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::NameAttribute CAE::SelRecipeAttributeStrategy::NameAttribute@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use CAE::SelRecipeAttributeStrategy::NameAttribute instead.") NXString NameAttribute
            (
            );
            /** Sets or adds the name attribute. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::SetNameAttribute CAE::SelRecipeAttributeStrategy::SetNameAttribute@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use CAE::SelRecipeAttributeStrategy::SetNameAttribute instead.") void SetNameAttribute
            (
                const NXString & name /** name */ 
            );
            /** Sets or adds the name attribute. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::SetNameAttribute CAE::SelRecipeAttributeStrategy::SetNameAttribute@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetNameAttribute
            (
                const char * name /** name */ 
            );
            /** Removes the name attribute. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::RemoveNameAttribute CAE::SelRecipeAttributeStrategy::RemoveNameAttribute@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use CAE::SelRecipeAttributeStrategy::RemoveNameAttribute instead.") void RemoveNameAttribute
            (
            );
            /**Returns  the presence of the color attribute. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::HasColorAttribute CAE::SelRecipeAttributeStrategy::HasColorAttribute@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use CAE::SelRecipeAttributeStrategy::HasColorAttribute instead.") bool HasColorAttribute
            (
            );
            /**Returns  the color attribute. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::ColorAttribute CAE::SelRecipeAttributeStrategy::ColorAttribute@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use CAE::SelRecipeAttributeStrategy::ColorAttribute instead.") int ColorAttribute
            (
            );
            /** Sets or adds the color attribute. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::SetColorAttribute CAE::SelRecipeAttributeStrategy::SetColorAttribute@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use CAE::SelRecipeAttributeStrategy::SetColorAttribute instead.") void SetColorAttribute
            (
                int color /** color */ 
            );
            /** Removes the color attribute. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::RemoveColorAttribute CAE::SelRecipeAttributeStrategy::RemoveColorAttribute@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use CAE::SelRecipeAttributeStrategy::RemoveColorAttribute instead.") void RemoveColorAttribute
            (
            );
            /** Gets the names of all set user attributes. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::GetUserAttributeNames CAE::SelRecipeAttributeStrategy::GetUserAttributeNames@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use CAE::SelRecipeAttributeStrategy::GetUserAttributeNames instead.") void GetUserAttributeNames
            (
                std::vector<NXString> & userAttributeNames /** userattributenames */ 
            );
            /** Gets the presence of the user attribute with given name. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::GetHasUserAttributes CAE::SelRecipeAttributeStrategy::GetHasUserAttributes@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use CAE::SelRecipeAttributeStrategy::GetHasUserAttributes instead.") bool GetHasUserAttributes
            (
                const NXString & attributeName /** attributename */ 
            );
            /** Gets the presence of the user attribute with given name. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::GetHasUserAttributes CAE::SelRecipeAttributeStrategy::GetHasUserAttributes@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            bool GetHasUserAttributes
            (
                const char * attributeName /** attributename */ 
            );
            /** Gets all the attributes that have been set on the given object, if any, that satisfy the given iterator.
                    The results will not include information from associated attribute templates of unset attributes.
                    The elements of array attributes are returned individually in order of increasing indices. 
                    The returned Title of an array element is the array title (without index). The Index data member holds the index.
                    The date format set by the Customer Defaults is used.
                    Reference type attributes are returned as being of type @link NXOpen::NXObject::AttributeTypeString NXOpen::NXObject::AttributeTypeString@endlink ,
                    and both the ReferenceValue and the calculated StringValue are returned.  @return   
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::NXObject::AttributeInformation> GetUserAttributes
            (
                NXOpen::AttributeIterator * iterator /** @link NXOpen::AttributeIterator NXOpen::AttributeIterator@endlink  */
            );
            /** Gets all the attributes that have been set on the given object.
                    The results will not include information from associated attribute templates of unset attributes.
                    The elements of array attributes are returned individually in order of increasing indices. 
                    The returned Title of an array element is the array title (without index). The Index data member holds the index.
                    The date format set by the Customer Defaults is used.
                    Reference type attributes are returned as being of type @link NXOpen::NXObject::AttributeTypeString NXOpen::NXObject::AttributeTypeString@endlink ,
                    and both the ReferenceValue and the calculated StringValue are returned.  @return   
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::NXObject::AttributeInformation> GetUserAttributes
            (
            );
            /** Gets all the attributes of the given object.
                    Includes option to return information also from associated attribute templates of unset attributes.
                    The values returned for unset attributes are the default values from the templates.
                    The elements of array attributes are returned individually in order of increasing indices. 
                    The returned Title of an array element is the array title (without index). The Index data member holds the index.
                    The date format set by the Customer Defaults is used.
                    Reference type attributes are returns as being of type @link NXOpen::NXObject::AttributeTypeString NXOpen::NXObject::AttributeTypeString@endlink ,
                    and both the ReferenceValue and the calculated StringValue are returned.  @return   
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::NXObject::AttributeInformation> GetUserAttributes
            (
                bool includeUnset /** includeunset */ 
            );
            /** Gets all the attributes of the given object.
                    Includes option to return information also from associated attribute templates of unset attributes.
                    The values returned for unset attributes are the default values from the templates.
                    Includes an option to return the value not only in the natural type, but also converted to a string (effective only for non-string attributes).
                    The elements of array attributes are returned individually in order of increasing indices. 
                    The returned Title of an array element is the array title (without index). The Index data member holds the index.
                    The date format set by the Customer Defaults is used.
                    Reference type attributes are returned as being of type @link NXOpen::NXObject::AttributeTypeString NXOpen::NXObject::AttributeTypeString@endlink ,
                    and both the ReferenceValue and the calculated StringValue are returned.  @return   
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link GetUserAttributes GetUserAttributes@endlink  instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use GetUserAttributes instead.") std::vector<NXOpen::NXObject::AttributeInformation> GetUserAttributes
            (
                bool includeUnset /** includeunset */ ,
                bool addStringValues /** addstringvalues */ 
            );
            /** Gets the low and high value of user attribute with given name. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::GetUserAttributes CAE::SelRecipeAttributeStrategy::GetUserAttributes@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use CAE::SelRecipeAttributeStrategy::GetUserAttributes instead.") void GetUserAttributes
            (
                const NXString & attributeName /** attributename */ ,
                NXOpen::NXObject::AttributeInformation* lowValueAttribute /** lowvalueattribute */ ,
                NXOpen::NXObject::AttributeInformation* highValueAttribute /** highvalueattribute */ 
            );
            /** Gets the low and high value of user attribute with given name. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::GetUserAttributes CAE::SelRecipeAttributeStrategy::GetUserAttributes@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void GetUserAttributes
            (
                const char * attributeName /** attributename */ ,
                NXOpen::NXObject::AttributeInformation* lowValueAttribute /** lowvalueattribute */ ,
                NXOpen::NXObject::AttributeInformation* highValueAttribute /** highvalueattribute */ 
            );
            /** Sets or adds the low and high value of user attribute with given name. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::SetUserAttributes CAE::SelRecipeAttributeStrategy::SetUserAttributes@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use CAE::SelRecipeAttributeStrategy::SetUserAttributes instead.") void SetUserAttributes
            (
                const NXString & attributeName /** attributename */ ,
                const NXOpen::NXObject::AttributeInformation & lowValueAttribute /** lowvalueattribute */ ,
                const NXOpen::NXObject::AttributeInformation & highValueAttribute /** highvalueattribute */ 
            );
            /** Sets or adds the low and high value of user attribute with given name. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::SetUserAttributes CAE::SelRecipeAttributeStrategy::SetUserAttributes@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetUserAttributes
            (
                const char * attributeName /** attributename */ ,
                const NXOpen::NXObject::AttributeInformation & lowValueAttribute /** lowvalueattribute */ ,
                const NXOpen::NXObject::AttributeInformation & highValueAttribute /** highvalueattribute */ 
            );
            /** Removes the user attribute with given name. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::RemoveUserAttributes CAE::SelRecipeAttributeStrategy::RemoveUserAttributes@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use CAE::SelRecipeAttributeStrategy::RemoveUserAttributes instead.") void RemoveUserAttributes
            (
                const NXString & attributeName /** attributename */ 
            );
            /** Removes the user attribute with given name. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::RemoveUserAttributes CAE::SelRecipeAttributeStrategy::RemoveUserAttributes@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void RemoveUserAttributes
            (
                const char * attributeName /** attributename */ 
            );
            /** Clear all attributes 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::ClearAllAttributes CAE::SelRecipeAttributeStrategy::ClearAllAttributes@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use CAE::SelRecipeAttributeStrategy::ClearAllAttributes instead.") void ClearAllAttributes
            (
            );
            /** Convenience method to set multiple attributes at once. The name and color are optional.
                        It's recommended to use this method in case of setting multiple attributes, to avoid 
                        having the recipe resolve multiple times. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::SetUserAttributes CAE::SelRecipeAttributeStrategy::SetUserAttributes@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use CAE::SelRecipeAttributeStrategy::SetUserAttributes instead.") void SetUserAttributes
            (
                bool setNameAttribute /** setnameattribute */ ,
                const NXString & nameAttribute /** nameattribute */ ,
                bool setColorAttribute /** setcolorattribute */ ,
                int colorAttribute /** colorattribute */ ,
                std::vector<NXString> & userAttributeNames /** userattributenames */ ,
                const std::vector<NXOpen::NXObject::AttributeInformation> & lowValueAttributes /** lowvalueattributes */ ,
                const std::vector<NXOpen::NXObject::AttributeInformation> & highValueAttributes /** highvalueattributes */ 
            );
            /** Convenience method to set multiple attributes at once. The name and color are optional.
                        It's recommended to use this method in case of setting multiple attributes, to avoid 
                        having the recipe resolve multiple times. 
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link CAE::SelRecipeAttributeStrategy::SetUserAttributes CAE::SelRecipeAttributeStrategy::SetUserAttributes@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetUserAttributes
            (
                bool setNameAttribute /** setnameattribute */ ,
                const char * nameAttribute /** nameattribute */ ,
                bool setColorAttribute /** setcolorattribute */ ,
                int colorAttribute /** colorattribute */ ,
                std::vector<NXString> & userAttributeNames /** userattributenames */ ,
                const std::vector<NXOpen::NXObject::AttributeInformation> & lowValueAttributes /** lowvalueattributes */ ,
                const std::vector<NXOpen::NXObject::AttributeInformation> & highValueAttributes /** highvalueattributes */ 
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
