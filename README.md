# WhatToDrinkTonight-

Generating Text Embeddings with Azure OpenAI without fearing exposing your data and Storing in MongoDB Atlas.

## Introduction:
In the world of Natural Language Processing (NLP), text embeddings have emerged as a powerful technique for converting textual data into numerical representations that can be easily processed by machine learning models. This article dives into the exciting realm of generating text embeddings using Azure OpenAI and explores how these embeddings can be stored in MongoDB Atlas, a managed database solution. We will also investigate the potential differences in storage volume between databases with and without embeddings. This article is part of a series aimed at providing a comprehensive guide to utilizing text embeddings for various NLP tasks.


## What is text embedding?
Text embeddings are numerical representations of text that capture the semantic meaning and context of words and sentences. These embeddings allow machines to understand and process textual data, enabling various NLP tasks such as sentiment analysis, named entity recognition, and more.

## Getting Started with Azure OpenAI
Azure OpenAI provides a powerful platform for natural language processing tasks. One of its capabilities is generating text embeddings. By utilizing their API, you can seamlessly integrate text embeddings into your applications.

Before you begin, make sure you have the necessary tools and credentials in place. Install the required Python libraries, and obtain your Azure OpenAI API key.


Ensure that you have the necessary JSON dataset containing the text data you want to generate embeddings for.

I downloaded a wine review dataset from Kaggle. There are 130k reviews in this dataset, since I am not sure how much would it cost me to generate embeddings I reduces the dataset to 312 reviews.

## Generating Text Embeddings with Azure OpenAI
In this section, we’ll walk you through the process of generating text embeddings using Azure OpenAI.

Below is my code example showcasing how to generate text embeddings using the Azure OpenAI API. This code assumes you’ve set up your environment and obtained your API key.

```
import os
from dotenv import load_dotenv
import json

# Add OpenAI import
import openai

def get_embedding(query):
    # Call OpenAI API to get the embeddings.
    response = openai.Embedding.create(
        input=query,
        # Your deployment name
        engine="YourDeploymentName" 
    )
    embeddings = response['data'][0]['embedding']
    print(embeddings)
#    if response.status_code == 200:
    return embeddings
    #return response['data'][0]['embedding']
 #   else:
 #     raise Exception(f"Failed to get embedding. Status code: {response.status_code}")


def main(): 
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_model = os.getenv("AZURE_OAI_MODEL")
        
        # Set OpenAI configuration settings
        openai.api_type = "azure"
        openai.api_base = "Your azure OPEN AI endpoint"
        openai.api_version = "2023-03-15-preview"
        openai.api_key = "YOUR API KEY"
        # Load the JSON dataset
        with open('winereview_small.json', 'r') as json_file:
            wine_data = json.load(json_file)
            for wine in wine_data:
                description = wine['description']
                print("Description: " + description + "\n")


        # Replace this with actual embedding generation logic using libraries like spaCy or transformers
                description_embeddings = get_embedding(description)  # Placeholder embeddings
        
                wine['description_embeddings'] = description_embeddings

            #print("Summary: " + description_embeddings + "\n")
        
        with open('winereview_small_embeddings.json', 'w') as json_file:

            json.dump(wine_data, json_file, indent=4)
                 
    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()  
```  
  
The code begins by importing the necessary libraries and setting up the environment. It defines a function get_embedding that calls the Azure OpenAI API to generate embeddings for a given text input. The main function loads your JSON dataset, processes each entry, generates embeddings, and appends them to the dataset. The updated dataset is then saved to a new JSON file.

Once your run the script with the following command:

python embedding_generation.py
After running the code, you’ll have a new JSON file containing the original data with added description_embeddings embedding fields. These fields hold the generated embeddings for the corresponding descriptions.

## Upload JSON file into your managed MongoDB
I usually use Compass (Compass is a free interactive tool for querying, optimizing, and analyzing your MongoDB data.) to upload data into MongoDB which is the easiest way according to me.



Once I uploaded my two datasets of wine reviews: one with embeddings and another one without embedding, we could see the storage is not the same.


## Conclusion
Generating text embeddings using Azure OpenAI opens up possibilities for enhancing your NLP applications. You can now use these embeddings for various tasks like clustering, classification, and recommendation systems. Explore advanced models, try different engines, and fine-tune your embedding generation process to suit your specific needs.

In this article, we’ve demonstrated how to generate text embeddings with Azure OpenAI using practical code examples. Armed with this knowledge, you’re ready to leverage the power of embeddings in your own projects and applications.
