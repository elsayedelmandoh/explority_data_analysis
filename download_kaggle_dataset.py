from google.colab import files
import os
def download_kaggle_dataset(username, dataset_name, target_dir='/content'):
    # Step 1: Upload kaggle.json
    uploaded = files.upload()

    # Step 2: Move the uploaded kaggle.json file to the appropriate directory
    os.makedirs('/root/.kaggle', exist_ok=True)
    os.rename('kaggle.json', '/root/.kaggle/kaggle.json')

    # Step 3: Set permissions for the Kaggle API key
    !chmod 600 /root/.kaggle/kaggle.json

    # Step 4: Download the dataset from Kaggle
    download_command = f'kaggle datasets download -d {username}/{dataset_name} -p {target_dir}'
    !{download_command}

    # Step 5: Unzip the downloaded dataset
    unzip_command = f'unzip -q {target_dir}/{dataset_name}.zip -d {target_dir}/dataset'
    !{unzip_command}

download_kaggle_dataset(username='paultimothymooney', dataset_name='chest-xray-pneumonia', target_dir='/content')
