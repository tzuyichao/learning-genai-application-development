using System;
using System.Threading.Tasks;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Connectors.OpenAI;

class Program
{
	static async Task Main(string[] args)
	{
		string apiKey = Environment.GetEnvironmentVariable("OPENAI_API_KEY");
		if(string.IsNullOrEmpty(apiKey))
		{
			Console.WriteLine("請設定OPENAI_API_KEY環境變數");
			return;
		}
		Kernel kernel = Kernel.CreateBuilder()
			.AddOpenAIChatCompletion(
					modelId: "gpt-3.5-turbo",
					apiKey: apiKey)
			.Build();
		string chatPrompt = """
			<message role="user">你好,請使用繁體中文</message>
			""";
		Console.WriteLine(await kernel.InvokePromptAsync(chatPrompt));
	}
}
