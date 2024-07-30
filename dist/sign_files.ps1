# 서명할 파일들이 있는 디렉터리 경로
$directoryPath = "C:\Users\ykim513\python\KMPNS\Mailroom\dist\Manager\_internal"

# 인증서 파일 경로와 비밀번호
$certPath = "C:\Users\ykim513\python\KMPNS\Mailroom\dist\digital_signature\digital_signature\Robotic&AILab.pfx"
$certPassword = "G4QS836ncUGOYO9UC;J+-yd:cT57vR"

# 타임스탬프 URL
$timestampUrl = "http://timestamp.digicert.com"

# 서명할 파일 확장자
$fileExtension = "*.dll"

# Signtool 경로
$signtoolPath = "C:\Users\ykim513\python\KMPNS\Mailroom\dist\digital_signature\digital_signature\signtool.exe"

# 디렉터리 내의 모든 파일을 검색하여 서명
Get-ChildItem -Path $directoryPath -Filter $fileExtension -Recurse | ForEach-Object {
    $filePath = $_.FullName
    & $signtoolPath sign /f $certPath /p $certPassword /t $timestampUrl $filePath
}
