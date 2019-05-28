#check if QFIL.exe is running
$file = tasklist /FI "IMAGENAME eq QFIL.exe" /FO CSV

$containsWord = $file | %{$_ -match "QFIL.exe"}

if ($containsWord -contains $true) {
    Write-Host "QFIL is running!...Restart QFIL"
    taskkill /IM "QFIL.exe" /F
} else {
    Write-Host "Start QFIL"
}

start "C:\Program Files (x86)\Qualcomm\QPST\bin\QFIL.exe"
