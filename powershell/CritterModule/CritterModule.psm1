$FileList = Get-ChildItem $PSScriptRoot | Where-Object {$_.Name.EndsWith(".ps1")}

foreach ($File in $FileList)
{
    $FunctionName = $File.Name -replace ".ps1", ""
    . $File.FullName
    Export-ModuleMember -Function $FunctionName
}
