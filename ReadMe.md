# UC Sports Attendance Marker


[![codeclimate][codeclimate-image]][codeclimate-url]
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

Ante la inminente lata de rellenar tremendo form para marcar asitencia de mi deportivo todas las clases <https://docs.google.com/forms/d/e/1FAIpQLScaPxGIKPDwFNlVJcKmRRy7JHDUKQExt1fbrsIMvhwxJWt3kA/viewform>, cree un bot que lo hace por mí, prerellenando datos del usuario y solo pregutando por semana y día para marcar.

## Pruebalo en tu PC

Sólo debes descargar este `.zip` en tu PC, descomprimirlo y ejecutar `mark_attendance.exe` (ojo que el archivo `chromedriver.exe` debe estar en la misma carpeta siempre).

[Descargar .zip][release]

## Para desarrolladores

Debes tener una version de python instalada en tu PC

### Setear el ambiente

```bash
python3 -m venv env
```

**Activar ambiente en Windows**

```bash
env\Scripts\activate
```

**Activar ambiente en Linux o MAC**

```bash
source env/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar


```bash
python3 main.py
```

## LICENSE

[MIT LICENSE](./LICENSE)

[release]: https://github.com/Baelfire18/uc-sports-attendance-marker/releases/latest/download/mark_attendance.zip

[codeclimate-image]: https://codeclimate.com/github/Baelfire18/uc-sports-attendance-marker/badges/gpa.svg
[codeclimate-url]: https://codeclimate.com/github/Baelfire18/uc-sports-attendance-marker
