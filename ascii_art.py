from PIL import Image

# 1. 定义用来表示不同亮度的字符（从暗到亮）
# 字符越“密集”代表颜色越深
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """缩放图片，保持比例，并针对字符高度进行微调"""
    width, height = image.size
    # 因为字符通常比像素高，所以高度要额外缩小一点（0.55是常用比例）
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    return image.resize((new_width, new_height))

def grayify(image):
    """将图片转换为灰度图（黑白）"""
    return image.convert("L")

def pixels_to_ascii(image):
    """根据像素亮度值映射到 ASCII 字符"""
    pixels = image.getdata()
    # 将 0-255 的亮度值映射到 11 个字符索引上
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

def main(image_path, new_width=100):
    # 尝试打开图片
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"无法打开图片: {e}")
        return

    # 处理流程
    new_image_data = pixels_to_ascii(grayify(resize_image(image, new_width)))
    
    # 格式化成字符串：每隔 new_width 个字符换一行
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width)])

    # 打印到屏幕
    print(ascii_image)

    # 保存到文本文件
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
    print(f"\n成功！字符画已保存到 ascii_image.txt")

# --- 修改这里：把 'test.jpg' 改成你的图片文件名 ---
if __name__ == "__main__":
    image_name =  r"C:\Users\CNY GUO\Desktop\fun\test.jpg.jpg"  # 确保这张图在文件夹里
    main(image_name)