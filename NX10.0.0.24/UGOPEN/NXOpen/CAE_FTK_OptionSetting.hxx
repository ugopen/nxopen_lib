#ifndef NXOpen_CAE_FTK_OPTIONSETTING_HXX_INCLUDED
#define NXOpen_CAE_FTK_OPTIONSETTING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FTK_OptionSetting.ja
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
#include <NXOpen/CAE_AfuData.hxx>
#include <NXOpen/CAE_XYFunctionDataTypes.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        namespace FTK
        {
            class OptionSetting;
        }
    }
    namespace CAE
    {
        namespace FTK
        {
            class FTKManager;
        }
    }
    namespace CAE
    {
        namespace FTK
        {
            class OptionSettingImpl;
            /** Manager the options data for AFU Data Record  <br> Not support KF.  <br> 
             <br>  Created in NX6.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  OptionSetting
            {
                private: OptionSettingImpl * m_optionsetting_impl;
                private: NXOpen::CAE::FTK::FTKManager* m_owner;
                /// \cond NX_NO_DOC 
                public: explicit OptionSetting(NXOpen::CAE::FTK::FTKManager *owner);


                /// \endcond 
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                public: ~OptionSetting();
                /** Get the options data for an AFU Data Record 
                 <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAE::FTK::OptionSetting::GetRecordOptionData NXOpen::CAE::FTK::OptionSetting::GetRecordOptionData@endlink  with Denominator. <br>  

                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAE::FTK::OptionSetting::GetRecordOptionData with Denominator.") void GetOptionData
                (
                    NXString* recordName /** The name of the AFU Data Record */,
                    NXOpen::CAE::XyFunctionGeneralType* functionType /** Usage type of AFU Data Record used */,
                    NXOpen::CAE::AfuData::AbscissaType* abscissaType /** Abscissa specific data type */,
                    NXOpen::CAE::XyFunctionUnit* xUnit /** Unit Code of AFU data */,
                    NXOpen::CAE::AfuData::OrdinateType* oridinateType /** Ordinate specific data type */,
                    NXOpen::CAE::XyFunctionUnit* yUnit /** Unit Code of AFU data */,
                    bool* sortValueType /** If want to sort value in x direction */
                );
                /** Get the record options data for an AFU Data Record 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void GetRecordOptionData
                (
                    NXString* recordName /** The name of the AFU Data Record */,
                    NXOpen::CAE::XyFunctionGeneralType* functionType /** Usage type of AFU Data Record used */,
                    NXOpen::CAE::AfuData::AbscissaType* abscissaType /** Abscissa specific data type */,
                    NXOpen::CAE::XyFunctionUnit* xUnit /** Unit Code of AFU data */,
                    NXOpen::CAE::AfuData::OrdinateType* ordinateType /** Ordinate data type */,
                    NXOpen::CAE::XyFunctionUnit* yUnit /** Ordinate Numerator Unit Code of AFU data */,
                    NXOpen::CAE::XyFunctionUnit* yDenominatorUnit /** Ordinate Denominator Unit Code of AFU data */,
                    bool* sortValueType /** If want to sort value in x direction */
                );
                /** Set the options data for an AFU Data Record 
                 <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAE::FTK::OptionSetting::SetRecordOptionData NXOpen::CAE::FTK::OptionSetting::SetRecordOptionData@endlink  with Denominator. <br>  

                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAE::FTK::OptionSetting::SetRecordOptionData with Denominator.") void SetOptionData
                (
                    const NXString & recordName /** The name of the AFU Data Record   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                    NXOpen::CAE::XyFunctionGeneralType functionType /** Usage type of AFU Data Record used */,
                    NXOpen::CAE::AfuData::AbscissaType abscissaType /** Abscissa specific data type */,
                    NXOpen::CAE::XyFunctionUnit xUnit /** Unit Code of AFU data */,
                    NXOpen::CAE::AfuData::OrdinateType oridinateType /** Ordinate specific data type */,
                    NXOpen::CAE::XyFunctionUnit yUnit /** Unit Code of AFU data */,
                    bool sortValueType /** If want to sort value in x direction */
                );
                /** Set the options data for an AFU Data Record 
                 <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAE::FTK::OptionSetting::SetRecordOptionData NXOpen::CAE::FTK::OptionSetting::SetRecordOptionData@endlink  with Denominator. <br>  

                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                void SetOptionData
                (
                    const char * recordName /** The name of the AFU Data Record   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                    NXOpen::CAE::XyFunctionGeneralType functionType /** Usage type of AFU Data Record used */,
                    NXOpen::CAE::AfuData::AbscissaType abscissaType /** Abscissa specific data type */,
                    NXOpen::CAE::XyFunctionUnit xUnit /** Unit Code of AFU data */,
                    NXOpen::CAE::AfuData::OrdinateType oridinateType /** Ordinate specific data type */,
                    NXOpen::CAE::XyFunctionUnit yUnit /** Unit Code of AFU data */,
                    bool sortValueType /** If want to sort value in x direction */
                );
                /** Set the record options data for an AFU Data Record 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetRecordOptionData
                (
                    const NXString & recordName /** The name of the AFU Data Record   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                    NXOpen::CAE::XyFunctionGeneralType functionType /** Usage type of AFU Data Record used */,
                    NXOpen::CAE::AfuData::AbscissaType abscissaType /** Abscissa specific data type */,
                    NXOpen::CAE::XyFunctionUnit xUnit /** Unit Code of AFU data */,
                    NXOpen::CAE::AfuData::OrdinateType ordinateType /** Ordinate data type */,
                    NXOpen::CAE::XyFunctionUnit yUnit /** Unit Code of AFU data */,
                    NXOpen::CAE::XyFunctionUnit yDenominatorUnit /** Unit Code of AFU data */,
                    bool sortValueType /** If want to sort value in x direction */
                );
                /** Set the record options data for an AFU Data Record 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                void SetRecordOptionData
                (
                    const char * recordName /** The name of the AFU Data Record   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                    NXOpen::CAE::XyFunctionGeneralType functionType /** Usage type of AFU Data Record used */,
                    NXOpen::CAE::AfuData::AbscissaType abscissaType /** Abscissa specific data type */,
                    NXOpen::CAE::XyFunctionUnit xUnit /** Unit Code of AFU data */,
                    NXOpen::CAE::AfuData::OrdinateType ordinateType /** Ordinate data type */,
                    NXOpen::CAE::XyFunctionUnit yUnit /** Unit Code of AFU data */,
                    NXOpen::CAE::XyFunctionUnit yDenominatorUnit /** Unit Code of AFU data */,
                    bool sortValueType /** If want to sort value in x direction */
                );
                /** Get the adding header flag when export to CSV file  @return  If want to add header when export to CSV file 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: bool GetHeaderFlag
                (
                );
                /** Set the adding header flag when export to CSV file 
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetHeaderFlag
                (
                    bool addHeader /** If want to add header when export to CSV file */
                );
            }; //lint !e1712 default constructor not defined for class  

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
