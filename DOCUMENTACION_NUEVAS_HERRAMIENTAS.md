# NUEVAS HERRAMIENTAS APLICADAS AL PROYECTO
## Sistema Web de Gestión Operativa, Inventario y Ventas para "Mecánica Yeyko"

**Proyecto de Grado / Desarrollo Tecnológico**  
**Postulante:** Ivan Chiri Lupinta  
**Entorno:** Versión Optimizada (`mecanica yeyko optimisado`)  

---

## Índice de Contenidos

1. [Herramienta Devin (Cognition Labs)](#1-herramienta-devin-cognition-labs)
   - [1.1. Enlaces Oficiales y Beneficios del Vibeathon](#11-enlaces-oficiales-y-beneficios-del-vibeathon)
   - [1.2. ¿Cómo funciona Devin?](#12-cómo-funciona-devin)
   - [1.3. Beneficios](#13-beneficios)
   - [1.4. Potencialidades](#14-potencialidades)
   - [1.5. Desventajas y Limitaciones](#15-desventajas-y-limitaciones)
   - [1.6. Aplicación Práctica en Mecánica Yeyko](#16-aplicación-práctica-en-mecánica-yeyko)
2. [Herramienta Slack (Colaboración Técnica y Alertas)](#2-herramienta-slack-colaboración-técnica-y-alertas)
   - [2.1. Enlaces Oficiales y Comunidad](#21-enlaces-oficiales-y-comunidad)
   - [2.2. ¿Cómo funciona Slack?](#22-cómo-funciona-slack)
   - [2.3. Beneficios](#23-beneficios)
   - [2.4. Potencialidades](#24-potencialidades)
   - [2.5. Desventajas y Limitaciones](#25-desventajas-y-limitaciones)
   - [2.6. Aplicación Práctica en Mecánica Yeyko](#26-aplicación-práctica-en-mecánica-yeyko)
3. [Herramienta Vercel (Despliegue Serverless & CDN Edge)](#3-herramienta-vercel-despliegue-serverless--cdn-edge)
   - [3.1. Enlaces Oficiales](#31-enlaces-oficiales)
   - [3.2. ¿Cómo funciona Vercel?](#32-cómo-funciona-vercel)
   - [3.3. Beneficios](#33-beneficios)
   - [3.4. Potencialidades](#34-potencialidades)
   - [3.5. Desventajas y Limitaciones](#35-desventajas-y-limitaciones)
   - [3.6. Aplicación Práctica en Mecánica Yeyko](#36-aplicación-práctica-en-mecánica-yeyko)
4. [Herramienta Comentera (Feedback Visual & QA Interactivo)](#4-herramienta-comentera-feedback-visual--qa-interactivo)
   - [4.1. Enlaces Oficiales](#41-enlaces-oficiales)
   - [4.2. ¿Cómo funciona Comentera?](#42-cómo-funciona-comentera)
   - [4.3. Beneficios](#43-beneficios)
   - [4.4. Potencialidades](#44-potencialidades)
   - [4.5. Desventajas y Limitaciones](#45-desventajas-y-limitaciones)
   - [4.6. Aplicación Práctica en Mecánica Yeyko](#46-aplicación-práctica-en-mecánica-yeyko)
5. [Gráficos 3D & Simulación Interactiva (OpenAI GPT-6 Astra / Three.js / WebGL)](#5-gráficos-3d--simulación-interactiva-openai-gpt-6-astra--threejs--webgl)
   - [5.1. Enlaces Oficiales y Demostración](#51-enlaces-oficiales-y-demostración)
   - [5.2. ¿Cómo funciona la Tecnología 3D y Razonamiento Multimodal?](#52-cómo-funciona-la-tecnología-3d-y-razonamiento-multimodal)
   - [5.3. Beneficios](#53-beneficios)
   - [5.4. Potencialidades](#54-potencialidades)
   - [5.5. Desventajas y Limitaciones](#55-desventajas-y-limitaciones)
   - [5.6. Aplicación Práctica en Mecánica Yeyko](#56-aplicación-práctica-en-mecánica-yeyko)
6. [Enlaces Principales del Proyecto](#6-enlaces-principales-del-proyecto)

---

## 1. Herramienta Devin (Cognition Labs)

### 1.1. Enlaces Oficiales y Beneficios del Vibeathon
- **Página oficial de Devin:** [https://devin.ai/](https://devin.ai/)
- **Devin en X (Twitter):** [https://x.com/DevinAI](https://x.com/DevinAI)
- **Ticket gratuito Devin + Supabase ($20 USD):** [https://www.trydevin.ai/devin-x-supabase-santa-cruz-vibeathon](https://www.trydevin.ai/devin-x-supabase-santa-cruz-vibeathon)

Desarrollado por Cognition Labs, Devin es catalogado como el primer ingeniero de software autónomo impulsado por Inteligencia Artificial. A diferencia de los asistentes de código tradicionales (como GitHub Copilot o autocompletadores sintácticos que solo sugieren fragmentos de código mientras el usuario escribe), Devin opera como un agente autónomo de ingeniería capaz de formular planes de trabajo, ejecutar comandos en terminal, gestionar repositorios, ejecutar pruebas y depurar errores de software de extremo a extremo sin intervención continua.

### 1.2. ¿Cómo funciona Devin?
Devin opera dentro de un entorno virtual seguro y aislado (*sandbox* en la nube) equipado con las herramientas fundamentales de un programador real:
1. **Terminal / Shell:** Para instalar librerías (`pip install`, `npm install`), correr servidores de prueba, migrar esquemas de bases de datos y ejecutar suites de tests.
2. **Editor de código autónomo:** Capaz de navegar por la totalidad del árbol de archivos del proyecto, leer contextos cruzados, refactorizar módulos enteros y resolver dependencias.
3. **Navegador web integrado:** Permite a Devin consultar documentación técnica oficial (FastAPI, Supabase, SQLAlchemy, Vercel), buscar soluciones en foros ante bugs complejos y visualizar aplicaciones web en tiempo real realizando clics e interactuando con formularios.

### 1.3. Beneficios
- **Autonomía de extremo a extremo:** Recibe directivas en lenguaje natural (ej. "Crea un endpoint transaccional para anular ventas y restaurar el kardex"), elabora el plan de arquitectura y lo implementa archivo por archivo.
- **Depuración activa y adaptativa:** Si un script falla o Supabase rechaza una consulta por Row Level Security (RLS), Devin lee el stack trace en consola, aplica logs de diagnóstico, identifica la discrepancia y autocorrige el código.
- **Integración nativa con flujos Git:** Clona repositorios, ramifica ramas de trabajo (`branches`), genera commits semánticos y abre Pull Requests listos para validación.
- **Descarga de tareas rutinarias:** Automatiza tareas repetitivas como la normalización de esquemas Pydantic, tipado estricto, documentación Swagger/OpenAPI y scripts de seed inicial.

### 1.4. Potencialidades
- **Alineación con benchmarks de la industria:** Referente en el benchmark SWE-bench para la resolución automatizada de incidencias reales de software en código abierto.
- **Aprendizaje dinámico en contexto:** Capacidad de asimilar librerías emergentes o cambios de versiones de APIs en minutos con solo examinar la documentación técnica.
- **Evolución del desarrollador a líder técnico:** Permite al desarrollador enfocarse en las decisiones de negocio, diseño de modelos y auditoría, delegando la codificación mecánica al agente.

### 1.5. Desventajas y Limitaciones
- **Consumo de recursos y costo operativo:** Al requerir entornos virtuales activos y múltiples llamadas de razonamiento profundo, su uso continuo tiene un costo computacional y financiero superior al de autocompletadores ligeros.
- **Riesgo de bucles y sobre-ingeniería:** Si las especificaciones de base de datos son ambiguas, puede iterar intentando resolver un problema secundario o crear abstracciones innecesariamente complejas.
- **Aislamiento de seguridad necesario:** Requiere políticas de seguridad claras y variables de entorno controladas para evitar escrituras destructivas accidentales en bases de datos productivas.
- **Dependencia de la supervisión humana:** El criterio del desarrollador sigue siendo mandatorio para validar la coherencia contable y lógica de negocio del taller.

### 1.6. Aplicación Práctica en Mecánica Yeyko
- Generación y mantenimiento automático de los esquemas de validación Pydantic v2 en `schemas.py`.
- Creación de pruebas de integración para la lógica del **Kardex Físico** (entradas por compra, salidas por venta y ajustes manuales).
- Verificación automática de compatibilidad entre SQLAlchemy y los poolers de Supabase PostgreSQL (IPv4 Session Pooler con `pg8000`).

---

## 2. Herramienta Slack (Colaboración Técnica y Alertas)

### 2.1. Enlaces Oficiales y Comunidad
- **Canal de Slack del Evento/Equipo:** [Acceso a Slack](https://app.slack.com/client/T0C9R799A4R/C0C9R7KBGTB?entry_point=default_oauth&source=browser)
- **Portafolio y Redes de Erasmo:** [https://www.erasmoh.dev/es](https://www.erasmoh.dev/es)

Slack es la plataforma líder de comunicación y orquestación para equipos de desarrollo de software y organizaciones ágiles. Más allá del chat tradicional, funciona como un centro neurálgico de integración para eventos de CI/CD, alertas de bases de datos y soporte técnico en vivo.

### 2.2. ¿Cómo funciona Slack?
- **Canales estructurados:** Permite separar discusiones por módulos (ej. `#mecanica-yeyko-alertas`, `#backend-supabase`, `#deploy-vercel`).
- **Webhooks entrantes (Incoming Webhooks):** Permite que servidores externos envíen mensajes en formato JSON que se renderizan como tarjetas enriquecidas en canales específicos.
- **Integraciones con bots:** Recepción de notificaciones de commits de GitHub, fallos de compilación en Vercel o caídas de servicios.

### 2.3. Beneficios
- **Centralización de la comunicación:** Mantiene en un solo espacio los hilos de feedback con mentores y colaboradores (como Erasmo y la comunidad de Santa Cruz Vibeathon).
- **Visibilidad inmediata de incidentes:** Notificación instantánea en el móvil o escritorio ante anomalías en el sistema del taller.
- **Reducción del uso de canales informales:** Desplaza el uso desorganizado de mensajería instantánea hacia un entorno profesional con búsqueda e indexación de archivos.

### 2.4. Potencialidades
- **Bot de Consulta Rápida de Inventario:** Creación de un comando slash (`/stock filtro_aceite`) para que el administrador consulte disponibilidad de piezas sin abrir el panel web.
- **Alertas Proactivas de Stock Crítico:** Disparo automático de alertas cuando la existencia de repuestos de alta rotación (bujías, pastillas de freno, filtros) caiga por debajo del stock mínimo.
- **Auditoría de Ventas Mayores:** Mensaje de notificación cuando se registre una venta o compra con montos superiores a un umbral determinado (ej. repuestos de motor pesados).

### 2.5. Desventajas y Limitaciones
- **Sobrecarga de notificaciones ("Notification Fatigue"):** Si los webhooks envían cada petición menor, los miembros del canal tienden a silenciar las alertas.
- **Límite de historial en plan gratuito:** Retención de mensajes limitada a 90 días en la versión estándar sin pago.
- **Requiere conexión activa:** Depende totalmente de acceso a internet para la recepción de webhooks.

### 2.6. Aplicación Práctica en Mecánica Yeyko
- Implementación de un servicio de alertas (`slack_notifier.py`) en FastAPI que envía un mensaje formateado al canal de Slack cuando:
  1. Se concreta una venta en el Punto de Venta.
  2. Un repuesto llega a cantidad 0 o por debajo del umbral mínimo configurado.
  3. Se realiza un despliegue exitoso en Vercel.

---

## 3. Herramienta Vercel (Despliegue Serverless & CDN Edge)

### 3.1. Enlaces Oficiales
- **Página oficial:** [https://vercel.com/](https://vercel.com/)

Vercel es una plataforma de nube de última generación especializada en el alojamiento de aplicaciones web modernas, arquitecturas frontend Jamstack y APIs Serverless escalables globalmente sin fricción operacional.

### 3.2. ¿Cómo funciona Vercel?
- **Arquitectura Serverless:** Las funciones de backend (como FastAPI en `api/index.py`) se compilan y ejecutan bajo demanda en micro-contenedores efímeros (AWS Lambda bajo el capó), cobrando únicamente por el tiempo exacto de cómputo consumido.
- **Edge Network Global:** Distribuye los archivos estáticos de la interfaz (`index.html`, imágenes, estilos Tailwind y librerías JavaScript) en cientos de puntos de presencia (PoPs) alrededor del mundo, ofreciendo tiempos de carga inferiores a 50 milisegundos.
- **Despliegue Continuo (CI/CD):** Cada cambio enviado a la rama principal de GitHub detona una compilación automática y despliegue a producción con certificados SSL/HTTPS automáticos.

### 3.3. Beneficios
- **Cero mantenimiento de servidores:** No se requiere configurar servidores Linux, Nginx, Apache, systemd ni parches de seguridad del sistema operativo.
- **Disponibilidad 24/7:** La aplicación permanece activa en la nube para que el taller mecánico pueda acceder desde cualquier PC, tablet o teléfono móvil.
- **Costos iniciales cero ($0 USD):** El nivel gratuito (Hobby) incluye suficiente ancho de banda y llamadas a funciones serverless para la operación diaria de una micro o pequeña empresa.
- **URLs de Previsualización (Preview Deployments):** Cada rama o Pull Request genera un enlace único para probar cambios antes de impactar a producción.

### 3.4. Potencialidades
- **Enrutamiento inteligente con `vercel.json`:** Redirección transparente de todas las rutas de la API y de la SPA (Single Page Application) sin configuración engorrosa.
- **Conectividad con Bases de Datos Serverless:** Integración fluida con Supabase mediante cadenas de conexión basadas en conexión HTTP o Poolers transaccionales (Transaction/Session Poolers en puerto 5432 / 6543).

### 3.5. Desventajas y Limitaciones
- **Arranque en frío (Cold Starts):** Si la aplicación no recibe peticiones durante cierto tiempo, la primera llamada puede demorar entre 1 a 2 segundos mientras se inicializa el entorno de Python.
- **Sistema de archivos efímero y de solo lectura:** No se pueden guardar archivos locales persistentes ni bases de datos SQLite en producción; todo debe persistirse en Supabase PostgreSQL o almacenamiento de objetos (S3 / Supabase Storage).
- **Límite de tiempo por ejecución (Timeout):** Las funciones serverless en cuentas gratuitas tienen un límite máximo de 10 a 60 segundos por petición HTTP.

### 3.6. Aplicación Práctica en Mecánica Yeyko
- Publicación de la versión optimizada de `Mecánica Yeyko` accesible públicamente a través de un dominio seguro `https://mecanica-yeyko.vercel.app`.
- Configuración de `vercel.json` y del adaptador `api/index.py` utilizando el driver `pg8000` (100% Python nativo, compatible sin dependencias binarias C de PostgreSQL).

---

## 4. Herramienta Comentera (Feedback Visual & QA Interactivo)

### 4.1. Enlaces Oficiales
- **Página oficial:** [https://www.comentera.app/](https://www.comentera.app/)

Comentera es una herramienta moderna de colaboración y aseguramiento de calidad (QA) visual diseñada para facilitar la retroalimentación directa sobre interfaces web en tiempo real. Permite que usuarios no técnicos, clientes y desarrolladores señalen elementos visuales y dejen notas contextuales sin necesidad de capturas de pantalla manuales.

### 4.2. ¿Cómo funciona Comentera?
- Se integra en la aplicación web mediante un pequeño script de JavaScript (o mediante su extensión de navegador).
- El usuario activa el modo de anotación, hace clic sobre cualquier botón, tabla o formulario de la pantalla, y se fija un "pin" interactivo donde se escribe el comentario o solicitud de cambio.
- Captura automáticamente metadatos esenciales para el desarrollador: resolución de pantalla, navegador web, sistema operativo y selector CSS exacto del componente señalado.

### 4.3. Beneficios
- **Eliminación de la ambigüedad:** Se acabaron los reportes imprecisos como *"el botón de guardar no se ve bien"*. El pin indica con precisión milimétrica a qué botón se refiere el usuario.
- **Ahorro de tiempo en QA:** Reduce drásticamente las reuniones de revisión de interfaz y los correos de ida y vuelta.
- **Facilidad para el usuario del taller:** El propietario o mecánico de Mecánica Yeyko puede reportar mejoras ergonómicas directamente sobre el sistema mientras lo utiliza en su jornada.

### 4.4. Potencialidades
- **Gestión visual de tareas (Kanban de incidencias):** Los comentarios de Comentera se organizan en estados ("Abierto", "En progreso", "Resuelto").
- **Historial visual de versiones:** Comparación de cómo lucía la interfaz antes y después de implementar los cambios solicitados.

### 4.5. Desventajas y Limitaciones
- **Dependencia de servicios externos:** Requiere conexión a los servidores de Comentera para almacenar los hilos de anotación.
- **Capas visuales complejas:** En aplicaciones con elementos flotantes dinámicos (modales de SweetAlert2, dropdowns emergentes), puede requerir ajuste de `z-index` para que los pines no queden ocultos.

### 4.6. Aplicación Práctica en Mecánica Yeyko
- Integración en la interfaz web de prueba (`index.html`) para que el administrador valide los módulos de:
  1. Carga de repuestos en el Inventario.
  2. Experiencia de cobro en el Punto de Venta.
  3. Visualización de los balances de Kardex.

---

## 5. Gráficos 3D & Simulación Interactiva (OpenAI GPT-6 Astra / Three.js / WebGL)

### 5.1. Enlaces Oficiales y Demostración
- **Presentación OpenAI GPT-6 Astra:** [https://openai.com/es-419/index/gpt-6-astra/](https://openai.com/es-419/index/gpt-6-astra/)
- **Demostración Interactiva (Juego de autos de carreras / Simulación WebGL):** [https://fracer-production.up.railway.app/player?room=UBTVCB&pwd=5734](https://fracer-production.up.railway.app/player?room=UBTVCB&pwd=5734)

La convergencia entre modelos de inteligencia artificial multimodal de frontera (representados conceptualmente por las capacidades de razonamiento espacial avanzado de OpenAI Astra) y los motores de renderizado 3D en el navegador (WebGL, Three.js, Babylon.js) abre una nueva era en las aplicaciones de gestión automotriz.

### 5.2. ¿Cómo funciona la Tecnología 3D y Razonamiento Multimodal?
- **Renderizado por GPU en el Navegador (WebGL / Three.js):** Permite renderizar geometrías tridimensionales complejas, mallas de vehículos, materiales metálicos, reflejos e iluminación en tiempo real sin requerir instalación de plugins.
- **Razonamiento Espacial Multimodal (Astra AI):** Modelos capaces de interpretar geometrías 3D, entender la relación física y espacial entre partes mecánicas (ej. ubicación del cigüeñal respecto a las bielas y pistones) y generar diagnósticos basados en diagramas o escaneos tridimensionales.

### 5.3. Beneficios
- **Experiencia de usuario inmersiva e interactiva:** Sustituye tablas planas de repuestos por una vista tridimensional dinámica del automóvil donde las piezas son visualizables y seleccionables.
- **Claridad pedagógica y de diagnóstico:** Permite mostrar a clientes no expertos exactamente dónde se encuentra la avería en su vehículo y por qué se requiere sustituir determinado repuesto.
- **Diferenciación competitiva de alto nivel:** Eleva el sistema de Mecánica Yeyko de un software de inventario estándar a una plataforma moderna con tecnología de vanguardia.

### 5.4. Potencialidades
- **Selector 3D de Repuestos del Taller:** El mecánico hace clic sobre la rueda delantera en el modelo 3D y el sistema despliega automáticamente el stock disponible de pastillas de freno, discos y amortiguadores en Supabase.
- **Ficha Técnica con Gemelo Digital del Automóvil:** Registro del estado de chapa, pintura y componentes de cada vehículo que ingresa al taller mediante puntos interactivos en la carrocería 3D.
- **Simulador / Gamificación para Capacitación Mecánica:** Pruebas dinámicas de vehículos virtuales (como el simulador interactivo de carreras referenciado) para testear comportamiento y rendimiento de configuraciones mecánicas.

### 5.5. Desventajas y Limitaciones
- **Demanda de hardware y rendimiento:** Modelos 3D con demasiados polígonos pueden ralentizar computadoras antiguas o teléfonos inteligentes de gama baja utilizados en talleres mecánicos.
- **Optimización de activos 3D:** Los archivos `.gltf` o `.glb` deben comprimirse rigurosamente (mediante Draco compression) para garantizar descargas ligeras bajo conexiones de internet inestables.
- **Curva de desarrollo:** Requiere conocimientos de matemáticas tridimensionales, matrices de transformación, shaders y manipulación de cámaras virtuales.

### 5.6. Aplicación Práctica en Mecánica Yeyko
- Incorporación de un visor 3D interactivo en la pestaña de Dashboard o Inventario (mediante Three.js cargado vía CDN), permitiendo inspeccionar un automóvil en 360 grados, identificar zonas de mantenimiento (Motor, Frenos, Suspensión, Electricidad) y enlazar las zonas con las categorías de repuestos del inventario.

---

## 6. Enlaces Principales del Proyecto

| Recurso | Enlace / Estado | Descripción |
| :--- | :--- | :--- |
| **Repositorio / Carpeta Base** | `d:\mecanica yeyko` | Proyecto original en producción (Intacto y protegido). |
| **Repositorio / Carpeta Optimizada** | `d:\mecanica yeyko optimisado` | Espacio de trabajo activo para innovaciones y mejoras. |
| **Base de Datos Supabase (Original)** | Protegida en `.env` original (`pprrylxkwyitwjjoiitw`) | Contiene los datos productivos actuales del taller. |
| **Base de Datos Supabase (Nueva)** | Conectada (`ikouwdfhymexiilyopgc` en `us-east-1`) | Nueva instancia con todas las tablas, RLS y datos creados. |
| **Link de Diapositiva** | `[INSERTAR LINK DE DIAPOSITIVA]` | Presentación ejecutiva del proyecto de grado / defensa. |
| **Link del Proyecto (Producción)** | `[INSERTAR LINK DEL PROYECTO / VERCEL]` | Despliegue en vivo en Vercel para acceso de usuarios. |
| **Demostración 3D / WebGL** | [Simulador 3D en Vivo](https://fracer-production.up.railway.app/player?room=UBTVCB&pwd=5734) | Referencia visual interactiva de autos de carreras. |

