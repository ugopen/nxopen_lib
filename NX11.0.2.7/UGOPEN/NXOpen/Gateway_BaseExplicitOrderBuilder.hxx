#ifndef NXOpen_GATEWAY_BASEEXPLICITORDERBUILDER_HXX_INCLUDED
#define NXOpen_GATEWAY_BASEEXPLICITORDERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Gateway_BaseExplicitOrderBuilder.ja
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
#include <NXOpen/Gateway_BaseExplicitOrderBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_gateway_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Gateway
    {
        class BaseExplicitOrderBuilder;
    }
    class Builder;
    namespace Gateway
    {
        class _BaseExplicitOrderBuilderBuilder;
        class BaseExplicitOrderBuilderImpl;
        /** This is the @link NXOpen::Gateway::BaseExplicitOrderBuilder NXOpen::Gateway::BaseExplicitOrderBuilder@endlink  for the explicit order <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_GATEWAYEXPORT  BaseExplicitOrderBuilder : public NXOpen::Builder
        {
            private: BaseExplicitOrderBuilderImpl * m_baseexplicitorderbuilder_impl;
            private: friend class  _BaseExplicitOrderBuilderBuilder;
            protected: BaseExplicitOrderBuilder();
            public: ~BaseExplicitOrderBuilder();
            /**Returns  the save name 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString SaveName
            (
            );
            /**Sets  the save name 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSaveName
            (
                const NXString & saveName /** savename */ 
            );
            /**Sets  the save name 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            void SetSaveName
            (
                const char * saveName /** savename */ 
            );
            /** Saves an explicit order defined by the user 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void Save
            (
                std::vector<NXString> & orderList /** orderlist */ ,
                const NXString & saveName /** savename */ 
            );
            /** Saves an explicit order defined by the user 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            void Save
            (
                std::vector<NXString> & orderList /** orderlist */ ,
                const char * saveName /** savename */ 
            );
            /** Pastes the rows that have been previously selected using the cut operation  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> Paste
            (
                int pastePoint /** pastepoint */ ,
                std::vector<NXString> & selectedEntries /** selectedentries */ ,
                std::vector<NXString> & currentOrder /** currentorder */ 
            );
            /** Deletes the saved order/orders that has/have been selected by the user from the list of saved orders  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> Delete
            (
                std::vector<NXString> & selectedEntries /** selectedentries */ ,
                std::vector<NXString> & currentOrder /** currentorder */ ,
                int numOfRemainingEntries /** numofremainingentries */ 
            );
            /** Clears the current order and restores it to the default order 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void Clear
            (
            );
            /** Moves down the row/rows selected by the user in the lists  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> DownArrow
            (
                std::vector<NXString> & selectedEntries /** selectedentries */ ,
                std::vector<NXString> & currentOrder /** currentorder */ 
            );
            /** Moves up the row/rows selected by the user in the lists  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> UpArrow
            (
                std::vector<NXString> & selectedEntries /** selectedentries */ ,
                std::vector<NXString> & currentOrder /** currentorder */ 
            );
            /** Saves the selected saved order in the form of a text file 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SaveAsTextFile
            (
                const NXString & savedOrderName /** savedordername */ ,
                const NXString & saveFileName /** savefilename */ ,
                bool overwriteFile /** overwritefile */ 
            );
            /** Saves the selected saved order in the form of a text file 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            void SaveAsTextFile
            (
                const char * savedOrderName /** savedordername */ ,
                const char * saveFileName /** savefilename */ ,
                bool overwriteFile /** overwritefile */ 
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
