#ifndef NXOpen_CAE_AFUDATA_HXX_INCLUDED
#define NXOpen_CAE_AFUDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AfuData.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CAE_AfuHeaderId.hxx>
#include <NXOpen/CAE_XYFunctionDataTypes.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class AfuData;
    }
    namespace CAE
    {
        class AfuHeaderId;
    }
    namespace CAE
    {
        /** the data used to create an AFU Data Record */
        class NXOPENCPPEXPORT AfuData : public TransientObject
        {
            /** Defines abscissa data type for AFU data record */
            public: enum AbscissaType
            {
                AbscissaTypeEven/** The abscissa value is even and calculated by increment */,
                AbscissaTypeUneven/** The abscissa value is uneven and input by user */,
                AbscissaTypeSequence/** The abscissa value is a sequence and input by user */
            };

            /** Defines ordinate data type for AFU data record */
            public: enum OrdinateType
            {
                OrdinateTypeReal/** Ordinate Data is a single Real value */,
                OrdinateTypeRealImaginary/** Ordinate Data is Complex with Real and Imaginary values */,
                OrdinateTypeMagnitudePhase/** Ordinate Data is Complex with Amplitude and Phase values*/
            };

            public: explicit AfuData(void *ptr);
            /** Free the AFU Data transient object memory  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: virtual ~AfuData();
            /**Sets  the name of AFU file  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetFileName
            (
                const NXString & afu_file_name /** The full name of the AFU file */
            );
            /**Returns  the name of AFU file  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: NXString FileName
            (
            );
            /**Sets  the name of the AFU Data Record  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetRecordName
            (
                const NXString & afu_record_name /** The name of AFU Data Record */
            );
            /**Returns  the name of the AFU Data Record  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: NXString RecordName
            (
            );
            /** Sets the main AFU Data Record ID information  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetIdInformation
            (
                const NXString & reference /** String to define reference direction sense.
                                                                      Up to 4 characters are allowed and
                                                                      the redundant characters will be ignored.
                                                                      ( X, Y, Z, RX, RY, and RZ have specific
                                                                      meaning but the character set can be
                                                                      anything including a "+" or "-" as the
                                                                      last character. examples:  ABC+  RSTU )
                                                                      <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int reference_id /** ID of reference element or node */,
                const NXString & response /** String to define response direction sense.
                                                                     Up to 4 characters are allowed and the redundant
                                                                     characters will be ignored.
                                                                    ( X, Y, Z, RX, RY, and RZ have specific
                                                                      meaning but the character set can be
                                                                      anything including a "+" or "-" as the
                                                                      last character. examples:  ABC+  RSTU )
                                                                       <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                int response_id /** ID of response element or node */
            );
            /** Returns main AFU Data Record ID information  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void GetIdInformation
            (
                NXString* reference /** String to define reference direction sense.
                                                                    Up to 4 characters are allowed and the redundant
                                                                    characters will be ignored.
                                                                    ( X, Y, Z, RX, RY, and RZ have specific
                                                                      meaning but the character set can be
                                                                      anything including a "+" or "-" as the
                                                                      last character. examples:  ABC+  RSTU )
                                                                */,
                int* reference_id /** ID of reference element or node */,
                NXString* response /** String to define response direction sense.
                                                                    Up to 4 characters are allowed and the
                                                                    redundant characters will be ignored.
                                                                    ( X, Y, Z, RX, RY, and RZ have specific
                                                                      meaning but the character set can be
                                                                      anything including a "+" or "-" as the
                                                                      last character. examples:  ABC+  RSTU )
                                                                */,
                int* response_id /** ID of response element or node */
            );
            /** Set the Abscissa Axis definitions of an AFU Data Record  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetAxisDefinition
            (
                NXOpen::CAE::AfuData::AbscissaType abscissa_type /** Abscissas specific data type */,
                NXOpen::CAE::XyFunctionUnit x_unit /** Unit Code of abscissa data */,
                NXOpen::CAE::AfuData::OrdinateType oridinate_type /** Ordinate specific data type */,
                NXOpen::CAE::XyFunctionUnit y_unit /** Unit Code of ordinate data */
            );
            /** Get the Abscissa Axis definitions of an AFU Data Record  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void GetAxisDefinition
            (
                NXOpen::CAE::AfuData::AbscissaType* abscissa_type /** Abscissa specific data type */,
                NXOpen::CAE::XyFunctionUnit* x_unit /** Unit Code of abscissa data */,
                NXOpen::CAE::AfuData::OrdinateType* oridinate_type /** Ordinate specific data type */,
                NXOpen::CAE::XyFunctionUnit* y_unit /** Unit Code of ordinate data */
            );
            /** Set the Abscissa Information for AFU Data Record when abscissa type is even  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetEvenData
            (
                double x_minimum /** Minimum abscissa data value */,
                double x_increment /** Abscissa increment */,
                int number_of_points /** Number of abscissa elements */
            );
            /** Get the Abscissa Information for an AFU Data Record when the abscissa type is even  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void GetEvenData
            (
                double* x_minimum /** Minimum abscissa data value */,
                double* x_increment /** Abscissa increment */,
                int* number_of_points /** Number of abscissa elements */
            );
            /** Set the XY Data of an AFU Data Record when the ordinate type is real  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetRealData
            (
                const std::vector<double> & x_values /** Abscissa element data values */,
                const std::vector<double> & y_values /** Ordinate element data values */
            );
            /** Get the XY Data of an AFU Data Record when the ordinate type is real  @return  Ordinate element data values  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: std::vector<double> GetRealData
            (
                std::vector<double> & x_values /** Abscissa element data values */
            );
            /** Set the XY Data of an AFU record when the ordinate type is Complex  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetComplexData
            (
                const std::vector<double> & x_values /** Abscissa element data values*/,
                const std::vector<double> & y_values /** Ordinate element data values for real part or magnitude part */,
                const std::vector<double> & z_values /** Ordinate element data values for imaginary part or phase part */
            );
            /** Get the XY data of an AFU Data Record when the ordinate type is Complex  @return  Ordinate element data values for imaginary part or phase part  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: std::vector<double> GetComplexData
            (
                std::vector<double> & x_values /** Abscissa element data values*/,
                std::vector<double> & y_values /** Ordinate element data values for real part or magnitude part */
            );
            /**Sets  the data type of the AFU Data Record  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetFunctionDataType
            (
                NXOpen::CAE::XyFunctionDataType function_data_type /** The data type of a function in AFU */
            );
            /**Returns  the data type of the AFU Data Record  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: NXOpen::CAE::XyFunctionDataType FunctionDataType
            (
            );
            /**Sets  the AFU Header Id data of the AFU Data Record  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetAfuHeaderId
            (
                NXOpen::CAE::AfuHeaderId * afu_header_id /** The AFU Header Id data */
            );
            /**Returns  the AFU Header Id data of the AFU Data Record  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: NXOpen::CAE::AfuHeaderId * AfuHeaderId
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif