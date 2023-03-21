function Get-CritterAuthParameters
{
    Param(
        [Parameter(Mandatory=$True)][String] $Region,
        [Parameter(Mandatory=$True)][String] $Username,
        [Parameter(Mandatory=$True)][String] $ClientId,
        [Parameter(Mandatory=$True)][String] $ClientSecretId,
        [Parameter(Mandatory=$True)][String] $UserSecretId
    )

    $UserSecretValue = Get-CritterSecretValue -Region $BaseTags.Region -SecretId $UserSecretId

    $ClientSecretValue = Get-CritterSecretValue -Region $BaseTags.Region -SecretId $ClientSecretId

    $HmacKeyBytes = [Text.Encoding]::UTF8.GetBytes($ClientSecretValue.SecretString)

    $HmacDataBytes = [Text.Encoding]::UTF8.GetBytes($Username + $ClientId)

    $HmacDigest = [Security.Cryptography.HMACSHA256]::new($HmacKeyBytes).ComputeHash($HmacDataBytes)

    $HmacHash = [Convert]::ToBase64String($HmacDigest)

    return "USERNAME=$Username,PASSWORD=$($UserSecretValue.SecretString),SECRET_HASH=$HmacHash"
}
