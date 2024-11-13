from moviepy.editor import VideoFileClip


def calcular_bitrate(tamano_deseado_gb, duracion_segundos):
    """
    Calcula el bitrate necesario para alcanzar un tamaño de archivo específico.

    :param tamano_deseado_gb: Tamaño deseado del archivo de salida en GB.
    :param duracion_segundos: Duración del video en segundos.
    :return: Bitrate en bits por segundo.
    """
    tamano_deseado_bytes = (
        tamano_deseado_gb * 1024 * 1024 * 1024
    )  # Convertir GB a bytes
    bitrate_bps = (
        tamano_deseado_bytes * 8
    ) / duracion_segundos  # Bitrate en bits por segundo
    bitrate_kbps = bitrate_bps / 1000  # Convertir a kbps
    return f"{int(bitrate_kbps)}k"  # Convertir a formato '500k'


def reducir_calidad_video(ruta_entrada, ruta_salida, tamano_deseado_gb):
    """
    Reduce la calidad de un video para alcanzar un tamaño de archivo específico.

    :param ruta_entrada: Ruta del archivo de video de entrada.
    :param ruta_salida: Ruta donde se guardará el archivo de video de salida.
    :param tamano_deseado_gb: Tamaño deseado del archivo de salida en GB.
    """
    # Cargar el video
    video = VideoFileClip(ruta_entrada)

    # Calcular el bitrate necesario para el tamaño deseado
    bitrate = calcular_bitrate(tamano_deseado_gb, video.duration)

    # Reducir la calidad y exportar el video con el nuevo bitrate
    video.write_videofile(
        ruta_salida, codec="libx264", bitrate=bitrate, audio_codec="aac"
    )

    print(f"Video guardado en {ruta_salida} con bitrate {bitrate}")


# Ejemplo de uso
ruta_video_entrada = "C:\\Users\\User\\Videos\\robot.mp4"
ruta_video_salida = "C:\\Users\\User\\Videos\\Robotsalvaje(2024).mp4"
tamano_deseado_gb = 0.9  # Tamaño máximo deseado en GB (equivalente a 900 MB)

reducir_calidad_video(ruta_video_entrada, ruta_video_salida, tamano_deseado_gb)
