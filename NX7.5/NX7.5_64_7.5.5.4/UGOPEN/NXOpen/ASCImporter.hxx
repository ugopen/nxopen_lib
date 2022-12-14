#ifndef NXOpen_ASCIMPORTER_HXX_INCLUDED
#define NXOpen_ASCIMPORTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ASCImporter.ja
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
#include <NXOpen/ASCImporter.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class ASCImporter;
    class Builder;
    class _ASCImporterBuilder;
    class ASCImporterImpl;
    /**
        Represents a @link ASCImporter ASCImporter@endlink .  This class is
        used to import .ASC and .DWG files
         <br> To create a new instance of this class, use @link DexManager::CreateAscImporter DexManager::CreateAscImporter@endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    PartUnitsEnum </td> <td> 
     
    Millimeters </td> </tr> 

    </table>  
    */
    class NXOPENCPPEXPORT  ASCImporter : public Builder
    {
        /**The Part Units selection Enum */
        public: enum Units
        {
            UnitsMillimeters/** Millimeters Selection */,
            UnitsInches/** Inches Selection */
        };

        private: ASCImporterImpl * m_ascimporter_impl;
        private: friend class  _ASCImporterBuilder;
        protected: ASCImporter();
        public: ~ASCImporter();
        /**Returns  the input file - name of a file which is being imported  <br> License requirements : nx_drafting_plus ("Drafting Plus") */
        public: NXString InputFile
        (
        );
        /**Sets  the input file - name of a file which is being imported  <br> License requirements : nx_drafting_plus ("Drafting Plus") */
        public: void SetInputFile
        (
            const NXString & filename /** filename */ 
        );
        /**Returns  the output file - name of a file which is being created  <br> License requirements : nx_drafting_plus ("Drafting Plus") */
        public: NXString OutputFile
        (
        );
        /**Sets  the output file - name of a file which is being created  <br> License requirements : nx_drafting_plus ("Drafting Plus") */
        public: void SetOutputFile
        (
            const NXString & filename /** filename */ 
        );
        /**Returns  the part units enum  <br> License requirements : nx_drafting_plus ("Drafting Plus") */
        public: NXOpen::ASCImporter::Units PartUnitsEnum
        (
        );
        /**Sets  the part units enum  <br> License requirements : nx_drafting_plus ("Drafting Plus") */
        public: void SetPartUnitsEnum
        (
            NXOpen::ASCImporter::Units partUnitsEnum /** partunitsenum */ 
        );
    };
}
#undef EXPORTLIBRARY
#endif
