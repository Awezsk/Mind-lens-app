import cv2
import numpy as np
from transformers import DetrImageProcessor, DetrForObjectDetection
import torch

processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

def analyze_workspace(image_path):
    image = cv2.imread(image_path)
    results = {
        'object_count': count_objects(image),
        'back_support': analyze_back_support(image),
        'screen_distance': analyze_screen_distance(image)
    }
    return results

def count_objects(image):
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    
    # Extract results
    target_sizes = torch.tensor([image.shape[:2]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]
    
    counts = {
        'screens': 0,
        'laptops': 0,
        'keyboard': 0,
        'mouse': 0
    }
    
    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        label_name = model.config.id2label[label.item()]
        if label_name in ['tv', 'laptop']:
            counts['screens'] += 1
        if label_name == 'laptop':
            counts['laptops'] += 1
        if label_name == 'keyboard':
            counts['keyboard'] += 1
        if label_name == 'mouse':
            counts['mouse'] += 1
    
    return counts

def analyze_back_support(image):
    # This is a placeholder. In a real implementation, you'd use a pose estimation model
    # to detect the person's posture and analyze back support.
    return {
        'upper_back': 'Supported',
        'mid_back': 'Not Supported',
        'lower_back': 'Supported'
    }

def analyze_screen_distance(image):
    # This is a placeholder. In a real implementation, you'd use depth estimation
    # or other computer vision techniques to estimate the distance.
    return "One arm's length"
