# 📰 Django News Portal

Un portal de noticias desarrollado con Django que permite gestionar categorías, artículos y usuarios. Este proyecto incluye funcionalidades como búsqueda de artículos, navegación responsiva y una interfaz amigable para dispositivos móviles.

---
## 🤝 Integrantes:

-Erik Campos
-Adrian Heredia
-Joel Gutierrez

## 🚀 Características

- **Gestión de usuarios**: Incluye un superusuario para administrar el contenido.
- **Categorías y artículos**: Organización de noticias por categorías.
- **Búsqueda avanzada**: 🔍 Filtra artículos por título y contenido.
- **Diseño responsivo**: 📱 Optimizado para dispositivos móviles.
- **Interfaz amigable**: Navegación intuitiva y moderna.

---

## 📂 Estructura del Proyecto

```
news_portal/
├── src/
│   ├── news/
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── seed_data.py  # Script para poblar la base de datos
│   │   ├── templates/
│   │   │   └── news/
│   │   │       ├── base.html  # Plantilla base
│   │   │       ├── home.html  # Página principal
│   │   │       └── article_detail.html  # Detalle de artículos
│   │   ├── urls.py  # Rutas del proyecto
│   │   ├── views.py  # Vistas del proyecto
│   │   └── models.py  # Modelos de datos
└── README.md  # Documentación del proyecto
```

---

## 🛠️ Instalación y Configuración

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/usuario/news_portal.git
   cd news_portal/src
   ```

2. **Crear y activar un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Migrar la base de datos**:
   ```bash
   python manage.py migrate
   ```

5. **Poblar la base de datos con datos de ejemplo**:
   ```bash
   python manage.py seed_data
   ```

6. **Iniciar el servidor**:
   ```bash
   python manage.py runserver
   ```

---

## 🌐 Uso

1. Accede al portal en [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
2. Usa la barra de navegación para explorar categorías y buscar artículos.
3. Inicia sesión como administrador en [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) con las credenciales:
   - **Usuario**: `admin`
   - **Contraseña**: `admin123`

---

## 📋 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un pull request para sugerir mejoras.




