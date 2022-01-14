# Rynchops
A Fast Abstractive Summarization & Translation Demo App

![An Image of Rynchops niger (Black Skimmer) skimming water.](https://upload.wikimedia.org/wikipedia/commons/2/27/Black_skimmer_%28Rynchops_niger%29_in_flight.jpg)
_Rynchops niger (Black Skimmer) skimming in flight by [Charles J. Sharp](https://en.wikipedia.org/wiki/File:Black_skimmer_(Rynchops_niger)_in_flight.jpg). [Skimmers fly low and fast aross the surface of the water with their lower beak submerged to catch and eat fish](https://youtu.be/Rg6k-9tkhYA). Image from Wikimedia Commons, available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)._

This repository contains an app to demonstrate the proof-of-concept for the Fast Abstractive Summarization & Translation project. The app is a streamlit application that runs in the browser. It utilizes a number of machine learning models.

## Running The Application

### Prerequisites
The Rynchops app requires several python packages. To run the app, one needs Python and a package manager. We use Conda as our package manager.
  * [Python 3.7+](https://www.python.org/downloads/)
  * [Conda Package Manager](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

### Obtaining This Code
To run the app, you will need this code. The best way to obtain the code is to "clone" it. This is a proccess that copies the code to your computer and sets up a [git repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories) in it. This allows you to get updates to the code whenever this repository is updated, and allows you to contribute your own code to this repository. To clone a git repository, please refer to the official documentation, ["Cloning a repository"](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

### Creating the Conda Environment
The packages for the app are listed in `environment.yml`. You will need to install those packages with conda. To do so, once you have installed conda and python and downloaded the , you may create an environment containing the packages with the following command.
```bash
conda create -f environment.yml
```

## POCs
The points of contact for this project are [Elias Jaffe](https://github.com/Ejjaffe) & Mike Brasseur.

(c) ATS 2021

![Video](<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Rg6k-9tkhYA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>)

![](https://www.youtube-nocookie.com/embed/Rg6k-9tkhYA)








# Prod
```bash
conda activate rynchops
streamlit run app.py
```
![Screenshot of app summarization translation](img/screenshot1.png)

# Roadmap
## Phase 1: Demo
```
Input -> Chunker for variable size output -> Same-language Summarizer Model -> Translator -> Output
                              |-> NER 
```
1. Model Pipelining
2. Demo Application Development

## Phase 2: Product Development
```
Input -> Chunker for variable size output -> Cross-language Summarizer Model -> Output
                               | -> NER
```
1. Data Collection
2. Dataset labeling
3. Model training
4. Develop Service Platform

