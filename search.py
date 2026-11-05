
from config import tavily_client


def search_career_information(query):
    """
    Search the web for current career-related information.
    """

    try:
        response = tavily_client.search(
            query=query,
            topic="general",
            search_depth="basic",
            max_results=5
        )

        results = response.get("results", [])

        if not results:
            return "No relevant search results found."

        formatted_results = []

        for index, result in enumerate(results, start=1):
            title = result.get("title", "No title")
            content = result.get("content", "No description")
            url = result.get("url", "")

            formatted_results.append(
                f"""
Source {index}: {title}
Information: {content}
URL: {url}
"""
            )

        return "\n".join(formatted_results)

    except Exception as error:
        print("Tavily Search Error:", error)
        return "Web search is temporarily unavailable."
