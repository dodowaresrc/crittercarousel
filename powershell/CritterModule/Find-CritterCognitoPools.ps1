function Find-CritterCognitoPools
{
    [CmdletBinding()]

    Param(
        [Parameter(Mandatory=$True)][string] $Region,
        [Hashtable] $Tags,
        [Hashtable] $ExtraTags
    )

    $ErrorActionPreference = "Stop"

    $Pools = New-Object Collections.ArrayList

    $AwsBaseArgs = @("cognito-idp", "list-user-pools", "--region", $Region, "--max-results", 10)

    $AwsArgs = $AwsBaseArgs

    while ($True)
    {
        $Result = Invoke-CritterAwsClient -AwsArgs $AwsArgs

        foreach ($Pool in $Result.UserPools)
        {
            $PoolDescription = Get-CritterCognitoPoolDescription -Region $Region -PoolId $Pool.Id

            $HasTags = Test-CritterItemHasTags `
                -Item $PoolDescription `
                -Tags $Tags `
                -ExtraTags $ExtraTags `
                -TagsProperty UserPoolTags `
                -SimpleTags

            if ($HasTags)
            {
                $Pools.Add($PoolDescription) | Out-Null
            }
        }

        if (-not $Result.NextToken)
        {
            break
        }

        $AwsArgs = $AwsBaseArgs + @("--starting-token", $Result.NextToken)
    }

    return $Pools
}
