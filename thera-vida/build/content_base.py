# -*- coding: utf-8 -*-
"""Datos del negocio, zonas, categorías secundarias y textos del inicio."""

DOMAIN = "https://TU-DOMINIO-AQUI"   # sin "/" final. Cámbialo aquí y vuelve a ejecutar build.py
BRAND = "Thera+Vida"
PHONE_DISPLAY = "317 012 1268"
PHONE_INTL = "+573170121268"
CITY = "Bogotá"

MAP_IFRAME_SRC = ("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3976.068354263849!2d-74.0434449"
                  "!3d4.7581342!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e3f85127fc97111%3A0xe26f89117e4bf7c6"
                  "!2sMasajes%20a%20domicilio%20en%20Bogota%20%7C%20Thera%2BVida!5e0!3m2!1ses-419!2sco!4v1791215987877!5m2!1ses-419!2sco")
MAP_CID_URL = "https://maps.google.com/?cid=16316410683212953542"

# 20 zonas de cobertura (aparecen en todas las páginas)
ZONES = [
    "Usaquén", "Cedritos", "Santa Bárbara", "Toberín", "Chicó", "Chapinero", "Rosales",
    "Teusaquillo", "Galerías", "Barrios Unidos", "Salitre", "Modelia", "Fontibón",
    "Engativá", "Suba", "Niza", "Colina Campestre", "Kennedy", "Castilla", "Puente Aranda",
]

# ---------------------------------------------------------------------------
# PÁGINA PRINCIPAL — categoría principal de GBP: masajes a domicilio
# ---------------------------------------------------------------------------
HOME = {
    "title": "Masajes a Domicilio en Bogotá 24 Horas | Thera+Vida",
    "desc": "Masajes a domicilio en Bogotá las 24 horas: masaje terapéutico, drenaje linfático, enfermería y rehabilitación en casa. Agenda por WhatsApp al 317 012 1268.",
    "h1": "Masajes a domicilio en Bogotá",
    "lead": ("Los masajes a domicilio en Bogotá de Thera+Vida llegan a tu casa, tu apartamento o tu oficina, "
             "a cualquier hora del día o de la noche. Además del masaje terapéutico, nuestro equipo hace drenajes, "
             "acompaña procesos de rehabilitación y presta servicios de enfermería, para que el cuidado completo "
             "ocurra en un solo lugar: donde tú estás."),
    "tagline": "Enfermería con vocación, terapia con propósito.",
    "wa": "Hola Thera+Vida, quiero agendar un masaje a domicilio en Bogotá.",
}

