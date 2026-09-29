from PIL import Image

def flip_left_right(input_img: Image.Image) -> Image.Image:
    """
    图片左右翻转函数
    :param input_img: 输入图片对象
    :return: 左右翻转后的图片对象
    """
    flipped_img = input_img.transpose(Image.FLIP_LEFT_RIGHT)
    return flipped_img

if __name__ == "__main__":
    # 读取图片，替换成你自己图片路径
    origin_img = Image.open("my_pic.jpg")
    # 调用翻转函数
    result_img = flip_left_right(origin_img)
    # 在屏幕同时显示原图和翻转后的图片
    print("====原始图片====")
    origin_img.show()
    print("====左右翻转图片====")
    result_img.show()
