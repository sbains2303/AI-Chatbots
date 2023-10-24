## Fine-tuning

- Some official guidances from openai about how to fine-tune their pre-trained model, seems have a cost as well. 
- Maybe useful if we want to fine-tune it, instead of using original model.
  
https://platform.openai.com/docs/guides/fine-tuning

https://openai.com/blog/gpt-3-5-turbo-fine-tuning-and-api-updates

- Chatgpt's suggestions about fine-tuning the chatbot using openai API:
1. Choose the Appropriate Model: Select a model that supports fine-tuning. Depending on the current offerings, you might consider GPT-3, GPT-4, or other relevant models.
2. Request Fine-Tuning Access: If you haven't already, you may need to request access to OpenAI's fine-tuning platform, which allows you to fine-tune a model on your specific dataset or task.
3. Prepare Your Dataset: Create or gather a dataset that is relevant to your chatbot application. The dataset should be properly formatted and labeled, with input and output pairs or conversations.
4. Fine-Tune the Model: Follow the guidelines and documentation provided by OpenAI to fine-tune the selected model on your dataset. This process typically involves training the model on your data to make it more specialized for your specific task.
5. Integrate the Fine-Tuned Model: Once the model is fine-tuned, you can integrate it into your webpage chatbot. You can use the API provided for the fine-tuned model to send user inputs and receive model responses.
6. Monitor and Optimize: Continuously monitor the performance of your chatbot and make any necessary adjustments to improve its accuracy and usefulness.
Please note that the specific process and details may change over time as OpenAI updates its offerings and features. Therefore, I recommend referring to OpenAI's official documentation and reaching out to OpenAI directly for the most up-to-date information and guidance on fine-tuning a chatbot using their APIs.

## Additional external input documents

- A paper about how their model processes with not only text but also images.

Paper: https://arxiv.org/pdf/2303.04671v1.pdf

Code: https://github.com/microsoft/visual-chatgpt
