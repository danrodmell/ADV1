# 📋 VERCEL: PASO A PASO COMPLETO

Esta guía te lleva por cada click que necesitas hacer en Vercel para deployar tu agente.

---

## PASO 1: PREPARAR CÓDIGO EN GITHUB (5 min)

### 1.1 - Inicializar Git (en tu máquina)

Abre terminal en la carpeta `ai-readiness-agent` y ejecuta:

```bash
cd FactorySystem/ai-readiness-agent
git init
git add .
git commit -m "Initial: AI Readiness Agent MVP"
```

### 1.2 - Crear repositorio en GitHub

1. Abre: https://github.com/new
2. Completa:
   - **Repository name**: `ai-readiness-agent`
   - **Description**: `AI Readiness Assessment Tool`
   - **Public** o **Private** (tu elección)
3. Click: **Create repository**

### 1.3 - Conectar y hacer push

GitHub te dará comandos. Ejecuta en terminal:

```bash
git remote add origin https://github.com/TU-USERNAME/ai-readiness-agent.git
git branch -M main
git push -u origin main
```

**Reemplaza `TU-USERNAME` con tu usuario de GitHub**

### Verificación
- Ve a: https://github.com/TU-USERNAME/ai-readiness-agent
- Deberías ver todos los archivos ahí

✅ **Paso 1 completado**

---

## PASO 2: CREAR PROYECTO EN VERCEL (2 min)

### 2.1 - Abre Vercel Dashboard

Abre: https://vercel.com/dashboard

Haz login si es necesario (puedes usar GitHub)

### 2.2 - Click "Add New" → "Project"

En la parte superior derecha verás un botón grande "Add New"

Click en la flechita → **Project**

### 2.3 - Conecta GitHub

1. Click: **Continue with GitHub**
2. Autoriza si es necesario
3. Busca tu repo: `ai-readiness-agent`
4. Click: **Import**

### Verás una pantalla con:
- Nombre del proyecto
- Nombre del repo
- Botón azul **Deploy**

✅ **Paso 2 completado**

---

## PASO 3: AGREGAR VARIABLE DE ENTORNO (2 min)

**ANTES de hacer click en Deploy**

### 3.1 - Encuentra "Environment Variables"

En la pantalla de import, desplázate hacia abajo.

Verás una sección: **Environment Variables**

### 3.2 - Agrega la API Key

Click en el campo y agrega:

```
Name:  OPEN_ROUTER_API_KEY
Value: YOUR_OPEN_ROUTER_API_KEY
```

### 3.3 - Selecciona ambientes (recomendado)

En "Environments" (si lo pregunta):
- ✅ Production
- ✅ Preview
- ✅ Development

Click: **Add** (o el botón para guardar)

### Verificación

Deberías ver la variable listada:
```
OPEN_ROUTER_API_KEY = YOUR_OPEN_ROUTER_API_KEY
```

✅ **Paso 3 completado**

---

## PASO 4: DEPLOYAR (1 min)

### 4.1 - Click Deploy

En la pantalla de configuración, click el botón azul grande:

**Deploy**

### 4.2 - Espera el build

Vercel está:
- Descargando tu código
- Instalando dependencias
- Configurando funciones serverless
- Buildando el proyecto

Toma ~1-2 minutos.

Verás un progreso verde con checkmarks ✓

### 4.3 - Cuando termina

Cuando veas:
```
✓ Production
```

Click en **Visit** (botón azul)

O ve a:
```
https://ai-readiness-xxxxx.vercel.app
```

**Reemplaza `xxxxx` con tu proyecto ID**

✅ **Step 4 completado - ¡ESTÁS LIVE!**

---

## PASO 5: VERIFICAR QUE FUNCIONA (3 min)

### 5.1 - Abre tu URL

```
https://tu-proyecto.vercel.app
```

Deberías ver:
- Formulario bonito con fondo oscuro
- Campos: Nombre, Email, Empresa, Cargo
- Botón azul: "Continuar al Cuestionario"

### 5.2 - Prueba el formulario

1. Llena datos de prueba:
   - **Nombre**: Test User
   - **Email**: test@example.com
   - **Empresa**: Test Corp
   - **Cargo**: CTO (opcional)

2. Click: **Continuar al Cuestionario**

3. Verás paso 2 con 10 preguntas

