#ifndef NXOpen_VSA_TABFEATUREBUILDER_HXX_INCLUDED
#define NXOpen_VSA_TABFEATUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Vsa_TabFeatureBuilder.ja
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
        class TabFeatureBuilder;
    }
    class Builder;
    namespace Vsa
    {
        class _TabFeatureBuilderBuilder;
        class TabFeatureBuilderImpl;
        /**
            
        	 <br> To create a new instance of this class, use @link NXOpen::Vsa::VsaManager::CreateSlotFeatureBuilder  NXOpen::Vsa::VsaManager::CreateSlotFeatureBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        DoubleKurtosisForm </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DoubleKurtosisLoc </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DoubleKurtosisSize </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DoubleSkewnessForm </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DoubleSkewnessLoc </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DoubleSkewnessSize </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        EnumForm </td> <td> 
         
        Normal </td> </tr> 

        <tr><td> 
         
        EnumLoc </td> <td> 
         
        Normal </td> </tr> 

        <tr><td> 
         
        EnumSize </td> <td> 
         
        Normal </td> </tr> 

        </table>  

         <br>  Usable only on Windows <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_VSAEXPORT  TabFeatureBuilder : public NXOpen::Builder
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

            private: TabFeatureBuilderImpl * m_tabfeaturebuilder_impl;
            private: friend class  _TabFeatureBuilderBuilder;
            protected: TabFeatureBuilder();
            public: ~TabFeatureBuilder();
            /**Returns  the property represents tab feature name. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString StringName
            (
            );
            /**Sets  the property represents tab feature name. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetStringName
            (
                const NXString & stringName /** stringname */ 
            );
            /**Sets  the property represents tab feature name. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            void SetStringName
            (
                const char * stringName /** stringname */ 
            );
            /**Returns  the property represents tab feature discription. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString StringDescription
            (
            );
            /**Sets  the property represents tab feature discription. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetStringDescription
            (
                const NXString & stringDescription /** stringdescription */ 
            );
            /**Sets  the property represents tab feature discription. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            void SetStringDescription
            (
                const char * stringDescription /** stringdescription */ 
            );
            /**Returns  the property represents length of tab. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleLength
            (
            );
            /**Sets  the property represents length of tab. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleLength
            (
                double distance /** distance */ 
            );
            /**Returns  the property represents depth of tab. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleDepth
            (
            );
            /**Sets  the property represents depth of tab. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleDepth
            (
                double height /** height */ 
            );
            /**Returns  the property represents width of tab. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleWidth
            (
            );
            /**Sets  the property represents width of tab. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleWidth
            (
                double height /** height */ 
            );
            /**Returns  the property represents X value of anchor. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleAnchorX
            (
            );
            /**Sets  the property represents X value of anchor. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleAnchorX
            (
                double doubleAnchorX /** doubleanchorx */ 
            );
            /**Returns  the property represents Y value of anchor. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleAnchorY
            (
            );
            /**Sets  the property represents Y value of anchor. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleAnchorY
            (
                double doubleAnchorY /** doubleanchory */ 
            );
            /**Returns  the property represents Z value of anchor. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleAnchorZ
            (
            );
            /**Sets  the property represents Z value of anchor. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleAnchorZ
            (
                double doubleAnchorZ /** doubleanchorz */ 
            );
            /**Returns  the property represents X value of normal. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleDirectionI
            (
            );
            /**Sets  the property represents X value of normal. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleDirectionI
            (
                double doubleDirectionI /** doubledirectioni */ 
            );
            /**Returns  the property represents Y value of normal. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleDirectionJ
            (
            );
            /**Sets  the property represents Y value of normal. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleDirectionJ
            (
                double doubleDirectionJ /** doubledirectionj */ 
            );
            /**Returns  the property represents Z value of normal. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleDirectionK
            (
            );
            /**Sets  the property represents Z value of normal. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleDirectionK
            (
                double doubleDirectionK /** doubledirectionk */ 
            );
            /**Returns  the property represents X value of length vector. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleLengthVectorI
            (
            );
            /**Sets  the property represents X value of length vector. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleLengthVectorI
            (
                double doubleLengthVectorI /** doublelengthvectori */ 
            );
            /**Returns  the property represents Y value of length vector. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleLengthVectorJ
            (
            );
            /**Sets  the property represents Y value of length vector. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleLengthVectorJ
            (
                double doubleLengthVectorJ /** doublelengthvectorj */ 
            );
            /**Returns  the property represents Z value of length vector. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleLengthVectorK
            (
            );
            /**Sets  the property represents Z value of length vector. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleLengthVectorK
            (
                double doubleLengthVectorK /** doublelengthvectork */ 
            );
            /**Returns  the property represents value of swap length and depth. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool ToggleSwap
            (
            );
            /**Sets  the property represents value of swap length and depth. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetToggleSwap
            (
                bool boolSwap /** boolswap */ 
            );
            /**Returns  the property represents Size distribution type. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Vsa::TabFeatureBuilder::APIEnumSize EnumSize
            (
            );
            /**Sets  the property represents Size distribution type. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetEnumSize
            (
                NXOpen::Vsa::TabFeatureBuilder::APIEnumSize enumSize /** enumsize */ 
            );
            /**Returns  the property represents Size distribution Skewness. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleSkewnessSize
            (
            );
            /**Sets  the property represents Size distribution Skewness. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleSkewnessSize
            (
                double doubleSkewnessSize /** doubleskewnesssize */ 
            );
            /**Returns  the property represents Size distribution Kurtosis. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleKurtosisSize
            (
            );
            /**Sets  the property represents Size distribution Kurtosis. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleKurtosisSize
            (
                double doubleKurtosisSize /** doublekurtosissize */ 
            );
            /**Returns  the property represents Loc distribution type. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Vsa::TabFeatureBuilder::APIEnumLoc EnumLoc
            (
            );
            /**Sets  the property represents Loc distribution type. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetEnumLoc
            (
                NXOpen::Vsa::TabFeatureBuilder::APIEnumLoc enumLoc /** enumloc */ 
            );
            /**Returns  the property represents Loc distribution Skewness. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleSkewnessLoc
            (
            );
            /**Sets  the property represents Loc distribution Skewness. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleSkewnessLoc
            (
                double doubleSkewnessLoc /** doubleskewnessloc */ 
            );
            /**Returns  the property represents Loc distribution Kurtosis. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleKurtosisLoc
            (
            );
            /**Sets  the property represents Loc distribution Kurtosis. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleKurtosisLoc
            (
                double doubleKurtosisLoc /** doublekurtosisloc */ 
            );
            /**Returns  the property represents Form distribution type. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Vsa::TabFeatureBuilder::APIEnumForm EnumForm
            (
            );
            /**Sets  the property represents Form distribution type. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetEnumForm
            (
                NXOpen::Vsa::TabFeatureBuilder::APIEnumForm enumForm /** enumform */ 
            );
            /**Returns  the property represents Form distribution Skewness. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleSkewnessForm
            (
            );
            /**Sets  the property represents Form distribution Skewness. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_vsa_build (" Building VSA model") */
            public: void SetDoubleSkewnessForm
            (
                double doubleSkewnessForm /** doubleskewnessform */ 
            );
            /**Returns  the property represents Form distribution Kurtosis. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double DoubleKurtosisForm
            (
            );
            /**Sets  the property represents Form distribution Kurtosis. 
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
