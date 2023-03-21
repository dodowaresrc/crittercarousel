function Test-CritterItemHasTags
{
    [CmdletBinding()]

    Param(
        [Parameter(Mandatory=$True)][PSCustomObject] $Item,
        [Hashtable] $Tags,
        [Hashtable] $ExtraTags,
        [string] $TagsProperty = "Tags",
        [switch] $SimpleTags
    )
    
    $ErrorActionPreference = "Stop"

    $AllTags = @{}

    if ($Tags) { foreach ($Key in $Tags.Keys) { $AllTags[$Key] = $Tags[$Key] } }

    if ($ExtraTags) { foreach ($Key in $ExtraTags.Keys) { $AllTags[$Key] = $ExtraTags[$Key] } }

    if ($SimpleTags)
    {
        foreach ($Key in $AllTags.Keys)
        {
            if ($Item.$TagsProperty.$Key -ne $AllTags[$Key])
            {
                return $False
            }
        }

        return $True
    }

    foreach ($InputTagKey in $AllTags.Keys)
    {
        $Found = $False

        foreach ($ItemTag in $Item.$TagsProperty)
        {
            if ($ItemTag.Key -eq $InputTagKey -and $ItemTag.Value -eq $AllTags[$InputTagKey])
            {
                $Found = $True
                break
            }
        }

        if (-not $Found)
        {
            return $False
        }
    }

    return $True
}
