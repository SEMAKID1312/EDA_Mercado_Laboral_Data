# EDA Mercado Laboral Data

Analisis exploratorio de datos sobre perfiles profesionales del ambito tecnologico y de datos, con foco en salario, edad, nivel educativo, experiencia profesional, tipo de empleo, uso de IA, satisfaccion laboral e industria.

El proyecto trabaja con un dataset de perfiles profesionales de 2025 inspirado en Stack Overflow. El objetivo es limpiar, transformar y analizar los datos para identificar patrones relevantes del mercado laboral en perfiles relacionados con Data.

## Objetivo del analisis

El objetivo principal es estudiar que factores parecen estar asociados con la compensacion anual, la empleabilidad y la satisfaccion laboral de profesionales del sector Data.

El analisis se organiza alrededor de las siguientes hipotesis:

- **H1:** Existe una relacion positiva entre la edad y el salario anual.
- **H2:** El nivel educativo esta relacionado con la empleabilidad y el salario.
- **H2.1:** Un mayor nivel educativo esta asociado con mayor empleabilidad.
- **H2.2:** La cualificacion academica, combinada con la experiencia, ayuda a explicar diferencias salariales y de     empleabilidad.
- **H3:** La experiencia esta relacionada con el salario anual.
- **H3.1:** Una mayor experiencia profesional esta asociada con salarios mas altos.
- **H3.2:** La combinacion de experiencia laboral y experiencia tecnica aporta informacion adicional sobre el salario.
- **H4:** Existen diferencias salariales entre perfiles empleados y freelancers.
- **H5:** El uso de herramientas de IA esta relacionado con el salario y la satisfaccion laboral.
- **H6:** La industria en la que trabaja una persona influye en su salario anual.

## Dataset

El dataset original debe colocarse en la siguiente ruta:

```text
src/data/develop_dataset_2025.csv
```

Los archivos de datos no se incluyen en el repositorio porque estan ignorados mediante `.gitignore`.

Durante el proceso de limpieza se generan archivos derivados:

```text
src/data/develop_dataset_2025_limpio.csv
src/data/data_dictionary.csv
```

## Estructura del proyecto

```text
.
+-- README.md
+-- main.ipynb
+-- src
    +-- data
    |   +-- develop_dataset_2025.csv
    |   +-- develop_dataset_2025_limpio.csv
    |   +-- data_dictionary.csv
    +-- notebooks
    |   +-- notebook_eda_inicial.ipynb
    |   +-- analisis_univariante.ipynb
    |   +-- analisis_bivariante.ipynb
    |   +-- analisis_multivariante.ipynb
    +-- utils
        +-- funciones.py
```

## Archivos principales

### main.ipynb

Notebook principal que integra el pipeline completo del EDA. Esta dividido en celdas para poder ejecutar cada bloque desde VS Code:

1. Carga y limpieza de datos.
2. Analisis univariante.
3. Analisis bivariante.
4. Analisis multivariante.

### src/notebooks/notebook_eda_inicial.ipynb

Notebook dedicado a la carga inicial del dataset, seleccion de variables, limpieza de datos y generacion del dataset limpio.

Incluye:

- inspeccion inicial del dataset;
- seleccion de columnas relevantes;
- filtrado de perfiles relacionados con Data;
- tratamiento de valores nulos;
- correccion de valores anomalos;
- normalizacion de categorias;
- creacion del diccionario de datos;
- exportacion del dataset limpio.

### src/notebooks/analisis_univariante.ipynb

Analisis individual de las variables principales del dataset.

Permite estudiar distribuciones, frecuencias, medidas de tendencia central, dispersion y valores atipicos en variables como salario, edad, experiencia, nivel educativo, pais, industria, satisfaccion laboral y tipo de empleo.

### src/notebooks/analisis_bivariante.ipynb

Notebook centrado en el contraste de hipotesis mediante relaciones entre pares de variables.

Trabaja especialmente edad-salario, educacion-empleo, experiencia-salario, empleo-freelance, uso de IA-salario/satisfaccion e industria-salario.

### src/notebooks/analisis_multivariante.ipynb

Analisis conjunto de variables relacionadas con salario, empleabilidad, experiencia y educacion.

