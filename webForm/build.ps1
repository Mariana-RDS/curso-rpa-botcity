$exclude = @("venv", "webForm.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "webForm.zip" -Force