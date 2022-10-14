#ifndef NXOpen_TOOLING_BOMLISTDATAPROVIDER_HXX_INCLUDED
#define NXOpen_TOOLING_BOMLISTDATAPROVIDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_BomListDataProvider.ja
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
#include <NXOpen/ITableEditorDataProvider.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class BomListDataProvider;
    }
    class ITableEditorDataProvider;
    namespace Tooling
    {
        class _BomListDataProviderBuilder;
        class BomListDataProviderImpl;
        /**
            Provides basic data for BOM List.
            When @link Builder::Commit Builder::Commit@endlink  is called NULL will be returned.
             <br> To create a new instance of this class, use @link NXOpen::Tooling::MoldwizardManager::CreateBomListDataProvider  NXOpen::Tooling::MoldwizardManager::CreateBomListDataProvider @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  BomListDataProvider : public NXOpen::TaggedObject, public virtual NXOpen::ITableEditorDataProvider
        {
            /** Represents the exported status of a cell. */
            public: enum ExportedStatus
            {
                ExportedStatusNull/** No parts in the row are exported */,
                ExportedStatusPartial/** Partial parts in the row are exported */,
                ExportedStatusAll/** All parts in the row are exported */
            };

            private: BomListDataProviderImpl * m_bomlistdataprovider_impl;
            private: friend class  _BomListDataProviderBuilder;
            protected: BomListDataProvider();
            public: ~BomListDataProvider();
            /**Returns  the number of rows in the table 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: virtual int RowCount
            (
            );
            /**Sets  the number of rows in the table 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: virtual void SetRowCount
            (
                int rowCount /** the number of rows in the table */
            );
            /**Returns  the number of columns in the table 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: virtual int ColumnCount
            (
            );
            /**Sets  the number of columns in the table 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: virtual void SetColumnCount
            (
                int columnCount /** the number of columns in the table */
            );
            /** Sets string data at a particular location in the table.  @return  whether or not the data was successfully set. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: virtual bool SetString
            (
                int rows /** the row to set */,
                int column /** the column to set */,
                const NXString & stringData /** the string data to set */
            );
            /** Sets string data at a particular location in the table.  @return  whether or not the data was successfully set. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            virtual bool SetString
            (
                int rows /** the row to set */,
                int column /** the column to set */,
                const char * stringData /** the string data to set */
            );
            /** Sets string data on a range of table cells in a specified column. Returns whether any data was successfully set.  @return  whether or not the data was successfully set. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: virtual bool SetString
            (
                const std::vector<int> & rows /** the rows to set */,
                int column /** the column to be set */,
                const NXString & stringData /** the string data to set */
            );
            /** Sets string data on a range of table cells in a specified column. Returns whether any data was successfully set.  @return  whether or not the data was successfully set. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            virtual bool SetString
            (
                const std::vector<int> & rows /** the rows to set */,
                int column /** the column to be set */,
                const char * stringData /** the string data to set */
            );
            /** Gets the string data at a particular location in the table.  @return  the string data at the row and column specified 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXString GetString
            (
                int row /** the rows to query */,
                int column /** the column to query */
            );
            /** Sets integer data at a particular location in the table.  @return  whether or not the data was successfully set. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual bool SetInteger
            (
                int rows /** the row to set */,
                int column /** the column to set */,
                int integerData /** the integer data to set */
            );
            /** Sets integer data on a range of table cells in a specified column. Returns whether any data was successfully set.  @return  whether or not the data was successfully set. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual bool SetInteger
            (
                const std::vector<int> & rows /** the rows to set */,
                int column /** the column to be set */,
                int integerData /** the integer data to set */
            );
            /** Gets the integer data at a particular location in the table.  @return  the integer data at the row and column specified 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual int GetInteger
            (
                int row /** the rows to query */,
                int column /** the column to query */,
                bool* isUnassigned /** is the value unassigned */
            );
            /** Sets double data at a particular location in the table.  @return  whether or not the data was successfully set. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual bool SetDouble
            (
                int rows /** the row to set */,
                int column /** the column to set */,
                double doubleData /** the double data to set */
            );
            /** Sets double data on a range of table cells in a specified column. Returns whether any data was successfully set.  @return  whether or not the data was successfully set. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual bool SetDouble
            (
                const std::vector<int> & rows /** the rows to set */,
                int column /** the column to be set */,
                double doubleData /** the double data to set */
            );
            /** Gets the double data at a particular location in the table.  @return  the double data at the row and column specified 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual double GetDouble
            (
                int row /** the rows to query */,
                int column /** the column to query */,
                bool* isUnassigned /** is the value unassigned */
            );
            /** Sets boolean data at a particular location in the table.  @return  whether or not the data was successfully set. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual bool SetBoolean
            (
                int rows /** the row to set */,
                int column /** the column to set */,
                bool booleanData /** the boolean data to set */
            );
            /** Sets boolean data on a range of table cells in a specified column. Returns whether any data was successfully set.  @return  whether or not the data was successfully set. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual bool SetBoolean
            (
                const std::vector<int> & rows /** the rows to set */,
                int column /** the column to be set */,
                bool booleanData /** the boolean data to set */
            );
            /** Gets the boolean data at a particular location in the table.  @return  the boolean data at the row and column specified 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual bool GetBoolean
            (
                int row /** the rows to query */,
                int column /** the column to query */
            );
            /** Unsets the data at a particular location in the table.  @return  whether or not the data was successfully unset. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual bool UnsetValue
            (
                int row /** the row to unset */,
                int column /** the column to unset */
            );
            /** Unsets the data on a range of table cells in a specified column. Returns whether any data was successfully unset.  @return  whether or not the data was successfully unset. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual bool UnsetValue
            (
                const std::vector<int> & rows /** the rows to unset */,
                int column /** the column to be unset */
            );
            /** Deletes the data provider. This method should always be called when the data provider is no longer needed. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual void Destroy
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