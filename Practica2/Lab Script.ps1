function Get-StatusIP{
    param([Parameter(Mandatory)] [string]$IP,[Parameter()] [int]$intentos=2)
    $resultado = Test-Connection $IP -Quiet -Count $intentos
    if($resultado){
        Write-Host "La IP $IP esta activa"
    }
    else{
        Write-Host "La IP $IP NO esta activa"
    }
}
cls

do
    {
    #******** COMIENZO DEL SCRIPT ********
        Write-Host "*************************** BIENVENIDO ***************************"
        Write-Host " 1. Ver las USB's que se han conectado"
        Write-Host " 2. Ver las conexiones TCP "
        Write-Host " 3. Obtener el status de la IP"
        Write-Host "******************************************************************"
        $Opcion = Read-Host "Seleccione una opción: "

        switch($Opcion)
        {
            1
            {
                cls
                Get-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Enum\USBSTOR\*\* | select FriendlyName
                #$Ciclo = Read-Host "Desea volver al menú principal? [1]SI [2]NO"
                #cls
            }
            2
            {
                cls
                Get-NetTCPConnection |Select-Object -Property LocalAddress,RemoteAddress,State,OwningProcess|Format-Table -AutoSize
            }
            3
            {
                cls
                Get-StatusIP
            }
        }
$Ciclo = Read-Host "Desea volver al menú principal? [1]SI [2]NO"
cls

}while($Ciclo -eq "1")