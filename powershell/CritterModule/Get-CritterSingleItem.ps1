function Get-CritterSingleItem
{
    Param(
        [Parameter(Mandatory=$True)][AllowNull()][PSCustomObject[]] $ItemList,
        [Parameter(Mandatory=$True)][string] $ItemType
    )

    if (-not $ItemList -or $ItemList.Count -eq 0)
    {
        throw "$ItemType not found for input filters"
    }
    elseif ($ItemList.Count -gt 1)
    {
        throw "$ItemType not unique for input filters"
    }
    else
    {
        return $ItemList[0]
    }
}
