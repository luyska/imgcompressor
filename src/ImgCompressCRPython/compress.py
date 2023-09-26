from PIL import Image

def compress_image(path:str, dest_path:str, uquality:int=100, 
                                    uoptimize:bool=False) -> None:

    """
    Comprime una imagen tratando de no perder resolución y tratando de 
    no perder tanta calidad

    @param path La ruta de la imagen a comprimir
    @param dest_path La ruta donde se guarda la imagen comprimida
    @param uquality Indica la calidad que se va a utilizar en la imagen comprimida
    @param uoptimize Indica si se debe optimizar el proceso de compresión
    @retuns 
    """

    with Image.open(path) as img_to_compress:

        img_to_compress.save(
            dest_path,
            quality=uquality,
            optimize=uoptimize
        )

def resize_image(path:str, dest_path:str, width:int, height:int, 
                    	                    uoptimize:bool=False) -> None:

    """
    Establece un nuevo tamaño para una imagen 
    
    @param path La ruta de la imagen a comprimir
    @param dest_path La ruta donde se guarda la imagen comprimida
    @param width El ancho que tendrá la imagen
    @param height El alto que tendrá la imagen
    @param uoptimize Indica si se debe optimizar el proceso de compresión
    @retuns 
    """

    with Image.open(path) as img_to_resize:

        img_to_resize = img_to_resize.resize((width, height), Image.Resampling.LANCZOS)
        img_to_resize.save(
            dest_path,
            optimize=uoptimize
        )
