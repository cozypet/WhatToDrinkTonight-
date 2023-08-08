import os
from dotenv import load_dotenv
import json

# Add OpenAI import
import openai

def get_embedding(query):
    # Call OpenAI API to get the embeddings.
    response = openai.Embedding.create(
        input=query,
        engine="hanembeddings"
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
        openai.api_base = "https://openaitesthan.openai.azure.com/"
        openai.api_version = "2023-03-15-preview"
        openai.api_key = "b3c6120c8b9f4c23a932bd3833d61d34"
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
  
  
  
