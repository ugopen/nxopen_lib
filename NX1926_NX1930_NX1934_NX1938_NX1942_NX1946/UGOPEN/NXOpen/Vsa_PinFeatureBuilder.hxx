#ifndef NXOpen_VSA_PINFEATUREBUILDER_HXX_INCLUDED
#define NXOpen_VSA_PINFEATUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Vsa_PinFeatureBuilder.ja
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
#include <NXOpen/libnxopencpp_vsa_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Vsa
    {
        class PinFeatureBuilder;
    }
    class Builder;
    namespace Vsa
    {
        class _PinFeatureBuilderBuilder;
        class PinFeatureBuilderImpl;
        /**
            
             <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreatePinFeatureBuilder  NXOpen::Vsa::VsaManager::CreatePinFeatureBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        DoubleAnchorX </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DoubleAnchorY </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DoubleAnchorZ </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DoubleDiameter1 </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DoubleDiameter2 </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DoubleDirectionI </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DoubleDirectionJ </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DoubleDirectionK </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DoubleHeight </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DoubleKurtosisForm </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DoubleKurtosisLoc </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DoubleKurtosisSize </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DoubleSkewnessForm </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DoubleSkewnessLoc </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        DoubleSkewnessSize </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        EnumForm </term> <description> 
         
        Normal </description> </item> 

        <item><term> 
         
        EnumLoc </term> <description> 
         
        Normal </description> </item> 

        <item><term> 
         
        EnumSize </term> <description> 
         
        Normal </description> </item> 

        </list> 

         <br>  Usable only on Windows <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_VSAEXPORT  PinFeatureBuilder : public NXOpen::Builder
        {
            /**
                    
                    */
            public: enum APIEnumSize
            {
                APIEnumSizeNormal/** normal */ ,
                APIEnumSizeUniform/** uniform */ ,
                APIEnumSizeExtreme/** extreme */ ,
                APIEnumSizePearson/** pearson */ ,
                APIEnumSizeTrapeziodal/** trapeziodal */ 
            };

            /**
                    
                    */
            public: enum APIEnumLoc
            {
                APIEnumLocNormal/** normal */ ,
                APIEnumLocUniform/** uniform */ ,
                APIEnumLocExtreme/** extreme */ ,
                APIEnumLocPearson/** pearson */ ,
                APIEnumLocTrapeziodal/** trapeziodal */ 
            };

            /**
                    
                    */
            public: enum APIEnumForm
            {
                APIEnumFormNormal/** normal */ ,
                APIEnumFormUniform/** uniform */ ,
                APIEnumFormExtreme/** extreme */ ,
                APIEnumFormPearson/** pearson */ ,
                APIEnumFormTrapeziodal/** trapeziodal */ 
            };

            private: PinFeatureBuilderImpl * m_pinfeaturebuilder_impl;
            private: friend class  _PinFeatureBuilderBuilder;
            protected: PinFeatureBuilder();
            public: ~PinFeatureBuilder();
            /**Returns  the string name 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString StringName
            (
            );
            /**Sets  the string name 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetStringName
            (
                const NXString & stringName /** stringname */ 
            );
            /**Sets  the string name 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            void SetStringName
            (
                const char * stringName /** stringname */ 
            );
            /**Returns  the string description 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString StringDescription
            (
            );
            /**Sets  the string description 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetStringDescription
            (
                const NXString & stringDescription /** stringdescription */ 
            );
            /**Sets  the string description 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            void SetStringDescription
            (
                const char * stringDescription /** stringdescription */ 
            );
            /**Returns  the double height 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleHeight
            (
            );
            /**Sets  the double height 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleHeight
            (
                double doubleHeight /** doubleheight */ 
            );
            /**Returns  the double diameter1 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleDiameter1
            (
            );
            /**Sets  the double diameter1 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleDiameter1
            (
                double doubleDiameter1 /** doublediameter1 */ 
            );
            /**Returns  the double diameter2 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleDiameter2
            (
            );
            /**Sets  the double diameter2 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleDiameter2
            (
                double doubleDiameter2 /** doublediameter2 */ 
            );
            /**Returns  the double anchor x 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleAnchorX
            (
            );
            /**Sets  the double anchor x 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleAnchorX
            (
                double doubleAnchorX /** doubleanchorx */ 
            );
            /**Returns  the double anchor y 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleAnchorY
            (
            );
            /**Sets  the double anchor y 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleAnchorY
            (
                double doubleAnchorY /** doubleanchory */ 
            );
            /**Returns  the double anchor z 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleAnchorZ
            (
            );
            /**Sets  the double anchor z 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleAnchorZ
            (
                double doubleAnchorZ /** doubleanchorz */ 
            );
            /**Returns  the double direction i 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleDirectionI
            (
            );
            /**Sets  the double direction i 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleDirectionI
            (
                double doubleDirectionI /** doubledirectioni */ 
            );
            /**Returns  the double direction j 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleDirectionJ
            (
            );
            /**Sets  the double direction j 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleDirectionJ
            (
                double doubleDirectionJ /** doubledirectionj */ 
            );
            /**Returns  the double direction k 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleDirectionK
            (
            );
            /**Sets  the double direction k 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleDirectionK
            (
                double doubleDirectionK /** doubledirectionk */ 
            );
            /**Returns  the enum size 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Vsa::PinFeatureBuilder::APIEnumSize EnumSize
            (
            );
            /**Sets  the enum size 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetEnumSize
            (
                NXOpen::Vsa::PinFeatureBuilder::APIEnumSize enumSize /** enumsize */ 
            );
            /**Returns  the double skewness size 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleSkewnessSize
            (
            );
            /**Sets  the double skewness size 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleSkewnessSize
            (
                double doubleSkewnessSize /** doubleskewnesssize */ 
            );
            /**Returns  the double kurtosis size 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleKurtosisSize
            (
            );
            /**Sets  the double kurtosis size 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleKurtosisSize
            (
                double doubleKurtosisSize /** doublekurtosissize */ 
            );
            /**Returns  the enum loc 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Vsa::PinFeatureBuilder::APIEnumLoc EnumLoc
            (
            );
            /**Sets  the enum loc 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetEnumLoc
            (
                NXOpen::Vsa::PinFeatureBuilder::APIEnumLoc enumLoc /** enumloc */ 
            );
            /**Returns  the double skewness loc 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleSkewnessLoc
            (
            );
            /**Sets  the double skewness loc 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleSkewnessLoc
            (
                double doubleSkewnessLoc /** doubleskewnessloc */ 
            );
            /**Returns  the double kurtosis loc 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleKurtosisLoc
            (
            );
            /**Sets  the double kurtosis loc 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleKurtosisLoc
            (
                double doubleKurtosisLoc /** doublekurtosisloc */ 
            );
            /**Returns  the enum form 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Vsa::PinFeatureBuilder::APIEnumForm EnumForm
            (
            );
            /**Sets  the enum form 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetEnumForm
            (
                NXOpen::Vsa::PinFeatureBuilder::APIEnumForm enumForm /** enumform */ 
            );
            /**Returns  the double skewness form 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleSkewnessForm
            (
            );
            /**Sets  the double skewness form 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleSkewnessForm
            (
                double doubleSkewnessForm /** doubleskewnessform */ 
            );
            /**Returns  the double kurtosis form 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleKurtosisForm
            (
            );
            /**Sets  the double kurtosis form 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleKurtosisForm
            (
                double doubleKurtosisForm /** doublekurtosisform */ 
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
