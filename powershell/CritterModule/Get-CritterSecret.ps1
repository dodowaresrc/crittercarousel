function Get-CritterSecret
{
    [CmdletBinding()]

    Param(
        [Parameter(Mandatory=$True)][String] $Region,
        [Hashtable] $Tags,
        [Hashtable] $ExtraTags
    )

    $ErrorActionPreference = "Stop"

    $Secrets = Find-CritterSecrets -Region $Region -Tags $AllTags -ExtraTags $ExtraTags

    return Get-CritterSingleItem -ItemList $Secrets -ItemType "secret"
}
