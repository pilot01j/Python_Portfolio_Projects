import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import pixellib
from pixellib.instance import instance_segmentation


#  Donwload "mask_rcnn_ballon.h5" from https://github.com/matterport/Mask_RCNN/releases/


def detect_objecttion_on_an_image():
    segment_image = instance_segmentation(person=True)
    segment_image.load_model("C:\Python_Portfolio_Projects\ Finding_objects_in_image_(TensorFlow, PixelLib)\mask_rcnn_balloon.h5")
    target_class = segment_image.select_target_class()


    result = egment_image.segmentImage(
        image_path="city.jpg",
        show_bboxes=True,
        extrct_segmented_objects=True,
        save_extracted_objects=True,
        output_image_name = "output.jpg"
    )
    print("Objects find: ",len(result[0]["scores"]))

def main():
    detect_objecttion_on_an_image()

if __name__ == "__main__":
    main()