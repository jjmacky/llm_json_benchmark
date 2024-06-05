import pandas as pd
import os
import json
import anthropic
import sys
from instructions_config import get_instruction_1, get_instruction_2, get_instruction_3, get_instruction_4, get_instruction_5

# Define function to save Claude API response for later debugging
import json

def serialize_message(message):
    # Initialize an empty dictionary to capture various pieces of information
    serialized = {
        'id': message.id,
        'model': message.model,
        'role': message.role,
        'stop_reason': message.stop_reason,
        'type': message.type,
        'usage': {
            'input_tokens': message.usage.input_tokens,
            'output_tokens': message.usage.output_tokens
        }
    }

    # Initialize an empty list to capture content blocks
    content_blocks = []

    # Iterate through each content block in the message content
    for content_block in message.content:
        if content_block.type == 'text':
            try:
                # Attempt to parse the JSON content within the text attribute
                parsed_content = json.loads(content_block.text)
            except json.JSONDecodeError:
                # If parsing fails, use the raw text
                parsed_content = content_block.text

            content_blocks.append(parsed_content)

    # Add the parsed content blocks to the serialized output
    serialized['content_blocks'] = content_blocks

    return serialized

api_key = os.getenv("ANTHROPIC_API_KEY")
if api_key is None:
    raise ValueError("ANTHROPIC_API_KEY environment variable is not set.")

client = anthropic.Anthropic(
    api_key=api_key
)

# Define the directories for input batched files and output processed files
input_folder = 'Batched_files'
output_folder = 'JSON_results'

# Create the output directory if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print("Output folder not detected and created.")

# List all the batched files in the input directory
batched_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
print(f"Starting to process {len(batched_files)} files...")

