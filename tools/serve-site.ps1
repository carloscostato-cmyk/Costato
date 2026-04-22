param(
  [int]$Port = 5500,
  [string]$RootPath = "."
)

$ErrorActionPreference = "Stop"

function Get-MimeType {
  param([string]$Extension)
  switch ($Extension.ToLowerInvariant()) {
    ".html" { "text/html; charset=utf-8" }
    ".css" { "text/css; charset=utf-8" }
    ".js" { "application/javascript; charset=utf-8" }
    ".json" { "application/json; charset=utf-8" }
    ".svg" { "image/svg+xml" }
    ".png" { "image/png" }
    ".jpg" { "image/jpeg" }
    ".jpeg" { "image/jpeg" }
    ".webp" { "image/webp" }
    ".ico" { "image/x-icon" }
    default { "application/octet-stream" }
  }
}

$resolvedRoot = (Resolve-Path -LiteralPath $RootPath).Path
$listener = New-Object System.Net.HttpListener
$prefix = "http://localhost:$Port/"
$listener.Prefixes.Add($prefix)
$listener.Start()

Write-Host "Servidor local ativo em $prefix"
Write-Host "Pasta raiz: $resolvedRoot"

while ($listener.IsListening) {
  try {
    $context = $listener.GetContext()
    $request = $context.Request
    $response = $context.Response

    $relativePath = [System.Uri]::UnescapeDataString($request.Url.AbsolutePath.TrimStart('/'))
    if ([string]::IsNullOrWhiteSpace($relativePath)) {
      $relativePath = "index.html"
    }

    $candidatePath = Join-Path $resolvedRoot $relativePath
    $fullPath = [System.IO.Path]::GetFullPath($candidatePath)

    if (-not $fullPath.StartsWith($resolvedRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
      $response.StatusCode = 403
      $response.Close()
      continue
    }

    if (Test-Path -LiteralPath $fullPath -PathType Container) {
      $fullPath = Join-Path $fullPath "index.html"
    }

    if (Test-Path -LiteralPath $fullPath -PathType Leaf) {
      $bytes = [System.IO.File]::ReadAllBytes($fullPath)
      $response.StatusCode = 200
      $response.ContentType = Get-MimeType -Extension ([System.IO.Path]::GetExtension($fullPath))
      $response.ContentLength64 = $bytes.Length
      $response.OutputStream.Write($bytes, 0, $bytes.Length)
      $response.OutputStream.Close()
    } else {
      $message = [System.Text.Encoding]::UTF8.GetBytes("404 - Arquivo nao encontrado")
      $response.StatusCode = 404
      $response.ContentType = "text/plain; charset=utf-8"
      $response.ContentLength64 = $message.Length
      $response.OutputStream.Write($message, 0, $message.Length)
      $response.OutputStream.Close()
    }
  } catch {
    Write-Host "Erro no servidor: $($_.Exception.Message)"
  }
}
