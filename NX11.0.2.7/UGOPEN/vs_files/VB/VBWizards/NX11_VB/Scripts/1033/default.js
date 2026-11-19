//Upgraded to NX11 
function OnFinish(selProj, selObj)
{
	try
	{
		var strProjectPath = wizard.FindSymbol('PROJECT_PATH');
		var strProjectName = wizard.FindSymbol('PROJECT_NAME');
		var strProjTemplatePath = wizard.FindSymbol('TEMPLATES_PATH');//added
        
		var projType ='';
		var appType='';
		
		if (wizard.FindSymbol("DLL_APPLICATION"))
		    appType = "_dll";
		else
		    appType = "_exe";
		
		if (wizard.FindSymbol("VB_WIZARD_OPTION"))
		{
		    projType = "vbproj";
		    selProj = CreateVSProject(strProjectName, "." + projType, strProjectPath, strProjTemplatePath +"\\default" + appType + "." + projType);
		    AddFiles(selProj);
				    
		}
		else if (wizard.FindSymbol("CS_WIZARD_OPTION"))
		{
		    projType = "csproj";
		    selProj = CreateCSharpProject(strProjectName, strProjectPath, wizard.FindSymbol("WIZARD_NAME") + "\\Templates\\1033\\default" + appType + "." + projType);
		    
	    	var InfFile = CreateInfFile();
    		AddFilesToCSharpProject1(selProj , strProjectName, strProjectPath, InfFile, false );
    		
    		InfFile.Delete();
		}		
		
	}
	catch(e)
	{
		if (e.description.length != 0)
			SetErrorInfo(e); 
		return e.number;
	}
}

/******************************************************************************
    Description: Adds all the files to the project based on the Templates.inf file.
          oProj: Project object
 strProjectName: Project name
 strProjectPath: Project path
        InfFile: Templates.inf file object
    AddItemFile: Wether the wizard is invoked from the Add Item Dialog or not
******************************************************************************/
function AddFilesToCSharpProject1(oProj, strProjectName, strProjectPath, InfFile, AddItemFile)
{
    try
    {
        dte.SuppressUI = false;
        var projItems;
        if(AddItemFile)
            projItems = oProj;
        else
            projItems = oProj.ProjectItems;

        var strTemplatePath = wizard.FindSymbol("TEMPLATES_PATH");

        var strTpl = "";
        var strName = "";
        var strDependent = "";

        // if( Not a web project )
        if(strProjectPath.charAt(strProjectPath.length - 1) != "\\")
            strProjectPath += "\\"; 

        var strTextStream = InfFile.OpenAsTextStream(1, -2);
        
        while (!strTextStream.AtEndOfStream)
        {
            // Look to see if there is a dependency on another object.  The inf
            // file will show as:
            //
            // MasterObjectFileName;DependentObjectFileName
            strTpl = strTextStream.ReadLine();
            if (strTpl != "")
            {
                var sc = strTpl.indexOf(";");
                if (sc >= 0) 
                {
                    strName = strTpl.substr(0,sc);
                    if(sc < strTpl.length)
                    {
                        strDependent = strTpl.substr(sc+1);
                    }
                    else 
                    {
                        strDependent = "";
                    }
                }
                else
                {
                    strName = strTpl;
                    strDependent = "";
                }

                var strTarget = "";
                var strFile = "";
                strTarget = GetTargetName(strName, strProjectName);

                var fso;
                fso = new ActiveXObject("Scripting.FileSystemObject");
                var TemporaryFolder = 2;
                var tfolder = fso.GetSpecialFolder(TemporaryFolder);
                var strTempFolder = fso.GetAbsolutePathName(tfolder.Path);

                var strFile = strTempFolder + "\\" + fso.GetTempName();

                var strClassName = strTarget.split(".");
                wizard.AddSymbol("SAFE_CLASS_NAME", strClassName[0]);
                    wizard.AddSymbol("SAFE_ITEM_NAME", strClassName[0]);

                var strTemplate = strTemplatePath + "\\" + strName;
                var bCopyOnly = false;
                var strExt = strName.substr(strName.lastIndexOf("."));
                if(strExt==".bmp" || strExt==".ico" || strExt==".gif" || strExt==".rtf" || strExt==".css")
                    bCopyOnly = true;
                wizard.RenderTemplate(strTemplate, strFile, bCopyOnly, true);

                var projfile = projItems.AddFromTemplate(strFile, strTarget);
                SafeDeleteFile(fso, strFile);
                
                if(projfile)
                {
                    SetFileProperties(projfile, strName);
                    if (strDependent != "") 
                    {
                        // There is a dependent file.  Add this to the projfile we just added
                        var strDependentTarget = GetTargetName(strDependent, strProjectName);
                        
                        strTemplate = strTemplatePath + "\\" + strDependent;
                        strFile = strTempFolder + "\\" + fso.GetTempName();
                        strExt = strDependent.substr(strDependent.lastIndexOf("."));
                        if(strExt==".bmp" || strExt==".ico" || strExt==".gif" || strExt==".rtf" || strExt==".css")
                            bCopyOnly = true;
                        else
                            bCopyOnly = false;
                        wizard.RenderTemplate(strTemplate, strFile, bCopyOnly, true);
                        
                        var dependentItem = projfile.ProjectItems.AddFromTemplate(strFile, strDependentTarget);
                        SafeDeleteFile(fso, strFile);
                    }
                }

                var bOpen = false;
                if(AddItemFile)
                    bOpen = true;
                else if (DoOpenFile(strTarget))
                    bOpen = true;

                if(bOpen)
                {
                    var window = projfile.Open(vsViewKindPrimary);
                    window.visible = true;
                }
            }
        }
        strTextStream.Close();
    }
    catch(e)
    {
        strTextStream.Close();
        throw e;
    }
}

