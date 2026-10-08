# youtube_women_tech

Script en Python que busca en YouTube vídeos sobre mujeres en tecnología y guarda título, canal, visualizaciones, me gusta y fecha de publicación en `resultados.csv` y `resultados.json`.

## Requisitos

- Python 3
- Una clave de la [YouTube Data API v3](https://console.cloud.google.com/apis/library/youtube.googleapis.com)

## Instalación

```bash
pip install -r requirements.txt
```

## Clave de la API

La clave no se guarda en el repositorio. Créala en Google Cloud Console, activa YouTube Data API v3 y asígnala a la variable de entorno `YOUTUBE_API_KEY`.

En PowerShell, solo para la sesión actual:

```powershell
$env:YOUTUBE_API_KEY = "tu_clave"
```

En cmd:

```cmd
set YOUTUBE_API_KEY=tu_clave
```

En bash:

```bash
export YOUTUBE_API_KEY="tu_clave"
```

Puedes copiar `.env.example` a `.env` como recordatorio local. `.env` está en `.gitignore` y este proyecto no lo carga solo: la variable tiene que estar definida en el entorno antes de ejecutar el script.

Si la variable no existe o está vacía, el programa se detiene con un error y no llama a la API.

## Uso

Las búsquedas y el número de resultados por palabra están en `config.py` (`KEYWORDS` y `MAX_RESULTS`, máximo 50 por consulta).

```bash
python main.py
```

El script recorre cada palabra clave, pide los detalles de los vídeos y escribe:

- `resultados.csv`
- `resultados.json`

## Estructura

- `main.py`: recorre las palabras clave y guarda los resultados
- `youtube_api.py`: cliente de YouTube Data API v3
- `config.py`: palabras clave y límite de resultados
- `utils.py`: exportación a CSV/JSON y formato de fechas
