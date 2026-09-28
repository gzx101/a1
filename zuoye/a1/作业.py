from PIL import Image
import matplotlib.pyplot as plt

def flip_left_right(img):
    """
    图片左右翻转函数
    :param img: 输入PIL Image图片对象
    :return: 左右翻转后的图片对象
    """
    # 左右翻转：transpose(Image.FLIP_LEFT_RIGHT)
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return flipped_img


def show_two_images(original_img, flipped_img):
    """同时显示原图和翻转后的图片""