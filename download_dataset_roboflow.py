from roboflow import Roboflow

api_key = "5G0ggrmGr0aF2eo1iddB"
workspace_id = "sonic"
project_id = "soldier_person"
dataset_version = 1
yolo_version = "yolov8"

def download_dataset_roboflow(api_key, workspace_id, project_id, dataset_version, yolo_version):
    rf = Roboflow(api_key=api_key)
    try:
        dataset = rf.workspace(workspace_id).project(project_id).version(dataset_version).download(yolo_version)
        print("Dataset downloaded successfully.")
    
    except Exception as e:
        print(f"Error downloading image: {e}")
        
    return dataset

data = download_dataset_roboflow(api_key, workspace_id, project_id, dataset_version, yolo_version)
data