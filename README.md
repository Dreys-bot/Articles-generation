# An AI Chatbot using GPT model fine-tuned!

![](https://github.com/Dreys-bot/Articles-generation/blob/main/demo_gif.gif)

The following video present an wep AI chatbot app to generate **articles** by using **GPT model fine-tuned**. You can look ***fine-tuning.ipynb** file to look the process on articles dataset.
It is better to turn your model on GPU on **colab** to make less time. The model is not very good due to the limitations of computing resources.

## Requirements (libraries)
1. TensorFlow
2. Torch
1. Flask

## VsCode SetUp
1. Clone the repository-> cd into the cloned repository folder
2. Create a python virtual environment 
```
# macOS/Linux
# You may need to run sudo apt-get install python3-venv first
python3 -m venv .venv

# Windows
# You can also use py -3 -m venv .venv
python -m venv .venv
```
When you create a new virtual environment, a prompt will be displayed to allow you to select it for the workspace.

3. Activate the virtual environment
```
#linux
source ./venv/bin/activate  # sh, bash, or zsh

#windows
.\venv\Scripts\activate
```
4. Run this requirements
````
!pip install -U scikit-learn scipy matplotlib
!pip install transformers
!pip install datasets
!pip install nlp
!pip install colorama
!pip install torch
````

5. To access your bot on localhost, go to ```http://127.0.0.1:5000/```

### Explanation about Transformer Model used and how to create GPT model from Strach

You can find it in [Documentation](https://github.com/Dreys-bot/Articles-generation/tree/main/Doc)

### Execution
To run this Bot, first run the ```fine-tuning.ipynb``` file to train the model. This will generate a folder named ```new-articles_GPT```<br>
This is the model which will be used by the Flask REST API to easily give feedback without the need to retrain.<br>
After running ```fine-tuning.ipynb```, next run the ```app.py``` to initialize and start the bot.<br>
To add more terms and vocabulary to the bot, modify the dataset used in ***fine-tuning.ipynb*** file file and add your personalized words and retrain the model again.


