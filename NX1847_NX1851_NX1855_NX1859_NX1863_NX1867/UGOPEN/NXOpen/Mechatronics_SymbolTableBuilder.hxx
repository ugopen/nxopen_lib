#ifndef NXOpen_MECHATRONICS_SYMBOLTABLEBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_SYMBOLTABLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_SymbolTableBuilder.ja
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
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class SymbolTableBuilder;
    }
    class Builder;
    namespace Mechatronics
    {
        class _SymbolTableBuilderBuilder;
        class SymbolTableBuilderImpl;
        /**  @brief  Represents a @link NXOpen::Mechatronics::SymbolTableBuilder NXOpen::Mechatronics::SymbolTableBuilder@endlink  builder.  

          
                 SymbolTableBuilder is used to maintain the @link NXOpen::Mechatronics::SymbolTable NXOpen::Mechatronics::SymbolTable@endlink  
                          which is used for Signal creation. 
                
             <br> To create a new instance of this class, use @link NXOpen::Mechatronics::SymbolTableCollection::CreateSymbolTableBuilder  NXOpen::Mechatronics::SymbolTableCollection::CreateSymbolTableBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  SymbolTableBuilder : public NXOpen::Builder
        {
            /**  @brief  Represents the IO type.  

              */
            public: enum IOType
            {
                IOTypeInput/** Input  */,
                IOTypeOutput/** Output */,
                IOTypeInout/** Input/Output */
            };

            /**  @brief  Represents the data type.  

              */
            public: enum DataType
            {
                DataTypeBool/** bool   */,
                DataTypeInt/** int    */,
                DataTypeDouble/** double */
            };

             /**  @brief  Represents Symbol definition structure.  

              
                         The Symbol name must be unique in the context of Symbol Table. The comment is optional. 
                    */
            public:
            struct Symbol
            {
                public: /** Symbol Name          */NXString Name;
                public: /** IO type              */NXOpen::Mechatronics::SymbolTableBuilder::IOType EIOType;
                public: /** Data type            */NXOpen::Mechatronics::SymbolTableBuilder::DataType EDataType;
                public: /** Address              */NXString Address;
                public: /** Comment Text         */NXString Comment;
                public: Symbol() :
                    Name(),
                    EIOType((NXOpen::Mechatronics::SymbolTableBuilder::IOType)0),
                    EDataType((NXOpen::Mechatronics::SymbolTableBuilder::DataType)0),
                    Address(),
                    Comment()
                {
                }
                /** Constructor for the Symbol struct. */ 
                public: Symbol(const NXString &nameInitial /** Symbol Name          */, 
                        NXOpen::Mechatronics::SymbolTableBuilder::IOType eIOTypeInitial /** IO type              */, 
                        NXOpen::Mechatronics::SymbolTableBuilder::DataType eDataTypeInitial /** Data type            */, 
                        const NXString &addressInitial /** Address              */, 
                        const NXString &commentInitial /** Comment Text         */) :
                    Name(nameInitial),
                    EIOType(eIOTypeInitial),
                    EDataType(eDataTypeInitial),
                    Address(addressInitial),
                    Comment(commentInitial)
                {
                }
            };

             /**  @brief  Represents Symbol definition structure version 2.  

              
                         Adding additional originalName member than previous version. 
                    */
            public:
            struct SymbolV2
            {
                public: /** Symbol Name          */NXString Name;
                public: /** Imported external signal name which may contain special char  */NXString OriginalName;
                public: /** IO type              */NXOpen::Mechatronics::SymbolTableBuilder::IOType EIOType;
                public: /** Data type            */NXOpen::Mechatronics::SymbolTableBuilder::DataType EDataType;
                public: /** Address              */NXString Address;
                public: /** Comment Text         */NXString Comment;
                public: SymbolV2() :
                    Name(),
                    OriginalName(),
                    EIOType((NXOpen::Mechatronics::SymbolTableBuilder::IOType)0),
                    EDataType((NXOpen::Mechatronics::SymbolTableBuilder::DataType)0),
                    Address(),
                    Comment()
                {
                }
                /** Constructor for the SymbolV2 struct. */ 
                public: SymbolV2(const NXString &nameInitial /** Symbol Name          */, 
                        const NXString &originalNameInitial /** Imported external signal name which may contain special char  */, 
                        NXOpen::Mechatronics::SymbolTableBuilder::IOType eIOTypeInitial /** IO type              */, 
                        NXOpen::Mechatronics::SymbolTableBuilder::DataType eDataTypeInitial /** Data type            */, 
                        const NXString &addressInitial /** Address              */, 
                        const NXString &commentInitial /** Comment Text         */) :
                    Name(nameInitial),
                    OriginalName(originalNameInitial),
                    EIOType(eIOTypeInitial),
                    EDataType(eDataTypeInitial),
                    Address(addressInitial),
                    Comment(commentInitial)
                {
                }
            };

            private: SymbolTableBuilderImpl * m_symboltablebuilder_impl;
            private: friend class  _SymbolTableBuilderBuilder;
            protected: SymbolTableBuilder();
            public: ~SymbolTableBuilder();
            /**  @brief  Gets all Symbols.  

               @return  Array of Symbols 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: std::vector<NXOpen::Mechatronics::SymbolTableBuilder::Symbol> GetSymbols
            (
            );
            /**  @brief  Sets all Symbols.  

              
                         Each Symbol name must be unique in the context of input Symbol list. Or the builder will raise an exception. 
                    
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetSymbols
            (
                const std::vector<NXOpen::Mechatronics::SymbolTableBuilder::Symbol> & symbols /** Array of Symbols */
            );
            /**  @brief  Gets all Symbols V2.  

               @return  Array of Symbols 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: std::vector<NXOpen::Mechatronics::SymbolTableBuilder::SymbolV2> GetSymbolsV2
            (
            );
            /**  @brief  Sets all Symbols V2.  

              
                         Each Symbol name must be unique in the context of input Symbol list. Or the builder will raise an exception. 
                    
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetSymbolsV2
            (
                const std::vector<NXOpen::Mechatronics::SymbolTableBuilder::SymbolV2> & symbols /** Array of Symbols */
            );
            /**Returns   @brief  the name.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets   @brief  the name.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets   @brief  the name.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetName
            (
                const char * name /** name */ 
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
