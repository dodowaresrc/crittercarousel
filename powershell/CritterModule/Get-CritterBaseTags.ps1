function Get-CritterBaseTags
{
    [CmdletBinding()]

    Param(
        [Parameter(Mandatory=$True)][string] $Color,
        [Parameter(Mandatory=$True)][string] $Region,
        [string] $Component = "api",
        [string] $Environment = "development",
        [string] $Project = "crittercarousel"
    )

    $ErrorActionPreference = "Stop"

    $BaseTags = @{
        Color = $Color
        Component = $Component
        Environment = $Environment
        Project = $Project
        Region = $Region
    }

    return $BaseTags
}