for file_name in batched_files:
    print(f"Processing file: {file_name}")

    df = pd.read_csv(os.path.join(input_folder, file_name))
    
    # Calculate the number of words in each review
    df['word_count'] = df['text'].apply(lambda text: len(str(text).split()))

    # Initialize empty lists to store responses
    results_columns = [
        'date', 'user', 'stars', 'review_text', 'word_count', 'instruction_version', 'llm', 'error', "error_text",
        'coherence_and_clarity_of_review', 'empathy_of_ai', 'behavior_of_ai', 'inappropriate_frequency',
        'inappropriate_nature', 'ai_support_level', 'support_types', 'user_mental_state_before_ai',
        'effect_of_ai_on_user_mental_state', 'stress_before_ai', 'effect_of_ai_on_stress', 
        'loneliness_before_ai', 'effect_of_ai_on_loneliness', 'depression_or_anxiety_before_ai',
        'effect_of_ai_on_depression_or_anxiety', 'suicidal_thoughts_presence', 'effect_of_ai_on_suicidal_thoughts',
        'other_despair_types', 'effect_of_ai_on_other_despair', 'user_dependence', 'real_life_relationship_impact',
        'limitations_of_ai', 'technical_issues', 'privacy_concerns', 'feature_restriction_impact',
        'cost_impact_on_accessibility', 'impact_of_ai_updates', 'user_satisfaction_with_policy_decisions',
        'overall_mental_health_impact_of_company_decisions'
    ]
    results_df = pd.DataFrame(columns=results_columns)

    successfully_parsed_responses = []
    unsuccessfully_parsed_responses = []
    unsuccessful_content_blocks = []
    review_count_since_last_save = 0
    checkpoint_interval = 100

    # Loop through the first 10 reviews
    for index, row in df.iterrows():
        review_text = row['text']
        user_name = row['user']
        print(f"Processing index: {index + 1 }. Username: {user_name}")

        formatted_instructions_1 = get_instruction_1(review_text)
        formatted_instructions_2 = get_instruction_2(review_text)
        formatted_instructions_3 = get_instruction_3(review_text)
        formatted_instructions_4 = get_instruction_4(review_text)
        formatted_instructions_5 = get_instruction_5(review_text)

        instructions_array = {
            "instructions_version_1": formatted_instructions_1,
            "instructions_version_2": formatted_instructions_2,
            "instructions_version_3": formatted_instructions_3,
            "instructions_version_4": formatted_instructions_4,
            "instructions_version_5": formatted_instructions_5
            }

        for instruction_version, instruction_text in instructions_array.items():

            new_row = {
                # Basic info
                'date': df.at[index, "date"],
                'user': user_name,
                'stars': df.at[index, "stars"],
                'review_text': review_text,
                'word_count': df.at[index, "word_count"],
                'instruction_version': instruction_version,
                'llm': "Claude",
                'error': "true",
                "error_text": ""
            }

            try: 
                print("Calling API...") 
                # Make the API call
                completion = client.messages.create(
                    model="claude-3-opus-20240229",
                    max_tokens=4096,
                    system="Your task is to take the unstructured text provided and convert it into a well-organized table format using JSON. Identify the main entities, attributes, or categories mentioned in the text and use them as keys in the JSON object. Then, extract the relevant information from the text and populate the corresponding values in the JSON object. Ensure that the data is accurately represented and properly formatted within the JSON structure. The resulting JSON table should provide a clear, structured overview of the information presented in the original text.",
                    messages=[
                        {"role": "user", "content": instruction_text}
                    ]
                )

                print("API response recieved. Parsing response...")

                # Remove leading and trailing whitespace, uncomment based on use case
                # text = content_block.text 
                # start_index = text.find('{')
                # end_index = text.rfind('}') + 1
                # json_string = text[start_index:end_index]
                # parsed_response = json.loads(json_string)

                parsed_response = json.loads(completion.content[0].text)
                parsed_response['user_name'] = user_name

                # Simplifying access to nested structures
                ai_mental_health = parsed_response["mental_health_related_to_ai"]
                if_unwanted_responses = ai_mental_health.get("if_unwanted_inappropriate_responses", {})
                user_mental_state = ai_mental_health["user_mental_state"]
                user_conditions = ai_mental_health["user_conditions"]
                other_despair = user_conditions.get("other_despair_before_using_ai", {})
                company_policy_impact = parsed_response["company_policy_impact_on_mental_health"]

                # Creating the new_row dictionary with simplified access
                new_row.update({
                    # Demographic info
                    'coherence_and_clarity_of_review': parsed_response["coherence_and_clarity_of_review"],
                    'gender_of_user': parsed_response["gender_of_user"],
                    'gender_of_ai': parsed_response["gender_of_ai"],
                    'name_user_gave_ai': parsed_response["name_user_gave_ai"],
                    'age_of_user': parsed_response["age_of_user"],
                    'duration_of_app_usage': parsed_response["duration_of_app_usage"],
                    'frequency_of_app_usage': parsed_response["frequency_of_app_usage"],
                    'relationship_status_of_user': parsed_response["relationship_status_of_user"],
                    
                    # AI-related fields
                    'empathy_of_ai': ai_mental_health["empathy_of_ai"],
                    'behavior_of_ai': ai_mental_health["behavior_of_ai"],
                    'inappropriate_frequency': if_unwanted_responses.get("frequency", ""),
                    'inappropriate_nature': ', '.join(if_unwanted_responses.get("nature", [])),
                    'ai_support_level': ai_mental_health["ai_support_level"],
                    'support_types': ', '.join(ai_mental_health.get("support_types", [])),
                    'user_mental_state_before_ai': user_mental_state["before_ai_use"],
                    'effect_of_ai_on_user_mental_state': user_mental_state["effect_of_ai_use"],
                    
                    # Extracting deeply nested user conditions
                    'stress_before_ai': user_conditions["stress"]["before_ai"],
                    'effect_of_ai_on_stress': user_conditions["stress"]["effect_of_ai"],
                    'loneliness_before_ai': user_conditions["loneliness"]["before_ai"],
                    'effect_of_ai_on_loneliness': user_conditions["loneliness"]["effect_of_ai"],
                    'depression_or_anxiety_before_ai': user_conditions["depression_or_anxiety"]["before_ai"],
                    'effect_of_ai_on_depression_or_anxiety': user_conditions["depression_or_anxiety"]["effect_of_ai"],
                    'suicidal_thoughts_presence': user_conditions["suicidal_thoughts"]["presence"],
                    'effect_of_ai_on_suicidal_thoughts': user_conditions["suicidal_thoughts"]["effect_of_ai"],
                    'other_despair_types': ', '.join(other_despair.get("types", [])),
                    'effect_of_ai_on_other_despair': other_despair.get("effect_of_ai", ""),
                    
                    # Other fields
                    'user_dependence': ai_mental_health["user_dependence_on_ai"],
                    'real_life_relationship_impact': ai_mental_health["real_life_relationship_impact_of_ai"],
                    'limitations_of_ai': ', '.join(ai_mental_health.get("limitations_of_ai", [])),
                    
                    # Company policy impact fields
                    'technical_issues': company_policy_impact["technical_issues"],
                    'privacy_concerns': company_policy_impact["privacy_concerns"],
                    'feature_restriction_impact': company_policy_impact["feature_restriction_impact"],
                    'cost_impact_on_accessibility': company_policy_impact["cost_impact_on_accessibility"],
                    'impact_of_ai_updates': company_policy_impact["impact_of_ai_updates"],
                    'user_satisfaction_with_policy_decisions': company_policy_impact["user_satisfaction_with_policy_decisions"],
                    'overall_mental_health_impact_of_company_decisions': company_policy_impact["overall_mental_health_impact_of_company_decisions"]
                })

                new_row['error'] = "false"
                # Add the response to the successfully parsed list
                successfully_parsed_responses.append(parsed_response)
                print("Response parsed successfully.")

            except json.JSONDecodeError as e:
                print(f"JSON decoding failed: {e}")
                unsuccessful_content_blocks.append(serialize_message(completion))
                new_row['error_text'] = str(e)
                continue

            except Exception as e:
                unsuccessfully_parsed_responses.append(parsed_response)
                print(f"Error parsing response for index {index + 1}: {e}")
                new_row['error_text'] = str(e)
                continue

            finally:
                new_row_df = pd.DataFrame([new_row])  # Convert new_row to DataFrame
                results_df = pd.concat([results_df, new_row_df], ignore_index=True)
                review_count_since_last_save += 1

    # Construct output file names based on the input file name
    base_name = file_name.replace('.csv', '')
    csv_output_path = os.path.join(output_folder, f'{base_name}_analyzed_reviews.csv')
    success_json_output_path = os.path.join(output_folder, f'{base_name}_success_responses.json')
    unsuccessful_content_blocks_path = os.path.join(output_folder, f'{base_name}_unsuccessful_content_blocks.json')
    error_json_output_path = os.path.join(output_folder, f'{base_name}_error_responses.json')
    
    # Save the processed DataFrame to a CSV
    results_df.to_csv(csv_output_path, index=False)
    print(f"Saved processed data to {csv_output_path}")

    # Save successfully parsed responses to a JSON file
    with open(success_json_output_path, 'w') as file:
        json.dump(successfully_parsed_responses, file, indent=4)
    print(f"Saved successfully parsed responses to {success_json_output_path}")
    
    # Save unsuccessful content blocks
    with open(unsuccessful_content_blocks_path, 'w') as file:
        json.dump(unsuccessful_content_blocks, file, indent=4)
    print(f"Saved successfully parsed responses to {unsuccessful_content_blocks_path}")

    # Save unsuccessfully parsed responses to a JSON file
    with open(error_json_output_path, 'w') as file:
        json.dump(unsuccessfully_parsed_responses, file, indent=4)
    print(f"Saved unsuccessfully parsed responses to {error_json_output_path}") 

print("Completed processing all files.")