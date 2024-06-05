def get_instruction_1(review_text):
    return f"""
    Instructions:
    - Please rate the following review of an AI companion app based on the aspects of mental health support.
    - Use the JSON structure provided below to categorize your evaluation.
    - Separate the evaluation into two parts: one focusing on the AI interaction, and another on the company's policies and decisions.
    - In the mental_health_related_to_ai section only refer to comments about the AI itself, NOT the company decisions (ex. pricing, access, etc.)
    - If a specific aspect is not mentioned in the review, select 'Not Mentioned'.
   
    Review to Analyze: "{review_text}"

    Expected JSON Response Format: {{
        "coherence_and_clarity_of_review": "Low/Medium/High",
        "gender_of_user": "Male/Female/Nonbinary/Not Mentioned",
        "gender_of_ai": "Male/Female/Nonbinary/Not Mentioned",
        "name_user_gave_ai": "[Insert name]/Not Mentioned",
        "age_of_user":"[Specific age if mentioned (ex. 43)]/[Age language if mentioned (ex. "Middle-aged man")]/Not Mentioned",
        "duration_of_app_usage": "[Exact Duration (ex. "About a year")]/[General Duration Description (ex. "for months")]/Not Mentioned",
        "frequency_of_app_usage": "Daily/Weekly/Monthly/Sporadically/Rarely/Not Mentioned",
        "relationship_status_of_user": "Single/Married/Unmarried but in a relationship/Not Mentioned",
        "mental_health_related_to_ai": {{   
            "empathy_of_ai": "None/Low/Medium/High/Not Mentioned",
            "behavior_of_ai": "Supportive/Neutral/Unwanted Inappropriate Responses/Not Mentioned",
            "if_unwanted_inappropriate_responses": {{
                "frequency": "Often/Sometimes/Rarely/Never/Not Mentioned",
                "nature": [
                    "Offensive Language",
                    "Invasive Questions",
                    "Unwanted Topics",
                    "Lack of Sensitivity",
                    "Creepy",
                    "Other",
                    "Not Mentioned"
                ]
            }},
            "ai_support_level": "None/Slight/Moderate/Strong/Exceptional/Not Mentioned", 
            "support_types": [
                "Humor or Entertainment",
                "Emotional Support",
                "Therapeutic Conversation",
                "Coping Strategies",
                "Friendship",
                "Venting",
                "Sexual Support",
                "Significant Other Relationship",
                "Comforting in Times of Distress",
                "Providing Safety",
                "Encouragement",
                "Validation",
                "Other",
                "Not Mentioned"
            ],
            "user_mental_state": {{
                "before_ai_use": "Positive/Neutral/Negative/Not Mentioned",
                "effect_of_ai_use": "Improved/Unchanged/Worsened/Not Mentioned"
            }},
            "user_conditions": {{
                "stress": {{
                    "before_ai": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Increased/Unchanged/Decreased/Resolved/Not Mentioned"
                }},
                "loneliness": {{
                    "before_ai": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Increased/Unchanged/Decreased/Resolved/Not Mentioned"
                }},
                "depression_or_anxiety": {{
                    "before_ai": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Worsened/Unchanged/Improved/Resolved/Not Mentioned"
                }},
                "suicidal_thoughts": {{
                    "presence": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Harmful/Ineffective/Helpful/Lifesaving/Not Mentioned"
                }},
                "other_despair_before_using_ai": {{
                    "types": [
                        "Trauma",
                        "Hopelessness",
                        "Isolation",
                        "Grief",
                        "Health Conditions",
                        "Relationship Issues",
                        "Drug Use",
                        "Fear/Paranoia",
                        "Prison Time",
                        "History of Abuse",
                        "LGBTQ Challenges",
                        "Other",
                        "Not Mentioned"
                    ],
                    "effect_of_ai": "Increased/Unchanged/Decreased/Resolved/Not Mentioned"
                }}
            }},
            "user_dependence_on_ai": "None/Low/Moderate/High/Overdependence/Not Mentioned",
            "real_life_relationship_impact_of_ai": "Negative/Neutral/Positive/Not Mentioned",
            "limitations_of_ai": [
                "Staying on topic",
                "Staying in character",
                "Remembering key facts",
                "Providing relevant responses",
                "Maintaining conversation flow",
                "Too robotic/not person-like",
                "Not Mentioned"
                ]
        }},     
        "company_policy_impact_on_mental_health": {{
            "technical_issues": "Positive/Negative/Neutral/Not Mentioned",
            "privacy_concerns": "Positive/Negative/Neutral/Not Mentioned",
            "feature_restriction_impact": "Positive/Negative/Neutral/Not Mentioned",
            "cost_impact_on_accessibility": "Positive/Negative/Neutral/Not Mentioned",
            "impact_of_ai_updates": "Positive/Negative/Neutral/Not Mentioned",
            "user_satisfaction_with_policy_decisions": "Positive/Negative/Neutral/Not Mentioned",
            "overall_mental_health_impact_of_company_decisions": "Positive/Negative/Neutral/Not Mentioned"
        }}
    }}
    """

