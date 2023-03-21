function Get-CritterJsonWebToken
{
    [CmdletBinding()]

    Param(
        [Parameter(Mandatory=$True)][Hashtable] $BaseTags,
        [Parameter(Mandatory=$True)][string] $Username
    )

    $ErrorActionPreference = "Stop"

    $CognitoPool = Get-CritterCognitoPool -Region $BaseTags.Region -Tags $BaseTags

    $CognitoClient = Get-CritterCognitoClient `
        -Region $BaseTags.Region `
        -UserPoolId $CognitoPool.Id `
        -NamePattern "*-$($BaseTags.Color)"

    $UserSecret = Get-CritterSecret -Region $BaseTags.Region -Tags $BaseTags -ExtraTags @{Username=$Username}

    $ClientSecret = Get-CritterSecret -Region $BaseTags.Region -Tags $BaseTags -ExtraTags @{Username="cognitoclient"}

    $AuthParameters = Get-CritterAuthParameters `
        -Region $BaseTags.Region `
        -Username $Username `
        -ClientId $CognitoClient.ClientId `
        -ClientSecretId $ClientSecret.ARN `
        -UserSecretId $UserSecret.ARN

    $InitiateAuthArgs = @(
        "cognito-idp",
        "initiate-auth",
        "--auth-flow",
        "USER_PASSWORD_AUTH",
        "--region",
        $BaseTags.Region,
        "--client-id",
        $CognitoClient.ClientId,
        "--auth-parameters",
        $AuthParameters
    )

    $InitiateAuthResult = Invoke-CritterAwsClient -AwsArgs $InitiateAuthArgs

    return $InitiateAuthResult
}