function GetTargetName(strName, strProjectName)
{
	try
	{
		// TODO: set the name of the rendered file based on the template filename
		var strTarget = strName;
		
		if (strName == 'readme.txt')
			strTarget = 'ReadMe.txt';

		if (strName == 'sample.txt')
			strTarget = 'Sample.txt';
		if (strName == 'vbfile.vb')
		    strTarget = "Module1" + ".vb";
		if (strName == 'csfile.cs')
		    strTarget = "Program" +".cs";
        if (strName == 'cppfile.cpp')
		    strTarget = 'CPPfile.cpp';


		return strTarget; 
	}
	catch(e)
	{
		throw e;
	}
}

/******************************************************************************
 Description: Delete file using file system object. 
******************************************************************************/
function SafeDeleteFile( fso, strFilespec )
{
    if (fso.FileExists(strFilespec))
    {
        var tmpFile = fso.GetFile(strFilespec);
        tmpFile.Delete();
    }
}

function DoOpenFile(strName) {
      var bOpen = false;
    
      switch (strName) {
            case "Program.cs":
                  bOpen = true;
                  break;
      }
      return bOpen; 
}
 
function SetFileProperties(oFileItem, strFileName) {
    if(strFileName == "Program.cs") {
        oFileItem.Properties("SubType").Value = "Code";
    }
}

function AddFiles(selProj)
{
    
    try
    {
        
        var strProjectPath = wizard.FindSymbol('PROJECT_PATH');
	    var strProjectName = wizard.FindSymbol('PROJECT_NAME');
	    var strProjTemplatePath = wizard.FindSymbol('TEMPLATES_PATH');//added
	    var strTemplateFile = strProjTemplatePath + "\\Templates.inf";
        
        var InfFile = CreateInfFile(strProjectPath);
        
    	
    	
	    var strTpl = '';
	    var strName = '';

	    var strTextStream = InfFile.OpenAsTextStream(1, -2);
	    while (!strTextStream.AtEndOfStream)
	    {
			    strTpl = strTextStream.ReadLine();
			    if (strTpl != '')
			    {
				    strName = strTpl;
				    var strTarget = GetTargetName(strName, strProjectName);
				    var strTemplate = strProjTemplatePath + '\\' + strTpl;
				    var strFile = strProjectPath + '\\' + strTarget;

				    var bCopyOnly = false;  //"true" will only copy the file from strTemplate to strTarget without rendering/adding to the project
				    var strExt = strName.substr(strName.lastIndexOf("."));
				    if(strExt==".bmp" || strExt==".ico" || strExt==".gif" || strExt==".rtf" || strExt==".css")
					    bCopyOnly = true;
	     		    var item = AddFileToVSProject(strTarget, selProj, selProj.ProjectItems, strTemplate, bCopyOnly);
			    }
	    }
	    strTextStream.Close();
	    InfFile.Delete();
	}
	catch(e)
	{
		if (e.description.length != 0)
			SetErrorInfo(e);
		return e.number
	}
	
}

function CreateInfFile()
{
	try
	{
		var fso, TemplatesFolder, TemplateFiles, strTemplate;
		
		var languageType ;
		
		fso = new ActiveXObject('Scripting.FileSystemObject');

		var TemporaryFolder = 2;
		var tfolder = fso.GetSpecialFolder(TemporaryFolder);
		var strTempFolder = tfolder.Drive + '\\' + tfolder.Name;

		var strWizTempFile = strTempFolder + "\\" + fso.GetTempName();

		var strTemplatePath = wizard.FindSymbol('TEMPLATES_PATH');
		var strInfFile = strTemplatePath + '\\Templates.inf';
		wizard.RenderTemplate(strInfFile, strWizTempFile);

		var WizTempFile = fso.GetFile(strWizTempFile);
		return WizTempFile;
	}
	catch(e)
	{
		throw e;
	}
}



