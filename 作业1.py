from PIL import Image

def flip_image_left_right(img: Image.Image) -> Image.Image:
    """
    将输入图片进行左右翻转
    :param img: PIL Image对象，输入原图
    :return: PIL Image对象，左右翻转后的图片
    """
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return flipped_img