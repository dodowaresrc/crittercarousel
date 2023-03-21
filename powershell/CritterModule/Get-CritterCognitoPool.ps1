function Get-CritterCognitoPool
{
    Param(
        [Parameter(Mandatory=$True)][string] $Region,
        [Hashtable] $Tags,
        [Hashtable] $ExtraTags
    )

    $Pools = Find-CritterCognitoPools -Region $Region -Tags $Tags -ExtraTags $ExtraTags

    return Get-CritterSingleItem -ItemList $Pools -ItemType "cognito pool"
}