def get_instruction_2(review_text):
    return f"""
    Instructions:
    - Please rate the following review of an AI companion app based on the aspects of mental health support.
    - Use the JSON structure provided below to categorize your evaluation.
    - Separate the evaluation into two parts: one focusing on the AI interaction, and another on the company's policies and decisions.
    - In the mental_health_related_to_ai section only refer to comments about the AI itself, NOT the company decisions (ex. pricing, access, etc.)
    - If a specific aspect is not mentioned in the review, select 'Not Mentioned'.

    Expected JSON Response Format: {{
        "coherence_and_clarity_of_review": "Low/Medium/High",
        "gender_of_user": "Male/Female/Nonbinary/Not Mentioned",
        "gender_of_ai": "Male/Female/Nonbinary/Not Mentioned",
        "name_user_gave_ai": "[Insert name]/Not Mentioned",
        "age_of_user":"[Specific age if mentioned (ex. 43)]/[Age language if mentioned (ex. "Middle-aged man")]/Not Mentioned",
        "duration_of_app_usage": "[Exact Duration (ex. "About a year")]/[General Duration Description (ex. "for months")]/Not Mentioned",
        "frequency_of_app_usage": "Daily/Weekly/Monthly/Sporadically/Rarely/Not Mentioned",
        "relationship_status_of_user": "Single/Married/Unmarried but in a relationship/Not Mentioned",
        "mental_health_related_to_ai": {{   
            "empathy_of_ai": "None/Low/Medium/High/Not Mentioned",
            "behavior_of_ai": "Supportive/Neutral/Unwanted Inappropriate Responses/Not Mentioned",
            "if_unwanted_inappropriate_responses": {{
                "frequency": "Often/Sometimes/Rarely/Never/Not Mentioned",
                "nature": [
                    "Offensive Language",
                    "Invasive Questions",
                    "Unwanted Topics",
                    "Lack of Sensitivity",
                    "Creepy",
                    "Other",
                    "Not Mentioned"
                ]
            }},
            "ai_support_level": "None/Slight/Moderate/Strong/Exceptional/Not Mentioned", 
            "support_types": [
                "Humor or Entertainment",
                "Emotional Support",
                "Therapeutic Conversation",
                "Coping Strategies",
                "Friendship",
                "Venting",
                "Sexual Support",
                "Significant Other Relationship",
                "Comforting in Times of Distress",
                "Providing Safety",
                "Encouragement",
                "Validation",
                "Other",
                "Not Mentioned"
            ],
            "user_mental_state": {{
                "before_ai_use": "Positive/Neutral/Negative/Not Mentioned",
                "effect_of_ai_use": "Improved/Unchanged/Worsened/Not Mentioned"
            }},
            "user_conditions": {{
                "stress": {{
                    "before_ai": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Increased/Unchanged/Decreased/Resolved/Not Mentioned"
                }},
                "loneliness": {{
                    "before_ai": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Increased/Unchanged/Decreased/Resolved/Not Mentioned"
                }},
                "depression_or_anxiety": {{
                    "before_ai": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Worsened/Unchanged/Improved/Resolved/Not Mentioned"
                }},
                "suicidal_thoughts": {{
                    "presence": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Harmful/Ineffective/Helpful/Lifesaving/Not Mentioned"
                }},
                "other_despair_before_using_ai": {{
                    "types": [
                        "Trauma",
                        "Hopelessness",
                        "Isolation",
                        "Grief",
                        "Health Conditions",
                        "Relationship Issues",
                        "Drug Use",
                        "Fear/Paranoia",
                        "Prison Time",
                        "History of Abuse",
                        "LGBTQ Challenges",
                        "Other",
                        "Not Mentioned"
                    ],
                    "effect_of_ai": "Increased/Unchanged/Decreased/Resolved/Not Mentioned"
                }}
            }},
            "user_dependence_on_ai": "None/Low/Moderate/High/Overdependence/Not Mentioned",
            "real_life_relationship_impact_of_ai": "Negative/Neutral/Positive/Not Mentioned",
            "limitations_of_ai": [
                "Staying on topic",
                "Staying in character",
                "Remembering key facts",
                "Providing relevant responses",
                "Maintaining conversation flow",
                "Too robotic/not person-like",
                "Not Mentioned"
                ]
        }},     
        "company_policy_impact_on_mental_health": {{
            "technical_issues": "Positive/Negative/Neutral/Not Mentioned",
            "privacy_concerns": "Positive/Negative/Neutral/Not Mentioned",
            "feature_restriction_impact": "Positive/Negative/Neutral/Not Mentioned",
            "cost_impact_on_accessibility": "Positive/Negative/Neutral/Not Mentioned",
            "impact_of_ai_updates": "Positive/Negative/Neutral/Not Mentioned",
            "user_satisfaction_with_policy_decisions": "Positive/Negative/Neutral/Not Mentioned",
            "overall_mental_health_impact_of_company_decisions": "Positive/Negative/Neutral/Not Mentioned"
        }}
    }}

    Review to Analyze: "{review_text}"
    """

