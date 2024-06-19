using System;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Embeddings;
using OpenAI_API;
using OpenAI_API.Embedding;
using OpenAI_API.Models;

public class OpenAIEmbedder
{
    private readonly OpenAIAPI _apiClient;
    private readonly string _model;

    public OpenAIEmbedder(OpenAIAPI apiClient, string model = "text-embedding-3-large")
    {
        _apiClient = apiClient;
	_model = model;
    }

    public async Task<float[]> EmbedAsync(string text)
    {
        EmbeddingRequest embedRequest = new EmbeddingRequest
	{
	    Input = text,
	    Model = _model
	};

	EmbeddingResult response = await _apiClient.Embeddings.CreateEmbeddingAsync(embedRequest);

	if(response.Data != null && response.Data.Count > 0)
	{
	    return response.Data[0].Embedding.Select(Convert.ToSingle).ToArray();
	}
	throw new Exception("Embedding generation failed");
    }
}

class Program
{
    static async Task Main(string[] args) 
    {
        String? apiKey = Environment.GetEnvironmentVariable("OPENAI_API_KEY");
	if(string.IsNullOrEmpty(apiKey)) 
	{
	    Console.WriteLine("Please set OPENAI_API_KEY environment variable");
	    return;
	}
        OpenAIAPI openAIApiClient = new OpenAIAPI(new APIAuthentication(apiKey));
	OpenAIEmbedder embedder = new OpenAIEmbedder(openAIApiClient);

	string inputText = "This is a simple text.";
	float[] embedding = await embedder.EmbedAsync(inputText);

	Console.WriteLine("Embedding:");
	foreach(float value in embedding)
	{
	    Console.Write($"{value} ");
	}
    }
}
