
import os
from openai import OpenAI
import requests

def generate_and_save_image(client, prompt, n=1, size="1024x1024", quality="standard",
                                file_path="generated_image.png"):
        """
        Generate an image using the DALL-E 3 model and save it to a local file.
        Parameters:
        - client: The OpenAI client instance.
        - prompt: The text prompt to generate images for.
        - n: The number of images to generate (default is 1).
        - size: The resolution of the generated images (default is "1024x1024").
        - quality: The quality of the generated images ("standard" or "hd").
        - file_path: The local file path to save the generated image (default is "generated_image.png").
        Returns:
        The file path of the saved image or None if an error occurred.
        """
        print('generating image')
        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                n=n,
                size=size,
                quality=quality
            )
            # Assuming the response structure follows the provided documentation; may need adjustments.
            if response.data:
                image_url = response.data[0].url
                # Download the image content
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    # Save the image to a file
                    with open(file_path, 'wb') as file:
                        file.write(image_response.content)
                    print(f"Image saved to {file_path}")
                    return file_path
                else:
                    print("Failed to download the image.")
                    return None
            else:
                print("No images returned from the API.")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


def main():
    print('hello')
    client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
    )

    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": "Say this is a test",
    #         }
    #     ],
    #     model="gpt-3.5-turbo",
    # )
    generate_and_save_image(client, 'monkey')

if __name__ == '__main__':
    main()
 