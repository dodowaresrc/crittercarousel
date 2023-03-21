function Get-CritterCognitoPoolDescription
{
    [CmdletBinding()]

    Param(
        [Parameter(Mandatory=$True)] $Region,
        [Parameter(Mandatory=$True)] $PoolId
    )

    $ErrorActionPreference = "Stop"

    $AwsArgs = @(
        "cognito-idp",
        "describe-user-pool",
        "--region",
        $Region,
        "--user-pool-id",
        $PoolId
    )

    $Result = Invoke-CritterAwsClient -AwsArgs $AwsArgs

    $Result = $Result.UserPool

    return $Result
}
