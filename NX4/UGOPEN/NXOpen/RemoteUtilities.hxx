#ifndef NXOpen_REMOTEUTILITIES_HXX_INCLUDED
#define NXOpen_REMOTEUTILITIES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     RemoteUtilities.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class RemoteUtilities;
    class _RemoteUtilitiesBuilder;
    /** This class is primarily designed for use in a remote session, and allows client
        applications to access resources on a remote server.

         <br>  

        Note that due to security considerations, this class is independent of the main
        @link Session Session@endlink . The server must explicitly export a RemoteUtilities
        object in order to allow clients to access the methods in this class. Application
        writers should be aware that this class will allow clients to delete and modify files
        on the server.  

         <br> 
    */
    class NXOPENCPPEXPORT RemoteUtilities : public TaggedObject
    {
        private: static RemoteUtilities *theRemoteUtilities;
        public: static RemoteUtilities *GetRemoteUtilities();
        private: friend class  _RemoteUtilitiesBuilder;
        protected: RemoteUtilities();
        /** Renames a file.  <br> License requirements : None */
        public: void RenameFile
        (
            const NXString & old_filename /** Old filename.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            const NXString & new_filename /** New filename.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Copies a file.  <br> License requirements : None */
        public: void CopyFile
        (
            const NXString & original_filename /** Original filename.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            const NXString & new_filename /** Newly copied filename.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Tests to see that a file exists  @return  True if the file exists  <br> License requirements : None */
        public: bool FileExists
        (
            const NXString & test_filename /** Filename to query   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Deletes a file. Note that if the file does not exist, this method returns without any errors.  <br> License requirements : None */
        public: void DeleteFile
        (
            const NXString & filename /** File to be deleted.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Returns true if a file exists, and is writable by the NX session.  @return  True if the file exists, and is writable  <br> License requirements : None */
        public: bool IsFileWritable
        (
            const NXString & filename /** File to be checked.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Sets a file's permissions to be writable by the NX session.  <br> License requirements : None */
        public: void SetFileWritable
        (
            const NXString & filename /** File to be checked.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            bool writable /** True to make the file writable, false to make it readonly */
        );
        /** Creates a directory.  <br> License requirements : None */
        public: void CreateDirectory
        (
            const NXString & dirname /** Name of new directory   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Deletes a directory.  <br> License requirements : None */
        public: void RemoveDirectory
        (
            const NXString & dirname /** Name of directory  to be deleted   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Gets the value of an environment variable.  @return  The value of the variable.  <br> License requirements : None */
        public: NXString GetEnvironmentVariable
        (
            const NXString & variable_name /** The environment variable   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
    };
}
#undef EXPORTLIBRARY
#endif