function Get-CritterSecretValue
{
    [CmdletBinding()]

    Param(
        [Parameter(Mandatory=$True)][String] $Region,
        [Parameter(Mandatory=$True)][String] $SecretId
    )

    $ErrorActionPreference = "Stop"

    $AwsArgs = @("secretsmanager", "get-secret-value", "--region", $Region, "--secret-id", $SecretId)

    $AwsResult = Invoke-CritterAwsClient -AwsArgs $AwsArgs

    return $AwsResult
}