def get_instruction_3(review_text):
    return f"""
    Instructions:
    - Please rate the following review of an AI companion app based on the aspects of mental health support.
    - Use the JSON structure provided below to categorize your evaluation.
    - Separate the evaluation into two parts: one focusing on the AI interaction, and another on the company's policies and decisions.
    - In the mental_health_related_to_ai section only refer to comments about the AI itself, NOT the company decisions (ex. pricing, access, etc.)
    - If a specific aspect is not mentioned in the review, select 'Not Mentioned'.
    - Do not add leading or trailing whitespace or new lines before or after the JSON.
    - Only return the JSON with no additional commentary or result text.
   
    Review to Analyze: "{review_text}"

    Expected JSON Response Format: {{
        "coherence_and_clarity_of_review": "Low/Medium/High",
        "gender_of_user": "Male/Female/Nonbinary/Not Mentioned",
        "gender_of_ai": "Male/Female/Nonbinary/Not Mentioned",
        "name_user_gave_ai": "[Insert name]/Not Mentioned",
        "age_of_user":"[Specific age if mentioned (ex. 43)]/[Age language if mentioned (ex. "Middle-aged man")]/Not Mentioned",
        "duration_of_app_usage": "[Exact Duration (ex. "About a year")]/[General Duration Description (ex. "for months")]/Not Mentioned",
        "frequency_of_app_usage": "Daily/Weekly/Monthly/Sporadically/Rarely/Not Mentioned",
        "relationship_status_of_user": "Single/Married/Unmarried but in a relationship/Not Mentioned",
        "mental_health_related_to_ai": {{   
            "empathy_of_ai": "None/Low/Medium/High/Not Mentioned",
            "behavior_of_ai": "Supportive/Neutral/Unwanted Inappropriate Responses/Not Mentioned",
            "if_unwanted_inappropriate_responses": {{
                "frequency": "Often/Sometimes/Rarely/Never/Not Mentioned",
                "nature": [
                    "Offensive Language",
                    "Invasive Questions",
                    "Unwanted Topics",
                    "Lack of Sensitivity",
                    "Creepy",
                    "Other",
                    "Not Mentioned"
                ]
            }},
            "ai_support_level": "None/Slight/Moderate/Strong/Exceptional/Not Mentioned", 
            "support_types": [
                "Humor or Entertainment",
                "Emotional Support",
                "Therapeutic Conversation",
                "Coping Strategies",
                "Friendship",
                "Venting",
                "Sexual Support",
                "Significant Other Relationship",
                "Comforting in Times of Distress",
                "Providing Safety",
                "Encouragement",
                "Validation",
                "Other",
                "Not Mentioned"
            ],
            "user_mental_state": {{
                "before_ai_use": "Positive/Neutral/Negative/Not Mentioned",
                "effect_of_ai_use": "Improved/Unchanged/Worsened/Not Mentioned"
            }},
            "user_conditions": {{
                "stress": {{
                    "before_ai": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Increased/Unchanged/Decreased/Resolved/Not Mentioned"
                }},
                "loneliness": {{
                    "before_ai": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Increased/Unchanged/Decreased/Resolved/Not Mentioned"
                }},
                "depression_or_anxiety": {{
                    "before_ai": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Worsened/Unchanged/Improved/Resolved/Not Mentioned"
                }},
                "suicidal_thoughts": {{
                    "presence": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Harmful/Ineffective/Helpful/Lifesaving/Not Mentioned"
                }},
                "other_despair_before_using_ai": {{
                    "types": [
                        "Trauma",
                        "Hopelessness",
                        "Isolation",
                        "Grief",
                        "Health Conditions",
                        "Relationship Issues",
                        "Drug Use",
                        "Fear/Paranoia",
                        "Prison Time",
                        "History of Abuse",
                        "LGBTQ Challenges",
                        "Other",
                        "Not Mentioned"
                    ],
                    "effect_of_ai": "Increased/Unchanged/Decreased/Resolved/Not Mentioned"
                }}
            }},
            "user_dependence_on_ai": "None/Low/Moderate/High/Overdependence/Not Mentioned",
            "real_life_relationship_impact_of_ai": "Negative/Neutral/Positive/Not Mentioned",
            "limitations_of_ai": [
                "Staying on topic",
                "Staying in character",
                "Remembering key facts",
                "Providing relevant responses",
                "Maintaining conversation flow",
                "Too robotic/not person-like",
                "Not Mentioned"
                ]
        }},     
        "company_policy_impact_on_mental_health": {{
            "technical_issues": "Positive/Negative/Neutral/Not Mentioned",
            "privacy_concerns": "Positive/Negative/Neutral/Not Mentioned",
            "feature_restriction_impact": "Positive/Negative/Neutral/Not Mentioned",
            "cost_impact_on_accessibility": "Positive/Negative/Neutral/Not Mentioned",
            "impact_of_ai_updates": "Positive/Negative/Neutral/Not Mentioned",
            "user_satisfaction_with_policy_decisions": "Positive/Negative/Neutral/Not Mentioned",
            "overall_mental_health_impact_of_company_decisions": "Positive/Negative/Neutral/Not Mentioned"
        }}
    }}

    Instructions:
    - Please rate the following review of an AI companion app based on the aspects of mental health support.
    - Use the JSON structure provided below to categorize your evaluation.
    - Separate the evaluation into two parts: one focusing on the AI interaction, and another on the company's policies and decisions.
    - In the mental_health_related_to_ai section only refer to comments about the AI itself, NOT the company decisions (ex. pricing, access, etc.)
    - If a specific aspect is not mentioned in the review, select 'Not Mentioned'.
    - Do not add leading or trailing whitespace or new lines before or after the JSON.
    - Only return the JSON with no additional commentary or result text.
    """