### 5.3 - Contesta algunas preguntas

Selecciona respuestas (no es necesario todas)

Click: **Evaluar MI AI Readiness**

### 5.4 - Espera el diagnóstico

Deberías ver:
- Spinner "Analizando tu organización..."
- Después de 5-10 segundos:
- **Score**: XX/100
- **Diagnóstico**: Texto largo con análisis

✅ **¡FUNCIONA!**

---

## PASO 6: VER LOGS Y RESPUESTAS (2 min)

### 6.1 - Abre Vercel Logs

En tu proyecto en Vercel:

1. Abre: https://vercel.com/dashboard
2. Click en tu proyecto: `ai-readiness-agent`
3. Click tab: **Logs** (arriba a la derecha)

### 6.2 - Verás las interacciones

Deberías ver algo como:

```
[CONTACT] test@example.com from Test Corp
[ASSESSMENT] test@example.com - Score: 62
```

Estos son los registros automáticos de cada interacción.

✅ **Los datos se están guardando**

---

## RESUMEN: TODA LA SECUENCIA

| Paso | Acción | Tiempo |
|------|--------|--------|
| 1 | Git init + GitHub push | 5 min |
| 2 | Crear proyecto Vercel | 2 min |
| 3 | Agregar API key | 2 min |
| 4 | Click Deploy + esperar | 2 min |
| 5 | Probar el formulario | 3 min |
| 6 | Ver logs | 2 min |
| **TOTAL** | **¡LIVE!** | **16 min** |

---

## SI ALGO FALLA

### Error: "Build failed"

**Solución:**
1. Ve a Vercel → Tu proyecto → Settings
2. Click: **Environment Variables**
3. Verifica que `OPEN_ROUTER_API_KEY` está correcta
4. Click: **Redeploy** (en Deployments tab)

### Error: "Page not found" (404)

**Solución:**
1. Espera 2-3 minutos (Vercel aún puede estar configurando)
2. Recarga la página (Ctrl+R)
3. Si persiste, redeploy desde Vercel

### Error: "Assessment takes forever"

**Solución (normal):**
- Primer assessment es lento (~10 seg) - "cold start"
- Los siguientes son rápidos (~3-5 seg)
- Es completamente normal

### Error: "API key not configured"

**Solución:**
1. Ve a Vercel → Settings → Environment Variables
2. Verifica el nombre exacto: `OPEN_ROUTER_API_KEY`
3. Verifica el valor completo (no truncado)
4. Redeploy

---

## COMPARTIR TU LINK

Una vez que funciona, comparte:

```
https://tu-proyecto.vercel.app
```

Con esto, cualquiera puede hacer el assessment.

---

## PRÓXIMOS PASOS (Opcional - semana que viene)

1. **PDF Export**: Que el usuario descargue el diagnóstico
2. **Email**: Enviar resultados automáticamente
3. **Dashboard**: Ver histórico de assessments
4. **WhatsApp**: Integrar follow-up automático

Pero por ahora: ¡Ya tienes un producto LIVE!

---

## CHECKLIST FINAL

- [ ] Código en GitHub
- [ ] Proyecto creado en Vercel
- [ ] `OPEN_ROUTER_API_KEY` agregada
- [ ] Build completado sin errores
- [ ] Página carga en `https://tu-proyecto.vercel.app`
- [ ] Puedo llenar el formulario
- [ ] Recibo diagnóstico (5-10 seg)
- [ ] Veo logs en Vercel dashboard
- [ ] ✅ **¡LIVE Y FUNCIONA!**

---

## PREGUNTAS RÁPIDAS

**P: ¿Dónde veo el URL final?**
R: En Vercel dashboard, arriba del proyecto o en la pantalla de Deploy cuando termina.

**P: ¿Puedo cambiar el nombre del proyecto?**
R: Sí, en Vercel Settings, pero el URL cambia.

**P: ¿Cómo actualizo el código?**
R: Haz cambios locales → git push → Vercel redeploy automático.

**P: ¿Dónde se guardan las respuestas?**
R: En `/tmp/assessments.json` en los servidores de Vercel. Visible en logs.

**P: ¿Cuánto cuesta?**
R: Nada hasta ~1000 assessments/mes. Después ~$0.50 por 1000.

---

¡Listo! Sigue esta guía paso a paso y estarás LIVE en 16 minutos.
