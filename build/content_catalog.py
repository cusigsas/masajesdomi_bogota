# -*- coding: utf-8 -*-
"""Catálogo de servicios: primero masajes y drenajes, después rehabilitación y enfermería."""

CATALOG = {
    "title": "Catálogo de Masajes y Servicios a Domicilio en Bogotá | Thera+Vida",
    "desc": "Catálogo de masajes a domicilio en Bogotá: antiestrés, drenaje linfático, postoperatorio, colon, celulitis y más. También enfermería y rehabilitación. Agenda por WhatsApp.",
    "h1": "Catálogo de masajes y servicios a domicilio en Bogotá",
    "lead": "Elige el masaje o el servicio que necesitas y agéndalo directo por WhatsApp. Vamos a tu casa en Bogotá las 24 horas, con todo lo necesario para la sesión.",
    "wa": "Hola Thera+Vida, vi el catálogo y quiero agendar un servicio a domicilio en Bogotá.",
}

# Cada grupo: id del ancla, título (H2), texto, etiqueta del botón y servicios con su texto corto
CATALOG_GROUPS = [
    {
        "id": "masajes",
        "title": "Masajes y drenajes a domicilio",
        "text": "Masajes terapéuticos y drenajes hechos en tu casa, con camilla, aceites y toallas incluidos. La terapeuta ajusta la técnica y la presión a lo que tu cuerpo necesita ese día.",
        "button": "Quiero este masaje",
        "featured": True,
        "items": [
            ("masaje-antiestres-bogota", "Masaje antiestrés",
             "Para el cuello rígido, los hombros cargados y la cabeza que no se apaga. Maniobras lentas y profundas en espalda, cuello y hombros."),
            ("drenaje-linfatico-manual-bogota", "Drenaje linfático",
             "Maniobras suaves y rítmicas que ayudan a mover el líquido retenido. Ideal para piernas pesadas e hinchadas al final del día."),
            ("drenaje-postoperatorio-bogota", "Drenaje postoperatorio",
             "Después de liposucción, abdominoplastia o cirugía de mama, según la indicación de tu cirujano. Te ayudamos con la faja."),
            ("masaje-para-el-colon-bogota", "Masaje para el colon",
             "Malaxación colónica: masaje abdominal que acompaña el movimiento del intestino. Apoyo para el estreñimiento y la inflamación."),
            ("tratamiento-de-celulitis-bogota", "Masaje para celulitis",
             "Activación circulatoria, amasamiento y drenaje en piernas, glúteos y abdomen para mejorar la textura de la piel por sesiones."),
            ("drenaje-venoso-bogota", "Drenaje venoso",
             "Maniobras ascendentes para piernas cansadas, calambres nocturnos y tobillos hinchados. Buen complemento de las medias de compresión."),
        ],
    },
    {
        "id": "rehabilitacion",
        "title": "Rehabilitación a domicilio",
        "text": "Acompañamiento constante en casa para procesos largos, siempre con la autorización y las indicaciones de tu médico tratante.",
        "button": "Quiero este servicio",
        "featured": False,
        "items": [
            ("terapia-linfedema-lipedema-bogota", "Terapia de linfedema y lipedema",
             "Drenaje manual, compresión, cuidado de la piel y ejercicios, con seguimiento de medidas en cada visita."),
            ("rehabilitacion-cancer-de-mama-bogota", "Rehabilitación en cáncer de mama",
             "Movilidad del hombro, drenaje del brazo y prevención del linfedema después de la cirugía."),
            ("terapia-de-compresion-bogota", "Terapia y manejo de compresión",
             "Vendaje multicapa y ajuste de medias o prendas para mantener el resultado del drenaje."),
        ],
    },
    {
        "id": "enfermeria",
        "title": "Servicios de enfermería a domicilio",
        "text": "Procedimientos de enfermería en casa, con insumos y siguiendo las indicaciones del médico tratante. Atendemos de día, de noche y fines de semana.",
        "button": "Quiero este servicio",
        "featured": False,
        "items": [
            ("manejo-de-heridas-y-ulceras-bogota", "Manejo de heridas y úlceras por presión",
             "Curaciones en casa para úlceras por presión, heridas quirúrgicas y lesiones de difícil cicatrización."),
            ("cuidado-de-estomas-bogota", "Colocación y limpieza de estomas",
             "Cambio de bolsa, cuidado de la piel y enseñanza para colostomía, ileostomía y urostomía."),
            ("control-de-signos-vitales-bogota", "Control de signos vitales",
             "Presión arterial, pulso, oxigenación, temperatura y glucometría, con registro para tu médico."),
            ("podologia-a-domicilio-bogota", "Podología especializada",
             "Corte de uñas, callosidades y cuidado preventivo del pie diabético, con instrumental esterilizado."),
        ],
    },
]

CATALOG_FAQS = [
    ("¿Cómo agendo un servicio del catálogo?", "Toca el botón del masaje o servicio que quieres. Se abre WhatsApp con el mensaje listo; solo agrega tu barrio y el horario que prefieres, y te respondemos con la cotización y la disponibilidad."),
    ("¿Puedo combinar varios servicios en una visita?", "Sí. Por ejemplo, drenaje linfático con masaje para celulitis, o control de signos vitales con podología. Cuéntanos qué quieres combinar y te armamos la cotización."),
    ("¿Por qué el catálogo no muestra precios?", "El valor depende del servicio, la duración, la cantidad de sesiones y la zona de Bogotá. Te enviamos el precio exacto por WhatsApp antes de agendar, sin compromiso."),
]
