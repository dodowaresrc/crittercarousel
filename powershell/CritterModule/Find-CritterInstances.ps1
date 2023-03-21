function Find-CritterInstances
{
    [CmdletBinding()]

    Param(
        [Parameter(Mandatory=$True)][String] $Region,
        [Hashtable] $Tags
    )

    $ErrorActionPreference = "Stop"

    $AwsArgs = @("ec2", "describe-instances", "--region", $Region)

    $AwsResult = Invoke-CritterAwsClient -AwsArgs $AwsArgs

    $InstanceList = New-Object Collections.ArrayList

    foreach ($Reservation in $AwsResult.Reservations)
    {
        foreach ($Instance in $Reservation.Instances)
        {
            if (Test-CritterItemHasTags -Item $Instance -Tags $BaseTags)
            {
                $InstanceList.add($Instance) | Out-Null
            }
        }
    }

    return $InstanceList
}
