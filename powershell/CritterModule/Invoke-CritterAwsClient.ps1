function Invoke-CritterAwsClient
{
    [CmdletBinding()]

    Param(
        [Parameter(Mandatory=$True)][string[]] $AwsArgs
    )

    $ErrorActionPreference = "Stop"

    Write-Verbose "arguments:"

    foreach ($AwsArg in $AwsArgs)
    {
        Write-Verbose "    $AwsArg"
    }

    $Result = aws @($AwsArgs)

    Write-Verbose "output:"

    $Result -split "`n" | ForEach-Object {Write-Verbose "    $_"}

    return $Result | ConvertFrom-Json -Depth 100
}
