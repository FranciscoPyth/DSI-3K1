## RESUMEN DISEÑO DE SISTEMA DE INFORMACIÓN

**Ciclo de vida del Proceso Unificado de Desarrollo (PUD)**

![picture 1](./images/ciclo_vida_pud.png)

Pilares del PUD:
1. Dirigido por Casos de Uso
2. Centrado en la Arquitectura
3. Proceso Iterativo e Incremental

## ¿Qué es el diseño?
El diseño es una etapa/framework dentro del PUD (Proceso Unificado de Desarrollo) que se encarga de recibir los RF (Requerimientos Funcionales) trabajados en la etapa/framework anterior referido al análisis, en donde estos RF fueron trabajamos sin tener en cuenta ninguna limitación a nivel de software/hardware o regla de negocio, es decir, en el análisis se asume una topología interna perfecta y neutra (la cual no le da importancia a los RNF). En el diseño, tenemos que encargarnos de resolver los RNF del sistema, llevando el modelo lógico de la etapa de análisis a un modelo físico que empieza a tener en cuenta las restricciones de negocio. 

## ¿Qué se puede diseñar?
1. **Arquitectura**:
    - Es la más relevante de todas, ya que marca los lineamientos y la estructura general que seguirá nuestro sistema. El diseño de la arquitectura es un **proceso** que conlleva un conjunto de decisiones significativas que se toman para resolver los RNF (Requerimientos No Funcionales) afectando lo menos posible a los RF que llegan como entrada del framework de análisis.
2. **Procesos**
    - Se relaciona con patrones de diseño, para este momento no se amplía la información de este punto.
3. **Experiencia de usuario**
    - Relacionado con UX, todavía no profundizamos
4. **Datos**
    - Tiene que ver con la persistencia de los datos, de que forma se va a diseñar la transformación de POO al paradigma estructurado de las base de datos relacionales.
5. **Formas de E/S** 
    - Se requiere diseñar para estandarizar la forma en que ingresan datos al sistema (campos de un formulario) y las formas en que salen (reportes, estadísticas, etc)
6. **Procedimientos manuales / Procesos de negocio**
    - Se relaciona a los cambios que sufre el proceso de negocio a medida que avanza la tecnología y sistemas:
        - En lote (batch)
        - En línea
        - Sistemas en tiempo real (es un tipo de sistema en línea)

        Ejemplos: Sistema en batch o lotes son las elecciones, que se recauda toda la información en papeles y luego se ingresan esos datos en el sistema, el censo es otro ejemplo, que también aplica algo más híbrido, ya que se podía censar desde nuestras propias casas, sin necesidad que pase una persona a realizar el censo.

## Profundizamos un poco en el diseño de la arquitectura...
- Cada una de estas etapas tiene un rol asociado, que en este caso es el arquitecto de software, quien se encarga de desarrollar cada etapa y tiene asociadas responsabilidades:
    - Comunicar las decisiones tomadas al equipo
    - Negociar con los interesados o stakeholders
    - Documentar la arquitectura
    - Comunica la arquitectura, asegurando que los interesados la comprendan.
    - Direcciona los requerimientos no funcionales a la arquitectura.
    - Configura la arquitectura de hardware.
    - Se asegura que la arquitectura es respetada.
    - Trabaja con el Administrador del Proyecto (jefe o líder de proyecto), ayudando en la planificación, la  estimación, la distribución de las tareas y la calendarización del proyecto (organiza recursos, cumplir presupuestos, cumplir costos y tiempos).
El arquitecto es el trabajador en los 3 primeros workflows: requerimientos, análisis y diseño. Es una figura reciente en la 
ingeniería de software. También suele llamarse líder técnico. Tiene que tener muchas habilidades y capacidades, es un rol 
que se logra con el tiempo. Suelen ser desarrolladores con un perfil técnico que evolucionan. El rol del arquitecto suele ser 
colegiado (ejercido por más de una persona) ya que hay que saber un poco de todo. Los arquitectos deben poseer 
múltiples habilidades de software, ingeniería, tecnología, gestión y comunicaciones

- El diseño de la arquitectura, se encuentra compuesto por tres etapas claves:
    1. **Determinar RNF significativos**
    2. **Diseñar la arquitectura**
        - Elegir el framework arquitectónico, básicamente es elegir los patrones arquitectónicos que nos seguirán a lo largo de todo el diseño, es lo que identificará a nuestro sistema a nivel global/general. Podemos decir como ejemplo, patrón Broker, Publish and Suscribe, Layered, Messaging, Hexagonal, las cuales explicaremos más adelante en la sección de *Patrones y estilos arquitectónicos*
        - Distribuir los componentes, en esta etapa el arquitecto, debe encargarse de dividir las responsabilidades del sistema en componentes, buscando agrupar componentes en subsistemas muy cohesivos, para que resuelvan una tarea específica, también se debe buscar un bajo acoplamiento entre componentes (para evitar que se rompa todo). De aquí salen las vistas arquitectónicas, son 10 vistas las que se pueden realizar, cada vista representa una forma de modelar la arquitectura, la sumatoria de todas nos permitirán tener un entendimiento mucho mejor de la arquitectura, esta parte debe ir en el documento de arquitectura.
    3. **Validar la arquitectura**
        - Escenarios de prueba, son artefactos simples, que se utilizan para validar algún comportamiento de la arquitectura frente a algún evento/estímulo particular que pueden tener un gran impacto en la misma.
        - Ejemplos:
        ![picture 2](./images/examples_escenarios.png)
        - Prototipos, muchas veces sucede, que los escenarios se tornan un poco más complejos, por lo tanto, se requiere la realización de un mini prototipo, para poder validar el comportamiento de la arquitectura, se desarrolla una aplicación pequeña (una versión mínima) encargada de realizar un aspectos particular de nuestro sistema. Estos prototipos nos deben ayudar a responder alguna de estas dos preguntas:
            1. Prueba de conceptos: ¿Puede la arquitectura como fue diseñada ser construida de manera tal que satisfaga los requerimientos?
            2. Prueba de tecnología:  ¿La tecnología elegida (middleware, aplicaciones integradas, librerías, etc.) para implementar la arquitectura se comporta como es esperado?

            ![picture 4](./images/diseño_arquitectura.png)

