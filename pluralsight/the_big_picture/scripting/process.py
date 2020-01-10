import subprocess
pl = subprocess.Popen(['powershell', "-ExecutionPolicy", "unrestricted", "-nologo", "-command", "&{ Get-Module –ListAvailable }", '0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
print(pl.decode('utf-8'))