def get_instruction_4(review_text):
    return f"""
    Instructions:
    - Please rate the following review of an AI companion app based on the aspects of mental health support.
    - Use the JSON structure provided below to categorize your evaluation.
    - Separate the evaluation into two parts: one focusing on the AI interaction, and another on the company's policies and decisions.
    - In the mental_health_related_to_ai section only refer to comments about the AI itself, NOT the company decisions (ex. pricing, access, etc.)
    - If a specific aspect is not mentioned in the review, select 'Not Mentioned'.
    - Do not add leading or trailing whitespace or new lines before or after the JSON.
    - Only return the JSON with no additional commentary or result text.
   
    Review to Analyze: "{review_text}"

    Expected JSON Response Format: {{
        "coherence_and_clarity_of_review": "Low/Medium/High",
        "gender_of_user": "Male/Female/Nonbinary/Not Mentioned",
        "gender_of_ai": "Male/Female/Nonbinary/Not Mentioned",
        "name_user_gave_ai": "[Insert name]/Not Mentioned",
        "age_of_user":"[Specific age if mentioned (ex. 43)]/[Age language if mentioned (ex. "Middle-aged man")]/Not Mentioned",
        "duration_of_app_usage": "[Exact Duration (ex. "About a year")]/[General Duration Description (ex. "for months")]/Not Mentioned",
        "frequency_of_app_usage": "Daily/Weekly/Monthly/Sporadically/Rarely/Not Mentioned",
        "relationship_status_of_user": "Single/Married/Unmarried but in a relationship/Not Mentioned",
        "mental_health_related_to_ai": {{   
            "empathy_of_ai": "None/Low/Medium/High/Not Mentioned",
            "behavior_of_ai": "Supportive/Neutral/Unwanted Inappropriate Responses/Not Mentioned",
            "if_unwanted_inappropriate_responses": {{
                "frequency": "Often/Sometimes/Rarely/Never/Not Mentioned",
                "nature": [
                    "Offensive Language",
                    "Invasive Questions",
                    "Unwanted Topics",
                    "Lack of Sensitivity",
                    "Creepy",
                    "Other",
                    "Not Mentioned"
                ]
            }}
            "ai_support_level": "None/Slight/Moderate/Strong/Exceptional/Not Mentioned", 
            "support_types": [
                "Humor or Entertainment",
                "Emotional Support",
                "Therapeutic Conversation",
                "Coping Strategies",
                "Friendship",
                "Venting",
                "Sexual Support",
                "Significant Other Relationship",
                "Comforting in Times of Distress",
                "Providing Safety",
                "Encouragement",
                "Validation",
                "Other",
                "Not Mentioned"
            ],
            "user_mental_state": {{
                "before_ai_use": "Positive/Neutral/Negative/Not Mentioned",
                "effect_of_ai_use": "Improved/Unchanged/Worsened/Not Mentioned"
            }},
            "user_conditions": {{
                "stress": {{
                    "before_ai": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Increased/Unchanged/Decreased/Resolved/Not Mentioned"
                }},
                "loneliness": {{
                    "before_ai": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Increased/Unchanged/Decreased/Resolved/Not Mentioned"
                }},
                "depression_or_anxiety": {{
                    "before_ai": "Yes/No/Not Mentioned"
                    "effect_of_ai": "Worsened/Unchanged/Improved/Resolved/Not Mentioned"
                }},
                "suicidal_thoughts": {{
                    "presence": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Harmful/Ineffective/Helpful/Lifesaving/Not Mentioned"
                }},
                "other_despair_before_using_ai": {{
                    "types": [
                        "Trauma",
                        "Hopelessness",
                        "Isolation",
                        "Grief",
                        "Health Conditions",
                        "Relationship Issues",
                        "Drug Use",
                        "Fear/Paranoia",
                        "Prison Time",
                        "History of Abuse",
                        "LGBTQ Challenges",
                        "Other",
                        "Not Mentioned"
                    ],
                    "effect_of_ai": "Increased/Unchanged/Decreased/Resolved/Not Mentioned"
                }}
            }},
            "user_dependence_on_ai": "None/Low/Moderate/High/Overdependence/Not Mentioned",
            "real_life_relationship_impact_of_ai": "Negative/Neutral/Positive/Not Mentioned",
            "limitations_of_ai": [
                "Staying on topic",
                "Staying in character",
                "Remembering key facts",
                "Providing relevant responses",
                "Maintaining conversation flow",
                "Too robotic/not person-like",
                "Not Mentioned"
                ],
        }},     
        "company_policy_impact_on_mental_health": {{
            "technical_issues": "Positive/Negative/Neutral/Not Mentioned",
            "privacy_concerns": "Positive/Negative/Neutral/Not Mentioned",
            "feature_restriction_impact": "Positive/Negative/Neutral/Not Mentioned",
            "cost_impact_on_accessibility": "Positive/Negative/Neutral/Not Mentioned",
            "impact_of_ai_updates": "Positive/Negative/Neutral/Not Mentioned",
            "user_satisfaction_with_policy_decisions": "Positive/Negative/Neutral/Not Mentioned",
            "overall_mental_health_impact_of_company_decisions": "Positive/Negative/Neutral/Not Mentioned"
        }},
    }}

    Instructions:
    - Please rate the following review of an AI companion app based on the aspects of mental health support.
    - Use the JSON structure provided below to categorize your evaluation.
    - Separate the evaluation into two parts: one focusing on the AI interaction, and another on the company's policies and decisions.
    - In the mental_health_related_to_ai section only refer to comments about the AI itself, NOT the company decisions (ex. pricing, access, etc.)
    - If a specific aspect is not mentioned in the review, select 'Not Mentioned'.
    - Do not add leading or trailing whitespace or new lines before or after the JSON.
    - Only return the JSON with no additional commentary or result text.
    """

