# Estrategia de Precios & Posicionamiento Airbnb NYC

Proyecto de analítica de negocio para evaluar la estrategia de precios y posicionamiento de propiedades de Airbnb en Nueva York.

## Descripción del Proyecto & Problema de Negocio

El equipo directivo propuso fijar un precio de referencia de **225 USD por noche** para las propiedades del portafolio en NYC. Este proyecto evalúa esa propuesta frente al comportamiento real del mercado y busca responder tres preguntas de negocio:

- ¿El precio propuesto es competitivo y está respaldado por los datos?
- ¿Es razonable aplicar una tarifa uniforme entre los principales distritos?
- ¿Cómo debería adaptarse el precio según la duración mínima de la estadía?

El análisis convierte el conjunto de datos de Airbnb NYC en evidencia accionable para definir precios más competitivos, proteger el margen y mejorar el posicionamiento por mercado local.

## Metodología DataOps & Tecnologías

El flujo sigue una lógica DataOps reproducible: preparar los datos, transformar las variables relevantes, generar un resumen analítico y publicarlo para exploración ejecutiva.

1. **Ingesta y preparación:** Python carga el conjunto de datos de Airbnb NYC y trabaja con Pandas para realizar limpieza, segmentación y agregaciones estadísticas.
2. **Feature Engineering:** se crea `categoria_estadia` a partir de `minimum_nights`, agrupando las propiedades en cinco rangos: 1 noche, 2-3 noches, 4-7 noches, 8-29 noches y 30+ noches.
3. **Agregación:** se calculan precio promedio, mediana, noches mínimas promedio y total de propiedades por distrito, barrio, tipo de habitación y categoría de estadía.
4. **Modelado y visualización:** Power BI se mantiene en formato `.pbip`, con definiciones de modelo en TMDL y elementos de reporte en JSON. El resumen procesado se exporta a `data/processed/resumen_para_powerbi.csv`.
5. **Control y publicación:** Git/GitHub Desktop facilitan el versionado del proyecto y su despliegue público como pieza de portafolio.

### Tecnologías

- **Python + Pandas:** transformación, Feature Engineering y análisis estadístico.
- **Power BI `.pbip`:** modelo semántico TMDL, configuración del reporte y visualizaciones JSON.
- **Git / GitHub Desktop:** control de versiones y trazabilidad de cambios.
- **Despliegue público:** publicación del proyecto y sus resultados para consulta como portafolio de analítica.

## Hallazgos Clave & Refutación de Hipótesis

### 1. Precios: la propuesta de 225 USD está fuera de mercado

El precio propuesto de **225 USD** se encuentra muy por encima del comportamiento central del mercado:

| Indicador | Precio por noche |
| --- | ---: |
| Propuesta directiva | **225.00 USD** |
| Promedio real | **125.43 USD** |
| Mediana real | **106.45 USD** |

La propuesta supera el promedio real en **99.57 USD** y más que duplica la mediana. Además, el análisis de distribución muestra que 225 USD se ubica por encima del nivel de precios de la gran mayoría de las propiedades. La hipótesis de que un precio uniforme de 225 USD representa adecuadamente al mercado queda refutada: podría reducir la competitividad, la ocupación y la conversión, especialmente en segmentos sensibles al precio.

### 2. Geografía: Manhattan y Brooklyn no deben tratarse como un único mercado

Los resultados muestran una diferencia clara entre los dos distritos principales:

| Distrito | Precio promedio |
| --- | ---: |
| Manhattan | **176.22 USD** |
| Brooklyn | **118.11 USD** |

Manhattan presenta un nivel promedio **58.11 USD** superior al de Brooklyn. Aplicar una tarifa única ignoraría diferencias de demanda, ubicación, oferta y disposición a pagar. La estrategia debe incorporar segmentación geográfica: Manhattan puede sostener un posicionamiento premium, mientras Brooklyn requiere una referencia más competitiva y sensible al contexto del barrio y del tipo de habitación.

### 3. Estadías: se valida la hipótesis de descuentos por duración

El análisis clasifica las propiedades según su número mínimo de noches:

- **Corta:** 1 noche.
- **Corta-media:** 2-3 noches.
- **Semanal:** 4-7 noches.
- **Quincenal:** 8-29 noches.
- **Mensual / larga:** 30+ noches.

La tendencia general indica que, a medida que aumenta la estadía mínima, disminuye el precio promedio por noche. Este comportamiento valida la hipótesis del equipo para las estadías largas: los descuentos o tarifas escalonadas pueden incentivar reservas de mayor duración y reducir la fricción de compra. La decisión final debe revisarse por distrito, tipo de habitación y volumen de propiedades para evitar que un promedio global oculte oportunidades específicas.

## Estructura del Repositorio

```text
.
├── data/
│   ├── raw/                         # Datos originales de Airbnb NYC
│   └── processed/
│       └── resumen_para_powerbi.csv # Dataset agregado para Power BI
├── src/
│   └── analisis_airbnb.py           # Transformación y análisis en Python
├── power_bi/
│   ├── ANÁLISIS DE PROPIEDADES - AIRBNB-NYC.pbip
│   ├── ANÁLISIS DE PROPIEDADES - AIRBNB-NYC.Report/
│   │   └── definition/              # Reporte y visualizaciones JSON
│   └── ANÁLISIS DE PROPIEDADES - AIRBNB-NYC.SemanticModel/
│       └── definition/              # Modelo semántico TMDL
├── docs/                            # Documentación y materiales de publicación
└── README.md
```

## Resultado

El análisis recomienda abandonar la tarifa plana de 225 USD y adoptar una estrategia segmentada por **nivel de mercado, geografía y duración de estadía**. Esta combinación permite alinear el precio con la realidad observada y convertir los datos en una decisión comercial defendible.
