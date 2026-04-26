# Ndownloader

Una aplicación de escritorio para Windows moderna, minimalista y robusta para descargar videos y audio de diversas fuentes utilizando `yt-dlp` y `ffmpeg`.

![Logo de Ndownloader](assets/logo.png)

## Características
- **UI Premium Minimalista**: Interfaz ultra limpia con modos Oscuro y Claro puros.
- **Soporte Multilingüe**: Cambia entre español e inglés al instante.
- **Soporte de Miniaturas**: Mira exactamente lo que estás descargando.
- **Cola Organizada**: Pestañas separadas para Cola, Completados y Errores.
- **Soporte de Varios Formatos**: HLS (.m3u8), DASH (.mpd), MP4, WebM, MKV, MP3, etc.
- **Soporte de Plataformas**: YouTube, Vimeo, Twitter y más de 1000 sitios adicionales.
- **Detección de Portapapeles**: Detecta automáticamente URLs copiadas al portapapeles.
- **Control de Calidad**: Selecciona entre Mejor, 1080p, 720p o 480p.
- **FFmpeg Interno**: No requiere instalación en el sistema (incluido con la app).

## Instalación

### Para Usuarios
1. Descarga el último `Ndownloader.exe` desde la página de Lanzamientos.
2. ¡Ejecútalo y disfruta!

### Para Desarrolladores
1. Clona el repositorio.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```bash
   python main.py
   ```

## Compilación desde el código fuente
Para crear un ejecutable `.exe` independiente:
```bash
python build_exe.py
```

## Tecnologías
- **Python 3.10+**
- **PyQt6** (GUI)
- **yt-dlp** (Motor de descarga)
- **FFmpeg** (Procesamiento de medios)

---
© 2026 Shoropio Corporation. Todos los derechos reservados.

