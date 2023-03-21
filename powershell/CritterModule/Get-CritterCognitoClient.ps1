function Get-CritterCognitoClient
{
    [CmdletBinding()]

    Param(
        [Parameter(Mandatory=$True)][String] $Region,
        [Parameter(Mandatory=$True)][String] $UserPoolId,
        [string] $NameEquals,
        [string] $NamePattern
    )

    $ErrorActionPreference = "Stop"

    $Clients = Find-CritterCognitoClients -Region $Region -UserPoolId $UserPoolId -NameEquals $NameEquals -NamePattern $NamePattern

    return Get-CritterSingleItem -ItemList $Clients -ItemType "cognito client"
}
