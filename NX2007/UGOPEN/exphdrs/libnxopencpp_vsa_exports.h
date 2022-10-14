/*=============================================================================
File description:

    This contains the export symbols for the LIBNXOPENCPP_VSA library.

    Documentation at http://cipgweb/do/devops_nx:relnotes:autogenerated_export_headers

    Autogenerated by //nx/nx1899/build/tools/be/GenerateExportsHeaders.pm#3

==============================================================================*/
#ifndef LIBNXOPENCPP_VSA_EXPORTS_H_INCLUDED
#define LIBNXOPENCPP_VSA_EXPORTS_H_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

#ifdef __lint
#   pragma uginclude only_in_error "libnxopencpp_vsa_main.c*", "*.h", "*.hxx";
#endif

#if defined(DEFINE_LIBNXOPENCPP_VSA_EXPORTS)
#   if defined(__lint)
#       define NXOPENCPP_VSAEXPORT       __export(nxopencpp_vsa)
#       define NXOPENCPP_VSAGLOBAL       extern __global(nxopencpp_vsa)
#       define NXOPENCPP_VSAPRIVATE      extern __private(nxopencpp_vsa)
#   elif defined(_WIN32)
#       define NXOPENCPP_VSAEXPORT       __declspec(dllexport)
#       define NXOPENCPP_VSAGLOBAL       extern __declspec(dllexport)
#       define NXOPENCPP_VSAPRIVATE      extern
#   elif __GNUC__ >= 4
#       define NXOPENCPP_VSAEXPORT       __attribute__ ((visibility("default")))
#       define NXOPENCPP_VSAGLOBAL       extern __attribute__ ((visibility("default")))
#       define NXOPENCPP_VSAPRIVATE      extern __attribute__ ((visibility("hidden")))
#   elif __SUNPRO_CC >= 0x5130
#       define NXOPENCPP_VSAEXPORT       __attribute__ ((visibility("default")))
#       define NXOPENCPP_VSAGLOBAL       extern __attribute__ ((visibility("default")))
#       define NXOPENCPP_VSAPRIVATE      extern __attribute__ ((visibility("hidden")))
#   elif __IBMCPP__ >= 1320
#       define NXOPENCPP_VSAEXPORT       __attribute__ ((visibility("default")))
#       define NXOPENCPP_VSAGLOBAL       extern __attribute__ ((visibility("default")))
#       define NXOPENCPP_VSAPRIVATE      extern __attribute__ ((visibility("hidden")))
#   else
#       define NXOPENCPP_VSAEXPORT
#       define NXOPENCPP_VSAGLOBAL       extern
#       define NXOPENCPP_VSAPRIVATE      extern
#   endif
#else
#   if defined(__lint)
#       define NXOPENCPP_VSAEXPORT       __export(nxopencpp_vsa)
#       define NXOPENCPP_VSAGLOBAL       extern __global(nxopencpp_vsa)
#   elif defined(_WIN32) && !defined(WNT_STATIC_LINK)
#       define NXOPENCPP_VSAEXPORT       __declspec(dllimport)
#       define NXOPENCPP_VSAGLOBAL       extern __declspec(dllimport)
#   else
#       define NXOPENCPP_VSAEXPORT
#       define NXOPENCPP_VSAGLOBAL       extern
#   endif
#endif

#endif  /* LIBNXOPENCPP_VSA_EXPORTS_H_INCLUDED */