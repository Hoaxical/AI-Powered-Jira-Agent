# backend/convertairesponse.py

import json

def convert_ai_response_to_text(ai_data):
    """Convert AI JSON structure into readable text."""

    lines = []
    lines.append(f"Epic Title: {ai_data.get('epic_title', 'N/A')}")
    lines.append(f"Description: {ai_data.get('epic_description', 'N/A')}\n")

    # User Stories
    user_stories = ai_data.get("user_stories", [])
    if user_stories:
        lines.append("=== USER STORIES ===")
        for story in user_stories:
            lines.append(f"\n {story.get('title', 'Untitled')} (ID: {story.get('id', 'N/A')})")
            lines.append(f"Description: {story.get('description', '')}")
            lines.append(f"Story Points: {story.get('story_points', 'N/A')}")
            if "acceptance_criteria" in story:
                lines.append("Acceptance Criteria:")
                for criteria in story["acceptance_criteria"]:
                    lines.append(f"  - {criteria}")

    # Test Cases
    test_cases = ai_data.get("test_cases", [])
    if test_cases:
        lines.append("\n=== TEST CASES ===")
        for case in test_cases:
            lines.append(f"\n Test Case ID: {case.get('testcase_id', 'N/A')} (Story: {case.get('story_id', 'N/A')})")
            lines.append(f"Preconditions: {case.get('preconditions', '')}")
            lines.append("Steps:")
            for step in case.get("steps", []):
                lines.append(f"  - {step}")
            lines.append(f"Expected Result: {case.get('expected_results', '')}")

    return "\n".join(lines)