## Ventajas de diseñar y documentar la arquitectura
1. Comunicación con los involucrados: la arquitectura es una presentación que sirve para usarse como 
enfoque para la discusión de un amplio número de participantes.
2. Análisis del sistema: sirve para aclarar la arquitectura del sistema, para saber si se cumplen los 
requerimientos críticos.
3. Reutilización a gran escala: es posible desarrollar arquitecturas de línea de productos donde la misma 
arquitectura se reutilice mediante una amplia gama de sistemas relacionados.

## Conflictos arquitectónicos
1. Utilizar componentes de granularidad gruesa mejora la performance pero reduce la mantenibilidad. (gana la performance)
2. La introducción de datos redundantes mejora la disponibilidad pero hace más difícil la seguridad. (y la performance) Hay más lugares en donde se necesita controlar la seguridad y se tienen que agregar más capas de validación, esto hace que la performance se degrade, siendo más lento el sistema. 
3. La localización de aspectos de seguridad relacionados usualmente significa más comunicación, por lo tanto degrada la performance.


## Vistas Arquitectónicas
Las vistas arquitectónicas son formas de modelar la arquitectura del software, dentro del contexto del PUD, se toma como convención el enfoque de vistas arquitectónicas 4 + 1, estas 4 vistas están unidas por otra que es la vista de funcionalidad (casos de uso) la cual contiene los casos de uso significativos para la arquitectura. Se describirán a continuación:

![picture 3](./images/vistas_pud.png)

1. **Vista de Diseño (lógica)**, describe los elementos significativos de la arquitectura  y las relaciones entre ellos. Esta vista se diseña para el usuario final, es quien utilizará el sistema, para que pueda entender la arquitectura desde un punto de vista más sencillo. Describe cómo será provista la funcionalidad del sistema, qué clases, objetos o componentes voy a utilizar para dar soporte a la funcionalidad.
2. **Vista de Proceso**, se centra en describir la concurrencia y elementos de comunicación del sistema, se encuentra más relacionado con la performance.
3. **Vista de Despliegue (física)**, esta vista describe cómo los principales procesos y componentes se asignan al hardware de 
las aplicaciones. Muestra cómo el software será alojado en los diferentes componentes de hardware. Podría mostrar, por ejemplo, cómo se distribuye la base de datos y los servidores web de una aplicación en varias máquinas servidor.
4. **Vista Implementación (componentes)**, : Esto captura la organización interna de los componentes de código, normalmente cuando se mantienen en un entorno de desarrollo o herramienta de gestión de la configuración. Describe también las dependencias de los módulos de implementación (código fuente, bibliotecas, componentes de terceros).
5. **+1 Vista funcionalidad o de escenarios**, representa los casos de uso significativos para la arquitectura. 

Las vistas que utilizamos en el práctico son:
- Vista arquitectónica de funcionalidad - Diagrama de Casos de Uso
- Vista arquitectónica de diseño - Diagrama de Componentes
- Vista arquitectónica de despliegue - Diagrama de Despliegue

Cada vista tiene a su derecha el diagrama UML relacionado

![picture 5](./images/10_vistas.png)

Cabe aclarar que son 10 vistas en total las que se pueden modelar para la arquitectura, sólo vemos 3 y son estáticas en la parte práctica de la materia, pero en el cuadro de arriba podemos observar las 10, con su parte estática y dinámica. Aclaramos que todas las vistas se construyen en el workflow (WF) de diseño, menos la vista de funcionalidad estática que corresponde al WF de requerimientos y la dinámica que corresponde al WF de análisis.

Ahora nos preguntamos, ¿hace falta construir todas las vistas?, ¿hacen falta más vistas?
Las vistas son modelos simplificados para mostrar el contexto. No todos los sistemas requieren todas las vistas. Por ejemplo si tenemos:
- Un solo procesador: saltear la vista de despliegue.
- Procesos simples: saltear la vista de procesos.
- Programas muy pequeños: saltear la vista de implementación

*Sección preguntas:*
- ¿Por qué es importante diseñar la arquitectura del software?
- ¿Cómo se documenta la arquitectura del software?
- ¿En qué momento del ciclo de vida se diseña la arquitectura?
- Grafique y explique el proceso de diseño de la arquitectura del software que propone el autor Ian Gorton.
- Explique por qué se utilizan vistas para modelar la arquitectura, qué vistas se utilizan y qué diagramas de UML se emplean para modelar en cada vista.


## Patrones Arquitectónicos

*Sección preguntas:*
- Elija tres patrones arquitectónicos asociados a la vista de ejecución (runtime), y para cada uno de ellos explique su propósito y elija un caso para ejemplificar donde se justifica su aplicación.