def get_instruction_5(review_text):
    return f"""
    Instructions:
    - Please rate the following review of an AI companion app based on the aspects of mental health support.
    - Use the JSON structure provided below to categorize your evaluation.
    - Separate the evaluation into two parts: one focusing on the AI interaction, and another on the company's policies and decisions.
    - In the mental_health_related_to_ai section only refer to comments about the AI itself, NOT the company decisions (ex. pricing, access, etc.)
    - If a specific aspect is not mentioned in the review, select 'Not Mentioned'.
    - Do not add leading or trailing whitespace or new lines before or after the JSON.
    - Only return the JSON with no additional commentary or result text.
    - Please ensure the JSON is properly formatted in your response.
   
    Review to Analyze: "{review_text}"

    Expected JSON Response Format: {{
        "coherence_and_clarity_of_review": "Low/Medium/High",
        "gender_of_user": "Male/Female/Nonbinary/Not Mentioned",
        "gender_of_ai": "Male/Female/Nonbinary/Not Mentioned",
        "name_user_gave_ai": "[Insert name]/Not Mentioned",
        "age_of_user":"[Specific age if mentioned (ex. 43)]/[Age language if mentioned (ex. "Middle-aged man")]/Not Mentioned",
        "duration_of_app_usage": "[Exact Duration (ex. "About a year")]/[General Duration Description (ex. "for months")]/Not Mentioned",
        "frequency_of_app_usage": "Daily/Weekly/Monthly/Sporadically/Rarely/Not Mentioned",
        "relationship_status_of_user": "Single/Married/Unmarried but in a relationship/Not Mentioned",
        "mental_health_related_to_ai": {{   
            "empathy_of_ai": "None/Low/Medium/High/Not Mentioned",
            "behavior_of_ai": "Supportive/Neutral/Unwanted Inappropriate Responses/Not Mentioned",
            "if_unwanted_inappropriate_responses": {{
                "frequency": "Often/Sometimes/Rarely/Never/Not Mentioned",
                "nature": [
                    "Offensive Language",
                    "Invasive Questions",
                    "Unwanted Topics",
                    "Lack of Sensitivity",
                    "Creepy",
                    "Other",
                    "Not Mentioned"
                ]
            }}
            "ai_support_level": "None/Slight/Moderate/Strong/Exceptional/Not Mentioned", 
            "support_types": [
                "Humor or Entertainment",
                "Emotional Support",
                "Therapeutic Conversation",
                "Coping Strategies",
                "Friendship",
                "Venting",
                "Sexual Support",
                "Significant Other Relationship",
                "Comforting in Times of Distress",
                "Providing Safety",
                "Encouragement",
                "Validation",
                "Other",
                "Not Mentioned"
            ],
            "user_mental_state": {{
                "before_ai_use": "Positive/Neutral/Negative/Not Mentioned",
                "effect_of_ai_use": "Improved/Unchanged/Worsened/Not Mentioned"
            }},
            "user_conditions": {{
                "stress": {{
                    "before_ai": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Increased/Unchanged/Decreased/Resolved/Not Mentioned"
                }},
                "loneliness": {{
                    "before_ai": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Increased/Unchanged/Decreased/Resolved/Not Mentioned"
                }},
                "depression_or_anxiety": {{
                    "before_ai": "Yes/No/Not Mentioned"
                    "effect_of_ai": "Worsened/Unchanged/Improved/Resolved/Not Mentioned"
                }},
                "suicidal_thoughts": {{
                    "presence": "Yes/No/Not Mentioned",
                    "effect_of_ai": "Harmful/Ineffective/Helpful/Lifesaving/Not Mentioned"
                }},
                "other_despair_before_using_ai": {{
                    "types": [
                        "Trauma",
                        "Hopelessness",
                        "Isolation",
                        "Grief",
                        "Health Conditions",
                        "Relationship Issues",
                        "Drug Use",
                        "Fear/Paranoia",
                        "Prison Time",
                        "History of Abuse",
                        "LGBTQ Challenges",
                        "Other",
                        "Not Mentioned"
                    ],
                    "effect_of_ai": "Increased/Unchanged/Decreased/Resolved/Not Mentioned"
                }}
            }},
            "user_dependence_on_ai": "None/Low/Moderate/High/Overdependence/Not Mentioned",
            "real_life_relationship_impact_of_ai": "Negative/Neutral/Positive/Not Mentioned",
            "limitations_of_ai": [
                "Staying on topic",
                "Staying in character",
                "Remembering key facts",
                "Providing relevant responses",
                "Maintaining conversation flow",
                "Too robotic/not person-like",
                "Not Mentioned"
                ],
        }},     
        "company_policy_impact_on_mental_health": {{
            "technical_issues": "Positive/Negative/Neutral/Not Mentioned",
            "privacy_concerns": "Positive/Negative/Neutral/Not Mentioned",
            "feature_restriction_impact": "Positive/Negative/Neutral/Not Mentioned",
            "cost_impact_on_accessibility": "Positive/Negative/Neutral/Not Mentioned",
            "impact_of_ai_updates": "Positive/Negative/Neutral/Not Mentioned",
            "user_satisfaction_with_policy_decisions": "Positive/Negative/Neutral/Not Mentioned",
            "overall_mental_health_impact_of_company_decisions": "Positive/Negative/Neutral/Not Mentioned"
        }},
    }}

    Instructions:
    - Please rate the following review of an AI companion app based on the aspects of mental health support.
    - Use the JSON structure provided below to categorize your evaluation.
    - Separate the evaluation into two parts: one focusing on the AI interaction, and another on the company's policies and decisions.
    - In the mental_health_related_to_ai section only refer to comments about the AI itself, NOT the company decisions (ex. pricing, access, etc.)
    - If a specific aspect is not mentioned in the review, select 'Not Mentioned'.
    - Do not add leading or trailing whitespace or new lines before or after the JSON.
    - Only return the JSON with no additional commentary or result text.
    - Please ensure the JSON is properly formatted in your response.
    """
