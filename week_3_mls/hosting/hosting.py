from huggingface_hub import HfApi

import os

api = HfApi(token=os.getenv("HF_TOKEN"))
print("Pushing to HF")

api.upload_folder(
    folder_path="week_3_mls/deployment",     # the local folder containing your files
    #repo_id="praneeth232/Machine-Failure-Prediction",          # the target repo
    repo_id="rajaramsblr/Machine-Failure-Prediction-CICD",
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
