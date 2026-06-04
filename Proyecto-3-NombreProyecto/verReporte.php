<?php
// Ruta completa al ejecutable de Python para que Apache pueda encontrarlo.
$python = 'C:\\Users\\usuario\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe';
$script1 = __DIR__ . DIRECTORY_SEPARATOR . 'Reportes.py';
$script2 = __DIR__ . DIRECTORY_SEPARATOR . 'Graficas.py';

// Ejecutar reporte de texto
$command1 = escapeshellarg($python) . ' ' . escapeshellarg($script1) . ' 2>&1';
$output = shell_exec($command1);

if ($output === null || trim($output) === '') {
    $output = "No se pudo ejecutar Reportes.py. Compruebe que Python y shell_exec estén disponibles.";
}

// Guardar resultado en archivo de texto
$archivo_salida = __DIR__ . DIRECTORY_SEPARATOR . 'reporte_resultado.txt';
file_put_contents($archivo_salida, $output);

// Ejecutar generación de gráficas
$command2 = escapeshellarg($python) . ' ' . escapeshellarg($script2) . ' 2>&1';
$salida_graficas = shell_exec($command2);

if ($salida_graficas === null || trim($salida_graficas) === '') {
    $salida_graficas = "No se pudieron generar las gráficas. Compruebe que matplotlib esté instalado y que Graficas.py funcione correctamente.";
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte de Ventas</title>
</head>
<body>
    <h1>Reporte de Ventas Tecnología</h1>
    <h2>Reporte en texto</h2>
    <pre><?php echo htmlspecialchars($output); ?></pre>
    <p><a href="reporte_resultado.txt">Descargar reporte como TXT</a></p>

    <h2>Gráficas</h2>
    <div>
        <img src="ventas_producto.png" alt="Ventas por producto" style="max-width: 100%; height: auto;">
    </div>
    <div>
        <img src="ventas_mes.png" alt="Ventas por mes" style="max-width: 100%; height: auto;">
    </div>
    <div>
        <img src="porcentaje_producto.png" alt="Porcentaje de ventas por producto" style="max-width: 100%; height: auto;">
    </div>
    <h3>Estado de generación de gráficas</h3>
    <pre><?php echo htmlspecialchars($salida_graficas); ?></pre>
</body>
</html>
