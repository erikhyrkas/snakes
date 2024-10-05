import json
import os

from ys.inference.model_interface import ModelInterface

class MMLUProEvaluator:
    def __init__(self, model: ModelInterface):
        self.model = model

    @staticmethod
    def prompt_format_question_answer(question):
        options_text = "\n".join([f"{chr(65 + i)}. {opt}" for i, opt in enumerate(question['options'])])
        return f"Question: {question['question']}\n{options_text}\n<start>Answer: "

    @staticmethod
    def prompt_format_q_a(question):
        options_text = "\n".join([f"{chr(65 + i)}. {opt}" for i, opt in enumerate(question['options'])])
        return f"Q: {question['question']}\n{options_text}\n<start>A: "

    @staticmethod
    def prompt_format(question):
        options_text = "\n".join([f"{chr(65 + i)}. {opt}" for i, opt in enumerate(question['options'])])
        return f"{question['question']}\n{options_text}\n<start>"

    def evaluate(self, path):
        results = []
        total_correct = 0
        total_questions = 0
        dataset = []
        with open(path, 'r') as file:
            for line in file:
                question_data = json.loads(line)
                dataset.append(question_data)
        for question in dataset:
            prompt = self.prompt_format(question)
            print(f"Prompt: {prompt}")
            response = self.model.complete(prompt, 1.0, 128)
            print(f"Raw response: {response}")
            response = response.replace(prompt, '')
            response = response.strip()

            response = response.split('\n')[0].strip() # only keep first line of text to ignore explanations.

            correct_answer_letter = chr(65 + question['answer_index'])  # Convert answer_index to A, B, C, etc.
            correct_answer_text = question['options'][question['answer_index']]  # Get the correct answer text
            correct_combined_1 = f"{correct_answer_letter}. {correct_answer_text}"  # Letter + text
            correct_combined_2 = f"{correct_answer_letter}: {correct_answer_text}"
            correct_combined_3 = f"{correct_answer_letter}, {correct_answer_text}"
            correct_combined_4 = f"{correct_answer_letter}; {correct_answer_text}"
            correct_combined_5 = f"{correct_answer_letter} ({correct_answer_text})"
            print(f"Expected response: {correct_combined_1}")
            # Normalize response to account for various possibilities
            response = response.strip().lower()

            # Check if the response matches any of the possible formats
            is_correct = (
                    response == correct_answer_letter.lower() or  # Single letter match
                    response == correct_answer_text.strip().lower() or  # Text match
                    response == correct_combined_1.strip().lower() or  # Letter + text match
                    response == correct_combined_2.strip().lower() or
                    response == correct_combined_3.strip().lower() or
                    response == correct_combined_4.strip().lower() or
                    response == correct_combined_5.strip().lower()
            )
            if is_correct:
                print(f"Correct Response: {response}")
            else:
                print(f"Incorrect Response: {response}")
            if is_correct:
                total_correct += 1
            total_questions += 1

            results.append({
                'question_id': question['question_id'],
                'response': response,
                'correct': is_correct
            })

        accuracy = total_correct / total_questions if total_questions > 0 else 0

        for result in results:
            status = "Correct" if result['correct'] else "Incorrect"
            print(f"Question ID: {result['question_id']}, Your Answer: {result['response']}, {status}")
        print(f"Overall Accuracy: {accuracy * 100:.2f}%")

def evauluate_snakes():
    base_path = os.getenv("YS_LLM_BASE_PATH", "./")

    model_path = f"{base_path}model/model.bin"
    if not os.path.isfile(model_path):
        model_path = f"{base_path}model/model_checkpoint.bin"

    tokenizer_path = f"{base_path}model/tokenizer.pkl"
    config_save_path = f"{base_path}model/model_config.json"
    if not os.path.exists(model_path):
        print("Did you forget to train the model?")
        return
    if not os.path.exists(tokenizer_path):
        print("Did you forget to train the tokenizer?")
        return

    print("Loading...")
    model_interface = ModelInterface(model_save_path=model_path, tokenizer_save_path=tokenizer_path,
                               config_save_path=config_save_path)
    evaluator = MMLUProEvaluator(model_interface)
    evaluator.evaluate("benchmark_data/mmlu-pro.jsonl")

if __name__ == '__main__':
    evauluate_snakes()