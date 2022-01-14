# Rynchops
Cross-lingual summary service.

![An Image of Rynchops niger (Black Skimmer) skimming water.](https://upload.wikimedia.org/wikipedia/commons/2/27/Black_skimmer_%28Rynchops_niger%29_in_flight.jpg)
_Rynchops niger (Black Skimmer) skimming in flight by [Charles J. Sharp](https://en.wikipedia.org/wiki/File:Black_skimmer_(Rynchops_niger)_in_flight.jpg). Image from Wikimedia Commons, available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en).


# Dev
## Getting Started

```bash
conda create -f rynchops.yml
```

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
