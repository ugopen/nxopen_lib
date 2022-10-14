#ifndef NXOpen_CAE_PROPERTYTABLE_HXX_INCLUDED
#define NXOpen_CAE_PROPERTYTABLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PropertyTable.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class PropertyTable;
    }
    class CoordinateSystem;
    class Direction;
    class Expression;
    namespace Fields
    {
        class FieldExpression;
    }
    class NXObject;
    namespace CAE
    {
        class _PropertyTableBuilder;
        /**  @brief  Represents a property table  

           <br> This is a sub object <br> */
        class NXOPENCPPEXPORT PropertyTable : public NXObject
        {
            private: friend class  _PropertyTableBuilder;
            protected: PropertyTable();
            /**The count of properties in the table  @return  count of properties  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: int GetPropertyCount
            (
            );
            /** Returns the name of the property  @return  name of the property  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString GetPropertyNameByIndex
            (
                int index /** index of the property */
            );
            /** Returns the string value of the property
                      @return  value of the property  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString GetStringPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the string value of the property
                      <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetStringPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & property_value /** value of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Returns the text value of the property
                      @return  value of the property  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: std::vector<NXString> GetTextPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the text value of the property
                      <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetTextPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                std::vector<NXString> & property_value /** value of the property */
            );
            /** Returns the boolean value of the property
                      @return  value of the property  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool GetBooleanPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the boolean value of the property
                      <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetBooleanPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                bool property_value /** value of the property */
            );
            /** Returns the integer value of the property
                      @return  value of the property  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: int GetIntegerPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the integer value of the property
                      <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetIntegerPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int property_value /** value of the property */
            );
            /** Returns the double value of the property
                      @return  value of the property  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: double GetDoublePropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the double value of the property
                      <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetDoublePropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                double property_value /** value of the property */
            );
            /** Returns the expression @link Expression Expression@endlink  value of the property
                      @return  value of the property  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::Expression * GetScalarPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the expression @link Expression Expression@endlink  value of the property
                      <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetScalarPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Expression * property_value /** value of the property */
            );
            /** Returns the field expression @link Fields::FieldExpression Fields::FieldExpression@endlink  value of the property
                      @return  value of the property  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::Fields::FieldExpression * GetScalarFieldPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the field expression @link Fields::FieldExpression Fields::FieldExpression@endlink  value of the property
                      <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetScalarFieldPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Fields::FieldExpression * property_value /** value of the property */
            );
            /** Returns the direction @link Direction Direction@endlink  value of the property
                      @return  value of the property  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::Direction * GetVectorPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the direction @link Direction Direction@endlink  value of the property
                      <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetVectorPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Direction * property_value /** value of the property */
            );
            /** Returns the coordinate system @link CoordinateSystem CoordinateSystem@endlink  
                      @return  value of the property  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CoordinateSystem * GetCoordinateSystemPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the coordinate system @link CoordinateSystem CoordinateSystem@endlink 
                      <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCoordinateSystemPropertyValue
            (
                const NXString & property_name /** name of the property   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::CoordinateSystem * property_value /** value of the property */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif