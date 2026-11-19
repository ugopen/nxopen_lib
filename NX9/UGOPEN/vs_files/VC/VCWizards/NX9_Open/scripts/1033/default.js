//@<DEL>@ TEXT ENCLOSED within delete markers will be REMOVED
// Default settings for the NX4 AppWizard for the WNTX64 platform - Initial release
// 26-Jul-2006  Linda Jeziorski - add definitions to default to x64 on wnti64 - NX5 ph 14 and NX4.0.3.2
// 01-Oct-2009  Linda Jeziorski Add _SECURE_SCL=0 flag for use in Studio 2008
// 19-Oct-10 Rhishikesh Jagtap Add entries for libnxopencpp*
// 28-Oct-10 Rhishikesh Jagtap Removed hardcoded entries of libnxopencpp*
// 03-Feb-2010 Linda Jeziorski Upgrade for NX8 to VS2010 - remove CLTool.Detect64BitPortabilityProblems
// 06-Aug-2012 Sudhir Pawar    ARCH9321: Added libufun_cae.lib and libugopenint_cae.lib
//TEXT ENCLOSED within delete markers will be REMOVED @<DEL>@

function OnFinish(selProj, selObj)
{
	try
	{
            var bodyTemplateFile = wizard.FindSymbol("TEMPLATES_PATH") + "\\" + "body_template.txt";
            var bodyTemplateText = wizard.RenderTemplateToString(bodyTemplateFile);
            wizard.AddSymbol("BODY_TEMPLATE", bodyTemplateText);

            var entryPointsTemplateFile = wizard.FindSymbol("TEMPLATES_PATH") + "\\" + "entry_points_template.txt";
            var entryPointsTemplateText = wizard.RenderTemplateToString(entryPointsTemplateFile);
            wizard.AddSymbol("ENTRY_POINTS_TEMPLATE", entryPointsTemplateText);

            var unloadOption = "UF_UNLOAD_UG_TERMINATE";
            if ( wizard.FindSymbol( "UNLOAD_IMMEDIATELY" ) )
            {
                unloadOption = "UF_UNLOAD_IMMEDIATELY";
            }
            else if ( wizard.FindSymbol( "UNLOAD_SEL_DIALOG" ) )
            {
                unloadOption = "UF_UNLOAD_SEL_DIALOG";
            }
            wizard.AddSymbol("UF_UNLOAD_OPTION", unloadOption);


            // Assign the project path and project name
            var strProjectPath = wizard.FindSymbol("PROJECT_PATH");
            var strProjectName = wizard.FindSymbol("PROJECT_NAME");

            // Create the Visual C++ project and call it "NXOpenProj"
            selProj = CreateProject(strProjectName, strProjectPath);
//            selProj.Object.Keyword = "NXOpenProj"

            // Add common and specific configurations to the project
            AddCommonConfig(selProj, strProjectName);
            AddSpecificConfig(selProj, strProjectName);
//            selProj.Object.keyword = "MFCDLLProj";

            //Set the project filters  
            SetupFilters(selProj);
            
            // Add files to the project from the project's Templates.inf file
            AddFilesToProjectWithInfFile(selProj, strProjectName);

           selProj.Object.Save();
	}
	catch(e)
	{
		if (e.description.length != 0)
			SetErrorInfo(e);
		return e.number
	}
}

function SetFileProperties(projfile, strName)
{
	return false;
}

function DoOpenFile(strTarget)
{
	return false;
}

function GetTargetName(strName, strProjectName, strResPath, strHelpPath)
{
	try
	{
		var strTarget = strName;
		if (strName.substr(0, 4) == "root")
		{
			var strlen = strName.length;
			if (strName == "root.ico" || strName == "root.rc2")
			{
				var strSafeProjectName = wizard.FindSymbol("SAFE_PROJECT_NAME");
				strSafeTarget = strSafeProjectName + strName.substr(4, strlen - 4);
				strTarget = strResPath + "\\" + strSafeTarget;
			}
                        else if (strName == "root.txt" )
                        {
                            strTarget = strProjectName;
                            if ( wizard.FindSymbol("CXX_LANGUAGE") )
                            {
                                strTarget += ".cpp";
                            }
                            else
                            {
                                strTarget += ".c";
                            }
                        }
			else
			{
				strTarget = strProjectName + strName.substr(4, strlen - 4);
			}
			return strTarget;
		}

		switch (strName)
		{
			case "readme.txt":
				strTarget = "ReadMe.txt";
				break;
			case "all.rc":
			case "dlgall.rc":
				strTarget = strProjectName + ".rc";
				break;
			case "dlgres.h":
			case "resource.h":
				strTarget = "Resource.h";
				break;
			default:
				break;
		}
		return strTarget; 
	}
	catch(e)
	{
		throw e;
	}
}

function AddSpecificConfig(proj, strProjectName)
{
	try
	{
		var isDllApp = wizard.FindSymbol("DLL_APPLICATION");
		var isOpenpp = wizard.FindSymbol("OPENPP_CALLS");
            var isCxx = wizard.FindSymbol("CXX_LANGUAGE");

        var appType;
        var appExtension;

        proj.ConfigurationManager.AddPlatform("x64", "Win32", true);

        if ( isDllApp )
        {
            appType = typeDynamicLibrary;
            appExtension = ".dll";
        }
        else
        {
            appType = typeApplication;
            appExtension = ".exe";
        }

        var linkLibs = "libufun.lib";
		    linkLibs += " libufun_cae.lib";

        if ( isCxx)
		{
			var wshell = new ActiveXObject("WScript.Shell")
			var libpath = wshell.ExpandEnvironmentStrings("%UGII_BASE_DIR%") + "\\ugopen";
			var Fo =new ActiveXObject("Scripting.FileSystemObject");
			var FSo = new Enumerator(Fo.GetFolder(libpath).Files);
			var nxopencppName = "libnxopencpp";
			for(; !FSo.atEnd(); FSo.moveNext())
			{
				if(FSo.item().name.match("^"+nxopencppName)==nxopencppName) //check if file name start with libnxopencpp
				if(FSo.item().name.slice(FSo.item().name.lastIndexOf(".")+1).toLowerCase() == "lib") //check if file has '.lib' as an extension
				{
					linkLibs =  linkLibs + " " + FSo.item().name;
				}
			}
        }
        
        if ( isDllApp )
        {
            linkLibs += " libugopenint.lib";
			linkLibs += " libugopenint_cae.lib";
			
            if ( isCxx)
                linkLibs += " libnxopenuicpp.lib";
        }
        if ( isOpenpp )
        {
            linkLibs += " libopenpp.lib";
            if ( isDllApp )
            {
                linkLibs += " libopenintpp.lib";
                
            }
            linkLibs += " libvmathpp.lib";

        }

        //=================================================================
        //  Debug Configuration
        //=================================================================
//LRJ - add x64
		var config = proj.Object.Configurations("Debug|x64");
		config.ConfigurationType = appType;
		config.CharacterSet      = charSetUnicode;
		config.useOfMfc          = useMfcStdWin;

		var CLTool = config.Tools("VCCLCompilerTool");
		var strDefines = GetPlatformDefine(config);
		strDefines += "_SECURE_SCL=0";
		if ( isDllApp )
                {
			strDefines += ";_USRDLL";
                }
                else
                {
                        strDefines += ";_CONSOLE";
                }

		CLTool.PreprocessorDefinitions = strDefines;

        config.UseOfMFC = useMfcDynamic;
        CLTool.RuntimeLibrary = rtMultiThreadedDLL;

		CLTool.TreatWChar_tAsBuiltInType = true;
		CLTool.DebugInformationFormat = debugEditAndContinue;
        CLTool.AdditionalIncludeDirectories = "$(UGII_BASE_DIR)\\ugopen";
        if ( isOpenpp )
        {
            CLTool.AdditionalIncludeDirectories += ";$(UGII_BASE_DIR)\\ugopenpp";
        }

        CLTool.RuntimeTypeInfo = 1;
        CLTool.UsePrecompiledHeader = pchNone;

//LRJ - change for X64 - add TargetMachine
		var LinkTool = config.Tools("VCLinkerTool");
                LinkTool.TargetMachine = machineAMD64;
		LinkTool.LinkIncremental = linkIncrementalYes;
		LinkTool.GenerateDebugInformation = true;
		LinkTool.OutputFile = "$(OutDir)/" + strProjectName + appExtension;
		if ( isDllApp )
            LinkTool.ImportLibrary = "$(OutDir)/" + strProjectName + ".lib";
        LinkTool.AdditionalLibraryDirectories = "$(UGII_BASE_DIR)\\ugopen";
        LinkTool.AdditionalDependencies       = linkLibs;
        LinkTool.SubSystem                    = subSystemConsole;
//LRJ - add following line for X64 definition
        dte.ExecuteCommand("Build.SolutionPlatforms", "x64");

        //=================================================================
        //  Release Configuration
        //=================================================================
//LRJ - add X64 definition to configuration line
		config = proj.Object.Configurations("Release|x64");
		config.ConfigurationType = appType;
		config.CharacterSet      = charSetUnicode;
		config.useOfMfc          = useMfcStdWin;

		CLTool = config.Tools("VCCLCompilerTool");
		strDefines = GetPlatformDefine(config);
		strDefines += "_SECURE_SCL=0";
		if ( isDllApp )
                {
			strDefines += ";_USRDLL";
                }
                else
                {
                        strDefines += ";_CONSOLE";
                }

		CLTool.PreprocessorDefinitions = strDefines;

        config.UseOfMFC = useMfcDynamic;
        CLTool.RuntimeLibrary = rtMultiThreadedDLL;

		CLTool.InlineFunctionExpansion = expandOnlyInline;
		CLTool.TreatWChar_tAsBuiltInType = true;
		CLTool.DebugInformationFormat = debugEnabled;

        CLTool.AdditionalIncludeDirectories += ";$(UGII_BASE_DIR)\\ugopen";
        if ( isOpenpp )
        {
            CLTool.AdditionalIncludeDirectories += ";$(UGII_BASE_DIR)\\ugopenpp";
        }

        CLTool.RuntimeTypeInfo = 1;
        CLTool.UsePrecompiledHeader = pchNone;

		LinkTool = config.Tools("VCLinkerTool");
//LRJ - add following line for X64 definition
                LinkTool.TargetMachine = machineAMD64;
		LinkTool.OutputFile = "$(OutDir)/" + strProjectName + appExtension;
		if ( isDllApp )
            LinkTool.ImportLibrary = "$(OutDir)/" + strProjectName + ".lib";
		LinkTool.GenerateDebugInformation = true;
		LinkTool.LinkIncremental = linkIncrementalNo;
        LinkTool.AdditionalLibraryDirectories += ";$(UGII_BASE_DIR)\\ugopen";
        LinkTool.AdditionalDependencies       = linkLibs;
        LinkTool.SubSystem                    = subSystemConsole;
//LRJ - add following line for X64 definition
        dte.ExecuteCommand("Build.SolutionPlatforms", "x64");
	}
	catch(e)
	{
		throw e;
	}
}

