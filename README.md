# Computational Methods for Particle Physics


Lecture slides, jupyter notebooks and datasets that go along with the lecture series to introduce computation methods and tools that might be useful for particle physics research. The lectures were initially put together by Matthew Bass and modified by Giacomo Artoni. This is the updated version for 2022.

There are four lectures in total and material for each can be found in the dedicated folder. External datasets are in the Dataset folder so make sure to always grab those.

All of the examples require a working python implementation 

## Possible ways to get the data

- Download the content of the gitlab repository or single directories as a zip file
- Import it directly into your personal gitlab/github

## Running the code

There are various ways to run the code.

### On your local machine

1. Make sure you have a running python installation including the necessary packages for jupyter notebooks
2. In your terminal from the desired folder type `jupyter notebook`
3. A browser window will open with an interactive jupyter notebook session

### CERN SWAN

1. Go to [https://swan.cern.ch](https://swan.cern.ch) and log in. You can pick any flavour of VM: it doesn't matter much.
2. Click on the + button to add a project, and enter `https://gitlab.cern.ch/oxford-physics/cmpp.git`
3. You can the click on any of the notebooks in the repository

### Google Colab

1. Open [this notebook](https://colab.research.google.com/drive/1ewhewi9h2fVfMno1s9n2lwK4uq2iPEn5) and run it. (You will need to authorize it to access your Google Drive.)
2. Once you have executed the above, you will have a folder My Drive > OxfordCMPP > cmpp ; open it.
3. You can then click on any of the notebooks to execute them.

### Docker

1. Build the container locally using `docker build -t cmpp docker`
2. Run the Python Notebook: `docker run --rm -it -p 127.0.0.1:8888:8888/tcp -v $(pwd):/cmpp cmpp:latest /cmpp/docker/runNotebook.sh`
3. Point your favorite browser to the URL displayed (note: pick the URL with 127.0.0.1 or replace whatever hostname is shown by localhost)
