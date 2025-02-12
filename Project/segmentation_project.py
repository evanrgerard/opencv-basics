from slider import (Sliders)

def main():
	slider = Sliders(image_path = "../Resources/test_image1.jpg", slider_type = "HSV", image_scale = 1, num_blur_passes = 1, blur_filter_size = (3, 3))
	slider.Start_Slider_Display()

if __name__ == "__main__":
	main()