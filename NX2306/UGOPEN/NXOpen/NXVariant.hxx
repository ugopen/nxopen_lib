/*******************************************************************************
               Copyright (c) 2022 Siemens
                      Unpublished - All Rights Reserved


*******************************************************************************/

#pragma once


#include <variant>
#include <vector>
#include <NXOpen/NXString.hxx>

#if ((defined(_MSVC_LANG) && _MSVC_LANG >= 201703L) || __cplusplus >= 201703L)

namespace NXOpen
{
    class TaggedObject;

    /**  @brief An NXVariantEntry represents possible arguments to a NXOpen method that can take in variants.
    
       <br>
       Be aware that the following code block below will assign a bool instead of NXOpen::NXString
       <br>
      \code{.cpp}
      std::vector<NXOpen::NXVariant> args;
      args.push_back("A String Argument");
      \endcode
      <br>
      This is due to how C++ deals with the conversion.  As char * to bool is a built-in conversion and is given priority over the user-defined conversion of const char * to NXString.
      To resolve this, either expliclity use NXString or denote the literal as string.
      <br>
      \code{.cpp}
      using namespace std::string_literals;


      std::vector<NXOpen::NXVariant> args;
      args.push_back(NXOpen::NXString("A String Argument"));
      args.push_back("A different String Argument"s);
      \endcode
 
    */
    using NXVariantEntry = std::variant <std::monostate, int, double, bool, NXOpen::TaggedObject*, NXOpen::NXString>;
    
    /**  @brief An type representing possible arguments to a NXOpen method that can take in variants.
    
    This can be a single NXVariantEntry or an array of them.*/
    using NXVariant = std::variant <std::monostate, NXVariantEntry, std::vector<NXVariantEntry>>;

}

#endif

