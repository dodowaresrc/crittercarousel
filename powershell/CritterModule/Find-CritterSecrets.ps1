function Find-CritterSecrets
{
    [CmdletBinding()]

    Param(
        [Parameter(Mandatory=$True)][String] $Region,
        [Hashtable] $Tags,
        [Hashtable] $ExtraTags
    )

    $ErrorActionPreference = "Stop"

    $SecretList = New-Object Collections.ArrayList

    $BaseAwsArgs = @("secretsmanager", "list-secrets", "--region", $Region)

    $AwsArgs = $BaseAwsArgs

    while ($True)
    {
        $ListSecretsResult = Invoke-CritterAwsClient -AwsArgs $AwsArgs

        foreach ($Secret in $ListSecretsResult.SecretList)
        {
            if (Test-CritterItemHasTags -Item $Secret -Tags $Tags -ExtraTags $ExtraTags)
            {
                $SecretList.Add($Secret) | Out-Null
            }
        }

        if (-not $ListSecretsResult.NextToken) { break }

        $AwsArgs = $AwsBaseArgs + @("--starting-token", $Result.NextToken)
    }

    return $SecretList
}
