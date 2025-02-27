from imageai.Detection import ObjectDetection

detector = ObjectDetection()
model_path = "path/to/retinanet.h5"  # Download the RetinaNet model file
input_image = "path/to/input_image.jpg"
output_image = "path/to/output_image.jpg"

detector.setModelTypeAsRetinaNet()
detector.setModelPath(model_path)
detector.loadModel()

detections = detector.detectObjectsFromImage(input_image, output_image)
for detection in detections:
    print(f"{detection['name']} : {detection['percentage_probability']}")

print("Object detection completed. Output saved to", output_image)