Incluye cruces entre educacion y experiencia, matriz de correlaciones y modelos lineales simples para aproximar la relacion entre variables.

### src/utils/funciones.py

Modulo auxiliar con funciones reutilizadas durante el analisis, como calculos de calidad de datos, simplificacion de niveles educativos y asignacion de puntuaciones educativas.

## Librerias utilizadas

El proyecto utiliza principalmente:

- pandas
- numpy
- matplotlib
- seaborn

## Como ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/SEMAKID1312/EDA_Mercado_Laboral_Data.git
```

2. Entrar en la carpeta del proyecto:

```bash
cd EDA_Mercado_Laboral_Data
```

3. Crear o comprobar la carpeta de datos:

```text
src/data/
```

4. Colocar el dataset original con este nombre:

```text
src/data/develop_dataset_2025.csv
```

5. Ejecutar el notebook principal:

```text
main.ipynb
```

Tambien se pueden ejecutar los notebooks por separado en este orden:

```text
src/notebooks/notebook_eda_inicial.ipynb
src/notebooks/analisis_univariante.ipynb
src/notebooks/analisis_bivariante.ipynb
src/notebooks/analisis_multivariante.ipynb
```

## Pipeline del analisis

### 1. Carga y limpieza

Se carga el dataset original, se seleccionan columnas relevantes y se filtran perfiles profesionales relacionados con Data:

- Data engineer
- Data scientist
- Data or business analyst
- Applied scientist
- Database administrator or engineer
- AI/ML engineer
- Developer, AI apps or physical AI

Despues se eliminan duplicados, se tratan valores nulos, se normalizan categorias y se exporta el dataset limpio.

### 2. Analisis univariante

Se estudia cada variable de forma individual mediante:

- frecuencias de variables categoricas;
- medias, medianas, minimos y maximos;
- distribuciones;
- boxplots;
- deteccion de outliers mediante IQR.

### 3. Analisis bivariante

Se analizan relaciones entre pares de variables para contrastar las hipotesis principales.

Entre los cruces analizados estan:

- edad y salario;
- nivel educativo y empleo;
- nivel educativo y salario;
- experiencia y salario;
- tipo de empleo y salario;
- uso de IA, salario y satisfaccion laboral;
- industria y salario.

### 4. Analisis multivariante

Se incorporan variables derivadas y cruces de mayor complejidad:

- puntuacion educativa;
- variable binaria de empleabilidad;
- salario logaritmico;
- grupos de experiencia;
- matriz de correlaciones;
- modelo lineal sobre salario;
- modelo lineal sobre empleabilidad.

## Hipotesis y resultados principales

### H1: Edad y salario anual

El analisis muestra una tendencia general positiva entre la edad y el salario anual. Los grupos de mayor edad presentan, en terminos generales, medianas salariales mas altas que los grupos mas jovenes.

La relacion no es completamente lineal y puede verse afectada por valores atipicos, diferencias entre paises, tipo de puesto y tamanos muestrales desiguales entre grupos de edad.

**Conclusion:** H1 se acepta parcialmente. La edad parece estar asociada con salarios mas altos, aunque no explica por si sola la variabilidad salarial.

### H2: Nivel educativo, empleabilidad y salario

El nivel educativo muestra relacion con la empleabilidad y con el salario, aunque la intensidad de esta relacion varia segun la categoria educativa y el tamano muestral.

Los niveles educativos superiores tienden a presentar mejores indicadores, pero el salario tambien depende de otros factores como experiencia, industria, pais y rol profesional.

**Conclusion:** H2 se acepta parcialmente. La educacion influye, pero no actua como unico factor explicativo.

### H2.1: Nivel educativo y empleabilidad

El analisis de la distribucion de empleo por nivel educativo indica que los perfiles con mayor formacion academica suelen presentar mayores porcentajes de personas empleadas.

Esta relacion debe interpretarse con cautela porque algunas categorias educativas tienen menor representacion y porque la empleabilidad tambien puede depender de experiencia previa, especializacion tecnica y mercado local.

**Conclusion:** H2.1 se acepta parcialmente. Un mayor nivel educativo se asocia con mejores indicadores de empleabilidad, aunque no garantiza por si solo estar empleado.

### H2.2: Educacion, experiencia, empleabilidad y salario

El analisis multivariante combina nivel educativo, experiencia profesional y empleabilidad para observar relaciones mas complejas.

La cualificacion academica aporta informacion util, pero los resultados sugieren que su efecto se entiende mejor cuando se analiza junto con la experiencia laboral y tecnica.

**Conclusion:** H2.2 se acepta parcialmente. La educacion contribuye a explicar diferencias salariales y de empleabilidad, especialmente al combinarse con experiencia.

### H3: Experiencia y salario anual

La experiencia aparece como una variable relevante para entender diferencias salariales. En general, los perfiles con mas anos de experiencia tienden a alcanzar salarios mas altos.

No obstante, la relacion presenta dispersion y no todos los incrementos de experiencia se traducen en aumentos proporcionales de salario.

**Conclusion:** H3 se acepta parcialmente. La experiencia esta asociada con el salario, pero su efecto no es completamente lineal.

### H3.1: Experiencia profesional y salario

Al agrupar los anos de experiencia laboral en rangos, se observa un incremento progresivo de la mediana salarial desde perfiles junior hasta perfiles mas senior.

La correlacion lineal puede ser moderada o debil debido a la influencia de otros factores, como pais, industria, rol, educacion y valores extremos.

**Conclusion:** H3.1 se acepta parcialmente. La experiencia profesional esta asociada con salarios mas altos, especialmente al analizarla por rangos.

### H3.2: Experiencia laboral, experiencia tecnica y salario

El cruce entre experiencia laboral y anos programando permite distinguir mejor entre experiencia profesional general y experiencia tecnica acumulada.

Los perfiles con mayor combinacion de experiencia laboral y tecnica tienden a situarse en niveles salariales superiores, aunque la relacion mantiene dispersion.

**Conclusion:** H3.2 se acepta parcialmente. La combinacion de experiencia laboral y tecnica ayuda a interpretar mejor el salario que cualquiera de las dos variables por separado.

### H4: Empleados frente a freelancers

El analisis compara la distribucion salarial de perfiles empleados y freelancers.

Se observan diferencias entre ambos grupos, aunque la interpretacion requiere cautela porque los freelancers pueden presentar mayor variabilidad en ingresos, dedicacion, pais, tipo de cliente y estabilidad laboral.

**Conclusion:** H4 se acepta parcialmente. El tipo de empleo parece influir en el salario, pero la comparacion entre empleados y freelancers debe contextualizarse.

### H5: Uso de IA, salario y satisfaccion laboral

El uso de herramientas de IA se analiza frente al salario anual y la satisfaccion laboral.

Los resultados permiten observar si quienes usan IA presentan diferencias en compensacion o satisfaccion. Sin embargo, esta relacion puede estar mediada por el rol, la industria, la seniority y el tipo de tareas realizadas.

**Conclusion:** H5 se acepta parcialmente. El uso de IA puede estar relacionado con salario y satisfaccion, aunque no permite establecer causalidad.

### H6: Industria y salario anual

Los resultados muestran diferencias salariales claras entre industrias. Algunas areas presentan medianas salariales notablemente superiores, mientras que otras se situan en niveles mas bajos.

Tambien existe alta dispersion salarial dentro de determinados sectores, por lo que la mediana resulta mas adecuada que la media para comparar industrias.

**Conclusion:** H6 se acepta. La industria en la que trabaja una persona parece influir en el salario anual.

## Conclusion general

El analisis exploratorio permite identificar varios factores asociados al salario y a la empleabilidad en perfiles profesionales del ambito Data.

La edad, el nivel educativo, la experiencia, el tipo de empleo, el uso de herramientas de IA y la industria muestran relaciones relevantes con el salario anual y otros indicadores profesionales. Sin embargo, ninguna variable explica por si sola las diferencias observadas.

La presencia de valores atipicos, la dispersion salarial y los distintos tamanos muestrales hacen necesario interpretar los resultados con prudencia.

En conjunto, el proyecto muestra que el salario depende de una combinacion de factores formativos, profesionales, tecnologicos y sectoriales. Por ello, el analisis refuerza la importancia de estudiar el mercado laboral desde una perspectiva multivariable.
