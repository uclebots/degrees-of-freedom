from pytest import fixture

import pandas as pd
from pathlib import Path

from misa.dataaccess import CommentsDataSet, Comments, Post
from misa.constants import COLUMNS, COMMENT_COLUMNS
_PARQUET_FILENAME = "./test/dev.parquet"

_TITLE = "China ofrece un crédito multimillonario para que Latinoamérica pueda acceder a la vacuna contra el coronavirus"
_CONTEXT_TWEET = 'Wuhan celebra el fin de la cuarentena por el coronavirus con un mensaje para el resto del mundo: "Aprendan de nuestros errores" https://t.co/mBLG1XfOGD'
_BODY = 'Miles de chinos celebraron con euforia este miércoles 8 de abril el final de más de dos meses de confinamiento en Wuhan, cuna de la pandemia de coronavirus. Mientras tanto, el virus no da tregua a Estados Unidos y Europa, donde no se logra generar una respuesta económica unificada y las muertes volvieron a aumentar en España\u200b.\n\nEn medio de la aterradora marcha del nuevo coronavirus, el mundo vio una luz de esperanza con la imágenes de miles de pasajeros que a partir de la medianoche del martes empezaron a tomar por asalto estaciones de micros y trenes, algunos de ellos con atuendos de protección integral, en Wuhan, la capital de la provincia china de Hubei.\n\n"Me levanté a las cuatro hoy. ¡Me siento tan bien!", dijo una feliz Hao Mei, de 39 años y oriunda de Enshi, ciudad a 450 kilómetros al oeste de Wuhan. Estaba a punto de subirse a un tren para regresar con sus dos hijos, a los que tuvo que dejar solos durante más de dos meses, ya que quedó atrapada a fines de enero en Wuhan. El encierro empezó el 23 de enero, y se prolongó por dos meses y medio.\n\n"Al principio, lloraba cada noche. Me sentía mal, porque mi hija es aún muy joven. Tiene apenas diez años", dijo.\n\nUn taxista limpia su auto en una parada de taxis en Wuhan, la ciudad epicentro de la pandemia de coronavirus que salió de la cuarentena. / Xinhua\n\nSe calcula que al menos 65 mil personas abandonaron la ciudad china una vez que se levantaron las restricciones para viajar a la población de 11 millones de habitantes. Innumerables automóviles y buses atravesaban los peajes en los límites de la ciudad tras levantarse los controles de carretera, según constató la AFP.\n\nSin contar el tráfico vehicular, 55 mil personas se tomaron el tren, mientras que más de 10 mil optaron por el avión tras la reapertura del Wuhan Tianhe, el aeropuerto local, donde ya hay más de 200 vuelos ida y vuelta. Por ahora están excluidas las conexiones internacionales, como así también los viajes hacia Beijing. Quien quiere ir a la capital, según los medios locales, tendrá que someterse a un test anticoronavirus en Wuhan y al llegar.\n\nWuhan fue por lejos el lugar más golpeado en China\u200b por la epidemia. Cerca de 2500 personas murieron en esta ciudad, del total de más de 3330 fallecimientos oficialmente registrados en todo el país.\n\nQué es el Coronavirus Cómo se contagia y cómo son sus síntomas Mirá el especial\n\nEsta ciudad, donde apareció el nuevo coronavirus a fines de 2019, fu la primera del mundo en sufrir un draconiano aislamiento con todos sus habitantes confinados.\n\nCon la propagación del virus a todo el mundo, varios países adoptaron medidas similares. Hoy, la mitad de la humanidad está de una manera u otra confinada.\n\nEn Wuhan, la cuarentena parece haber dado resultados, tras una espectacular reducción en las últimas semanas de los casos de contaminación y de muertes en China. El martes, Beijing anunció por primera vez cero muertos por el nuevo coronavirus desde que surgió la pandemia.\n\nSin embargo, existen dudas sobre la fiabilidad de las cifras oficiales de muertos. Varias familias han indicado que personas muertas en sus domicilios no fueron contabilizadas, o no fueron sometidas a análisis al principio de la epidemia, cuando los hospitales estaban desbordados.\n\nImagen combinada de la calle Chuhehan en Wuhan, provincia de Hubei, en el centro de China, el 26 de enero de 2020 (arriba) y el 8 de abril de 2020 (abajo). China, levantó las restricciones a los viajes de salida a partir del miércoles después de cerca de 11 semanas de confinamiento para frenar la propagación de la COVID-19. /Xinhua\n\n"Una ciudad de héroes"\n\nEn un video publicado por la cadena británica BBC, numerosos residentes de Wuhan narraron cómo fue la experiencia de pasar aislados las 11 semanas. En medio del relato sobre las costumbres que debieron modificar hasta cómo se hace para llevar adelante la convivencia en esas condiciones, sobresalió el mensaje que buscaron transmitirle al resto del mundo que sigue transitando los momentos más duros de la pandemia.\n\n"Espero que el resto de la gente pueda aprender de Wuhan, así otros no tienen que sacrificarse tanto y se cometen menos errores. Aprendan de nuestros errores", afirma una chica con barbijo mientras mira a la cámara.\n\nPasajeros abordan un taxi frente a la Estación de Trenes de Hankou en Wuhan, provincia de Hubei, en el centro de China. La ciudad epicentro de la cuarentena abandonó el encierro luego de 11 semanas. /XINHUA\n\n"En vez de decir que la cuarentena fue un sacrificio, prefiero decir que la ciudad hizo un sacrificio para luchar contra la pandemia. Todo el que se queda en casa está contribuyendo", explica otra mujer.\n\nTodos advierten contra los riesgos domésticos y laborales que conlleva una situación. Para quienes conviven con otros, tratar de ser más comunicativos y pacientes, y para quienes tienen la suerte de poder seguir trabajando, saber cortar a tiempo y establecer una separación entre las horas laborales y las de tiempo libre.\n\n"Wuhan merece ser llamada una ciudad de héroes", decía un mensaje divulgado el miércoles en una estación de la ciudad.\n\n"Los habitantes de Wuhan pagaron un elevado precio", declaró a AFP Yao, un joven de 21 años, que embarca en tren hacia Shanghai (este), donde trabaja en un restaurante. "Nos alegra que se levante el encierro".\n\nEn una estación, un robot circula en medio de la muchedumbre de pasajeros, arrojando desinfectante a sus pies, mientras emite un mensaje grabado en el que se insta a todos a portar mascarilla.\n\nLos pasajeros deben someterse a controles de temperatura y mostrar en su smartphone un código QR verde. Éste es entregado por las autoridades y permite demostrar que no se está contaminado por el covid-19 ni se reside en un barrio considerado aún de alto riesgo.\n\nLa prensa china saludaba de forma unánime el levantamiento de la cuarentena. Con un titular recurrente: : "Wuhan, feliz de volverte a ver después de todo este tiempo".\n\nLos habitantes de Wuhan empiezan a retomar su vida normal luego de que las 11 semanas de cuarentena por el coronavirus finalmente se levantaran. / AP\n\nPero, pese al levantamiento del bloqueo, el retorno a la normalidad no será inmediato.\n\nSe mantendrán diversas restricciones para evitar una segunda oleada epidémica. Las escuelas siguen cerradas. Y se insta a los habitantes a no dejar la ciudad, y ni siquiera sus domicilios. Además, ante los temores que generan los habitantes de Wuhan en otros lugares del país, quienes quieran irse deberán someterse en varios casos a una cuarentena de 14 días en su ciudad de destino.\n\nEn Europa y Estados Unidos, una lucha sin cuartel\n\nSi la pandemia parece controlada en China (donde surgió a fines de diciembre), la situación en otras parte del mundo sigue siendo complicada. El virus continúa haciendo estragos en Estados Unidos, que registró un récord mundial de cerca de 2.000 muertos en las últimas 24 horas, y también en Europa, el continente más afectado con más de 57.000 decesos.\n\nAcechados por este enemigo invisible y confinados desde hace semanas, los europeos asisten, impotentes, a la destrucción de su economía, y los gobiernos de la UE no logran ponerse de acuerdo sobre un plan conjunto para enfrentar la debacle.\n\nTras una noche entera de negociaciones el martes en Bruselas, los países del norte seguían oponiéndose a los del sur, que reclaman un esfuerzo financiero sin precedentes.\n\nEl presidente de Estados Unidos, Donald Trump, todavía sigue enfrascado en una batalla por detener la expansión del coronavirus. / AFP\n\n"Tras 16 horas negociando, nos acercamos a un acuerdo, pero todavía no lo logramos. Suspendí el Eurogrupo" y seguiremos "mañana jueves", escribió el ministro portugués y presidente del Eurogrupo, Mario Centeno, el miércoles a primera hora, en su cuenta en la red social Twitter.\n\nUnos 1.250 millones de trabajadores corren el riesgo de ser despedidos o de que les reduzcan el salario, anunció la Organización Internacional del Trabajo (OIT), que vaticinó que los trabajadores del mundo podrían perder 3,4 billones de dólares en ingresos este año por la pandemia.\n\nEn Estados Unidos, el gobierno del presidente Donald Trump inició nuevas negociaciones con el Congreso para liberar 250.000 millones de dólares adicionales para salvar empleos en las pequeñas y medianas empresas.\n\nTrump también amenazó con suspender el financiamiento de Washington a la Organización Mundial de la Salud (OMS), acusando al organismo de la ONU de mal manejo de la pandemia y de una actitud sesgada hacia Beijing.\n\nEl mundo se encamina hacia la cifra simbólica de 100.000 muertos. El recuento, a partir de cifras oficiales, se encuentra sin embargo por debajo de la realidad, ya que muchas personas mueren sin que se les hay efectuado el test y lejos de los hospitales.\n\nEn América Latina, todavía relativamente a salvo de la pandemia, se han registrado unas 1400 muertes sobre más de 36.000 casos, de los cuales más de un tercio en Brasil (unos 14.000, con casi 700 muertos).\n\nFuente: AP, ANSA, AFP y BBC'

