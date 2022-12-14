#ifndef NXOpen_CAE_POSTCUSTOMHEADERLINES_HXX_INCLUDED
#define NXOpen_CAE_POSTCUSTOMHEADERLINES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostCustomHeaderLines.ja
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
#include <NXOpen/TransientObject.hxx>
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
        class PostCustomHeaderLines;
    }
    namespace CAE
    {
        class PostCustomHeaderLinesImpl;
        /**  @brief  This class has the information related to post legend custom header lines.
             

          <br> An instance of this class can not be created.   <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostCustomHeaderLines : public NXOpen::TransientObject
        {
            /** Header tokens used for customization */
            public: enum Token
            {
                TokenAbsoluteValue/** absolute value */ ,
                TokenBeamCsys/** beam csys */ ,
                TokenBeamSection/** beam section */ ,
                TokenCombination/** combination */ ,
                TokenComplex/** complex */ ,
                TokenComponent/** component */ ,
                TokenCrossSectionViewBeamInfo/** cross section view beam info */ ,
                TokenCsys/** csys */ ,
                TokenDeformation/** deformation */ ,
                TokenDisplayedMinMax/** displayed min max */ ,
                TokenFormula/** formula */ ,
                TokenIteration/** iteration */ ,
                TokenLoadcase/** loadcase */ ,
                TokenModelSummary/** model summary */ ,
                TokenPlyIdAndLayer/** ply id and layer */ ,
                TokenResult/** result */ ,
                TokenResultEnvironment/** result environment */ ,
                TokenResultMinMax/** result min max */ ,
                TokenScale/** scale */ ,
                TokenShellSection/** shell section */ ,
                TokenSolution/** solution */ ,
                TokenSubcase/** subcase */ ,
                TokenStreamlineData/** streamline data */ ,
                TokenUnit/** unit */ ,
                TokenUsertext/** usertext */ 
            };

             /** Container for token and usertext for legend header customization */
            public:
            struct HeaderToken
            {
                public: /** enumtoken */ NXOpen::CAE::PostCustomHeaderLines::Token EnumToken;
                public: /** usertext */ NXString UserText;
                public: HeaderToken() :
                    EnumToken((NXOpen::CAE::PostCustomHeaderLines::Token)0),
                    UserText()
                {
                }
                /** Constructor for the HeaderToken struct. */ 
                public: HeaderToken(NXOpen::CAE::PostCustomHeaderLines::Token enumTokenInitial /** enumtoken */ , 
                        const NXString &userTextInitial /** usertext */ ) :
                    EnumToken(enumTokenInitial),
                    UserText(userTextInitial)
                {
                }
            };

            private: PostCustomHeaderLinesImpl * m_postcustomheaderlines_impl;
            /// \cond NX_NO_DOC 
            public: explicit PostCustomHeaderLines(void *ptr);
            /// \endcond 
            /** Inserts a line to the custom header line list at the specified index 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void InsertNthLine
            (
                int index /** index */ ,
                const std::vector<NXOpen::CAE::PostCustomHeaderLines::HeaderToken> & line /** line */ 
            );
            /** Gets the number of lines in the custom header line list 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: int GetNumLines
            (
            );
            /** Gets the line at the specified index from the custom header line list 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: std::vector<NXOpen::CAE::PostCustomHeaderLines::HeaderToken> GetNthLine
            (
                int index /** index */ 
            );
            /** Erases the line at the specified index from the the custom header line list 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void DeleteNthLine
            (
                int index /** index */ 
            );
            /** Deletes all the lines of custom header line list 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void ClearLines
            (
            );
            /** Destroys the object 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~PostCustomHeaderLines();
        }; //lint !e1712 default constructor not defined for class  

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
