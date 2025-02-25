import json
from openocr import OpenOCR
#olaa
def process_ocr_results(results):
    """
    Extracts and combines OCR transcriptions into a single string.
    """
    try:
        # Ensure results are in the expected format
        if results and isinstance(results, list) and results[0]:
            # Extract the JSON part from the first entry and parse it
            raw_json = results[0].split("\t", 1)[1]
            parsed_results = json.loads(raw_json)
            return " ".join(item.get('transcription', '') for item in parsed_results)
        else:
            print("Unexpected or empty OCR results.")
    except (IndexError, KeyError, json.JSONDecodeError) as e:
        print(f"Error processing OCR results: {e}")
    return None

def main():
    image_path = "image6.png"

    try:
        engine = OpenOCR()
        results, elapse = engine(image_path)

        # Debug: Print raw results
        print(f"Raw OCR Results: {results}")

        # Process results
        processed_text = process_ocr_results(results)
        if processed_text:
            print(f"Extracted Text:\n{processed_text}")
            print(f"Time Elapsed: {elapse:.2f} seconds")
        else:
            print("No valid text extracted.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Ensure any resources used by OpenOCR are cleaned up
        if hasattr(engine, 'close'):
            engine.close()

if __name__ == "__main__":
    main()