@fixture
def sample_dataframe():
    return pd.DataFrame(
        [(
          _TITLE, 
          _CONTEXT_TWEET, 
          _BODY,
          345556, 
          "@usuario Estos ñatos la tienen clara eh!", 
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
         (
          _TITLE, 
          _CONTEXT_TWEET, 
          _BODY,
          345567, 
          "@usuario La concha de tu madre China.", 
          1, 0, 0, 1, 0, 0, 0, 0, 0, 0),
         (
          _TITLE, 
          _CONTEXT_TWEET, 
          _BODY,
          345560, 
          "@usuario Más que ofrecer un crédito China debería PAGAR TODAS LAS VACUNAS !!!!\nMás de 600.000 muertos en el mundo por no haber tomado las medidas correspondientes en su momento. Deberían hacerse cargo de los daños como ha ocurrido con algunos países después de la guerra", 
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        ], 
        columns=COLUMNS)

# TODO: context manaher
def run_in_context(mocker, sample_dataframe, fn):
    Path("./test").mkdir(exist_ok=True)        
    with open(_PARQUET_FILENAME, "wb") as f:        
        sample_dataframe.to_parquet(f, index=False)
    with open(_PARQUET_FILENAME, "rb") as f:
        f.stem = "dev"

        mocker.patch("misa.dataaccess.Path.glob", return_value=[f])
        fn()    

def test_constructor(mocker, sample_dataframe):
    def assertion():
        assert CommentsDataSet("./test").datasets["dev"].raw().equals(sample_dataframe)
    
    run_in_context(mocker, sample_dataframe, assertion)
        
def test_dataset_by_name(mocker, sample_dataframe):
    def assertion():
        assert CommentsDataSet("./test").dataset("dev").raw().equals(sample_dataframe)
    run_in_context(mocker, sample_dataframe, assertion)
        

def test_dataset(mocker, sample_dataframe):
    def assertion():
        assert CommentsDataSet("./test").dataset().raw().equals(sample_dataframe)
    run_in_context(mocker, sample_dataframe, assertion)
        
def test_posts(sample_dataframe):
    assert Comments(sample_dataframe).posts() == [Post(
        _TITLE, 
        _CONTEXT_TWEET, 
        _BODY, sample_dataframe[COMMENT_COLUMNS])]
    
def test_post_eq(sample_dataframe):
    assert Post(
        _TITLE, 
        _CONTEXT_TWEET, 
        _BODY, sample_dataframe[COMMENT_COLUMNS]) != "aString"    