# ---------------------------------------------------------------------------
# CATEGORÍAS SECUNDARIAS (una página cada una)
# ---------------------------------------------------------------------------
CATEGORIES = [
    {
        "slug": "masaje-terapeutico-a-domicilio-bogota",
        "name": "Masaje terapéutico a domicilio",
        "menu": "Masaje terapéutico",
        "h1": "Masaje terapéutico a domicilio en Bogotá",
        "title": "Masaje Terapéutico a Domicilio en Bogotá | Thera+Vida",
        "desc": "Masaje terapéutico a domicilio en Bogotá: masaje antiestrés, masaje para el colon y tratamiento de celulitis. Atención 24 horas. Agenda por WhatsApp.",
        "img": "imagen7.jpg", "img_alt": "Masaje terapéutico a domicilio en Bogotá",
        "img2": "imagen2.jpg", "img2_alt": "Terapeuta haciendo un masaje terapéutico en casa en Bogotá",
        "wa": "Hola Thera+Vida, quiero información sobre el masaje terapéutico a domicilio en Bogotá.",
        "services": ["masaje-antiestres-bogota", "masaje-para-el-colon-bogota", "tratamiento-de-celulitis-bogota"],
        "home_text": [
            "El masaje terapéutico a domicilio en Bogotá es el corazón de lo que hacemos. No es un masaje de paso: antes de empezar, la terapeuta pregunta dónde está la molestia, cómo dormiste, si tienes alguna condición médica o si tomas medicamentos, y con eso decide la presión, el ritmo y las zonas que va a trabajar.",
            "Muchas personas nos llaman al final de una semana pesada, con el cuello rígido de tantas horas frente al computador o la espalda cargada después de un trayecto largo por la ciudad. Para ellas está el masaje antiestrés, que combina maniobras lentas y profundas con una respiración pausada. Otras llegan por algo más puntual: el estreñimiento que no cede, para el que trabajamos el masaje de colon o malaxación colónica, o la celulitis en piernas y glúteos, que tratamos con maniobras que estimulan la circulación.",
            "Llevamos la camilla, los aceites y las toallas, así que solo necesitas un espacio tranquilo de unos dos por dos metros. La sesión se ajusta a tu horario porque atendemos las 24 horas, y al terminar puedes quedarte en tu cama en lugar de enfrentarte al tráfico de regreso.",
            "En la página de masaje terapéutico a domicilio te contamos en detalle cada tipo de masaje, para quién es y qué esperar de la primera sesión.",
        ],
        "intro": [
            "Un buen masaje terapéutico empieza antes de tocar la piel. La terapeuta llega a tu casa, conversa contigo unos minutos sobre la molestia que tienes, revisa si hay alguna condición médica que deba tener en cuenta y solo entonces decide qué técnica usar y con cuánta presión.",
            "En Bogotá trabajamos tres líneas de masaje terapéutico a domicilio: el masaje antiestrés, el masaje para el colon o malaxación colónica y el tratamiento manual de la celulitis. Cada uno tiene su propia página con más detalle, y aquí te contamos lo esencial para que sepas cuál se ajusta a lo que buscas.",
        ],
        "why": [
            "Llevamos camilla, aceites, toallas y todo lo que la sesión requiere; tú solo pones el espacio.",
            "La terapeuta adapta la presión y la técnica a tu cuerpo ese día, no a un protocolo fijo.",
            "Atendemos a cualquier hora, incluso de noche o un domingo, porque estamos disponibles las 24 horas.",
            "Después del masaje no tienes que salir: puedes ducharte, descansar y dejar que el cuerpo asimile la sesión.",
        ],
        "faqs": [
            ("¿Qué necesito tener en casa para el masaje terapéutico?", "Solo un espacio despejado de unos dos por dos metros, cerca de un tomacorriente si quieres música o luz cálida. La terapeuta lleva la camilla plegable, sábanas, toallas y aceites."),
            ("¿Cuánto dura una sesión de masaje terapéutico a domicilio?", "La duración depende del tipo de masaje y de lo que acordemos al agendar. Te lo confirmamos por WhatsApp junto con la cotización, antes de la visita."),
            ("¿Puedo pedir el masaje a domicilio de noche?", "Sí. Atendemos las 24 horas, todos los días, en Bogotá y municipios cercanos. Solo escríbenos con anticipación para coordinar la terapeuta disponible."),
            ("¿Hay casos en los que no se recomienda el masaje?", "Sí: fiebre, infecciones en la piel, trombosis, heridas abiertas o algunas condiciones cardíacas. Por eso preguntamos por tu salud antes de empezar, y si hay dudas te pedimos la autorización de tu médico."),
        ],
    },
    {
        "slug": "drenaje-linfatico-a-domicilio-bogota",
        "name": "Drenaje linfático a domicilio",
        "menu": "Drenaje linfático",
        "h1": "Drenaje linfático a domicilio en Bogotá",
        "title": "Drenaje Linfático a Domicilio en Bogotá 24 Horas | Thera+Vida",
        "desc": "Drenaje linfático a domicilio en Bogotá: drenaje postoperatorio, drenaje linfático manual y drenaje venoso en tu casa. Agenda por WhatsApp.",
        "img": "imagen5.jpg", "img_alt": "Drenaje linfático a domicilio en Bogotá",
        "img2": "imagen2.jpg", "img2_alt": "Terapeuta realizando un drenaje en casa en Bogotá",
        "wa": "Hola Thera+Vida, quiero información sobre el drenaje linfático a domicilio en Bogotá.",
        "services": ["drenaje-postoperatorio-bogota", "drenaje-linfatico-manual-bogota", "drenaje-venoso-bogota"],
        "home_text": [
            "El drenaje linfático a domicilio en Bogotá es uno de los servicios que más nos piden, sobre todo después de una cirugía. Cuando alguien sale de una liposucción, una abdominoplastia o una cirugía de mama, lo último que quiere es subirse a un carro para ir a una sesión. Por eso vamos nosotros.",
            "El drenaje es un masaje muy distinto al que la mayoría imagina. Las maniobras son suaves, lentas y rítmicas, porque el sistema linfático está justo debajo de la piel y responde mejor a una presión ligera que a la fuerza. El objetivo es ayudar a que el líquido acumulado vuelva a circular, lo que suele traducirse en menos hinchazón y una sensación de alivio en las piernas o en la zona operada.",
            "Trabajamos tres tipos de drenaje: el postoperatorio, que siempre seguimos según las indicaciones de tu cirujano; el drenaje linfático manual, para quien retiene líquidos o siente las piernas pesadas; y el drenaje venoso, enfocado en la circulación de retorno de las piernas. En casa la sesión es más tranquila, porque puedes quedarte con tu faja, tu ropa cómoda y tu cama a pocos pasos.",
            "En la página de drenaje linfático a domicilio te explicamos cada tipo, cuántas sesiones se suelen necesitar y cuándo conviene empezar.",
        ],
        "intro": [
            "Después de una cirugía, con las piernas hinchadas al final del día o con la sensación de pesadez que deja estar muchas horas de pie, el drenaje linfático es de las terapias que más alivio dan. Y hacerlo en casa tiene una ventaja evidente: no tienes que moverte cuando menos ganas tienes de hacerlo.",
            "Nuestro equipo hace drenaje linfático a domicilio en toda Bogotá, las 24 horas. Trabajamos con maniobras suaves y rítmicas, siguiendo las indicaciones de tu médico cuando se trata de un postoperatorio, y te explicamos en cada visita cómo va evolucionando la zona.",
        ],
        "why": [
            "No tienes que salir de casa recién operada ni con las piernas inflamadas.",
            "En el postoperatorio seguimos las indicaciones de tu cirujano y respetamos los tiempos que él defina.",
            "La terapeuta revisa la zona antes de cada sesión y te avisa si nota algo que deba ver tu médico.",
            "Coordinamos las sesiones según tu horario, incluso de noche o fines de semana.",
        ],
        "faqs": [
            ("¿Cuándo puedo empezar el drenaje después de una cirugía?", "Lo define tu cirujano. Algunos lo indican desde los primeros días y otros prefieren esperar. Antes de la primera visita te pedimos que nos cuentes qué te recomendó, y seguimos esa indicación."),
            ("¿El drenaje linfático duele?", "En general no. Las maniobras son suaves. En un postoperatorio la zona puede estar sensible, y por eso la terapeuta ajusta la presión y va preguntando cómo te sientes."),
            ("¿Cuántas sesiones de drenaje necesito?", "Depende del motivo y de cómo responda tu cuerpo. En el postoperatorio suele hacerse una serie de sesiones; te damos una orientación en la primera visita y la ajustamos según la evolución."),
            ("¿Tengo que quitarme la faja para el drenaje?", "Sí, durante la sesión se retira para trabajar la zona, y al terminar te ayudamos a ponértela de nuevo."),
        ],
    },
    {
        "slug": "enfermeria-a-domicilio-bogota",
        "name": "Enfermería a domicilio",
        "menu": "Enfermería a domicilio",
        "h1": "Enfermería a domicilio en Bogotá",
        "title": "Enfermería a Domicilio en Bogotá 24 Horas | Thera+Vida",
        "desc": "Enfermería a domicilio en Bogotá las 24 horas: curación de heridas y úlceras, cuidado de estomas, control de signos vitales y podología en casa.",
        "img": "imagen4.jpg", "img_alt": "Enfermería a domicilio en Bogotá",
        "img2": "imagen8.jpg", "img2_alt": "Control de signos vitales a domicilio en Bogotá",
        "wa": "Hola Thera+Vida, quiero información sobre enfermería a domicilio en Bogotá.",
        "services": ["manejo-de-heridas-y-ulceras-bogota", "cuidado-de-estomas-bogota", "control-de-signos-vitales-bogota", "podologia-a-domicilio-bogota"],
        "home_text": [
            "La enfermería a domicilio en Bogotá resuelve algo que muchas familias viven en silencio: tener en casa a un adulto mayor, a una persona recién operada o a alguien con una herida que necesita cuidado diario, y no saber cómo hacerlo bien. Llevarlo a una clínica para cada curación es agotador para todos.",
            "Nuestro personal de enfermería va a tu casa con los insumos necesarios para cada procedimiento. Hacemos curación de heridas por presión y úlceras, colocación y limpieza de estomas, control de signos vitales y podología especializada, que en personas mayores o con diabetes es parte del cuidado diario y no un lujo.",
            "Siempre trabajamos de la mano de las indicaciones del médico tratante. Si en una visita notamos algo que no está bien, como una herida que cambia de color, fiebre o una presión arterial fuera de lo esperado, te lo decimos con claridad y te orientamos para que consultes a tiempo. También enseñamos a la familia lo que puede hacer entre visita y visita, porque el cuidado no termina cuando nos vamos.",
            "Atendemos las 24 horas, así que también podemos ir de noche o en fin de semana. En la página de enfermería a domicilio encuentras el detalle de cada servicio.",
        ],
        "intro": [
            "Cuidar a alguien en casa exige conocimiento técnico y mucha paciencia. Una curación mal hecha puede retrasar semanas la cicatrización, y un estoma mal manejado irrita la piel y genera angustia. Ahí es donde entra el personal de enfermería.",
            "Prestamos servicios de enfermería a domicilio en Bogotá las 24 horas, con insumos propios y siguiendo las indicaciones del médico tratante. Estos son los procedimientos que hacemos en casa.",
        ],
        "why": [
            "Llevamos los insumos de cada procedimiento y los desechamos de forma segura al terminar.",
            "Seguimos las órdenes de tu médico y te avisamos si algo cambia y conviene consultarle.",
            "Le explicamos a la familia qué observar y qué hacer entre una visita y otra.",
            "Vamos a cualquier hora: atendemos las 24 horas, todos los días.",
        ],
        "faqs": [
            ("¿Necesito una orden médica para la enfermería a domicilio?", "Para procedimientos como curaciones o manejo de estomas es ideal tener las indicaciones del médico tratante. Si no las tienes a mano, cuéntanos el caso por WhatsApp y te orientamos."),
            ("¿Ustedes llevan los insumos?", "Llevamos los insumos básicos de cada procedimiento. Si tu médico indicó un apósito o una bolsa de estoma específica, te lo decimos al agendar para que lo tengas en casa o lo incluyamos en la cotización."),
            ("¿Pueden ir todos los días?", "Sí. Podemos programar visitas diarias, interdiarias o según lo que necesite el paciente, incluidas noches y fines de semana."),
            ("¿Qué pasa si el paciente se complica durante la visita?", "Si hay señales de alarma te lo decimos de inmediato y te orientamos para acudir a urgencias o comunicarte con su médico. La enfermería a domicilio no reemplaza la atención de urgencias."),
        ],
    },
    {
        "slug": "rehabilitacion-a-domicilio-bogota",
        "name": "Rehabilitación a domicilio",
        "menu": "Rehabilitación a domicilio",
        "h1": "Rehabilitación a domicilio en Bogotá",
        "title": "Rehabilitación a Domicilio en Bogotá | Linfedema y Lipedema | Thera+Vida",
        "desc": "Rehabilitación a domicilio en Bogotá: acompañamiento en cáncer de mama, terapia de linfedema y lipedema y terapia de compresión en casa. Agenda por WhatsApp.",
        "img": "imagen3.jpg", "img_alt": "Rehabilitación a domicilio en Bogotá",
        "img2": "imagen5.jpg", "img2_alt": "Terapia de linfedema a domicilio en Bogotá",
        "wa": "Hola Thera+Vida, quiero información sobre la rehabilitación a domicilio en Bogotá.",
        "services": ["rehabilitacion-cancer-de-mama-bogota", "terapia-linfedema-lipedema-bogota", "terapia-de-compresion-bogota"],
        "home_text": [
            "La rehabilitación a domicilio en Bogotá está pensada para procesos largos, de esos en los que la constancia importa más que cualquier otra cosa. Cuando una persona termina un tratamiento de cáncer de mama, convive con un linfedema o tiene lipedema, las sesiones se cuentan por semanas o meses, y desplazarse cada vez termina por cansar.",
            "Por eso trabajamos en casa. Acompañamos la recuperación después del cáncer de mama con ejercicios suaves y drenaje del brazo, siempre con la autorización del médico tratante. En linfedema y lipedema combinamos drenaje manual, cuidado de la piel y ejercicios, y en la terapia de compresión te ayudamos con vendajes y prendas para que el resultado de cada sesión se mantenga.",
            "Lo que más valoran las pacientes es no tener que explicar su historia cada vez. Es el mismo equipo el que va siguiendo la evolución, mide, compara y ajusta. Y como estamos en tu casa, también vemos cómo es tu día a día y te damos recomendaciones que puedes aplicar de verdad.",
            "En la página de rehabilitación a domicilio te contamos cómo trabajamos cada caso y qué puedes esperar.",
        ],
        "intro": [
            "Hay recuperaciones que no se resuelven en una semana. El linfedema después de un cáncer de mama, el lipedema o la necesidad de usar compresión todos los días piden constancia, y la constancia es mucho más fácil cuando no tienes que salir de casa para cada sesión.",
            "Hacemos rehabilitación a domicilio en Bogotá siguiendo las indicaciones del médico tratante. Nuestro trabajo es complementario a tu tratamiento: no lo reemplaza, pero sí lo hace más llevadero.",
        ],
        "why": [
            "Es el mismo equipo el que sigue tu evolución sesión tras sesión.",
            "Trabajamos con la autorización y las indicaciones de tu médico tratante.",
            "Te enseñamos ejercicios y cuidados que puedes repetir en casa entre visitas.",
            "Ajustamos los horarios a tus controles y tratamientos, incluso de noche.",
        ],
        "faqs": [
            ("¿La rehabilitación a domicilio reemplaza la fisioterapia de mi EPS?", "No. Es un acompañamiento complementario. Si ya tienes un plan de rehabilitación, trabajamos en línea con él y con lo que indique tu médico."),
            ("¿Necesito autorización médica?", "En rehabilitación después de cáncer de mama y en linfedema, sí. Antes de empezar te pedimos que tu médico tratante esté al tanto y nos cuentes sus indicaciones."),
            ("¿Cada cuánto son las sesiones?", "Depende del caso. Lo definimos en la primera visita según tu evolución, tu tratamiento y tus horarios."),
            ("¿Atienden fuera de Bogotá?", "Atendemos Bogotá y algunos municipios cercanos. Escríbenos tu dirección por WhatsApp y te confirmamos la cobertura."),
        ],
    },
]
