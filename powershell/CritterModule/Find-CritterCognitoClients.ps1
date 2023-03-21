function Find-CritterCognitoClients
{
    [CmdletBinding()]

    Param(
        [Parameter(Mandatory=$True)][String] $Region,
        [Parameter(Mandatory=$True)][String] $UserPoolId,
        [String] $NameEquals,
        [String] $NamePattern
    )

    $ErrorActionPreference = "Stop"

    $PoolClients = New-Object Collections.ArrayList

    $BaseAwsArgs = @("cognito-idp", "list-user-pool-clients", "--region", $Region, "--user-pool-id", $UserPoolId)

    $AwsArgs = $BaseAwsArgs

    while ($True)
    {
        $Result = Invoke-CritterAwsClient -AwsArgs $AwsArgs

        foreach ($Client in $Result.UserPoolClients)
        {
            if ($NameEquals -and $Client.Name -ne $NameEquals) { continue }

            if ($NamePattern -and -not ($Client.ClientName -like $NamePattern)) { continue }

            $PoolClients.Add($Client) | Out-Null
        }

        if (-not $Result.NextToken) { break }

        $AwsArgs = $BaseAwsArgs + @("--starting-token", $Result.NextToken)
    }

    return $PoolClients
}
