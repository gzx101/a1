from PIL import Image

def flip_image_left_right(img: Image.Image) -> Image.Image:
    """
    将输入图片进行左右翻转
    :param img: PIL Image对象，输入原图
    :return: PIL Image对象，左右翻转后的图片
    """
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return flipped_img

# ========== 测试代码 ==========
if __name__ == "__main__":
    # 读取图片，替换为你的图片路径
    original_img = Image.open("test.jpg")
    # 调用翻转函数
    result_img = flip_image_left_right(original_img)
    # 保存翻转后的图片
    result_img.save("flipped_test.jpg")
    # 展示图片
    original_img.show()
    result_img.show()